"""Lagmar page marketing layer (13.10.2026): promo banner, add-on options with prices, block stats copy.

Option prices = SmartSpace unit price of the Grenton module (2025 quote) x 1.3 (programming),
plus 20% VAT, rounded up to 10 EUR — same basis as the package "from" prices.
PROMO is a default offer for the owner to approve or change (one place).
"""
import math

from content_v3 import PRICE_UNITS, PROGRAMMING_SHARE
from content_offer import VAT

OPTION_UNITS = {
    "panel": PRICE_UNITS["SP"],            # extra Smart Panel
    "touch": PRICE_UNITS["TP4"],           # extra Touch Panel 4 buttons
    "blinds": PRICE_UNITS["RS"],           # RollerShutter X3 module (3 motors), motors not included
    "dim": PRICE_UNITS["DIM"],             # dimmer module
    "rgbw": 115,                           # RGBW LED module
    "ac": 210 + 320,                       # Modbus gate + CoolMaster (first AC unit)
    "intercom": 360,                       # Akuvox 10" indoor panel
}


def option_price(k):
    return int(math.ceil(round(OPTION_UNITS[k] * (1 + VAT)) * (1 + PROGRAMMING_SHARE) / 10.0) * 10)


OPTION_PRICES = {k: option_price(k) for k in OPTION_UNITS}
OPTION_ICON = {"panel": "P", "touch": "P", "blinds": "C", "dim": "L", "rgbw": "L", "ac": "T", "intercom": "I"}
PROMO_PCT = 10  # % off Grenton equipment

