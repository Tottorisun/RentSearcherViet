# -*- coding: utf-8 -*-
"""dotproperty.com.ph, автоматический сбор: 2 объявлений, 2026-09-13.

Партию собрал collect_dotproperty.py -- без модели в контуре. Район взят из
разметки объявления (точное совпадение с CITIES либо однозначный прецедент на
сайте), описание собрано из полей разметки, возраст выведен из UUIDv7 в
идентификаторе записи и не превышает 14 дней.

Объявления, локальность которых не совпала ни с одним нашим районом и не имеет
однозначного прецедента, пропущены, а не приписаны к соседнему.
"""
from listing_lock import insert_listings

IDS = [3000564, 3000565]

N_RU = "Описание собрано программой из разметки объявления на dotproperty.com.ph — тип, спальни, санузлы, площадь, локальность и цена. Рекламный текст объявления не пересказан. Район поставлен по локальности из той же разметки; она изредка расходится с адресом в тексте объявления, поэтому адрес стоит сверить по ссылке. Дату размещения портал не публикует: возраст выведен из идентификатора записи (UUIDv7 хранит время создания) и означает «не моложе»."
N_EN = "This description was assembled by a program from the ad's own schema.org markup on dotproperty.com.ph — type, bedrooms, bathrooms, size, locality and price. The ad's marketing text is not retold. The district comes from the locality in that same markup, which occasionally disagrees with the address written in the ad, so check the address at the source. The portal publishes no posting date: the age is derived from the record id (a UUIDv7 carries its creation time) and means 'no newer than'."

NEW_SRC = r'''
L(3000564,"cebu","tlm","Дом",65000,164,
  "3-спальный дом, 164 м², Talamban, Себу — 2 санузла.",
  "https://www.dotproperty.com.ph/ads/3-bedroom-house-for-rent-in-talamban-cebu_d466ea581eb9-b5d0-7392-fdea-c8309f89","вчера",1,source="dotproperty",cur="PHP",
  descEn="3-bedroom house, 164 m², Talamban, Cebu City — 2 bathrooms.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjFkLWZiY2EtNzA2Mi05YzRlLTBlYjgxNGZiMzM1Yy8wMWEwOTYxZi00Y2EwLTczYjgtYjc5Ny0zNWQyMmIyZWMzMjcuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjFkLWZiY2EtNzA2Mi05YzRlLTBlYjgxNGZiMzM1Yy8wMWEwOTYxZi00Y2EwLTczYjgtYjc5Ny0zNWQyMmIyZWMzMjcuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjFkLWZiY2EtNzA2Mi05YzRlLTBlYjgxNGZiMzM1Yy8wMWEwOTYxZi00Y2QwLTcwMmQtYWRlZi1jMzM2ZTAyNDJmMWQuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjFkLWZiY2EtNzA2Mi05YzRlLTBlYjgxNGZiMzM1Yy8wMWEwOTYxZi00Y2QwLTcwMmQtYWRlZi1jMzM2ZTAyNDJmMWQuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjFkLWZiY2EtNzA2Mi05YzRlLTBlYjgxNGZiMzM1Yy8wMWEwOTYxZi00Y2Y3LTcyYzEtODFiZC03N2NiYzA2ZmRjYzEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjFkLWZiY2EtNzA2Mi05YzRlLTBlYjgxNGZiMzM1Yy8wMWEwOTYxZi00Y2Y3LTcyYzEtODFiZC03N2NiYzA2ZmRjYzEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000565,"cebu","bnl","Дом",80000,220,
  "3-спальный дом, 220 м², Banilad, Себу — 3 санузла.",
  "https://www.dotproperty.com.ph/ads/3-bedroom-house-for-rent-in-banilad-cebu_35730bca9ef6-cb11-a062-6e30-67309f89","вчера",1,source="dotproperty",cur="PHP",
  descEn="3-bedroom house, 220 m², Banilad, Cebu City — 3 bathrooms.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjIzLTk2YjMtNzM5Zi04OGVkLTNhYjBmZGU5NjI0Ni8wMWEwOTYyNC03Y2RhLTcxMGUtODA0Mi00OTAwNmU2MWVlYjEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjIzLTk2YjMtNzM5Zi04OGVkLTNhYjBmZGU5NjI0Ni8wMWEwOTYyNC03Y2RhLTcxMGUtODA0Mi00OTAwNmU2MWVlYjEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjIzLTk2YjMtNzM5Zi04OGVkLTNhYjBmZGU5NjI0Ni8wMWEwOTYyNC03Y2ZiLTcyMzgtOGE1NS02MTExMDIxYmRmM2QuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjIzLTk2YjMtNzM5Zi04OGVkLTNhYjBmZGU5NjI0Ni8wMWEwOTYyNC03Y2ZiLTcyMzgtOGE1NS02MTExMDIxYmRmM2QuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjIzLTk2YjMtNzM5Zi04OGVkLTNhYjBmZGU5NjI0Ni8wMWEwOTYyNC03YjA4LTcxYzItYmVkMC03MGY5MWY3N2FkZWEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo0OTAsImhlaWdodCI6MzI1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTA5NjIzLTk2YjMtNzM5Zi04OGVkLTNhYjBmZGU5NjI0Ni8wMWEwOTYyNC03YjA4LTcxYzItYmVkMC03MGY5MWY3N2FkZWEuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
