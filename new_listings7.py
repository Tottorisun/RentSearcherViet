# -*- coding: utf-8 -*-
NEW_SRC = r'''
L(305,"da-nang","ns","Квартира",24000000,None,
  "Пентхаус 2 спальни, ул. Nguyễn Thiện Kế — отдельный просторный двор, зона кафе/барбекю.",
  "https://www.facebook.com/groups/253329090046313/posts/1441019157943961/","только что",0,source="facebook",
  details={"notice":"автор Trần Tuấn, контакт +84 325 365 363"}),

L(306,"da-nang","st","Студия",8000000,None,
  "Меблированная студия на ул. Phạm Vấn, район Sơn Trà, максимум 2 человека, стирка на крыше.",
  "https://www.facebook.com/groups/253329090046313/posts/1441023687943508/","недавно",0,source="facebook",
  details={"electricity":"4 000 ₫/кВт·ч","water":"150 000 ₫/чел. (вкл. сервис)","deposit":"1 месяц","contract":"6 месяцев","policy":"принимают иностранцев","notice":"контакт/Zalo 0935 126 743"}),

L(307,"da-nang","st","Квартира",13000000,None,
  "2 спальни, 2 балкона, ул. Thế Lữ, район Sơn Trà, своя стиральная машина, лифт.",
  "https://www.facebook.com/groups/253329090046313/","только что",0,source="facebook",
  details={"electricity":"4 000 ₫/кВт·ч","water":"120 000 ₫/чел.","contract":"6 месяцев","policy":"принимают иностранцев и небольших животных",
           "notice":"автор Bắc House. Прямой ссылки на пост нет — открывает группу"}),

L(308,"da-nang","st","Студия",None,None,
  "Студия P302 со своей кухней и окном, ул. Vũ Tông Phan, район Sơn Trà, общая стиральная машина.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2180745062553153/","только что",0,source="facebook",
  details={"electricity":"4 500 ₫/кВт·ч","water":"150 000 ₫ (вкл. сервис)","notice":"цена только по запросу в Zalo/WhatsApp"}),

L(309,"da-nang","tk","Студия",None,None,
  "Студия №302 на ул. Trần Cao Vân, свободна и готова к заселению сейчас.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2180744729219853/","1 час назад",0,source="facebook",
  details={"notice":"цена не указана, контакт через Zalo/WhatsApp"}),

L(310,"da-nang","ns","Квартира",8800000,38,
  "1-спальная квартира на ул. Phan Tứ, район Ngũ Hành Sơn, полностью меблирована.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2180744892553170/","1 час назад",0,source="facebook",
  details={"policy":"принимают иностранцев","notice":"контакт только через Messenger"}),

L(311,"nha-trang","tl","Студия",3200000,15,
  "Студия на ул. Nguyễn Thiện Thuật, кухня и прачечная на 4 этаже.",
  "https://www.facebook.com/groups/749128438763331/posts/2981750618834424/","недавно",0,source="facebook",
  details={"deposit":"1 месяц","electricity":"4 500 ₫/кВт·ч","water":"120 000 ₫/чел.","notice":"общий сервис-сбор 200 000 ₫/чел., Zalo 0938 418 101"}),

L(312,"nha-trang","tl","Комната",9000000,None,
  "Комната №501 (5 этаж), ул. 35/69 Nguyễn Thiện Thuật.",
  "https://www.facebook.com/groups/749128438763331/posts/2955021024840717/","недавно",0,source="facebook",
  details={"electricity":"4 500 ₫/кВт·ч","water":"150 000 ₫/чел.","notice":"wifi+мусор+управление 100 000 ₫/чел., разрешены животные, без электровелосипедов, свободна с 01.08, тел. 0989 939 192"}),

L(313,"nha-trang","ph","Квартира",12500000,None,
  "1-спальная квартира с балконом, район Hà Quang 2 — Phước Hải.",
  "https://www.facebook.com/groups/749128438763331/posts/2982464848763001/","недавно",0,source="facebook",
  details={"electricity":"4 500 ₫/кВт·ч","water":"200 000 ₫/чел.","notice":"управление+мусор+wifi 250 000 ₫/чел., депозит 1 мес., Zalo 0905 087 168"}),

L(314,"nha-trang","vp","Квартира",7500000,35,
  "1-спальная квартира в переулке Đoàn Trần Nghiệp, север города, балкон/световой колодец, новый ремонт.",
  "https://www.facebook.com/groups/167625939644211/posts/1003639566042840/","недавно",0,source="facebook"),

L(315,"nha-trang","vt","Квартира",9000000,64,
  "2-спальная квартира у рынка Bình Tân (ул. Tô Hiệu), 5 минут до моря, меблирована.",
  "https://www.facebook.com/groups/167625939644211/posts/1000756796331117/","недавно",0,source="facebook",
  details={"deposit":"2 месяца (оплата за 1)","notice":"Zalo/WhatsApp 0905 285 896"}),

L(316,"nha-trang","ps","Квартира",4200000,None,
  "Дуплекс в районе Gò Găng, Vĩnh Điềm Trung.",
  "https://www.facebook.com/groups/167625939644211/posts/1004973992576064/","недавно",0,source="facebook",
  details={"deposit":"1 месяц","electricity":"4 000 ₫/кВт·ч","water":"100 000 ₫/чел."}),

L(317,"nha-trang","ph","Дом",18000000,None,
  "Дом целиком, 4 этажа, 5 спален со своими санузлами, район Phước Hải (ул. Thích Quảng Đức).",
  "https://www.facebook.com/groups/chothuenhanguyencannhatrang/posts/4622871407963854/","недавно",0,source="facebook",
  details={"deposit":"2 месяца + 1 оплата","notice":"площадка для сушки белья, заселение с 1 сентября, тел. 0394 257 517"}),

L(318,"nha-trang","vt","Дом",35000000,300,
  "Новый дом 3 спальни в КДТ Mỹ Gia (район Vĩnh Thái), лифт, терраса, охраняемый район.",
  "https://www.facebook.com/groups/chothuenhanguyencannhatrang/posts/4630872880497040/","недавно",0,source="facebook",
  details={"deposit":"2 месяца (оплата за 2)","contract":"1 год","managementFee":"770 000 ₫/мес","notice":"Zalo 0976 864 740"}),

L(319,"nha-trang","ps","Дом",4000000,None,
  "Одноэтажный дом, 2 спальни, район Chợ Ga (ул. Vĩnh Thạnh), долгосрочный контракт.",
  "https://www.facebook.com/groups/chothuenhanguyencannhatrang/posts/4632286153689046/","недавно",0,source="facebook",
  details={"notice":"тел. 0935 709 788"}),

L(320,"nha-trang","pl","Квартира",10000000,65,
  "Угловая 2-спальная квартира в КДТ Phước Long (CT4 Hud, ул. 28), балкон, качественная мебель.",
  "https://www.facebook.com/groups/chothuecanhonhatrangkhanhhoa/posts/27944490621827590/","недавно",0,source="facebook",
  details={"deposit":"2 месяца (оплата за 2)","notice":"тел. 0989 819 892"}),

L(321,"nha-trang","ps","Квартира",8500000,65,
  "2-спальная квартира в Vĩnh Điềm Trung (CT6), 3 кондиционера, рядом супермаркет Go.",
  "https://www.facebook.com/groups/chothuecanhonhatrangkhanhhoa/posts/27965768696366449/","недавно",0,source="facebook",
  details={"amenities":"3 кондиционера","deposit":"2 месяца (оплата за 2)","contract":"1 год","notice":"тел. 0773 701 937"}),

L(322,"nha-trang","lt","Квартира",14000000,None,
  "2-спальная квартира в ЖК Mường Thanh, 04 Trần Phú, вид на реку и башню Понагар.",
  "https://www.facebook.com/groups/chothuecanhonhatrangkhanhhoa/posts/27910007241942595/","недавно",0,source="facebook",
  details={"managementFee":"700 000 ₫/мес","notice":"паркинг мотоцикла 100 000 ₫/мес, wifi 250 000 ₫/мес"}),

L(323,"da-nang","ns","Дом",18000000,100,
  "Дом целиком, 3 этажа, 4 спальни, район Hói Kiểng (рядом ул. Minh Mạng), полная мебель.",
  "https://www.facebook.com/groups/599988861199745/posts/1857447832120502/","недавно",0,source="facebook",
  details={"amenities":"4 кондиционера, холодильник, стиральная машина","contract":"1-2 года","notice":"тел. 0905 999 196"}),

L(324,"da-nang","ns","Квартира",7500000,None,
  "Новая квартира рядом с Университетом экономики Дананга, район Ngũ Hành Sơn, паркинг в цоколе.",
  "https://www.facebook.com/groups/599988861199745/posts/1856747908857161/","недавно",0,source="facebook",
  details={"notice":"цена 7-8 млн ₫ в зависимости от планировки, тел. 0983 985 800 / 0983 136 134"}),

L(325,"da-nang","hcg","Квартира",6500000,30,
  "1-спальная квартира, район Hòa Cường (Hải Châu), лифт, бесплатная стирка.",
  "https://www.facebook.com/groups/198876884532146/posts/1819268872492931/","недавно",0,source="facebook",
  details={"electricity":"4 000 ₫/кВт·ч","water":"100 000 ₫/чел.","amenities":"бесплатная стирка","notice":"площадь 27-33 м² в зависимости от планировки, тел. 0979 820 348"}),

L(326,"da-nang","hc","Студия",6500000,None,
  "Студия в центре на ул. Đống Đa, рядом рынок Cồn и университет Duy Tân.",
  "https://www.facebook.com/groups/198876884532146/posts/1813916053028213/","недавно",0,source="facebook",
  details={"amenities":"своя стиральная машина","notice":"охрана 24/7, тел. 0846 034 456"}),

L(327,"da-lat","xh","Квартира",4200000,None,
  "1-спальная квартира на ул. Huyền Trân Công Chúa, балкон с видом на сосновый лес.",
  "https://www.facebook.com/groups/356237492011374/posts/1855996578702117/","недавно",0,source="facebook",
  details={"amenities":"бесплатный wifi, солнечный водонагреватель","electricity":"4 000 ₫/кВт·ч","water":"70 000 ₫/чел.","deposit":"1 месяц","notice":"без посредников, тел. 098 357 1317"}),

L(328,"da-lat","xh","Квартира",7000000,None,
  "2-спальная квартира (3 санузла) на ул. Trần Phú, 1 этаж, 700 м от админцентра.",
  "https://www.facebook.com/groups/356237492011374/posts/1850361402598968/","недавно",0,source="facebook",
  details={"deposit":"1 месяц","contract":"1 год","notice":"Zalo 0363 000 532"}),

L(329,"da-lat","xh","Квартира",9000000,None,
  "1-спальная квартира премиум-класса на ул. Lương Thế Vinh, рядом отель Dalat Palace, спальня + антресоль.",
  "https://www.facebook.com/groups/356237492011374/posts/1851224225846019/","недавно",0,source="facebook",
  details={"amenities":"полная мебель","electricity":"2 500 ₫/кВт·ч","water":"24 000 ₫/чел.","deposit":"10 млн ₫","notice":"тел. 0814 467 907"}),

L(330,"da-lat","lv","Дом",6000000,140,
  "Дом целиком, 2 спальни, ул. Mê Linh, район Lâm Viên, солнечный водонагреватель.",
  "https://www.facebook.com/nguyen.hieu.966682/posts/pfbid0oB73YvEAgycraFi51H4fHGrzZHvyJ6Z6k3sQkQSev56pEvPkBa7XP8ENXADXFERCl","недавно",0,source="facebook",
  details={"deposit":"1 месяц (торг уместен)","notice":"заселение с 15 августа, автор Nguyễn Hiếu, тел. 0854 526 727"}),

L(331,"da-lat","xh","Дом",5000000,180,
  "Дом целиком, 3 спальни, ул. Tô Hiến Thành, без мебели.",
  "https://www.facebook.com/nguyen.hieu.966682/posts/pfbid02sW4yCfMCVMPvE3cD2HA4MLGmvysLoqTWHdBTuCC82N5WrLYbsQwSs5G2P8vUU8TRl","недавно",0,source="facebook",
  details={"policy":"без мебели","deposit":"1 месяц","notice":"переулок для мотоциклов в 50 м от дороги, автор Nguyễn Hiếu, тел. 0854 526 727"}),

L(332,"da-lat","cl","Квартира",8000000,None,
  "2-спальная квартира, ул. Ô Tô Thi Sách, район Phường 6, лифт, балкон, большие окна.",
  "https://www.facebook.com/groups/975470559939040/posts/2324368275049255/","недавно",0,source="facebook",
  details={"amenities":"полная мебель, вода включена, wifi бесплатно","deposit":"1 месяц","contract":"от 1 года","notice":"тел. 07745 179 86"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted 28 listings")
