# -*- coding: utf-8 -*-
"""dotproperty.com.ph, автоматический сбор: 2 объявлений, 2026-10-14.

Партию собрал collect_dotproperty.py -- без модели в контуре. Район взят из
разметки объявления (точное совпадение с CITIES либо однозначный прецедент на
сайте), описание собрано из полей разметки, возраст выведен из UUIDv7 в
идентификаторе записи и не превышает 7 дней.

Объявления, локальность которых не совпала ни с одним нашим районом и не имеет
однозначного прецедента, пропущены, а не приписаны к соседнему.
"""
from listing_lock import insert_listings

IDS = [3002206, 3002207]

N_RU = "Описание собрано программой из разметки объявления на dotproperty.com.ph — тип, спальни, санузлы, площадь, локальность и цена. Рекламный текст объявления не пересказан. Район поставлен по локальности из той же разметки; она изредка расходится с адресом в тексте объявления, поэтому адрес стоит сверить по ссылке. Дату размещения портал не публикует: возраст выведен из идентификатора записи (UUIDv7 хранит время создания) и означает «не моложе»."
N_EN = "This description was assembled by a program from the ad's own schema.org markup on dotproperty.com.ph — type, bedrooms, bathrooms, size, locality and price. The ad's marketing text is not retold. The district comes from the locality in that same markup, which occasionally disagrees with the address written in the ad, so check the address at the source. The portal publishes no posting date: the age is derived from the record id (a UUIDv7 carries its creation time) and means 'no newer than'."

NEW_SRC = r'''
L(3002206,"cebu","tlm","Дом",130000,331,
  "4-спальный дом, 331 м², Talamban, Себу — 4 санузла.",
  "https://www.dotproperty.com.ph/ads/4-bedroom-house-for-rent-in-talamban-cebu_59fd5fa0b94e-2bb0-9552-809c-0f168f89","сегодня",0,source="dotproperty",cur="PHP",
  descEn="4-bedroom house, 331 m², Talamban, Cebu City — 4 bathrooms.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGE5LWQwOTEtNzQ0MC05ZWU3LWI1MGU5ZmE0Y2EwNC93YXRlcm1hcmsvMDFhMTM4YjMtNjkyOS03MDQ2LWEzY2UtOGI5NDg4MWVmN2M4LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6MTE3MCwiaGVpZ2h0Ijo3ODAsImZpdCI6ImNvdmVyIn19fQ==", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGE5LWQwOTEtNzQ0MC05ZWU3LWI1MGU5ZmE0Y2EwNC93YXRlcm1hcmsvMDFhMTM4YjMtNjkyOS03MDQ2LWEzY2UtOGI5NDg4MWVmN2M4LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6Mjc1LCJoZWlnaHQiOjE1NSwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGE5LWQwOTEtNzQ0MC05ZWU3LWI1MGU5ZmE0Y2EwNC93YXRlcm1hcmsvMDFhMTM4YjMtNjkyOS03MDQ2LWEzY2UtOGI5NDg4MWVmN2M4LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6OTYsImhlaWdodCI6NjQsImZpdCI6ImNvdmVyIn19fQ==", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGE5LWQwOTEtNzQ0MC05ZWU3LWI1MGU5ZmE0Y2EwNC93YXRlcm1hcmsvMDFhMTM4YjQtM2IyNS03MmJjLWFkYTEtZDg4MmE5YzUzZGM1LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6MTE3MCwiaGVpZ2h0Ijo3ODAsImZpdCI6ImNvdmVyIn19fQ==", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGE5LWQwOTEtNzQ0MC05ZWU3LWI1MGU5ZmE0Y2EwNC93YXRlcm1hcmsvMDFhMTM4YjQtM2IyNS03MmJjLWFkYTEtZDg4MmE5YzUzZGM1LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6Mjc1LCJoZWlnaHQiOjE1NSwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGE5LWQwOTEtNzQ0MC05ZWU3LWI1MGU5ZmE0Y2EwNC93YXRlcm1hcmsvMDFhMTM4YjQtM2IyNS03MmJjLWFkYTEtZDg4MmE5YzUzZGM1LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6OTYsImhlaWdodCI6NjQsImZpdCI6ImNvdmVyIn19fQ=="], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002207,"cebu","bnl","Дом",70000,250,
  "3-спальный дом, 250 м², Banilad, Себу — 3 санузла.",
  "https://www.dotproperty.com.ph/ads/3-bedroom-house-for-rent-in-banilad-cebu_bde77210fc94-115e-1a82-e08c-fc168f89","сегодня",0,source="dotproperty",cur="PHP",
  descEn="3-bedroom house, 250 m², Banilad, Cebu City — 3 bathrooms.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGRhLWQxOWItNzFmOC1iNDg4LTUwZGE5ODcyMmJjZS8wMWExMzhkYy1jN2M1LTcxMjUtOWE1Zi1jYmY5NzdiYTQzMTAuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGRhLWQxOWItNzFmOC1iNDg4LTUwZGE5ODcyMmJjZS8wMWExMzhkYy1jN2M1LTcxMjUtOWE1Zi1jYmY5NzdiYTQzMTAuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGRhLWQxOWItNzFmOC1iNDg4LTUwZGE5ODcyMmJjZS8wMWExMzhkYy1jN2M1LTcxMjUtOWE1Zi1jYmY5NzdiYTQzMTAuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoyNzUsImhlaWdodCI6MTU1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGRhLWQxOWItNzFmOC1iNDg4LTUwZGE5ODcyMmJjZS8wMWExMzhkYy1jN2U2LTczMDEtYTk5OC0xNDQ0ZWFkYjhjZjkuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGRhLWQxOWItNzFmOC1iNDg4LTUwZGE5ODcyMmJjZS8wMWExMzhkYy1jN2U2LTczMDEtYTk5OC0xNDQ0ZWFkYjhjZjkuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTEzOGRhLWQxOWItNzFmOC1iNDg4LTUwZGE5ODcyMmJjZS8wMWExMzhkYy1jNmM1LTcyODQtYmYwYi1jNzVhMGM4ZGFmZjYuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo0OTAsImhlaWdodCI6MzI1LCJmaXQiOiJjb3ZlciJ9fX0="], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