LAGMAR_MKT = {
    "ru": {
        "to_step2": "Выбрать пакет",
        "no_number": "Нет номера под рукой? Выберите по количеству комнат",
        "price_breakdown": "Из чего сложилась цена",
        "show_on_plan": "Показать на похожей планировке",
        "promo_caption": "с акцией −10% на оборудование до 30.06.2027",
        "strip": "Владельцам квартир в Lagmar: −10% на оборудование до 30.06.2027",
        "strip_cta": "Рассчитать",
        "next_title": "Что будет дальше",
        "next1": "Менеджер SmartSpace перезвонит в тот же рабочий день (Пн–Пт 9:00–18:00, Сб 10:00–14:00); на заявки, отправленные позже, — утром следующего рабочего дня.",
        "next2": "Консультация бесплатная — по телефону или в шоуруме на Strada Pajurii 11.",
        "next3": "Точную стоимость назовём после осмотра квартиры — без обязательств.",
        "call_instead": "Удобнее голосом?",
        "done_title": "Заявка отправлена",
        "done_text": "Мы получили ваш выбор. Менеджер SmartSpace перезвонит в тот же рабочий день, чтобы договориться о консультации.",
        "recap_title": "Ваш выбор", "recap_apt": "Квартира", "recap_none": "без опций", "recap_edit": "Изменить пакет или опции",
        "details_label": "Подробный состав пакетов для 2, 3 и 4 комнат", "pk_eyebrow": "Пакеты и цены",
        "faq_sub": "Не нашли ответ? Позвоните или напишите — подскажем пакет под вашу квартиру.",
        "stepper": ["Квартира", "Пакет", "Заявка"],
        "apts": "кв.", "range_hint": "Блок {b}: {c} кв., этажи {from}–{to} · номер вида 507, на партере P101",
        "promo_kicker": "Акция для жильцов Lagmar",
        "promo_title": "−10% на оборудование",
        "promo_text": "При заявке до 30 июня 2027 года. Консультация и предварительный расчёт — бесплатно.",
        "promo_cta": "Получить расчёт со скидкой", "promo_until": "до 30.06.2027",
        "tier_from": "от {p}",
        "opt_eyebrow": "Опции", "opt_title": "Дополните любой пакет",
        "opt_sub": "В цену каждой опции уже входят оборудование и его настройка. Можно добавить сейчас или позже — система расширяется без замены установленного.",
        "opt_s2": "Добавьте опции", "opt_add": "Добавить", "opt_added": "Добавлено",
        "options": {
            "panel": ("Ещё одна Smart Panel", "Экран с термостатом и сценариями — в дополнительной комнате"),
            "touch": ("Touch Panel, 4 кнопки", "Вместо обычного выключателя: свет, шторы, сценарии"),
            "blinds": ("Шторы: модуль на 3 привода", "Ещё три окна со шторами по расписанию (электроприводы оплачиваются отдельно)"),
            "dim": ("Плавная яркость ещё в одной зоне", "Свет без резких перепадов в спальне, гостиной или на кухне"),
            "rgbw": ("LED-подсветка RGBW", "Цветная или тёплая подсветка ниш, потолка, кухни"),
            "ac": ("Кондиционер в системе", "Управление кондиционером с панели и телефона (для одного кондиционера)"),
            "intercom": ("Панель видеодомофона 10″", "Видеть гостя на экране в квартире, а не только в телефоне"),
        },
        "sum_go": "Получить предложение на этот пакет", "sum_go_note": "Без обязательств · перезвоним в тот же рабочий день",
        "trust": "SmartSpace — официальный партнёр Lagmar по умному дому. Гарантия 24 месяца на оборудование с момента установки.",
        "sum_pkg": "Пакет", "sum_opts": "Опции", "sum_total": "Итого", "sum_promo": "По акции −10% на оборудование",
        "sum_note": "Оборудование и программирование, ориентировочно, с НДС. Датчики, приводы штор и монтаж посчитаем в персональном предложении после осмотра — до подписания и без обязательств.",
        "pick_pkg_first": "Выберите пакет выше — и итог посчитается здесь.",
    },
    "ro": {
        "to_step2": "Alege pachetul",
        "no_number": "Sau alege după numărul de camere",
        "price_breakdown": "Cum se formează prețul",
        "show_on_plan": "Vezi pe un plan asemănător",
        "promo_caption": "cu reducerea de 10% la echipamente, valabilă până la 30.06.2027",
        "strip": "Ai apartament în Lagmar? Ai 10% reducere la echipamente până la 30.06.2027",
        "strip_cta": "Calculează prețul",
        "next_title": "Ce urmează",
        "next1": "Te sună un consultant SmartSpace în aceeași zi lucrătoare (Lu–Vi 9:00–18:00, Sâ 10:00–14:00). Dacă cererea ajunge după program, te sunăm în dimineața următoarei zile lucrătoare.",
        "next2": "Consultația e gratuită, la telefon sau în showroomul nostru de pe strada Pajurii 11.",
        "next3": "Prețul exact ți-l spunem după ce vedem apartamentul.",
        "call_instead": "Preferi să vorbim direct?",
        "done_title": "Cererea a fost trimisă",
        "done_text": "Am primit cererea ta. Te sună un consultant SmartSpace în aceeași zi lucrătoare, ca să stabilim consultația.",
        "recap_title": "Alegerea ta", "recap_apt": "Apartament", "recap_none": "fără opțiuni", "recap_edit": "Schimbă pachetul sau opțiunile",
        "details_label": "Componența detaliată a pachetelor pentru 2, 3 și 4 camere", "pk_eyebrow": "Pachete și prețuri",
        "faq_sub": "N-ai găsit răspunsul? Sună-ne sau scrie-ne și îți recomandăm pachetul potrivit.",
        "stepper": ["Apartament", "Pachet", "Cerere"],
        "apts": "ap.", "range_hint": "Blocul {b}: {c} ap., etajele {from}–{to} · numerele arată ca 507, iar la parter ca P101",
        "promo_kicker": "Promoție pentru proprietarii de apartamente Lagmar",
        "promo_title": "−10% la echipamente",
        "promo_text": "Pentru cererile trimise până la 30 iunie 2027. Consultația și calculul preliminar sunt gratuite.",
        "promo_cta": "Primește calculul cu reducere", "promo_until": "până la 30.06.2027",
        "tier_from": "de la {p}",
        "opt_eyebrow": "Opțiuni", "opt_title": "Completează orice pachet",
        "opt_sub": "Fiecare opțiune include modulul și programarea lui. O adaugi acum sau mai târziu: sistemul se extinde fără să schimbi ce e montat.",
        "opt_s2": "Opțiuni suplimentare", "opt_add": "Adaugă", "opt_added": "Adăugat",
        "options": {
            "panel": ("Încă un Smart Panel", "Ecran cu termostat și scenarii în încă o cameră"),
            "touch": ("Touch Panel, 4 butoane", "În locul unui întrerupător obișnuit: lumină, jaluzele, scenarii"),
            "blinds": ("Jaluzele: modul pentru 3 motoare", "Încă trei ferestre cu jaluzele care se mișcă după program (motoarele se plătesc separat)"),
            "dim": ("Lumină reglabilă în încă o zonă", "Lumină blândă seara, puternică atunci când ai nevoie: în dormitor, living sau bucătărie"),
            "rgbw": ("Bandă LED RGBW", "Lumină colorată sau caldă în nișe, pe tavan sau în bucătărie"),
            "ac": ("Aerul condiționat, legat la sistem", "Comanzi aparatul tău de aer condiționat de pe panou și de pe telefon (preț pentru un aparat, fără aparatul propriu-zis)"),
            "intercom": ("Panou de videointerfon, 10″", "Vezi cine sună la ușă pe ecranul din apartament, nu doar pe telefon"),
        },
        "sum_go": "Primește oferta pentru acest pachet", "sum_go_note": "Fără obligații · te sunăm în aceeași zi lucrătoare",
        "trust": "SmartSpace este partener oficial Lagmar pentru casa inteligentă. Garanție de 24 de luni pentru echipamente, de la data montajului.",
        "sum_pkg": "Pachet", "sum_opts": "Opțiuni", "sum_total": "Total", "sum_promo": "Cu reducerea de 10% la echipamente",
        "sum_note": "Preț orientativ pentru echipamente și programare, cu TVA. Senzorii, motoarele pentru jaluzele și montajul le calculăm în oferta personalizată, după vizită. O primești înainte să semnezi ceva și nu te obligă la nimic.",
        "pick_pkg_first": "Alege un pachet mai sus și totalul apare aici.",
    },
    "en": {
        "to_step2": "Choose a package",
        "no_number": "Or simply choose by number of rooms",
        "price_breakdown": "What the price is made of",
        "show_on_plan": "Show on a similar floor plan",
        "promo_caption": "with 10% off equipment until 30 June 2027",
        "strip": "Lagmar residents: 10% off equipment until 30 June 2027",
        "strip_cta": "Calculate",
        "next_title": "What happens next",
        "next1": "A SmartSpace manager will call you the same working day (Mon–Fri 9:00–18:00, Sat 10:00–14:00); requests sent later get a call the next working morning.",
        "next2": "The consultation is free — by phone or at the showroom on Strada Pajurii 11.",
        "next3": "We'll confirm the exact price after visiting your apartment, with no obligation.",
        "call_instead": "Prefer to talk?",
        "done_title": "Request sent",
        "done_text": "We've received your selection. A SmartSpace manager will call you the same working day to arrange the consultation.",
        "recap_title": "Your choice", "recap_apt": "Apartment", "recap_none": "no options", "recap_edit": "Change package or options",
        "details_label": "Detailed package contents for 2, 3 and 4 rooms", "pk_eyebrow": "Packages and prices",
        "faq_sub": "Didn't find the answer? Call or message us and we will suggest the right package.",
        "stepper": ["Apartment", "Package", "Request"],
        "apts": "apts", "range_hint": "Block {b}: {c} apts, floors {from}–{to} · numbers look like 507, ground floor P101",
        "promo_kicker": "Offer for Lagmar residents",
        "promo_title": "10% off equipment",
        "promo_text": "For requests sent by 30 June 2027. Consultation and preliminary estimate are free.",
        "promo_cta": "Get a discounted estimate", "promo_until": "until 30 June 2027",
        "tier_from": "from {p}",
        "opt_eyebrow": "Options", "opt_title": "Add to any package",
        "opt_sub": "Each option includes the module and its programming. Add it now or later — the system grows without replacing what is installed.",
        "opt_s2": "Add options", "opt_add": "Add", "opt_added": "Added",
        "options": {
            "panel": ("One more Smart Panel", "OLED screen and scenes in one more room"),
            "touch": ("Touch Panel, 4 buttons", "Instead of a plain switch: light, blinds, scenes"),
            "blinds": ("Blinds: module for 3 motors", "Three more windows with scheduled blinds (motors not included)"),
            "dim": ("Dimming for one more zone", "Smooth brightness in the bedroom, living room or kitchen"),
            "rgbw": ("RGBW LED lighting", "Coloured or warm light for niches, ceiling, kitchen"),
            "ac": ("Air conditioning in the system", "Control your air conditioner from the panel and phone (price for the first unit)"),
            "intercom": ("10″ video intercom panel", "See the visitor on a screen in the apartment, not only on the phone"),
        },
        "sum_go": "Get the quote for this package", "sum_go_note": "No obligation · we call the same working day",
        "trust": "SmartSpace is Lagmar's official smart-home partner. 24-month warranty on equipment from installation.",
        "sum_pkg": "Package", "sum_opts": "Options", "sum_total": "Total", "sum_promo": "With 10% off equipment",
        "sum_note": "Equipment and programming, indicative, incl. VAT. Sensors, blind motors and installation are priced in your personal quote after our visit — before you sign, with no obligation.",
        "pick_pkg_first": "Pick a package above and the total appears here.",
    },
}

