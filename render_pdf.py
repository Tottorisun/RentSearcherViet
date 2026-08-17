# -*- coding: utf-8 -*-
exec(open("build_pdf.py", encoding="utf-8").read())

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                 HRFlowable, KeepTogether)

styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitleRU", fontName="Body-Bold", fontSize=19, leading=23,
                              textColor=colors.HexColor("#173B2B"), spaceAfter=4)
subtitle_style = ParagraphStyle("SubtitleRU", fontName="Body", fontSize=10.5, leading=14,
                                 textColor=colors.HexColor("#55624F"), spaceAfter=14)
section_style = ParagraphStyle("SectionRU", fontName="Body-Bold", fontSize=13.5, leading=16,
                                textColor=colors.white, spaceBefore=0, spaceAfter=0,
                                backColor=colors.HexColor("#1E7A4C"), borderPadding=(6,8,6,8))
card_title_style = ParagraphStyle("CardTitle", fontName="Body-Bold", fontSize=11.5, leading=14,
                                   textColor=colors.HexColor("#14201A"))
price_style = ParagraphStyle("Price", fontName="Body-Bold", fontSize=13, leading=15,
                              textColor=colors.HexColor("#A86A1B"))
meta_style = ParagraphStyle("Meta", fontName="Body", fontSize=9.5, leading=13,
                             textColor=colors.HexColor("#55624F"))
body_style = ParagraphStyle("Body", fontName="Body", fontSize=9.7, leading=13.5,
                             textColor=colors.HexColor("#22291F"), spaceBefore=4)
link_style = ParagraphStyle("Link", fontName="Body", fontSize=9.3, leading=13,
                             textColor=colors.HexColor("#1E7A4C"))
note_style = ParagraphStyle("Note", fontName="Body", fontSize=8.7, leading=12,
                             textColor=colors.HexColor("#8A6A2A"))
footer_style = ParagraphStyle("Footer", fontName="Body", fontSize=8.3, leading=11.5,
                               textColor=colors.HexColor("#8A9480"))

SRC_LABEL = {"chotot": "Chợ Tốt / Nhà Tốt", "batdongsan": "Batdongsan.com.vn", "facebook": "Facebook"}
SRC_COLOR = {"chotot": "#C7452B", "batdongsan": "#E0862B", "facebook": "#3B5FA6"}

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace("₫","VND").replace("’","'"))

def make_card(item, source_key, index):
    src = SRC_LABEL[source_key]
    col = SRC_COLOR[source_key]
    pill = f'<font color="{col}"><b>{src}</b></font>'
    header = Paragraph(f'{index}. {esc(item["title"])}', card_title_style)
    pricebar = Paragraph(f'{pill} &nbsp;&nbsp;·&nbsp;&nbsp; <b>{esc(item["price"])}</b> &nbsp;·&nbsp; {esc(item["area"])}', meta_style)
    price_big = Paragraph(esc(item["price"]), price_style)
    district = Paragraph(f'Район: <b>{esc(item["district"])}</b>', meta_style)
    addr = Paragraph(f'Адрес: {esc(item["address"])} — <link href="{gmaps(item["address"])}" color="#1E7A4C">открыть в Google Картах</link>', link_style)
    phone = Paragraph(f'Телефон: {esc(item["phone"])}', meta_style)
    desc = Paragraph(esc(item["desc"]), body_style)
    linktxt = "ссылка на пост (поиск в группе)" if source_key=="facebook" else "ссылка на объявление"
    link = Paragraph(f'<link href="{item["url"]}" color="#1E7A4C">Открыть {linktxt} &#8594;</link>', link_style)
    rows = [header, Spacer(1,3), pricebar, Spacer(1,2), district, addr, phone, desc]
    if item.get("note"):
        rows.append(Paragraph(esc(item["note"]), note_style))
    rows.append(Spacer(1,3))
    rows.append(link)
    rows.append(Spacer(1,10))
    rows.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#DAE2CC"), spaceAfter=10))
    return KeepTogether(rows) if False else rows  # allow natural breaks between fields but keep header+price together

def section_header(text):
    t = Table([[Paragraph(text, section_style)]], colWidths=[170*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#1E7A4C")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    return t

doc = SimpleDocTemplate("Aренда_Nha_Trang_do_10mln.pdf", pagesize=A4,
                         leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm,
                         title="Аренда квартир в Нячанге до 10 млн ₫/мес",
                         author="Жильё во Вьетнаме")

story = []
story.append(Paragraph("Аренда квартир в Нячанге — до 10 млн ₫/мес включительно", title_style))
story.append(Paragraph(
    f"Подборка от 15.08.2026 · {len(CHOTOT)} объявлений с Chợ Tốt · {len(BATDONGSAN)} с Batdongsan.com.vn · "
    f"{len(FACEBOOK)} из Facebook-групп · сортировка по возрастанию цены внутри каждого источника",
    subtitle_style))

story.append(section_header(f"Chợ Tốt / Nhà Tốt — {len(CHOTOT)} объявлений"))
story.append(Spacer(1,8))
for i, item in enumerate(CHOTOT, 1):
    story += make_card(item, "chotot", i)

story.append(Spacer(1, 4))
story.append(section_header(f"Batdongsan.com.vn — {len(BATDONGSAN)} объявления"))
story.append(Spacer(1,8))
for i, item in enumerate(BATDONGSAN, 1):
    story += make_card(item, "batdongsan", i)

story.append(Spacer(1, 4))
story.append(section_header(f"Facebook-группа «Căn hộ cho thuê Nha Trang» — {len(FACEBOOK)} постов"))
story.append(Spacer(1,8))
for i, item in enumerate(FACEBOOK, 1):
    story += make_card(item, "facebook", i)

story.append(Spacer(1, 6))
story.append(Paragraph(
    "Фото не встроены в PDF намеренно — вместо копирования чужих фотографий каждая карточка ссылается "
    "на оригинальное объявление, где фото смотрятся живьём и всегда актуальны. "
    "Телефоны у части объявлений на Chợ Tốt скрыты сайтом до нажатия «Hiện SĐT» — писать "
    "через встроенный чат тоже можно. Перед звонком/переводом денег всегда проверяйте актуальность "
    "цены и наличие по ссылке — объявления могут закрываться.", footer_style))

doc.build(story)
print("PDF built.")
