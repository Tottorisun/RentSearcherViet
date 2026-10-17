# -*- coding: utf-8 -*-
"""dotproperty.com.ph, автоматический сбор: 2 объявлений, 2026-10-17.

Партию собрал collect_dotproperty.py -- без модели в контуре. Район взят из
разметки объявления (точное совпадение с CITIES либо однозначный прецедент на
сайте), описание собрано из полей разметки, возраст выведен из UUIDv7 в
идентификаторе записи и не превышает 7 дней.

Объявления, локальность которых не совпала ни с одним нашим районом и не имеет
однозначного прецедента, пропущены, а не приписаны к соседнему.
"""
from listing_lock import insert_listings

IDS = [3002249, 3002250]

N_RU = "Описание собрано программой из разметки объявления на dotproperty.com.ph — тип, спальни, санузлы, площадь, локальность и цена. Рекламный текст объявления не пересказан. Район поставлен по локальности из той же разметки; она изредка расходится с адресом в тексте объявления, поэтому адрес стоит сверить по ссылке. Дату размещения портал не публикует: возраст выведен из идентификатора записи (UUIDv7 хранит время создания) и означает «не моложе»."
N_EN = "This description was assembled by a program from the ad's own schema.org markup on dotproperty.com.ph — type, bedrooms, bathrooms, size, locality and price. The ad's marketing text is not retold. The district comes from the locality in that same markup, which occasionally disagrees with the address written in the ad, so check the address at the source. The portal publishes no posting date: the age is derived from the record id (a UUIDv7 carries its creation time) and means 'no newer than'."

NEW_SRC = r'''
L(3002249,"cebu","lah","Квартира",80000,139,
  "3-спальная квартира, 139 м², Lahug, Себу — 2 санузла.",
  "https://www.dotproperty.com.ph/ads/3-bedroom-condo-for-sale-or-rent-in-lahug-cebu_89c6712761b0-7dc0-9af2-5d68-39158f89","сегодня",0,source="dotproperty",cur="PHP",
  descEn="3-bedroom flat, 139 m², Lahug, Cebu City — 2 bathrooms.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0ODA2LTEzYzQtN2FmMC05ZGMyLTllODMyNzgyM2QwMS93YXRlcm1hcmsvMDFhMTQ4MjctOWQ4Zi03MDY3LWE5YWMtY2I0OGQxYzg2NDI5LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6MTE3MCwiaGVpZ2h0Ijo3ODAsImZpdCI6ImNvdmVyIn19fQ==", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0ODA2LTEzYzQtN2FmMC05ZGMyLTllODMyNzgyM2QwMS93YXRlcm1hcmsvMDFhMTQ4MjctOWQ4Zi03MDY3LWE5YWMtY2I0OGQxYzg2NDI5LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6Mjc1LCJoZWlnaHQiOjE1NSwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0ODA2LTEzYzQtN2FmMC05ZGMyLTllODMyNzgyM2QwMS93YXRlcm1hcmsvMDFhMTQ4MjctOWQ4Zi03MDY3LWE5YWMtY2I0OGQxYzg2NDI5LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6OTYsImhlaWdodCI6NjQsImZpdCI6ImNvdmVyIn19fQ==", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0ODA2LTEzYzQtN2FmMC05ZGMyLTllODMyNzgyM2QwMS93YXRlcm1hcmsvMDFhMTQ4MjctOWU1ZC03MTgyLWJhNzQtNTVjYzMxYTFmYjdmLmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6MTE3MCwiaGVpZ2h0Ijo3ODAsImZpdCI6ImNvdmVyIn19fQ==", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0ODA2LTEzYzQtN2FmMC05ZGMyLTllODMyNzgyM2QwMS93YXRlcm1hcmsvMDFhMTQ4MjctOWU1ZC03MTgyLWJhNzQtNTVjYzMxYTFmYjdmLmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6OTYsImhlaWdodCI6NjQsImZpdCI6ImNvdmVyIn19fQ==", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0ODA2LTEzYzQtN2FmMC05ZGMyLTllODMyNzgyM2QwMS93YXRlcm1hcmsvMDFhMTQ4MjctOWU4NC03M2QzLWI2NDMtMWUxYTQzNzM5YjI1LmpwZyIsImJyYW5kIjoiZG90cHJvcGVydHkiLCJlZGl0cyI6eyJyb3RhdGUiOm51bGwsInJlc2l6ZSI6eyJ3aWR0aCI6MTE3MCwiaGVpZ2h0Ijo3ODAsImZpdCI6ImNvdmVyIn19fQ=="], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002250,"cebu","bnl","Дом",80000,180,
  "3-спальный дом, 180 м², Banilad, Себу — 3 санузла.",
  "https://www.dotproperty.com.ph/ads/3-bedroom-house-for-rent-in-banilad-cebu_ee1a7738baf1-4710-f142-977f-fc258f89","сегодня",0,source="dotproperty",cur="PHP",
  descEn="3-bedroom house, 180 m², Banilad, Cebu City — 3 bathrooms.",
  details={"photos": ["https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0N2RhLWEyMjAtNzU4YS05ODI1LThhZmUxNjIyZjhiYi8wMWExNDdkZS05Y2JiLTczYjgtYTI5My1lNzFlMDQxZTNjNTQuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0N2RhLWEyMjAtNzU4YS05ODI1LThhZmUxNjIyZjhiYi8wMWExNDdkZS05Y2JiLTczYjgtYTI5My1lNzFlMDQxZTNjNTQuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0N2RhLWEyMjAtNzU4YS05ODI1LThhZmUxNjIyZjhiYi8wMWExNDdkZS05Y2UwLTcwMzctYWMzYS04MmVmMTIyZjQ0MTIuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0N2RhLWEyMjAtNzU4YS05ODI1LThhZmUxNjIyZjhiYi8wMWExNDdkZS05Y2UwLTcwMzctYWMzYS04MmVmMTIyZjQ0MTIuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjoxMTcwLCJoZWlnaHQiOjc4MCwiZml0IjoiY292ZXIifX19", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0N2RhLWEyMjAtNzU4YS05ODI1LThhZmUxNjIyZjhiYi8wMWExNDdkZS05YjI3LTcyNjEtYWM0Zi0xYWJlODFjMmYyNmYuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo0OTAsImhlaWdodCI6MzI1LCJmaXQiOiJjb3ZlciJ9fX0=", "https://pix.dotproperty.co.th/eyJidWNrZXQiOiJwcmQtbGlmdWxsY29ubmVjdC1iYWNrZW5kLWIyYi1pbWFnZXMiLCJrZXkiOiJwcm9wZXJ0aWVzLzAxYTE0N2RhLWEyMjAtNzU4YS05ODI1LThhZmUxNjIyZjhiYi8wMWExNDdkZS05YjI3LTcyNjEtYWM0Zi0xYWJlODFjMmYyNmYuanBnIiwiYnJhbmQiOiJkb3Rwcm9wZXJ0eSIsImVkaXRzIjp7InJvdGF0ZSI6bnVsbCwicmVzaXplIjp7IndpZHRoIjo5NiwiaGVpZ2h0Ijo2NCwiZml0IjoiY292ZXIifX19"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