HOME_LG = {
    "ru": {"h1": "Умный дом в вашей квартире Lagmar уже начат",
           "lead": "Lagmar установил контроллер в электрощит каждой квартиры Smart Home 1 и Smart Home 2. Вы платите только за то, что добавляете: свет, тепло, шторы, защиту от протечки. Цену для своей квартиры узнаете за 2 минуты.",
           "cta": "Рассчитать цену для моей квартиры",
           "film": "Один день в квартире"},
    "ro": {"h1": "Casa inteligentă e deja începută în apartamentul tău din Lagmar",
           "lead": "Lagmar a montat unitatea centrală în tabloul fiecărui apartament din Smart Home 1 și Smart Home 2. Tu plătești doar ce adaugi: lumină, căldură, jaluzele, protecție la inundații. Prețul pentru apartamentul tău îl afli în 2 minute.",
           "cta": "Calculează prețul pentru apartamentul tău",
           "film": "Vezi o zi în apartament"},
    "en": {"h1": "The smart home in your Lagmar apartment is already started",
           "lead": "Lagmar has fitted the controller in the switchboard of every apartment in Smart Home 1 and Smart Home 2. You pay only for what you add: lighting, heating, blinds, leak protection. The price for your apartment takes 2 minutes.",
           "cta": "Get a price for my apartment",
           "film": "See a day in the apartment"},
}
