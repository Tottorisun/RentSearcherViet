# -*- coding: utf-8 -*-
"""dotproperty.com.ph, автоматический сбор: 2 объявлений, 2026-09-25.

Партию собрал collect_dotproperty.py -- без модели в контуре. Район взят из
разметки объявления (точное совпадение с CITIES либо однозначный прецедент на
сайте), описание собрано из полей разметки, возраст выведен из UUIDv7 в
идентификаторе записи и не превышает 7 дней.

Объявления, локальность которых не совпала ни с одним нашим районом и не имеет
однозначного прецедента, пропущены, а не приписаны к соседнему.
"""
from listing_lock import insert_listings

IDS = [3001359, 3001360]

N_RU = "Описание собрано программой из разметки объявления на dotproperty.com.ph — тип, спальни, санузлы, площадь, локальность и цена. Рекламный текст объявления не пересказан. Район поставлен по локальности из той же разметки; она изредка расходится с адресом в тексте объявления, поэтому адрес стоит сверить по ссылке. Дату размещения портал не публикует: возраст выведен из идентификатора записи (UUIDv7 хранит время создания) и означает «не моложе»."
N_EN = "This description was assembled by a program from the ad's own schema.org markup on dotproperty.com.ph — type, bedrooms, bathrooms, size, locality and price. The ad's marketing text is not retold. The district comes from the locality in that same markup, which occasionally disagrees with the address written in the ad, so check the address at the source. The portal publishes no posting date: the age is derived from the record id (a UUIDv7 carries its creation time) and means 'no newer than'."

NEW_SRC = r'''
L(3001359,"cebu","bnl","Дом",110000,462,
  "5-спальный дом, 462 м², Banilad, Себу — 4 санузла.",
  "https://www.dotproperty.com.ph/ads/5-bedroom-house-for-sale-or-rent-in-banilad-cebu_fbc0f9ceb2f1-0bcf-0372-b240-c95c9f89","вчера",1,source="dotproperty",cur="PHP",
  descEn="5-bedroom house, 462 m², Banilad, Cebu City — 4 bathrooms.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkNDBkLTk1N2UtNzI2OS1hZGU5LThhN2ViZDBhOWRlYS8wMWEwZDQwZS1iYTQ3LTcxMmEtYjg0MC1hYmZkNmEyZDQ1MmIuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo0OTAsImhlaWdodCI6MzI1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkNDBkLTk1N2UtNzI2OS1hZGU5LThhN2ViZDBhOWRlYS8wMWEwZDQwZS1iYTQ3LTcxMmEtYjg0MC1hYmZkNmEyZDQ1MmIuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkNDBkLTk1N2UtNzI2OS1hZGU5LThhN2ViZDBhOWRlYS8wMWEwZDQwZS1iYTQ3LTcxMmEtYjg0MC1hYmZkNmEyZDQ1MmIuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkNDBkLTk1N2UtNzI2OS1hZGU5LThhN2ViZDBhOWRlYS8wMWEwZDQwZS1iYTQ3LTcxMmEtYjg0MC1hYmZkNmEyZDQ1MmIuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoyNzUsImhlaWdodCI6MTU1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkNDBkLTk1N2UtNzI2OS1hZGU5LThhN2ViZDBhOWRlYS8wMWEwZDQwZS1kOTM3LTcwODEtYjBkOC1lMmY4NGM5MzJjOGMuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkNDBkLTk1N2UtNzI2OS1hZGU5LThhN2ViZDBhOWRlYS8wMWEwZDQwZS1kOTM3LTcwODEtYjBkOC1lMmY4NGM5MzJjOGMuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001360,"cebu","bnl","Дом",80000,200,
  "3-спальный дом, 200 м², Banilad, Себу — 3 санузла.",
  "https://www.dotproperty.com.ph/ads/3-bedroom-house-for-rent-in-banilad-cebu_19382425cefd-f890-0752-138e-ba6c9f89","вчера",1,source="dotproperty",cur="PHP",
  descEn="3-bedroom house, 200 m², Banilad, Cebu City — 3 bathrooms.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkM2ZlLWIxNjgtNzQyOS05MDFhLWNhYmQ0NzU3MTYwOC8wMWEwZDNmZi1hN2RlLTcxYzctOTExYS1hNmYzMTk1ZmVkOTUuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkM2ZlLWIxNjgtNzQyOS05MDFhLWNhYmQ0NzU3MTYwOC8wMWEwZDNmZi1hN2RlLTcxYzctOTExYS1hNmYzMTk1ZmVkOTUuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkM2ZlLWIxNjgtNzQyOS05MDFhLWNhYmQ0NzU3MTYwOC8wMWEwZDNmZi1hNGRhLTczYTUtOTI0ZS05Y2JhZGE5ZTZjYmEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo0OTAsImhlaWdodCI6MzI1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkM2ZlLWIxNjgtNzQyOS05MDFhLWNhYmQ0NzU3MTYwOC8wMWEwZDNmZi1hNGRhLTczYTUtOTI0ZS05Y2JhZGE5ZTZjYmEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkM2ZlLWIxNjgtNzQyOS05MDFhLWNhYmQ0NzU3MTYwOC8wMWEwZDNmZi1hNGRhLTczYTUtOTI0ZS05Y2JhZGE5ZTZjYmEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTBkM2ZlLWIxNjgtNzQyOS05MDFhLWNhYmQ0NzU3MTYwOC8wMWEwZDNmZi1hNGRhLTczYTUtOTI0ZS05Y2JhZGE5ZTZjYmEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoyNzUsImhlaWdodCI6MTU1LCJmaXQiOiJjb3ZlciJ9fX0="], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
