# -*- coding: utf-8 -*-
"""dotproperty.com.ph, автоматический сбор: 2 объявлений, 2026-09-15.

Партию собрал collect_dotproperty.py -- без модели в контуре. Район взят из
разметки объявления (точное совпадение с CITIES либо однозначный прецедент на
сайте), описание собрано из полей разметки, возраст выведен из UUIDv7 в
идентификаторе записи и не превышает 7 дней.

Объявления, локальность которых не совпала ни с одним нашим районом и не имеет
однозначного прецедента, пропущены, а не приписаны к соседнему.
"""
from listing_lock import insert_listings

IDS = [3000740, 3000741]

N_RU = "Описание собрано программой из разметки объявления на dotproperty.com.ph — тип, спальни, санузлы, площадь, локальность и цена. Рекламный текст объявления не пересказан. Район поставлен по локальности из той же разметки; она изредка расходится с адресом в тексте объявления, поэтому адрес стоит сверить по ссылке. Дату размещения портал не публикует: возраст выведен из идентификатора записи (UUIDv7 хранит время создания) и означает «не моложе»."
N_EN = "This description was assembled by a program from the ad's own schema.org markup on dotproperty.com.ph — type, bedrooms, bathrooms, size, locality and price. The ad's marketing text is not retold. The district comes from the locality in that same markup, which occasionally disagrees with the address written in the ad, so check the address at the source. The portal publishes no posting date: the age is derived from the record id (a UUIDv7 carries its creation time) and means 'no newer than'."

NEW_SRC = r'''
L(3000740,"cebu","lah","Квартира",65000,82,
  "3-спальная квартира, 82 м², Lahug, Себу — 2 санузла.",
  "https://www.dotproperty.com.ph/ads/3-bedroom-apartment-for-rent-in-lahug-cebu_71b4b5c29de6-5710-bd62-337a-d45f9f89","сегодня",0,source="dotproperty",cur="PHP",
  descEn="3-bedroom flat, 82 m², Lahug, Cebu City — 2 bathrooms.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBhNDVjLWYyNjYtNzNjZS05ODI0LTNiYzA3ZDRlNWU4Mi8wMWEwYTQ2Mi0xODE5LTcwZDctODVjOC0xOTYwNjhkNjExM2EuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo0OTAsImhlaWdodCI6MzI1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBhNDVjLWYyNjYtNzNjZS05ODI0LTNiYzA3ZDRlNWU4Mi8wMWEwYTQ2Mi0xODE5LTcwZDctODVjOC0xOTYwNjhkNjExM2EuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBhNDVjLWYyNjYtNzNjZS05ODI0LTNiYzA3ZDRlNWU4Mi8wMWEwYTQ2Mi0xODE5LTcwZDctODVjOC0xOTYwNjhkNjExM2EuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBhNDVjLWYyNjYtNzNjZS05ODI0LTNiYzA3ZDRlNWU4Mi8wMWEwYTQ2Mi0xODE5LTcwZDctODVjOC0xOTYwNjhkNjExM2EuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoyNzUsImhlaWdodCI6MTU1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBhNDVjLWYyNjYtNzNjZS05ODI0LTNiYzA3ZDRlNWU4Mi8wMWEwYTQ2Mi0xOGU5LTcwNzItOTkxNS0wODQ1NTk5NjkyMzcuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBhNDVjLWYyNjYtNzNjZS05ODI0LTNiYzA3ZDRlNWU4Mi8wMWEwYTQ2Mi0xOGU5LTcwNzItOTkxNS0wODQ1NTk5NjkyMzcuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000741,"cebu","cap","Квартира",40000,40,
  "1-спальная квартира, 40 м², Luz, Себу — 1 санузел.",
  "https://www.dotproperty.com.ph/ads/1-bedroom-condo-for-rent-in-luz-cebu_fccba5e8d4e7-8c21-4582-2a30-26309f89","3 дня назад",3,source="dotproperty",cur="PHP",
  descEn="1-bedroom flat, 40 m², Luz, Cebu City — 1 bathroom.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjM3LTk2ZjctNzE0NS04N2QxLTJiNWMxYjRmZWRkYS8wMWEwOTYzOC00MGMyLTcwNTYtYWMwOC0wZjNhOTQ5NDhhZjEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo0OTAsImhlaWdodCI6MzI1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjM3LTk2ZjctNzE0NS04N2QxLTJiNWMxYjRmZWRkYS8wMWEwOTYzOC00MGMyLTcwNTYtYWMwOC0wZjNhOTQ5NDhhZjEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjM3LTk2ZjctNzE0NS04N2QxLTJiNWMxYjRmZWRkYS8wMWEwOTYzOC00MGMyLTcwNTYtYWMwOC0wZjNhOTQ5NDhhZjEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjM3LTk2ZjctNzE0NS04N2QxLTJiNWMxYjRmZWRkYS8wMWEwOTYzOC00MGMyLTcwNTYtYWMwOC0wZjNhOTQ5NDhhZjEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoyNzUsImhlaWdodCI6MTU1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjM3LTk2ZjctNzE0NS04N2QxLTJiNWMxYjRmZWRkYS8wMWEwOTYzOC00MTg2LTcyOWEtODg4Ny05Y2Y2ZDMwZGU0ZDIuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjM3LTk2ZjctNzE0NS04N2QxLTJiNWMxYjRmZWRkYS8wMWEwOTYzOC00MTg2LTcyOWEtODg4Ny05Y2Y2ZDMwZGU0ZDIuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
