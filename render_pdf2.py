# -*- coding: utf-8 -*-
exec(open("build_pdf2.py", encoding="utf-8").read())

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

CANDIDATES = [r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf", r"C:\Windows\Fonts\calibri.ttf"]
CANDIDATES_BOLD = [r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\calibrib.ttf"]
font_regular = next((f for f in CANDIDATES if os.path.exists(f)), None)
font_bold = next((f for f in CANDIDATES_BOLD if os.path.exists(f)), None)
pdfmetrics.registerFont(TTFont("Body", font_regular))
pdfmetrics.registerFont(TTFont("Body-Bold", font_bold or font_regular))

title_style = ParagraphStyle("TitleRU", fontName="Body-Bold", fontSize=18, leading=22,
                              textColor=colors.HexColor("#173B2B"), spaceAfter=4)
subtitle_style = ParagraphStyle("SubtitleRU", fontName="Body", fontSize=10, leading=14,
                                 textColor=colors.HexColor("#55624F"), spaceAfter=6)
disclaimer_style = ParagraphStyle("Disc", fontName="Body", fontSize=8.6, leading=12,
                                   textColor=colors.HexColor("#8A6A2A"), spaceAfter=14)
section_style = ParagraphStyle("SectionRU", fontName="Body-Bold", fontSize=13, leading=16,
                                textColor=colors.white)
card_title_style = ParagraphStyle("CardTitle", fontName="Body-Bold", fontSize=11, leading=13.5,
                                   textColor=colors.HexColor("#14201A"))
price_style = ParagraphStyle("Price", fontName="Body-Bold", fontSize=12.5, leading=15,
                              textColor=colors.HexColor("#A86A1B"))
meta_style = ParagraphStyle("Meta", fontName="Body", fontSize=9.3, leading=13,
                             textColor=colors.HexColor("#55624F"))
body_style = ParagraphStyle("Body", fontName="Body", fontSize=9.5, leading=13.2,
                             textColor=colors.HexColor("#22291F"), spaceBefore=3)
amenity_style = ParagraphStyle("Amenity", fontName="Body", fontSize=9, leading=12.5,
                                textColor=colors.HexColor("#1E7A4C"), spaceBefore=3,
                                backColor=colors.HexColor("#EDF3E7"), borderPadding=(4,5,4,5))
link_style = ParagraphStyle("Link", fontName="Body-Bold", fontSize=10, leading=14,
                             textColor=colors.HexColor("#1E7A4C"), spaceBefore=5)
note_style = ParagraphStyle("Note", fontName="Body", fontSize=8.4, leading=11.5,
                             textColor=colors.HexColor("#8A6A2A"))
footer_style = ParagraphStyle("Footer", fontName="Body", fontSize=8.2, leading=11.3,
                               textColor=colors.HexColor("#8A9480"))

SRC_LABEL = {"chotot": "Chợ Tốt / Nhà Tốt", "batdongsan": "Batdongsan.com.vn", "facebook": "Facebook"}
SRC_COLOR = {"chotot": "#C7452B", "batdongsan": "#E0862B", "facebook": "#3B5FA6"}

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("₫","VND"))

def make_card(item, source_key, index):
    col = SRC_COLOR[source_key]
    header = Paragraph(f'{index}. {esc(item["title"])}', card_title_style)
    price_line = Paragraph(f'<font color="{col}"><b>{esc(SRC_LABEL[source_key])}</b></font> &nbsp;·&nbsp; <b>{esc(item["price"])}</b> &nbsp;·&nbsp; {esc(item["area"])} &nbsp;·&nbsp; район <b>{esc(item["district"])}</b>', meta_style)
    addr = Paragraph(f'Адрес: {esc(item["address"])} — <link href="{gmaps(item["address"])}" color="#1E7A4C">открыть в Google Картах</link>', meta_style)
    phone = Paragraph(f'Телефон: {esc(item["phone"])}', meta_style)
    desc = Paragraph(esc(item["desc"]), body_style)
    amenity = Paragraph("🔧 " + esc(item["amenity_note"]), amenity_style)
    linktxt = "Смотреть фото и полный пост &#8594;" if source_key=="facebook" else "Смотреть фото и объявление &#8594;"
    link = Paragraph(f'<link href="{item["url"]}" color="#1E7A4C">{linktxt}</link>', link_style)
    rows = [header, Spacer(1,3), price_line, Spacer(1,2), addr, phone, desc, Spacer(1,3), amenity]
    if item.get("note"):
        rows.append(Spacer(1,2))
        rows.append(Paragraph(esc(item["note"]), note_style))
    rows.append(link)
    rows.append(Spacer(1,10))
    rows.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#DAE2CC"), spaceAfter=10))
    return rows

def section_header(text):
    t = Table([[Paragraph(text, section_style)]], colWidths=[174*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#1E7A4C")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    return t

doc = SimpleDocTemplate("Nha_Trang_6_9mln.pdf", pagesize=A4,
                         leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm,
                         title="Аренда квартир в Нячанге 6-9 млн VND/мес",
                         author="Жильё во Вьетнаме")

total = len(CHOTOT) + len(BATDONGSAN) + len(FACEBOOK)
story = []
story.append(Paragraph("Аренда квартир в Нячанге — 6&#8211;9 млн ₫/мес", title_style))
story.append(Paragraph(
    f"Подборка на 15.08.2026 · {total} объявлений: {len(CHOTOT)} с Chợ Tốt, {len(BATDONGSAN)} с Batdongsan.com.vn, "
    f"{len(FACEBOOK)} из Facebook-группы «Căn hộ cho thuê Nha Trang» · внутри раздела — по возрастанию цены",
    subtitle_style))
story.append(Paragraph(
    "Фото не встроены — вместо копирования чужих фотографий каждая карточка ведёт прямой ссылкой "
    "на оригинал, где все фото живые и актуальные (кнопка «Смотреть фото и объявление» под каждой карточкой).",
    disclaimer_style))

story.append(section_header(f"1. Chợ Tốt / Nhà Tốt — {len(CHOTOT)} объявлений"))
story.append(Spacer(1,8))
for i, item in enumerate(CHOTOT, 1):
    story += make_card(item, "chotot", i)

story.append(Spacer(1, 4))
story.append(section_header(f"2. Batdongsan.com.vn — {len(BATDONGSAN)} объявления"))
story.append(Spacer(1,8))
for i, item in enumerate(BATDONGSAN, 1):
    story += make_card(item, "batdongsan", i)

story.append(Spacer(1, 4))
story.append(section_header(f"3. Facebook — {len(FACEBOOK)} постов"))
story.append(Spacer(1,8))
for i, item in enumerate(FACEBOOK, 1):
    story += make_card(item, "facebook", i)

story.append(Spacer(1, 6))
story.append(Paragraph(
    "О технике (🔧): большинство вьетнамских объявлений пишут просто «полностью меблировано» без "
    "детального списка бытовой техники — это норма для рынка, а не пробел в подборке. Где в тексте или "
    "на фото было видно что-то конкретное (стиральная машина, кухня, кондиционер) — отмечено отдельно. "
    "Рабочее место как отдельная опция во вьетнамских объявлениях почти никогда не упоминается — "
    "уточняйте у хозяина при просмотре. Телефоны на Chợ Tốt и Batdongsan частично скрыты сайтом до "
    "нажатия «Hiện SĐT» / «Hiện số» — писать через встроенный чат тоже можно. Перед переводом денег "
    "всегда проверяйте актуальность цены и наличие по ссылке.", footer_style))

doc.build(story)
print("PDF built:", len(CHOTOT)+len(BATDONGSAN)+len(FACEBOOK), "listings")
