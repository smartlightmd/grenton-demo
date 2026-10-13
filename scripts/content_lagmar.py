"""Lagmar page marketing layer (13.10.2026): promo banner, add-on options with prices, block stats copy.

Option prices = SmartSpace unit price of the Grenton module (2025 quote) x 1.3 (programming),
rounded up to 10 EUR, VAT excluded — same basis as the package "from" prices.
PROMO is a default offer for the owner to approve or change (one place).
"""
import math

from content_v3 import PRICE_UNITS, PROGRAMMING_SHARE

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
    return int(math.ceil(OPTION_UNITS[k] * (1 + PROGRAMMING_SHARE) / 10.0) * 10)


OPTION_PRICES = {k: option_price(k) for k in OPTION_UNITS}
OPTION_ICON = {"panel": "P", "touch": "P", "blinds": "C", "dim": "L", "rgbw": "L", "ac": "T", "intercom": "I"}
PROMO_PCT = 10  # % off Grenton equipment

LAGMAR_MKT = {
    "ru": {
        "apts": "кв.", "range_hint": "Блок {b}: {c} кв., номера {from}–{to}",
        "promo_kicker": "Акция для жильцов Lagmar",
        "promo_title": "−10% на оборудование Grenton",
        "promo_text": "При заявке до 31 декабря 2026 года. Консультация и предварительный расчёт — бесплатно.",
        "promo_cta": "Получить расчёт со скидкой", "promo_until": "до 31.12.2026",
        "tier_from": "от {p}",
        "opt_eyebrow": "Опции", "opt_title": "Дополните любой пакет",
        "opt_sub": "Каждая опция — модуль Grenton с программированием. Можно добавить сейчас или позже — система расширяется без замены установленного.",
        "opt_s2": "Добавьте опции", "opt_add": "Добавить", "opt_added": "Добавлено",
        "options": {
            "panel": ("Ещё одна Smart Panel", "OLED-экран и сценарии ещё в одной комнате"),
            "touch": ("Touch Panel, 4 кнопки", "Вместо обычного выключателя: свет, шторы, сцены"),
            "blinds": ("Шторы: модуль на 3 привода", "Ещё три окна со шторами по расписанию (приводы отдельно)"),
            "dim": ("Диммирование ещё 2 зон", "Плавная яркость в спальне, гостиной или на кухне"),
            "rgbw": ("LED-подсветка RGBW", "Цветная или тёплая подсветка ниш, потолка, кухни"),
            "ac": ("Кондиционер в системе", "Управление кондиционером с панели и телефона (первый блок)"),
            "intercom": ("Панель видеодомофона 10″", "Видеть гостя на экране в квартире, а не только в телефоне"),
        },
        "sum_pkg": "Пакет", "sum_opts": "Опции", "sum_total": "Итого", "sum_promo": "По акции −10% на оборудование",
        "sum_note": "Ориентировочно, без НДС. Точная сумма — в персональном предложении после осмотра.",
        "pick_pkg_first": "Выберите пакет выше — и итог посчитается здесь.",
    },
    "ro": {
        "apts": "ap.", "range_hint": "Blocul {b}: {c} ap., numere {from}–{to}",
        "promo_kicker": "Ofertă pentru locatarii Lagmar",
        "promo_title": "−10% la echipamentele Grenton",
        "promo_text": "Pentru cererile trimise până la 31 decembrie 2026. Consultația și calculul preliminar — gratuit.",
        "promo_cta": "Primește calculul cu reducere", "promo_until": "până la 31.12.2026",
        "tier_from": "de la {p}",
        "opt_eyebrow": "Opțiuni", "opt_title": "Completează orice pachet",
        "opt_sub": "Fiecare opțiune e un modul Grenton cu programare. O poți adăuga acum sau mai târziu — sistemul se extinde fără a înlocui ce e montat.",
        "opt_s2": "Adaugă opțiuni", "opt_add": "Adaugă", "opt_added": "Adăugat",
        "options": {
            "panel": ("Încă un Smart Panel", "Ecran OLED și scenarii în încă o cameră"),
            "touch": ("Touch Panel, 4 butoane", "În locul unui întrerupător: lumină, rulouri, scene"),
            "blinds": ("Rulouri: modul pentru 3 motoare", "Încă trei ferestre cu rulouri după program (motoarele separat)"),
            "dim": ("Reglaj de intensitate pentru încă 2 zone", "Lumină lină în dormitor, living sau bucătărie"),
            "rgbw": ("Iluminat LED RGBW", "Lumină colorată sau caldă în nișe, tavan, bucătărie"),
            "ac": ("Aer condiționat în sistem", "Comanda aerului condiționat de pe panou și telefon (prima unitate)"),
            "intercom": ("Panou videointerfon 10″", "Vezi vizitatorul pe ecranul din apartament, nu doar în telefon"),
        },
        "sum_pkg": "Pachet", "sum_opts": "Opțiuni", "sum_total": "Total", "sum_promo": "Cu oferta −10% la echipamente",
        "sum_note": "Orientativ, fără TVA. Suma exactă — în oferta personală după vizită.",
        "pick_pkg_first": "Alege un pachet mai sus — totalul se calculează aici.",
    },
    "en": {
        "apts": "apts", "range_hint": "Block {b}: {c} apts, numbers {from}–{to}",
        "promo_kicker": "Offer for Lagmar residents",
        "promo_title": "−10% on Grenton equipment",
        "promo_text": "For requests sent by 31 December 2026. Consultation and preliminary estimate are free.",
        "promo_cta": "Get a discounted estimate", "promo_until": "until 31.12.2026",
        "tier_from": "from {p}",
        "opt_eyebrow": "Options", "opt_title": "Add to any package",
        "opt_sub": "Each option is a Grenton module with programming. Add it now or later — the system grows without replacing what is installed.",
        "opt_s2": "Add options", "opt_add": "Add", "opt_added": "Added",
        "options": {
            "panel": ("One more Smart Panel", "OLED screen and scenes in one more room"),
            "touch": ("Touch Panel, 4 buttons", "Instead of a plain switch: light, blinds, scenes"),
            "blinds": ("Blinds: module for 3 motors", "Three more windows with scheduled blinds (motors extra)"),
            "dim": ("Dimming for 2 more zones", "Smooth brightness in the bedroom, living room or kitchen"),
            "rgbw": ("RGBW LED lighting", "Coloured or warm light for niches, ceiling, kitchen"),
            "ac": ("Air conditioning in the system", "Control the AC from the panel and phone (first unit)"),
            "intercom": ("10″ video intercom panel", "See the visitor on a screen in the apartment, not only on the phone"),
        },
        "sum_pkg": "Package", "sum_opts": "Options", "sum_total": "Total", "sum_promo": "With the −10% equipment offer",
        "sum_note": "Indicative, excl. VAT. The exact amount is in your personal offer after the visit.",
        "pick_pkg_first": "Pick a package above and the total appears here.",
    },
}
