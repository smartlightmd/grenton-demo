#!/usr/bin/env python3
"""Static site generator for the Grenton showcase (RO/RU/EN) — SmartSpace, official Grenton representative in Moldova."""
import html as _html
import json
import os
import re

from content_offer_txt import OFFER_TXT
from content_lagmar import HOME_LG, LAGMAR_MKT, OPTION_ICON, OPTION_PRICES, PROMO_PCT
from content_contact import CONTACT_V3, EMAIL, GEO, HOURS, PAGE_HERO_MEDIA, SOCIAL, WA_NUMBER
from content_v3 import (APP, CMP, DAY, DAY_BLINDS, DAY_LIGHTS, DAY_STATES, FEATURE_PHOTO, GAL, HOME_V3,
                        PHOTO_ALT, PRICES, PROGRAMMING_SHARE, SCENE_PHOTO, fmt_eur)
from content_offer import EQUIPMENT, OFFER, PACKAGE_SPEC, PRICES  # noqa: E402  (overrides content_v3.PRICES)
from content_pages import (CTA_LAGMAR, FEATURES, HOME_CARDS, HOME_V2, HOW, META_DESC_NEW, SCENARIOS, SL_BRANDS,
                           SMARTLIGHT_URL, SMARTLIGHT_UTM, TIER_CHIP)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = "https://smartlightmd.github.io/grenton-demo"
PRIVACY_URL = "https://smartspace.md/privacy"
API_URL = "https://app.smartspace.md/api/public/lagmar-quote-request"
PHONE_DISPLAY = "+373 78 202 020"
PHONE_TEL = "+37378202020"

LANGS = ["ro", "ru", "en"]
LANG_LABEL = {"ro": "RO", "ru": "RU", "en": "EN"}
OG_LOCALE = {"ro": "ro_RO", "ru": "ru_RU", "en": "en_US"}
# Share cards rendered by scripts/og_cards.mjs (1200x630)
OG_IMG_ALT = {
    "grenton": {"ro": "Grenton — SmartSpace, reprezentant oficial în Moldova",
                "ru": "Grenton — SmartSpace, официальный представитель в Молдове",
                "en": "Grenton — SmartSpace, official representative in Moldova"},
    "lagmar": {"ro": "Lagmar Smart Home — configurator Grenton: pachetele Basic, Comfort, Premium",
               "ru": "Lagmar Smart Home — конфигуратор Grenton: пакеты Basic, Comfort, Premium",
               "en": "Lagmar Smart Home — Grenton configurator: Basic, Comfort, Premium packages"},
}

NAV_LABELS = {
    "ro": {"home": "Acasă", "lagmar": "Alege și calculează", "features": "Funcții", "scenarios": "Scenarii", "how": "Cum funcționează", "contact": "Contact"},
    "ru": {"home": "Главная", "lagmar": "Подобрать и рассчитать", "features": "Возможности", "scenarios": "Сценарии", "how": "Как это работает", "contact": "Контакты"},
    "en": {"home": "Home", "lagmar": "Get a quote", "features": "Features", "scenarios": "Scenes", "how": "How it works", "contact": "Contact"},
}
THEME_LABEL = {"ro": "Schimbă tema", "ru": "Переключить тему", "en": "Toggle theme"}

BUILDINGS = list("ABCDEFGHIJK")

REP = {"ro": "Reprezentant oficial", "ru": "Официальный представитель", "en": "Official representative"}

FOOTER = {
    "ro": "Site informativ realizat de SmartSpace, reprezentant oficial Grenton în Moldova. Fotografiile produselor aparțin Grenton sp. z o.o.",
    "ru": "Информационный сайт SmartSpace, официального представителя Grenton в Молдове. Фотографии продуктов принадлежат Grenton sp. z o.o.",
    "en": "Informational site by SmartSpace, the official Grenton representative in Moldova. Product photos belong to Grenton sp. z o.o.",
}
PRIVACY_LABEL = {"ro": "Politica de confidențialitate", "ru": "Политика конфиденциальности", "en": "Privacy policy"}

DEALER_BAND = {
    "ro": {"h": "SmartSpace — reprezentant oficial Grenton în Moldova",
           "p": "Consultanță, proiectare, montaj și service pentru sistemul Grenton — de la un singur apartament până la clădiri întregi.",
           "cta": "Solicită o ofertă"},
    "ru": {"h": "SmartSpace — официальный представитель Grenton в Молдове",
           "p": "Консультация, проектирование, монтаж и сервис системы Grenton — от одной квартиры до целых зданий.",
           "cta": "Запросить предложение"},
    "en": {"h": "SmartSpace — official Grenton representative in Moldova",
           "p": "Consulting, design, installation and service for the Grenton system — from a single apartment to entire buildings.",
           "cta": "Request a quote"},
}

CONTACT_INFO = {
    "ro": {"addr": "Strada Pajurii 11, MD-2059 Chișinău", "phone": PHONE_DISPLAY, "note": "Programare vizită / consultație gratuită"},
    "ru": {"addr": "Strada Pajurii 11, MD-2059 Chișinău (Кишинёв)", "phone": PHONE_DISPLAY, "note": "Запись на визит / бесплатная консультация"},
    "en": {"addr": "Strada Pajurii 11, MD-2059 Chișinău", "phone": PHONE_DISPLAY, "note": "Book a visit / free consultation"},
}

HOME_LAGMAR = {
    "ro": {"eyebrow": "Proiectul nostru", "h2": "Lagmar Smart Home: 1 065 de apartamente pe Grenton",
           "p": "Lagmar Smart Home este un complex rezidențial din Chișinău (11 blocuri) în care casa inteligentă funcționează pe sistemul Grenton — proiectat, instalat și întreținut de SmartSpace. Ai un apartament în Lagmar? Găsește-l în configurator, alege pachetul Basic, Comfort sau Premium și primești o ofertă preliminară în câteva minute.",
           "cta": "Configurează-ți apartamentul"},
    "ru": {"eyebrow": "Наш проект", "h2": "Lagmar Smart Home: 1 065 квартир на Grenton",
           "p": "Lagmar Smart Home — жилой комплекс в Кишинёве (11 блоков), где умный дом построен на системе Grenton — её проектирует, устанавливает и обслуживает SmartSpace. У вас квартира в Lagmar? Найдите её в конфигураторе, выберите пакет Basic, Comfort или Premium и получите предварительное предложение за пару минут.",
           "cta": "Настроить свою квартиру"},
    "en": {"eyebrow": "Our project", "h2": "Lagmar Smart Home: 1,065 apartments on Grenton",
           "p": "Lagmar Smart Home is a residential complex in Chișinău (11 blocks) where the smart home runs on Grenton — designed, installed and supported by SmartSpace. Own an apartment in Lagmar? Find it in the configurator, pick Basic, Comfort or Premium and get a preliminary quote in minutes.",
           "cta": "Configure your apartment"},
}

META_DESC = {
    "home": {
        "ro": "Grenton — sistem smart home din Polonia: iluminat, climă, rulouri, audio și securitate într-un singur ecosistem. SmartSpace, reprezentant oficial Grenton în Moldova.",
        "ru": "Grenton — система умного дома из Польши: свет, климат, шторы, аудио и безопасность в одной экосистеме. SmartSpace — официальный представитель Grenton в Молдове.",
        "en": "Grenton — a Polish smart-home system: lighting, climate, blinds, audio and security in one ecosystem. SmartSpace, official Grenton representative in Moldova.",
    },
    "contact": {
        "ro": "Consultație gratuită SmartSpace, reprezentant oficial Grenton în Moldova: Strada Pajurii 11, Chișinău, +373 78 202 020. Proiectare, montaj și service.",
        "ru": "Бесплатная консультация SmartSpace, официального представителя Grenton в Молдове: Strada Pajurii 11, Кишинёв, +373 78 202 020. Проект, монтаж, сервис.",
        "en": "Free consultation with SmartSpace, official Grenton representative in Moldova: Strada Pajurii 11, Chișinău, +373 78 202 020. Design, installation, service.",
    },
    "lagmar": {
        "ro": "Configurator smart home Grenton pentru apartamentele din Lagmar Smart Home: găsește-ți apartamentul, alege pachetul Basic, Comfort sau Premium și primești oferta de la SmartSpace.",
        "ru": "Конфигуратор умного дома Grenton для квартир в Lagmar Smart Home: найдите свою квартиру, выберите пакет Basic, Comfort или Premium и получите предложение от SmartSpace.",
        "en": "Grenton smart-home configurator for Lagmar Smart Home apartments: find your apartment, choose Basic, Comfort or Premium and get a quote from SmartSpace.",
    },
}

META_DESC.update(META_DESC_NEW)

PAGES = {}

PAGES["home"] = {
    "ro": {
        "title": "Grenton smart home în Moldova — SmartSpace, reprezentant oficial",
        "eyebrow": "Ecosistem smart home",
        "h1": "Casa ta, controlată dintr-un singur loc",
        "lead": "Grenton este un sistem de automatizare a locuinței produs în Polonia: iluminat, climă, rulouri, muzică și securitate — toate conectate într-un singur ecosistem. SmartSpace instalează și configurează sistemul Grenton în Moldova.",
        "cta_primary": ("Configuratorul Lagmar", "lagmar.html"),
        "cta_secondary": ("Ce știe sistemul", "features.html"),
        "cards": HOME_CARDS["ro"],
    },
    "ru": {
        "title": "Умный дом Grenton в Молдове — SmartSpace, официальный представитель",
        "eyebrow": "Экосистема умного дома",
        "h1": "Ваш дом — под управлением из одной точки",
        "lead": "Grenton — система домашней автоматизации из Польши: свет, климат, шторы, музыка и безопасность объединены в одну экосистему. SmartSpace устанавливает и настраивает Grenton в Молдове.",
        "cta_primary": ("Конфигуратор Lagmar", "lagmar.html"),
        "cta_secondary": ("Что умеет система", "features.html"),
        "cards": HOME_CARDS["ru"],
    },
    "en": {
        "title": "Grenton smart home in Moldova — SmartSpace, official representative",
        "eyebrow": "Smart home ecosystem",
        "h1": "Your home, controlled from one place",
        "lead": "Grenton is a Polish-made home automation system: lighting, climate, blinds, audio and security — all connected in one ecosystem. SmartSpace installs and configures Grenton in Moldova.",
        "cta_primary": ("Lagmar configurator", "lagmar.html"),
        "cta_secondary": ("What it can do", "features.html"),
        "cards": HOME_CARDS["en"],
    },
}

PAGES["contact"] = {
    "ro": {
        "title": "Contact — SmartSpace, reprezentant oficial Grenton în Moldova",
        "eyebrow": "Hai să vorbim",
        "h1": "Programează o consultație gratuită",
        "lead": "Echipa SmartSpace te ajută să alegi configurația Grenton potrivită pentru proiectul tău — apartament, casă sau clădire.",
        "cta_primary": ("Sună acum", f"tel:{PHONE_TEL}"),
        "cta_secondary": ("Cum funcționează", "how.html"),
        "cards": [],
    },
    "ru": {
        "title": "Контакты — SmartSpace, официальный представитель Grenton в Молдове",
        "eyebrow": "Давайте обсудим",
        "h1": "Запишитесь на бесплатную консультацию",
        "lead": "Команда SmartSpace поможет подобрать конфигурацию Grenton под ваш проект — квартиру, дом или здание.",
        "cta_primary": ("Позвонить", f"tel:{PHONE_TEL}"),
        "cta_secondary": ("Как это работает", "how.html"),
        "cards": [],
    },
    "en": {
        "title": "Contact — SmartSpace, official Grenton representative in Moldova",
        "eyebrow": "Let's talk",
        "h1": "Book a free consultation",
        "lead": "The SmartSpace team helps you choose the right Grenton setup for your project — apartment, house or building.",
        "cta_primary": ("Call now", f"tel:{PHONE_TEL}"),
        "cta_secondary": ("How it works", "how.html"),
        "cards": [],
    },
}

LAGMAR_UI = {
    "ru": {
        "title": "Умный дом Grenton для квартиры в Lagmar Smart Home — конфигуратор | SmartSpace",
        "eyebrow": "Ваш дом в Lagmar Smart Home",
        "h1": "Рассчитайте умный дом для своей квартиры в Lagmar",
        "lead": "Найдите свою квартиру — покажем пакеты на её планировке и сразу посчитаем цену. Контроллер Grenton в квартире уже стоит, платите только за то, что добавляем. Персональное предложение от SmartSpace, официального представителя Grenton.",
        "step1_title": "1. Найдите свою квартиру",
        "building_label": "Блок", "building_placeholder": "Выберите блок",
        "apt_label": "№ квартиры", "apt_placeholder": "например, 21",
        "apt_hint": "Только номер квартиры — без буквы блока и «кв.»",
        "find_btn": "Найти", "loading": "Загружаем список квартир…",
        "choose_building": "Сначала выберите блок.",
        "found_prefix": "Найдено:", "floor_word": "этаж", "floor_ground": "первый этаж (parter)", "rooms_word": "комн.", "area_word": "м²",
        "not_found_text": "Не нашли такую квартиру — не страшно, выберите тип квартиры вручную:",
        "manual_label": "Комнат",
        "edge_hint": "Для квартир от 5 комнат и студий готовим индивидуальный расчёт — пакеты ниже ориентировочные.",
        "step2_title": "2. Выберите комплектацию",
        "tariff_required": "Выберите комплектацию, чтобы продолжить.",
        "step3_title": "3. Оставьте контакты — пришлём предложение",
        "name_label": "Имя", "phone_label": "Телефон", "phone_hint": "Например, +373 6x xxx xxx или 06x xxx xxx",
        "email_label": "Email (необязательно)",
        "consent_text": "Согласен(-на) на обработку персональных данных для подготовки предложения —",
        "consent_link": "политика конфиденциальности",
        "disclaimer": "Предложение носит предварительный, информационный характер и не является публичной офертой; итоговая цена подтверждается менеджером SmartSpace после осмотра квартиры.",
        "submit_btn": "Получить предложение", "sending": "Отправляем…",
        "success_title": "Готово!", "success_text": "Ваше персональное предложение готово:",
        "success_link": "Открыть предложение",
        "success_next": "Менеджер SmartSpace свяжется с вами, чтобы уточнить детали.",
        "again": "Отправить для другой квартиры",
        "error_text": "Не удалось отправить автоматически. Свяжитесь с нами напрямую:",
        "error_phone": "Проверьте номер телефона — похоже, он введён с ошибкой.",
        "error_name": "Как к вам обращаться? Введите имя — хотя бы 2 буквы.",
        "error_consent": "Отметьте согласие на обработку данных — без него мы не можем подготовить предложение.",
        "error_rate": "Слишком много запросов — попробуйте через несколько минут.",
        "packages_title": "Что входит в пакеты",
        "faq_title": "Вопросы и ответы",
    },
    "ro": {
        "title": "Casă inteligentă Grenton pentru apartamentul tău în Lagmar Smart Home — configurator | SmartSpace",
        "eyebrow": "Apartamentul tău din Lagmar Smart Home",
        "h1": "Calculează casa inteligentă pentru apartamentul tău din Lagmar",
        "lead": "Găsește-ți apartamentul — îți arătăm pachetele pe planul lui și calculăm prețul pe loc. Unitatea Grenton e deja montată, plătești doar ce adăugăm. Oferta personalizată de la SmartSpace, reprezentant oficial Grenton.",
        "step1_title": "1. Găsește-ți apartamentul",
        "building_label": "Blocul", "building_placeholder": "Alege blocul",
        "apt_label": "Nr. apartament", "apt_placeholder": "de ex. 21",
        "apt_hint": "Doar numărul apartamentului — fără litera blocului și fără „ap.”",
        "find_btn": "Caută", "loading": "Se încarcă lista apartamentelor…",
        "choose_building": "Alege mai întâi blocul.",
        "found_prefix": "Găsit:", "floor_word": "etaj", "floor_ground": "parter", "rooms_word": "camere", "area_word": "m²",
        "not_found_text": "Nu am găsit acest apartament — nicio problemă, alege tipul de apartament manual:",
        "manual_label": "Camere",
        "edge_hint": "Pentru apartamente cu 5+ camere sau garsoniere pregătim un calcul individual — pachetele de mai jos sunt orientative.",
        "step2_title": "2. Alege pachetul",
        "tariff_required": "Alege un pachet pentru a continua.",
        "step3_title": "3. Lasă-ne datele de contact — îți trimitem oferta",
        "name_label": "Nume", "phone_label": "Telefon", "phone_hint": "De ex. +373 6x xxx xxx sau 06x xxx xxx",
        "email_label": "Email (opțional)",
        "consent_text": "Sunt de acord cu prelucrarea datelor personale pentru pregătirea ofertei —",
        "consent_link": "politica de confidențialitate",
        "disclaimer": "Oferta generată este preliminară, are caracter informativ și nu constituie ofertă publică; prețul final se confirmă de managerul SmartSpace după vizita la apartament.",
        "submit_btn": "Primește oferta", "sending": "Se trimite…",
        "success_title": "Gata!", "success_text": "Oferta ta personalizată este pregătită:",
        "success_link": "Deschide oferta",
        "success_next": "Un manager SmartSpace te va contacta pentru detalii.",
        "again": "Trimite pentru alt apartament",
        "error_text": "Nu am putut trimite automat. Contactează-ne direct:",
        "error_phone": "Verifică numărul de telefon — pare introdus greșit.",
        "error_name": "Cum să ne adresăm? Introdu numele — cel puțin 2 litere.",
        "error_consent": "Bifează acordul pentru prelucrarea datelor — fără el nu putem pregăti oferta.",
        "error_rate": "Prea multe cereri — încearcă din nou peste câteva minute.",
        "packages_title": "Ce include fiecare pachet",
        "faq_title": "Întrebări frecvente",
    },
    "en": {
        "title": "Grenton smart home for your Lagmar Smart Home apartment — configurator | SmartSpace",
        "eyebrow": "Your home in Lagmar Smart Home",
        "h1": "Price a smart home for your Lagmar apartment",
        "lead": "Find your apartment — we show the packages on its floor plan and price them right away. The Grenton controller is already installed; you pay only for what we add. A personal quote from SmartSpace, the official Grenton representative.",
        "step1_title": "1. Find your apartment",
        "building_label": "Block", "building_placeholder": "Choose your block",
        "apt_label": "Apartment No.", "apt_placeholder": "e.g. 21",
        "apt_hint": "Apartment number only — no block letter, no “apt.”",
        "find_btn": "Find", "loading": "Loading the apartment list…",
        "choose_building": "Choose your block first.",
        "found_prefix": "Found:", "floor_word": "floor", "floor_ground": "ground floor", "rooms_word": "rooms", "area_word": "m²",
        "not_found_text": "We couldn't find that apartment — no problem, pick your apartment type manually:",
        "manual_label": "Rooms",
        "edge_hint": "For 5+ room apartments and studios we prepare an individual estimate — the packages below are indicative.",
        "step2_title": "2. Choose a package",
        "tariff_required": "Choose a package to continue.",
        "step3_title": "3. Leave your details — we'll send your quote",
        "name_label": "Name", "phone_label": "Phone", "phone_hint": "e.g. +373 6x xxx xxx or 06x xxx xxx",
        "email_label": "Email (optional)",
        "consent_text": "I agree to the processing of my personal data to prepare the quote —",
        "consent_link": "privacy policy",
        "disclaimer": "The quote is preliminary and for information only; it is not a binding offer. The final price is confirmed by a SmartSpace manager after a site visit.",
        "submit_btn": "Get my quote", "sending": "Sending…",
        "success_title": "Done!", "success_text": "Your personal quote is ready:",
        "success_link": "Open quote",
        "success_next": "A SmartSpace manager will contact you to confirm the details.",
        "again": "Submit for another apartment",
        "error_text": "We couldn't send your request automatically. Please contact us directly:",
        "error_phone": "Please check the phone number — it looks mistyped.",
        "error_name": "How should we address you? Enter a name — at least 2 letters.",
        "error_consent": "Please tick the consent to data processing — we cannot prepare a quote without it.",
        "error_rate": "Too many requests — please try again in a few minutes.",
        "packages_title": "What each package includes",
        "faq_title": "Questions & answers",
    },
}

FAQ = {
    "ru": [
        ("Можно ли установить Grenton после ремонта?", "Да. Grenton работает по проводной шине и поддерживает беспроводные модули Z-Wave — для готового ремонта подбираем беспроводную часть без штробления. Оптимально закладывать систему до чистовой отделки."),
        ("Работает ли умный дом без интернета?", "Да. Сценарии выполняются локально на центральном модуле CLU; интернет нужен только для удалённого доступа из приложения myGrenton."),
        ("Кто устанавливает и обслуживает систему?", "SmartSpace — официальный представитель Grenton в Молдове: проектирование, монтаж, настройка и сервис."),
        ("Сколько занимает монтаж?", "Зависит от пакета и стадии отделки — от нескольких дней для базового пакета до пары недель для полной автоматизации. Сроки подтверждаем после осмотра квартиры."),
        ("Можно начать с Basic и расширить позже?", "Да, система модульная: модули, панели и датчики добавляются по мере необходимости без замены уже установленного."),
    ],
    "ro": [
        ("Se poate instala Grenton după finalizarea renovării?", "Da. Grenton funcționează pe magistrală cablată și acceptă module wireless Z-Wave — pentru un apartament deja finisat alegem partea wireless, fără șlițuri. Ideal este ca sistemul să fie prevăzut înainte de finisaje."),
        ("Funcționează casa inteligentă fără internet?", "Da. Scenariile rulează local pe unitatea centrală CLU; internetul este necesar doar pentru accesul de la distanță din aplicația myGrenton."),
        ("Cine instalează și întreține sistemul?", "SmartSpace — reprezentant oficial Grenton în Moldova: proiectare, montaj, configurare și service."),
        ("Cât durează montajul?", "Depinde de pachet și de stadiul finisajelor — de la câteva zile pentru pachetul de bază până la câteva săptămâni pentru automatizare completă. Termenele se confirmă după vizita la apartament."),
        ("Pot începe cu Basic și extinde mai târziu?", "Da, sistemul este modular: modulele, panourile și senzorii se adaugă pe măsură ce este nevoie, fără a înlocui ce este deja instalat."),
    ],
    "en": [
        ("Can Grenton be installed after the renovation is finished?", "Yes. Grenton runs on a wired bus and supports Z-Wave wireless modules — for a finished apartment we use the wireless part, no chasing walls. Ideally the system is planned before finishing works."),
        ("Does the smart home work without internet?", "Yes. Scenes run locally on the CLU central unit; internet is only needed for remote access from the myGrenton app."),
        ("Who installs and services the system?", "SmartSpace — the official Grenton representative in Moldova: design, installation, configuration and service."),
        ("How long does installation take?", "It depends on the package and the finishing stage — from a few days for the basic package to a couple of weeks for full automation. Timing is confirmed after a site visit."),
        ("Can I start with Basic and expand later?", "Yes, the system is modular: modules, panels and sensors are added as needed without replacing what is already installed."),
    ],
}

PLAN_IMG_BASE = "https://api.lagmarsmarthome.md/images/apartments/"

LAGMAR_VIS = {
    "ru": {
        "kicker": "Lagmar Smart Home × Grenton",
        "stats": [("11", "блоков"), ("1 065", "квартир"), ("Grenton", "умный дом в каждой")],
        "hero_stats": [("3", "шага до предложения"), ("≈2 мин", "на расчёт"), ("0 €", "за контроллер — уже стоит")],
        "cta_find": "Найти мою квартиру", "cta_examples": "Пакеты на планировке",
        "blocks_title": "Выберите свой блок", "blocks_sub": "Нажмите на блок — номер квартиры введёте ниже.",
        "block_word": "Блок",
        "examples_eyebrow": "Наглядно", "examples_title": "Пакеты на реальных планировках Lagmar",
        "examples_sub": "Типовые квартиры комплекса — переключайте Basic / Comfort / Premium и смотрите, что и где появляется.",
        "tabs": {"2": "2 комнаты · 46 м²", "3": "3 комнаты · 82 м²", "4": "4 комнаты · 99 м²"},
        "plan_alt": "Планировка типовой {n}-комнатной квартиры Lagmar",
        "example_note": "Иллюстрация: примерная расстановка на типовой планировке Lagmar. Точный проект — после осмотра вашей квартиры.",
        "your_plan": "Планировка вашей квартиры", "your_block": "Ваш блок",
        "s2_plan_title": "Как это выглядит на похожей планировке",
        "devices": {"L": "Группа света", "P": "Панель управления", "T": "Зона климата", "W": "Датчик протечки",
                    "S": "Датчик дыма", "M": "Датчик движения", "C": "Привод штор", "A": "Аудио-зона",
                    "Q": "Multisensor (CO₂)", "I": "Видеодомофон"},
    },
    "ro": {
        "kicker": "Lagmar Smart Home × Grenton",
        "stats": [("11", "blocuri"), ("1 065", "apartamente"), ("Grenton", "casă inteligentă în fiecare")],
        "hero_stats": [("3", "pași până la ofertă"), ("≈2 min", "pentru calcul"), ("0 €", "pentru unitate — e deja montată")],
        "cta_find": "Găsește-mi apartamentul", "cta_examples": "Pachetele pe plan",
        "blocks_title": "Alege-ți blocul", "blocks_sub": "Apasă pe bloc — numărul apartamentului îl introduci mai jos.",
        "block_word": "Blocul",
        "examples_eyebrow": "Concret", "examples_title": "Pachetele pe planuri reale Lagmar",
        "examples_sub": "Apartamente tipice din complex — comută Basic / Comfort / Premium și vezi ce apare și unde.",
        "tabs": {"2": "2 camere · 46 m²", "3": "3 camere · 82 m²", "4": "4 camere · 99 m²"},
        "plan_alt": "Planul unui apartament tipic Lagmar cu {n} camere",
        "example_note": "Ilustrație: amplasare orientativă pe un plan tipic Lagmar. Proiectul exact — după vizita la apartamentul tău.",
        "your_plan": "Planul apartamentului tău", "your_block": "Blocul tău",
        "s2_plan_title": "Cum arată pe un plan asemănător",
        "devices": {"L": "Grup de iluminat", "P": "Panou de comandă", "T": "Zonă de climă", "W": "Senzor de scurgere",
                    "S": "Senzor de fum", "M": "Senzor de mișcare", "C": "Motor rulou", "A": "Zonă audio",
                    "Q": "Multisensor (CO₂)", "I": "Videointerfon"},
    },
    "en": {
        "kicker": "Lagmar Smart Home × Grenton",
        "stats": [("11", "blocks"), ("1,065", "apartments"), ("Grenton", "smart home in every one")],
        "hero_stats": [("3", "steps to a quote"), ("≈2 min", "to price it"), ("0 €", "for the controller — already in")],
        "cta_find": "Find my apartment", "cta_examples": "Packages on a floor plan",
        "blocks_title": "Choose your block", "blocks_sub": "Tap a block — you'll enter the apartment number below.",
        "block_word": "Block",
        "examples_eyebrow": "See it", "examples_title": "Packages on real Lagmar floor plans",
        "examples_sub": "Typical apartments in the complex — switch Basic / Comfort / Premium and see what appears and where.",
        "tabs": {"2": "2 rooms · 46 m²", "3": "3 rooms · 82 m²", "4": "4 rooms · 99 m²"},
        "plan_alt": "Floor plan of a typical {n}-room Lagmar apartment",
        "example_note": "Illustration: indicative layout on a typical Lagmar floor plan. The exact design follows a visit to your apartment.",
        "your_plan": "Your apartment's floor plan", "your_block": "Your block",
        "s2_plan_title": "How it looks on a similar floor plan",
        "devices": {"L": "Lighting group", "P": "Control panel", "T": "Climate zone", "W": "Leak sensor",
                    "S": "Smoke sensor", "M": "Motion sensor", "C": "Blind motor", "A": "Audio zone",
                    "Q": "Multisensor (CO₂)", "I": "Video intercom"},
    },
}

DEVICE_ORDER = ["L", "P", "T", "W", "C", "M", "S", "Q", "A", "I"]

# Illustrative device placement on three typical Lagmar plans (F-27 46 m², B-57 82 m², C-32 99 m²).
# (type, x%, y%, tiers) — tiers: b=Basic, c=Comfort, p=Premium (cumulative upward).
PLAN_MARKERS = {
    "2": [
        ("L", 24, 40, "bcp"), ("L", 72, 42, "bcp"), ("L", 30, 84, "bcp"), ("L", 62, 68, "bcp"), ("L", 86, 90, "bcp"),
        ("P", 12, 70, "bcp"), ("T", 58, 62, "bcp"), ("W", 89, 57, "bcp"), ("W", 79, 95, "bcp"), ("I", 66, 92, "bcp"),
        ("L", 12, 22, "cp"), ("L", 70, 15, "cp"), ("L", 45, 93, "cp"),
        ("C", 28, 7, "cp"), ("C", 4, 86, "cp"), ("T", 40, 28, "cp"), ("M", 66, 63, "cp"), ("S", 52, 70, "cp"),
        ("P", 40, 50, "cp"), ("P", 58, 45, "cp"),
        ("L", 15, 62, "p"), ("L", 84, 30, "p"), ("L", 40, 72, "p"), ("L", 35, 30, "p"), ("L", 88, 15, "p"), ("L", 18, 93, "p"),
        ("Q", 22, 90, "p"), ("A", 20, 78, "p"), ("A", 34, 42, "p"), ("C", 66, 7, "p"),
    ],
    "3": [
        ("L", 17, 40, "bcp"), ("L", 45, 35, "bcp"), ("L", 75, 25, "bcp"), ("L", 25, 80, "bcp"), ("L", 70, 82, "bcp"),
        ("L", 50, 92, "bcp"), ("L", 90, 90, "bcp"),
        ("P", 55, 55, "bcp"), ("T", 62, 78, "bcp"), ("W", 14, 62, "bcp"), ("W", 48, 94, "bcp"), ("W", 88, 78, "bcp"),
        ("I", 79, 96, "bcp"),
        ("L", 12, 12, "cp"), ("L", 35, 20, "cp"), ("L", 64, 12, "cp"), ("L", 12, 90, "cp"), ("L", 30, 55, "cp"),
        ("T", 75, 42, "cp"), ("T", 30, 74, "cp"),
        ("C", 40, 3, "cp"), ("C", 70, 3, "cp"), ("C", 2, 82, "cp"),
        ("M", 60, 60, "cp"), ("S", 60, 66, "cp"), ("P", 72, 48, "cp"), ("P", 38, 72, "cp"), ("P", 25, 30, "cp"),
        ("L", 50, 15, "p"), ("L", 60, 30, "p"), ("L", 82, 12, "p"), ("L", 20, 93, "p"), ("L", 88, 70, "p"), ("L", 5, 30, "p"),
        ("Q", 45, 50, "p"), ("A", 40, 38, "p"), ("A", 80, 30, "p"), ("A", 18, 84, "p"), ("C", 18, 3, "p"),
    ],
    "4": [
        ("L", 22, 15, "bcp"), ("L", 62, 18, "bcp"), ("L", 58, 37, "bcp"), ("L", 52, 52, "bcp"), ("L", 20, 86, "bcp"),
        ("L", 66, 86, "bcp"), ("L", 88, 57, "bcp"), ("L", 14, 42, "bcp"), ("L", 14, 60, "bcp"),
        ("P", 70, 50, "bcp"), ("T", 80, 56, "bcp"), ("W", 72, 21, "bcp"), ("W", 9, 45, "bcp"), ("W", 9, 63, "bcp"),
        ("I", 90, 68, "bcp"),
        ("L", 30, 25, "cp"), ("L", 40, 62, "cp"), ("L", 30, 92, "cp"), ("L", 60, 4, "cp"), ("L", 75, 92, "cp"),
        ("L", 45, 44, "cp"), ("L", 65, 64, "cp"),
        ("T", 25, 22, "cp"), ("T", 25, 80, "cp"), ("T", 60, 80, "cp"),
        ("C", 20, 1.5, "cp"), ("C", 22, 98.5, "cp"), ("C", 65, 98.5, "cp"),
        ("M", 85, 50, "cp"), ("M", 50, 71, "cp"), ("S", 80, 67, "cp"),
        ("P", 31, 12, "cp"), ("P", 31, 79, "cp"), ("P", 50, 79, "cp"), ("P", 55, 25, "cp"),
        ("L", 10, 15, "p"), ("L", 70, 40, "p"), ("L", 35, 50, "p"), ("L", 60, 70, "p"), ("L", 10, 80, "p"),
        ("L", 45, 92, "p"), ("L", 90, 50, "p"), ("L", 50, 30, "p"),
        ("Q", 50, 58, "p"), ("A", 44, 49, "p"), ("A", 15, 22, "p"), ("A", 15, 89, "p"), ("A", 70, 90, "p"),
    ],
}
# packages no longer include intercom/audio (they are options) -> no such markers on plans
PLAN_MARKERS = {n: [m for m in ms if m[0] not in "IA"] for n, ms in PLAN_MARKERS.items()}
# Extra positions (by room) used when a package needs more devices than the drawing had.
PLAN_EXTRA = {
    "2": [("P", 88, 68), ("P", 60, 82), ("M", 20, 50)],
    "3": [("P", 66, 72), ("P", 40, 22), ("S", 18, 72), ("M", 48, 62)],
    "4": [("P", 90, 57), ("P", 40, 33), ("P", 60, 64), ("C", 58, 1.5), ("C", 76, 44), ("S", 40, 69), ("M", 28, 52), ("Q", 20, 85)],
}


def _sync_markers(n):
    from content_offer import PACKAGE_SPEC
    need = {"L": lambda x: x["l"] + x["d"], "P": lambda x: x["sp"] + x["tp4"] + x["tp8"], "T": lambda x: x["h"],
            "W": lambda x: x["leak"], "C": lambda x: x["b"], "S": lambda x: x["smoke"], "M": lambda x: x["motion"],
            "Q": lambda x: x["multi"]}
    sp = PACKAGE_SPEC[n]
    order = {"bcp": 0, "cp": 1, "p": 2}
    out = []
    for t, f in need.items():
        cand = sorted([m for m in PLAN_MARKERS[n] if m[0] == t], key=lambda m: order[m[3]])
        cand = [(m[1], m[2]) for m in cand] + [(x, y) for tt, x, y in PLAN_EXTRA[n] if tt == t]
        nb, nc, np_ = f(sp["basic"]), f(sp["comfort"]), f(sp["premium"])
        assert len(cand) >= np_, (n, t, len(cand), np_)
        for i, (x, y) in enumerate(cand[:np_]):
            out.append((t, x, y, "bcp" if i < nb else "cp" if i < nc else "p"))
    return out


PLAN_MARKERS = {n: _sync_markers(n) for n in PLAN_MARKERS}
PLAN_SIZE = {"2": (424, 589), "3": (767, 615), "4": (558, 1064)}

PAGE_IMG = {"home": "monolith.png", "contact": "project-1.png"}
IMG_ALT = {
    "monolith.png": "Grenton Monolith — сенсорная панель / touch panel", "clu.jpg": "Grenton CLU — central unit",
    "smart-panel.jpg": "Grenton Smart Panel", "audio-integration.png": "Grenton — audio integration",
    "project-1.png": "Smart home project", "project-2.png": "Smart home project",
}

PAGE_ORDER = ["home", "lagmar", "features", "scenarios", "how", "contact"]
PAGE_FILE = {"home": "index.html", "lagmar": "lagmar.html", "features": "features.html", "scenarios": "scenarios.html",
             "how": "how.html", "contact": "contact.html"}
LEGACY_REDIRECTS = {"system.html": "how.html", "control.html": "how.html#interfaces", "sensors.html": "features.html#safety"}


def esc(s):
    return _html.escape(str(s), quote=True)


def org_jsonld(lang):
    return {
        "@context": "https://schema.org", "@type": "Organization", "@id": "https://smartspace.md/#org",
        "name": "SmartSpace", "url": "https://smartspace.md/", "telephone": PHONE_TEL,
        "address": {"@type": "PostalAddress", "streetAddress": "Strada Pajurii 11", "postalCode": "MD-2059",
                    "addressLocality": "Chișinău", "addressCountry": "MD"},
        "sameAs": ["https://smartspace.md/", "https://smartlight.md/"],
    }


def head_html(lang, key, title, desc, extra_jsonld=None):
    file = PAGE_FILE[key]
    alternates = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE_URL}/{l}/{file}">' for l in LANGS)
    jsonld = [org_jsonld(lang)] + (extra_jsonld or [])
    jsonld_html = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    card = "lagmar" if key == "lagmar" else "grenton"
    og_img = f"{BASE_URL}/assets/og/og-{card}-{lang}.jpg"
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{BASE_URL}/{lang}/{file}">
{alternates}<link rel="alternate" hreflang="x-default" href="{BASE_URL}/ro/{file}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{BASE_URL}/{lang}/{file}">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:site_name" content="SmartSpace — Grenton Moldova">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(OG_IMG_ALT[card][lang])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" href="../assets/img/favicon-32.png" sizes="32x32">
<link rel="icon" href="../assets/img/favicon-16.png" sizes="16x16">
<link rel="apple-touch-icon" href="../assets/img/apple-touch-icon.png">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#f8f9fb" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0b0f17" media="(prefers-color-scheme: dark)">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<link rel="stylesheet" href="../assets/css/style.css">
{jsonld_html}'''


NAV_ARIA = {"ru": "Основное меню", "ro": "Meniu principal", "en": "Main menu"}
SKIP_TXT = {"ru": "К содержимому", "ro": "Salt la conținut", "en": "Skip to content"}


def nav_html(lang, current):
    labels = NAV_LABELS[lang]
    links = []
    for key in PAGE_ORDER:
        cls = ' class="active"' if key == current else ""
        links.append(f'<a{cls} href="{PAGE_FILE[key]}">{labels[key]}</a>')
    lang_links = []
    for l in LANGS:
        cls = ' class="active"' if l == lang else ""
        lang_links.append(f'<a{cls} href="../{l}/{PAGE_FILE[current]}" hreflang="{l}">{LANG_LABEL[l]}</a>')
    return f'''<header class="site">
  <div class="wrap bar">
    <a class="brand" href="index.html">
      <span class="brand-name">SmartSpace</span>
      <span class="by">by <img src="../assets/img/favicon-32.png" alt="" width="14" height="14"> GRENTON</span>
    </a>
    <nav class="main" aria-label="{NAV_ARIA[lang]}">
      {''.join(links)}
    </nav>
    <div class="controls">
      <div class="langs">{''.join(lang_links)}</div>
      <button type="button" class="theme-toggle" aria-label="{THEME_LABEL[lang]}" title="{THEME_LABEL[lang]}">
        <svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
        <svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2.2M12 19.8V22M4.2 4.2l1.6 1.6M18.2 18.2l1.6 1.6M2 12h2.2M19.8 12H22M4.2 19.8l1.6-1.6M18.2 5.8l1.6-1.6"/></svg>
      </button>
    </div>
  </div>
</header>
<script>(function(){{var b=document.querySelector(".theme-toggle");if(!b)return;var m=window.matchMedia("(prefers-color-scheme: dark)");b.addEventListener("click",function(){{var r=document.documentElement,cur=r.dataset.theme||(m.matches?"dark":"light"),n=cur==="dark"?"light":"dark";r.dataset.theme=n;try{{localStorage.setItem("theme",n)}}catch(e){{}}}});}})();</script>'''


CLOSING_Q = {"ru": "Остались вопросы?", "ro": "Ai întrebări?", "en": "Still have questions?"}


def dealer_band_html(lang, key=""):
    """The one closing block every page ends with (before the footer)."""
    d = DEALER_BAND[lang]
    c = CTA_LAGMAR[lang]
    tel = f'<a class="btn btn-light" href="tel:{PHONE_TEL}">{ico("phone")}{c["alt"]} · {PHONE_DISPLAY}</a>'
    if key == "lagmar":
        title, text = CLOSING_Q[lang], d["p"]
        btns = tel + f'<a class="btn btn-wa" href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener">{ico("chat")}WhatsApp</a>'
    else:
        title, text = c["title"], c["text"]
        btns = f'<a class="btn btn-primary" href="lagmar.html#step1">{c["btn"]} {ico("arrow")}</a>' + ("" if key == "contact" else tel)
    return f'''<section class="closing">
  <div class="wrap closing-inner">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="cta-row cta-left">{btns}</div>
    <p class="closing-rep">{d["h"]}</p>
  </div>
</section>'''


def footer_html(lang):
    return f'''<footer class="site">
  <div class="wrap">
    <div>SmartSpace · Strada Pajurii 11, MD-2059 Chișinău · <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
    <div class="disclaimer">{FOOTER[lang]} · <a href="{PRIVACY_URL}" rel="noopener">{PRIVACY_LABEL[lang]}</a></div>
  </div>
</footer>'''


def badges_html(lang):
    return f'''<div class="badge-row">
      <span class="badge">Grenton</span>
      <span class="badge">SmartSpace · Moldova</span>
      <span class="badge">{REP[lang]}</span>
    </div>'''


def page_html(key, lang):
    p = PAGES[key][lang]
    img = PAGE_IMG[key]
    cards_html = ""
    if p["cards"]:
        def _card(c):
            h, b = c[0], c[1]
            if len(c) > 2:
                return (f'<a class="card card-link" href="{c[2]}"><div class="body"><h3>{h}</h3><p>{b}</p>'
                        f'<span class="more">{c[3]} <span aria-hidden="true">→</span></span></div></a>')
            return f'<div class="card"><div class="body"><h3>{h}</h3><p>{b}</p></div></div>'
        items = "".join(_card(c) for c in p["cards"])
        cards_html = f'<section class="block"><div class="wrap"><div class="grid">{items}</div></div></section>'

    extra = ""
    if key == "contact":
        c = CONTACT_INFO[lang]
        extra = f'''<section class="block">
  <div class="wrap">
    <div class="grid">
      <div class="card"><div class="body"><h3 class="ico-h">{ico("pin")}{c["addr"]}</h3><p>{c["note"]}</p></div></div>
      <div class="card"><div class="body"><h3 class="ico-h">{ico("phone")}<a href="tel:{PHONE_TEL}">{c["phone"]}</a></h3><p>SmartSpace</p></div></div>
    </div>
  </div>
</section>'''
    if key == "home":
        hl = HOME_LAGMAR[lang]
        extra = f'''<section class="block alt lagmar-block" id="lagmar">
  <div class="wrap split">
    <div>
      <span class="eyebrow">{hl["eyebrow"]}</span>
      <h2 class="h2">{hl["h2"]}</h2>
      <p class="sub">{hl["p"]}</p>
      <a class="btn btn-primary" href="lagmar.html">{hl["cta"]}</a>
    </div>
    <a href="lagmar.html" class="lagmar-teaser"><img class="rounded" src="../assets/lagmar/hero-960.jpg" alt="Lagmar Smart Home" width="960" height="540" loading="lazy"><img class="lagmar-teaser-logo" src="../assets/lagmar/logo-lagmar.png" alt="" width="140" height="42"></a>
  </div>
</section>'''

    primary_label, primary_href = p["cta_primary"]
    secondary_label, secondary_href = p["cta_secondary"]
    media_block = "" if key == "home" else f'''<section class="block alt">
  <div class="wrap split">
    <img src="../assets/img/{img}" alt="{IMG_ALT.get(img, 'Grenton')}" loading="lazy">
    {badges_html(lang)}
  </div>
</section>'''

    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_html(lang, key, p["title"], META_DESC[key][lang])}
</head>
<body>
{sprite_html()}
{nav_html(lang, key)}
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">{p["eyebrow"]}</span>
    <h1>{p["h1"]}</h1>
    <p class="lead">{p["lead"]}</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="{primary_href}">{primary_label}</a>
      <a class="btn btn-ghost" href="{secondary_href}">{secondary_label}</a>
    </div>
  </div>
</section>
{media_block}
{cards_html if key != "home" else ""}
{extra}
{cards_html if key == "home" else ""}
{dealer_band_html(lang)}
{footer_html(lang)}
</body>
</html>'''


LAGMAR_JS = r"""
(function () {
  var LANG = "__LANG__";
  var UI = __UI__;
  var API_URL = "__API__";
  var PHONE_DISPLAY = "__PHONE_DISPLAY__";
  var PHONE_TEL = "__PHONE_TEL__";
  var PLAN_BASE = "__PLAN_BASE__";
  var APTS = JSON.parse(document.getElementById("apt-data").textContent);
  var PK = JSON.parse(document.getElementById("pk-data").textContent);
  var LOCALE = LANG === "en" ? "en-GB" : (LANG === "ru" ? "ru-RU" : "ro-RO");
  var state = { building: "", apt: "", floor: null, rooms: null, roomsActual: null, area: null, tariff: null, opts: {} };

  function $(id) { return document.getElementById(id); }
  function show(el, on) { el.hidden = !on; }
  function clipRooms(r) { return Math.max(2, Math.min(4, r)); }
  function fmtArea(a) { try { return Number(a).toLocaleString(LOCALE, { maximumFractionDigits: 2 }); } catch (e) { return String(a); } }
  function normNum(s) {
    s = String(s || "").replace(/[０-９]/g, function (d) { return String.fromCharCode(d.charCodeAt(0) - 0xFEE0); });
    s = s.replace(/[^0-9]/g, "").replace(/^0+/, "");
    return s;
  }
  function normPhone(s) {
    var d = String(s || "").replace(/\D/g, "");
    if (d.indexOf("00") === 0) d = d.slice(2);
    if (d.length === 8) d = "373" + d;
    else if (d.length === 9 && d.charAt(0) === "0") d = "373" + d.slice(1);
    if (d.indexOf("373") === 0 && d.length === 11) return "+" + d;
    if (d.length >= 10 && d.length <= 15) return "+" + d;
    return null;
  }
  function scrollTo(el) {
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    el.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
  }
  function resetBelow() {
    state.tariff = null; state.rooms = null; state.roomsActual = null; state.area = null; state.floor = null;
    show($("step2"), false); show($("step3"), false); show($("cfg-result"), false); show($("cfg-form"), true);
    show($("cfg-aptcard"), false);
    $("cfg-tariffs").innerHTML = "";
  }
  function setTier(fig, tier) {
    if (!fig) return;
    fig.dataset.tier = tier;
    Array.prototype.forEach.call(fig.querySelectorAll("[data-set-tier]"), function (b) { b.setAttribute("aria-pressed", b.dataset.setTier === tier ? "true" : "false"); });
  }
  Array.prototype.forEach.call(document.querySelectorAll("[data-set-tier]"), function (b) {
    b.addEventListener("click", function () { setTier(b.closest(".planx"), b.dataset.setTier); });
  });
  Array.prototype.forEach.call(document.querySelectorAll("[data-show-plan]"), function (t) {
    t.addEventListener("click", function () {
      Array.prototype.forEach.call(document.querySelectorAll("[data-show-plan]"), function (x) {
        x.setAttribute("aria-pressed", x === t ? "true" : "false");
        show($(x.dataset.showPlan), x === t);
      });
    });
  });
  Array.prototype.forEach.call(document.querySelectorAll(".blk"), function (tile) {
    tile.addEventListener("click", function () {
      $("cfg-building").value = tile.dataset.block; rangeHint(tile.dataset.block);
      Array.prototype.forEach.call(document.querySelectorAll(".blk"), function (x) { x.setAttribute("aria-pressed", x === tile ? "true" : "false"); });
      show($("cfg-found"), false); show($("cfg-manual"), false); resetBelow();
      $("cfg-apt").focus();
    });
  });
  function eur(v) { return String(v).replace(/\B(?=(\d{3})+(?!\d))/g, LANG === "en" ? "," : "\u00a0") + "\u00a0€"; }
  function rangeHint(b) {
    var st = UI.bstats[b], hint = $("cfg-apt-hint"), inp = $("cfg-apt");
    if (st) { hint.textContent = UI.range_hint.replace("{b}", b).replace("{c}", st[0]).replace("{from}", st[1]).replace("{to}", st[2]); inp.placeholder = st[1] + "–" + st[2]; }
    else { hint.textContent = UI.apt_hint; inp.placeholder = UI.apt_placeholder; }
  }
  var REDUCE = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  function pulse(el) {
    if (!el || REDUCE || !el.animate) return;
    el.animate([{ opacity: 0.35, transform: "translateY(4px)" }, { opacity: 1, transform: "none" }], { duration: 200, easing: "cubic-bezier(0.23, 1, 0.32, 1)" });
  }
  function recalc() {
    var M = UI.mkt, opts = 0, keys = Object.keys(state.opts).filter(function (k) { return state.opts[k]; });
    keys.forEach(function (k) { opts += UI.opt_prices[k] || 0; });
    var pkg = state.tariff && state.rooms && UI.price_num[String(state.rooms)] ? UI.price_num[String(state.rooms)][state.tariff] : null;
    show($("sum-empty"), !pkg); show($("sum-rows"), !!pkg);
    if (!pkg) return null;
    var eq = UI.equip_num[String(state.rooms)][state.tariff] + opts / (1 + UI.prog_share);
    var total = pkg + opts, promo = Math.round((total - eq * UI.promo_pct / 100) / 10) * 10;
    $("sum-pkg-l").textContent = M.sum_pkg + " " + (PK.labels[state.tariff] || "");
    $("sum-pkg").textContent = eur(pkg); $("sum-opts").textContent = opts ? "+" + eur(opts) : "—";
    $("sum-old").textContent = eur(total); $("sum-total").textContent = eur(promo);
    Array.prototype.forEach.call(document.querySelectorAll(".offer-inline .oc"), function (c) { c.hidden = c.dataset.oc !== String(state.rooms) + "-" + state.tariff; });
    pulse($("sum-total")); pulse($("rc-total"));
    var apt = state.building ? UI.block_word + " " + state.building + (state.apt ? " · № " + state.apt : "") : "";
    if (state.area) apt += (apt ? " · " : "") + fmtArea(state.area) + " " + UI.area_unit;
    $("rc-apt").textContent = apt || "—";
    $("rc-pkg").textContent = (PK.labels[state.tariff] || "") + " · " + eur(pkg);
    $("rc-opts").textContent = keys.length ? keys.map(function (k) { return UI.opt_names[k]; }).join(", ") + " · +" + eur(opts) : M.recap_none;
    $("rc-old").textContent = eur(total); $("rc-total").textContent = eur(promo);
    return total;
  }
  Array.prototype.forEach.call(document.querySelectorAll("[data-opt]"), function (b) {
    b.addEventListener("click", function () {
      var k = b.dataset.opt; state.opts[k] = !state.opts[k];
      b.setAttribute("aria-pressed", state.opts[k] ? "true" : "false");
      recalc();
    });
  });
  (function () {
    var bar = $("stepper"); if (!bar) return;
    function upd() {
      var done = !$("cfg-result").hidden && !$("cfg-result").querySelector(".cfg-error");
      var cur = done ? 4 : !$("step3").hidden ? 3 : !$("step2").hidden ? 2 : 1;
      Array.prototype.forEach.call(bar.children, function (li) {
        var k = +li.dataset.step; li.className = k < cur ? "done" : k === cur ? "on" : "";
        li.querySelector("a").setAttribute("aria-current", k === cur ? "step" : "false");
      });
    }
    var mo = new MutationObserver(upd);
    ["step2", "step3", "cfg-result"].forEach(function (id) { mo.observe($(id), { attributes: true, attributeFilter: ["hidden"], childList: id === "cfg-result" }); });
    Array.prototype.forEach.call(bar.querySelectorAll("a"), function (a) {
      a.addEventListener("click", function (e) { var t = $(a.getAttribute("href").slice(1)); if (!t || t.hidden) { e.preventDefault(); } });
    });
    upd();
  })();
  (function () {
    var of = document.querySelector(".offer"); if (!of) return;
    function sync() {
      Array.prototype.forEach.call(of.querySelectorAll(".oc"), function (c) { c.hidden = c.dataset.oc !== of.dataset.size + "-" + of.dataset.tier; });
      Array.prototype.forEach.call(of.querySelectorAll("[data-of-size]"), function (b) { b.setAttribute("aria-pressed", b.dataset.ofSize === of.dataset.size ? "true" : "false"); });
      Array.prototype.forEach.call(of.querySelectorAll("[data-of-tier]"), function (b) { b.setAttribute("aria-pressed", b.dataset.ofTier === of.dataset.tier ? "true" : "false"); });
    }
    if (window.matchMedia && matchMedia("(max-width: 700px)").matches) {
      Array.prototype.forEach.call(of.querySelectorAll(".oc-det"), function (d) { d.open = false; });
    }
    Array.prototype.forEach.call(of.querySelectorAll("[data-of-size]"), function (b) { b.addEventListener("click", function () { of.dataset.size = b.dataset.ofSize; sync(); }); });
    Array.prototype.forEach.call(of.querySelectorAll("[data-of-tier]"), function (b) { b.addEventListener("click", function () { of.dataset.tier = b.dataset.ofTier; sync(); }); });
  })();
  $("cfg-to-step2").addEventListener("click", function () { scrollTo($("step2")); });
  $("cfg-no-number").addEventListener("click", function () {
    show($("cfg-notfound-text"), false); show($("cfg-manual"), true); scrollTo($("cfg-manual"));
  });
  (function () {
    var pb = (new URLSearchParams(location.search).get("b") || "").toUpperCase();
    var tile = pb && document.querySelector('.blk[data-block="' + pb + '"]');
    if (tile) { tile.click(); setTimeout(function () { scrollTo($("step1")); }, 50); }
  })();
  function markBlock(b) {
    rangeHint(b);
    Array.prototype.forEach.call(document.querySelectorAll(".blk"), function (x) { x.setAttribute("aria-pressed", x.dataset.block === b ? "true" : "false"); });
  }
  function showAptCard(found) {
    var plan = $("cfg-plan-img"), blk = $("cfg-block-img");
    var pfig = plan.closest("figure");
    if (found.p) { plan.src = PLAN_BASE + found.p; plan.alt = UI.your_plan + " — " + found.b + "/" + found.n; show(pfig, true); }
    else { plan.removeAttribute("src"); show(pfig, false); }
    blk.src = "../assets/lagmar/blocks/" + found.b + ".jpg"; blk.alt = UI.block_word + " " + found.b;
    $("cfg-block-cap").textContent = UI.your_block + ": " + found.b;
    show($("cfg-aptcard"), true);
  }

  function renderTariffs(cls) {
    var cat = PK[String(cls)];
    var wrap = $("cfg-tariffs");
    wrap.innerHTML = "";
    if (!cat) { $("cfg-upsell").textContent = UI.error_text + " " + PHONE_DISPLAY; return; }
    ["basic", "comfort", "premium"].forEach(function (tier) {
      var card = document.createElement("button");
      card.type = "button"; card.className = "card tariff-card"; card.setAttribute("role", "radio");
      card.setAttribute("aria-checked", "false"); card.dataset.tier = tier;
      var body = document.createElement("div"); body.className = "body";
      var h3 = document.createElement("h3"); h3.textContent = PK.labels[tier] || tier;
      if (tier === "comfort") { var b = document.createElement("span"); b.className = "badge-rec"; b.textContent = PK.labels.recommended || ""; h3.appendChild(b); }
      var pr = document.createElement("p"); pr.className = "tariff-price"; var px = PK.price_txt && PK.price_txt[String(cls)]; if (px) { var pb = document.createElement("b"); pb.textContent = px[tier]; var ps = document.createElement("small"); ps.textContent = PK.labels.price_vat; pr.appendChild(pb); pr.appendChild(ps); } else { pr.textContent = PK.labels.price_note || ""; }
      var ul = document.createElement("ul"); ul.className = "tariff-list";
      (cat[tier] || []).forEach(function (t) { var li = document.createElement("li"); li.textContent = t; ul.appendChild(li); });
      body.appendChild(h3); body.appendChild(pr); body.appendChild(ul); card.appendChild(body);
      card.addEventListener("click", function () {
        Array.prototype.forEach.call(wrap.querySelectorAll(".tariff-card"), function (c) { c.setAttribute("aria-checked", "false"); });
        card.setAttribute("aria-checked", "true");
        state.tariff = tier; recalc();
        setTier($("s2-" + state.rooms), tier);
        show($("step3"), true);
        scrollTo($("cfg-opts-title"));
      });
      wrap.appendChild(card);
    });
    $("cfg-upsell").textContent = "";
  }

  function showStep2(roomsActual, area, floor) {
    state.roomsActual = roomsActual; state.rooms = clipRooms(roomsActual); state.area = area || null; state.floor = floor;
    show($("cfg-edge"), roomsActual < 2 || roomsActual > 4);
    renderTariffs(state.rooms); recalc();
    ["2", "3", "4"].forEach(function (k) { show($("s2-" + k), String(state.rooms) === k); });
    setTier($("s2-" + state.rooms), "comfort");
    show($("step2"), true);
    if (state.found) { scrollTo($("cfg-found")); } else { scrollTo($("step2")); }
  }

  function doFind() {
    var b = $("cfg-building").value;
    var n = normNum($("cfg-apt").value);
    resetBelow();
    show($("cfg-manual"), false); show($("cfg-found"), false); show($("cfg-notfound-text"), true);
    state.building = b; state.apt = n;
    if (!b) { $("cfg-found").textContent = UI.choose_building; show($("cfg-found"), true); $("cfg-building").focus(); return; }
    if (!n) { show($("cfg-manual"), true); return; }
    var found = null;
    for (var i = 0; i < APTS.length; i++) { if (APTS[i].b === b && normNum(APTS[i].n) === n) { found = APTS[i]; break; } }
    if (found) {
      var fl = String(found.f) === "0" ? UI.floor_ground : (UI.floor_word + " " + found.f);
      $("cfg-found").textContent = UI.found_prefix + " " + UI.building_label + " " + b + " · " + fl + " · " + found.r + " " + UI.rooms_word + " · " + fmtArea(found.a) + " " + UI.area_word;
      show($("cfg-found"), true);
      markBlock(b);
      showAptCard(found);
      state.found = true;
      showStep2(found.r, found.a, String(found.f));
    } else {
      show($("cfg-manual"), true);
    }
  }

  $("cfg-search").addEventListener("submit", function (ev) { ev.preventDefault(); doFind(); });
  $("cfg-building").addEventListener("change", function () { markBlock($("cfg-building").value); show($("cfg-found"), false); show($("cfg-manual"), false); resetBelow(); });
  $("cfg-apt").addEventListener("input", function () { show($("cfg-found"), false); show($("cfg-manual"), false); resetBelow(); });
  Array.prototype.forEach.call(document.querySelectorAll(".cfg-room-btn"), function (btn) {
    btn.addEventListener("click", function () {
      Array.prototype.forEach.call(document.querySelectorAll(".cfg-room-btn"), function (x) { x.setAttribute("aria-pressed", "false"); });
      btn.setAttribute("aria-pressed", "true");
      state.found = false;
      showStep2(parseInt(btn.dataset.rooms, 10), null, null);
    });
  });

  function showResult(node) { var r = $("cfg-result"); r.innerHTML = ""; r.appendChild(node); show(r, true); }
  function phoneLink() { var a = document.createElement("a"); a.href = "tel:" + PHONE_TEL; a.textContent = PHONE_DISPLAY; return a; }
  function successNode(url) {
    var d = document.createElement("div");
    var s = document.createElement("strong"); s.textContent = UI.success_title + " "; d.appendChild(s);
    if (url) {
      d.appendChild(document.createTextNode(UI.success_text + " "));
      var a = document.createElement("a"); a.href = url; a.target = "_blank"; a.rel = "noopener noreferrer"; a.className = "btn btn-primary btn-sm"; a.textContent = UI.success_link; d.appendChild(a);
    }
    var p = document.createElement("p"); p.textContent = UI.success_next; d.appendChild(p);
    var again = document.createElement("a"); again.href = "lagmar.html"; again.className = "cfg-again"; again.textContent = UI.again; d.appendChild(again);
    return d;
  }
  function errorNode(text, withPhone) {
    var d = document.createElement("div"); d.className = "cfg-error";
    d.appendChild(document.createTextNode(text + " "));
    if (withPhone) d.appendChild(phoneLink());
    return d;
  }
  function fieldError(id, text) {
    var el = $(id), host = el.closest("label") || el, msg = document.createElement("p");
    msg.className = "field-error"; msg.id = id + "-err"; msg.setAttribute("role", "alert"); msg.textContent = text;
    host.insertAdjacentElement("afterend", msg);
    el.setAttribute("aria-invalid", "true"); el.setAttribute("aria-describedby", msg.id);
    host.scrollIntoView({ block: "center", behavior: "smooth" }); el.focus({ preventScroll: true });
  }
  function clearFieldErrors() {
    Array.prototype.forEach.call(document.querySelectorAll("#cfg-form .field-error"), function (m) { m.remove(); });
    ["cfg-name", "cfg-phone", "cfg-consent"].forEach(function (id) { var el = $(id); el.removeAttribute("aria-invalid"); });
    $("cfg-phone").setAttribute("aria-describedby", "cfg-phone-hint"); $("cfg-name").removeAttribute("aria-describedby"); $("cfg-consent").removeAttribute("aria-describedby");
  }
  ["cfg-name", "cfg-phone", "cfg-consent"].forEach(function (id) {
    $(id).addEventListener(id === "cfg-consent" ? "change" : "input", function () {
      var m = $(id + "-err"); if (m) { m.remove(); $(id).removeAttribute("aria-invalid"); }
    });
  });
  function validQuoteUrl(u) { return typeof u === "string" && /^https:\/\/app\.smartspace\.md\/q\/[A-Za-z0-9_-]{10,}$/.test(u); }

  $("cfg-form").addEventListener("submit", function (ev) {
    ev.preventDefault();
    var btn = $("cfg-submit");
    if ($("cfg-hp").value) { showResult(successNode(null)); show($("cfg-form"), false); return; }
    if (!state.tariff || !state.rooms) { showResult(errorNode(UI.tariff_required, false)); scrollTo($("step2")); return; }
    clearFieldErrors();
    var name = $("cfg-name").value.trim();
    if (name.length < 2) { fieldError("cfg-name", UI.error_name); return; }
    var phone = normPhone($("cfg-phone").value);
    if (!phone) { fieldError("cfg-phone", UI.error_phone); return; }
    if (!$("cfg-consent").checked) { fieldError("cfg-consent", UI.error_consent); return; }
    show($("cfg-result"), false);
    btn.disabled = true; btn.textContent = UI.sending;
    var payload = {
      name: name, phone: phone, email: $("cfg-email").value.trim() || null,
      building: state.building || null, floor: state.floor, apartment_number: state.apt || null,
      rooms: state.rooms, rooms_actual: state.roomsActual, area_m2: state.area, tariff: state.tariff,
      options: Object.keys(state.opts).filter(function (k) { return state.opts[k]; }), estimate_eur: recalc(),
      lang: LANG, source: "grenton-demo", page_url: location.href, consent: $("cfg-consent").checked
    };
    var ctrl = typeof AbortController !== "undefined" ? new AbortController() : null;
    var timer = ctrl ? setTimeout(function () { ctrl.abort(); }, 15000) : null;
    fetch(API_URL, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload), signal: ctrl ? ctrl.signal : undefined })
      .then(function (r) {
        if (r.status === 422) throw new Error("422");
        if (r.status === 429) throw new Error("429");
        if (!r.ok) throw new Error("http" + r.status);
        return r.json();
      })
      .then(function (data) {
        var url = data && validQuoteUrl(data.quote_url) ? data.quote_url : null;
        showResult(successNode(url));
        $("step3").classList.add("is-done");
        show($("cfg-form"), false);
      })
      .catch(function (e) {
        var msg = String(e && e.message);
        if (msg === "422") showResult(errorNode(UI.error_phone, false));
        else if (msg === "429") showResult(errorNode(UI.error_rate, false));
        else showResult(errorNode(UI.error_text, true));
        btn.disabled = false; btn.textContent = UI.submit_btn;
      })
      .finally(function () { if (timer) clearTimeout(timer); });
  });
})();
"""



def _json_for_script(obj, lang=None):
    if lang:
        obj = typo_data(obj, lang)  # strings the page scripts render get the HTML typography too
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def packages_static_html(lang, pk):
    lab = pk["labels"]
    m = LAGMAR_MKT[lang]

    def why(key, tier):
        txt = lab[key]
        q, _, rest = txt.partition("?")
        return (f'<div class="why-card why-{tier}"><span class="tier tier-{tier}">{esc(lab[tier])}</span>'
                f'<b>{esc(q.strip())}?</b><p>{esc(rest.strip())}</p></div>')
    blocks = []
    for n in ["2", "3", "4"]:
        tiers = "".join(
            f'<div class="pk-tier"><h4>{esc(lab[t])}</h4><ul>' + "".join(f"<li>{esc(x)}</li>" for x in pk[n][t]) + "</ul></div>"
            for t in ["basic", "comfort", "premium"])
        blocks.append(f'<div class="pk-size"><h3>{esc(lab["size_title"].replace("{n}", n))}</h3><div class="pk-grid">{tiers}</div></div>')
    return (f'<div class="why-cards">{why("why_comfort", "comfort")}{why("why_premium", "premium")}</div>'

            f'<p class="cfg-footnote">{esc(lab["footnote"])}</p>')


def faq_html(lang):
    return "".join(f'<details class="faq"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in FAQ[lang])


def faq_jsonld(lang):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ[lang]]}


def plan_widget_html(lang, n, pk, wid, extra_cls="", hidden=False):
    v = LAGMAR_VIS[lang]
    w, h = PLAN_SIZE[n]
    lab = pk["labels"]
    marks = "".join(
        f'<span class="mk mk-{t}" data-t="{tiers}" style="left:{x}%;top:{y}%;--i:{i}" title="{esc(v["devices"][t])}">{ico(t)}</span>'
        for i, (t, x, y, tiers) in enumerate(PLAN_MARKERS[n]))
    tier_btns = "".join(
        f'<button type="button" class="planx-tier" data-set-tier="{t}" aria-pressed="{"true" if t == "comfort" else "false"}">{esc(lab[t])}'
        f'<small>{LAGMAR_MKT[lang]["tier_from"].replace("{p}", fmt_eur(PRICES[n][t], lang))}</small></button>'
        for t in ["basic", "comfort", "premium"])
    legend = []
    for t in DEVICE_ORDER:
        cnt = {k: sum(1 for m in PLAN_MARKERS[n] if m[0] == t and k in m[3]) for k in "bcp"}
        if not any(cnt.values()):
            continue
        legend.append(f'<li class="lg-{t}" data-has="{"".join(k for k in "bcp" if cnt[k])}"><i class="mk mk-{t}">{ico(t)}</i>'
                      f'{esc(v["devices"][t])} <b class="c-b">{cnt["b"]}</b><b class="c-c">{cnt["c"]}</b><b class="c-p">{cnt["p"]}</b></li>')
    hid = " hidden" if hidden else ""
    return f'''<figure class="planx {extra_cls}" id="{wid}" data-tier="comfort" data-cls="{n}"{hid}>
  <div class="planx-tiers" role="group">{tier_btns}</div>
  <div class="planx-body">
    <div class="planx-stage"><div class="planx-canvas"><img src="../assets/lagmar/plans/plan-{n}.png" width="{w}" height="{h}" alt="{esc(v["plan_alt"].replace("{n}", n))}" loading="lazy">{marks}</div></div>
    <figcaption><ul class="planx-legend">{"".join(legend)}</ul><p class="planx-note">{esc(v["example_note"])}</p></figcaption>
  </div>
</figure>'''


def lagmar_hero_html(lang, u):
    v = LAGMAR_VIS[lang]
    stats = "".join(f'<li><b>{esc(a)}</b><span>{esc(b)}</span></li>' for a, b in v["hero_stats"])
    return f'''<section class="lg-hero">
  <img class="lg-hero-bg" src="../assets/lagmar/hero.jpg" srcset="../assets/lagmar/hero-960.jpg 960w, ../assets/lagmar/hero.jpg 1920w" sizes="100vw" alt="Lagmar Smart Home" fetchpriority="high">
  <video class="lg-hero-bg lg-hero-vid" muted loop playsinline preload="none" data-auto aria-hidden="true" data-src-mobile="../assets/lagmar/hero-loop-mobile.mp4"><source src="../assets/lagmar/hero-loop-{lang}.mp4" type="video/mp4"></video>
  <div class="wrap lg-hero-inner">
    <div class="lg-logos"><img src="../assets/lagmar/logo-lagmar.png" alt="Lagmar Smart Home" width="160" height="48"><span class="x">×</span><span class="gr">SmartSpace <small>by Grenton</small></span></div>
    <h1>{u["h1"]}</h1>
    <p class="lead">{u["lead"]}</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="#step1">{v["cta_find"]}</a>
    </div>
    <ul class="lg-stats">{stats}</ul>
    <noscript><p class="lead"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p></noscript>
  </div>
</section>'''


def block_stats(apartments):
    st = {}
    for x in apartments:
        n = int(re.sub(r"\D", "", str(x["n"])) or 0)
        c, lo, hi = st.get(x["b"], (0, 10 ** 6, 0))
        st[x["b"]] = (c + 1, min(lo, n), max(hi, n))
    return st


def lagmar_blocks_html(lang, stats):
    v = LAGMAR_VIS[lang]
    m = LAGMAR_MKT[lang]
    tiles = "".join(
        f'<button type="button" class="blk" data-block="{b}" aria-pressed="false"><img src="../assets/lagmar/blocks/{b}.jpg" width="330" height="508" alt="{esc(v["block_word"])} {b}" loading="lazy"><span>{b}</span>'
        + (f'<small class="blk-meta"><b>{stats[b][0]}</b> {m["apts"]}<br>№ {stats[b][1]}–{stats[b][2]}</small>' if b in stats else "")
        + '</button>'
        for b in BUILDINGS)
    return f'<p class="cfg-note"><b>{v["blocks_title"]}.</b> {v["blocks_sub"]}</p><div class="blk-row">{tiles}</div>'


def spec_lines(spec, lang):
    t = OFFER_TXT[lang]["spec"]
    rows = []
    light = spec["l"] + spec["d"]
    rows.append((t["light"], f'{light}' + (f' · {t["light_dim"].replace("{d}", str(spec["d"]))}' if spec["d"] else "")))
    if spec["led"]:
        rows.append((t["led"], str(spec["led"])))
    rows.append((t["s"], str(spec["s"])))
    if spec["b"]:
        rows.append((t["b"], str(spec["b"])))
    rows.append((t["h"], str(spec["h"])))
    pan = [f"Smart Panel × {spec['sp']}"] if spec["sp"] else []
    if spec["tp4"] + spec["tp8"]:
        pan.append(f"Touch Panel × {spec['tp4'] + spec['tp8']}")
    rows.append((t["panels"], ", ".join(pan)))
    rows.append((t["leak"], str(spec["leak"]) + (f' {t["valve"]}' if spec["valve"] else "")))
    if spec["smoke"]:
        rows.append((t["smoke"], str(spec["smoke"])))
    if spec["motion"]:
        rows.append((t["motion"], str(spec["motion"])))
    if spec["multi"]:
        rows.append((t["multi"], str(spec["multi"])))
    rows.append((t["app"], t["yes"]))
    return rows


def offer_card_html(lang, n, tier):
    o = OFFER_TXT[lang]
    off = OFFER[n][tier]
    spec = PACKAGE_SPEC[n][tier]
    get = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in spec_lines(spec, lang))
    rows = [f'<tr class="oc-group oc-pre-g"><th colspan="4" scope="rowgroup">{o["groups"]["pre"]}</th></tr>']
    for code, qty in off["pre"]:
        name, what = o["bom"][code]
        rows.append(f'<tr class="oc-pre"><th scope="row"><b>{name}</b><small>{what}</small></th><td class="num">{qty}</td>'
                    f'<td class="num"><span class="oc-tag">{o["pre_price"]}</span></td><td class="num">{fmt_eur(0, lang)}</td></tr>')  # price: tag; sum: 0 (phones hide the price cell)
    group_of = {"SP": "wall", "TP4": "wall", "TP8": "wall", "LEAK": "sens", "VALVE": "sens", "SMOKE": "sens", "MOTION": "sens", "MULTI": "sens"}
    last = None
    for code, qty, unit in off["bom"]:
        g = group_of.get(code, "cab")
        if g != last:
            rows.append(f'<tr class="oc-group"><th colspan="4" scope="rowgroup">{o["groups"][g]}</th></tr>')
            last = g
        name, what = o["bom"][code]
        if unit is None:
            price, total = f'<span class="oc-na">{o["in_offer"]}</span>', "—"
        else:
            price, total = fmt_eur(unit, lang), fmt_eur(unit * qty, lang)
        rows.append(f'<tr><th scope="row"><b>{name}</b><small>{what}</small></th><td class="num">{qty}</td><td class="num">{price}</td><td class="num">{total}</td></tr>')
    sensors = f'<p class="oc-note">{o["sensors_note"]}</p>' if off["unpriced"] else ""
    return f'''<div class="oc" data-oc="{n}-{tier}"{"" if (n, tier) == ("2", "comfort") else " hidden"}>
  <div class="oc-get">
    <h3>{o["get"]}</h3>
    <dl class="oc-spec">{get}</dl>
  </div>
  <div class="oc-built">
    <details class="oc-det" open>
    <summary><h3>{o["built"]}</h3><span class="oc-sum">{o["items"].replace("{n}", str(len(off["bom"]) + len(off["pre"])))} · <b>{fmt_eur(off["total"], lang)}</b></span></summary>
    <div class="oc-scroll"><table class="oc-bom">
      <thead><tr><th scope="col">{o["col_item"]}</th><th scope="col" class="num">{o["col_qty"]}</th><th scope="col" class="num">{o["col_unit"]}</th><th scope="col" class="num">{o["col_sum"]}</th></tr></thead>
      <tbody>{"".join(rows)}</tbody>
      <tfoot>
        <tr><th scope="row" colspan="3">{o["equipment"]}</th><td class="num">{fmt_eur(off["equipment"], lang)}</td></tr>
        <tr><th scope="row" colspan="3">{o["programming"]}<small>{o["programming_note"]}</small></th><td class="num">{fmt_eur(off["programming"], lang)}</td></tr>
        <tr class="oc-total"><th scope="row" colspan="3">{o["total"]}</th><td class="num">{fmt_eur(off["total"], lang)}</td></tr>
      </tfoot>
    </table></div>
    </details>
    {sensors}
  </div>
</div>'''


def preinstall_html(lang):
    o = OFFER_TXT[lang]
    chips = "".join(f'<li>{ico("check")}{o["bom"][c][0]}</li>' for c, _q in OFFER["2"]["basic"]["pre"])
    return (f'<div class="preinst"><p class="preinst-t">{o["pre_title"]}</p><ul class="preinst-l">{chips}</ul>'
            f'<p class="preinst-x">{o["pre_text"]}</p></div>')


def offer_html(lang, pk):
    o = OFFER_TXT[lang]
    lab = pk["labels"]
    sizes = "".join(f'<button type="button" data-of-size="{n}" aria-pressed="{"true" if n == "2" else "false"}">{CMP[lang]["sizes"][n]}</button>' for n in ["2", "3", "4"])
    tiers = "".join(
        f'<button type="button" data-of-tier="{t}" aria-pressed="{"true" if t == "comfort" else "false"}">{esc(lab[t])}'
        + "".join(f'<small class="ofp ofp-{n}">{fmt_eur(PRICES[n][t], lang)}</small>' for n in ["2", "3", "4"]) + "</button>"
        for t in ["basic", "comfort", "premium"])
    cards = "".join(offer_card_html(lang, n, t) for n in ["2", "3", "4"] for t in ["basic", "comfort", "premium"])
    steps = "".join(f'<li><span>{i}</span><b>{a}</b><p>{b}</p></li>' for i, (a, b) in enumerate(o["steps"], 1))
    incl = "".join(f"<li>{ico('check')}{x}</li>" for x in o["incl"])
    notincl = "".join(f'<li><span class="x" aria-hidden="true">×</span>{x}</li>' for x in o["not_incl"])
    return f'''<div class="offer" data-size="2" data-tier="comfort">
  <div class="offer-ctl">
    <div class="of-row"><span>{o["size"]}</span><div class="of-sizes" role="group">{sizes}</div></div>
    <div class="of-row"><span>{o["tier"]}</span><div class="of-tiers" role="group">{tiers}</div></div>
  </div>
  {cards}
  <div class="offer-how">
    <h3>{o["how"]}</h3>
    <ol class="how-steps">{steps}</ol>
    <div class="how-lists">
      <div><h4>{o["incl_title"]}</h4><ul class="incl">{incl}</ul></div>
      <div><h4>{o["not_incl_title"]}</h4><ul class="notincl">{notincl}</ul></div>
    </div>
    <p class="oc-note">{o["base_note"]} {o["sources"]}</p>
  </div>
</div>'''


def promo_html(lang):
    m = LAGMAR_MKT[lang]
    return f'''<div class="promo-strip" role="note"><div class="wrap promo-strip-inner">
  <b class="promo-strip-badge">−{PROMO_PCT}%</b><span>{m["strip"]}</span><a href="#step1">{m["strip_cta"]} {ico("arrow")}</a>
</div></div>'''

def options_html(lang, interactive):
    m = LAGMAR_MKT[lang]
    items = []
    for k, (t, d) in m["options"].items():
        price = "+" + fmt_eur(OPTION_PRICES[k], lang)
        inner = (f'<span class="mk mk-{OPTION_ICON[k]}">{ico(OPTION_ICON[k])}</span>'
                 f'<span class="opt-t"><b>{t}</b><small>{d}</small></span><span class="opt-p">{price}</span>')
        if interactive:
            items.append(f'<button type="button" class="opt" data-opt="{k}" aria-pressed="false">{inner}<span class="opt-check">{ico("check")}</span></button>')
        else:
            items.append(f'<div class="opt">{inner}</div>')
    return f'<div class="opts{" opts-pick" if interactive else " rail"}">{"".join(items)}</div>'

def lagmar_examples_html(lang, pk):
    v = LAGMAR_VIS[lang]
    tabs = "".join(
        f'<button type="button" class="ex-tab" data-show-plan="ex-{n}" aria-pressed="{"true" if n == "2" else "false"}">{esc(v["tabs"][n])}</button>'
        for n in ["2", "3", "4"])
    widgets = "".join(plan_widget_html(lang, n, pk, f"ex-{n}", "ex-plan", hidden=(n != "2")) for n in ["2", "3", "4"])
    return f'''<section class="block alt" id="examples">
  <div class="wrap">
    <span class="eyebrow">{v["examples_eyebrow"]}</span>
    <h2 class="h2">{v["examples_title"]}</h2>
    <p class="sub">{v["examples_sub"]}</p>
    <div class="ex-tabs" role="group">{tabs}</div>
    {widgets}
  </div>
</section>'''


def lagmar_page_html(lang, apartments, packages_all):
    u = LAGMAR_UI[lang]
    v = LAGMAR_VIS[lang]
    pk = packages_all[lang]
    ui_js = dict(u, block_word=v["block_word"], your_plan=v["your_plan"], your_block=v["your_block"],
                 bstats={b: list(x) for b, x in block_stats(apartments).items()}, range_hint=LAGMAR_MKT[lang]["range_hint"],
                 mkt={k: LAGMAR_MKT[lang][k] for k in ("sum_pkg", "sum_opts", "sum_total", "sum_promo", "pick_pkg_first", "opt_add", "opt_added", "recap_none")},
                 opt_names={k: t for k, (t, _d) in LAGMAR_MKT[lang]["options"].items()}, area_unit={"ru": "м²"}.get(lang, "m²"),
                 opt_prices=OPTION_PRICES, promo_pct=PROMO_PCT, prog_share=PROGRAMMING_SHARE, price_num=PRICES, equip_num=EQUIPMENT)
    bst = block_stats(apartments)
    m = LAGMAR_MKT[lang]
    building_options = "".join(
        f'<option value="{b}">{b}' + (f' · {bst[b][0]} {m["apts"]} · {bst[b][1]}–{bst[b][2]}' if b in bst else "") + '</option>'
        for b in BUILDINGS)
    js = (LAGMAR_JS.replace("__LANG__", lang).replace("__UI__", _json_for_script(ui_js, lang)).replace("__API__", API_URL)
          .replace("__PHONE_DISPLAY__", PHONE_DISPLAY).replace("__PHONE_TEL__", PHONE_TEL)
          .replace("__PLAN_BASE__", PLAN_IMG_BASE))
    s2_widgets = "".join(plan_widget_html(lang, n, pk, f"s2-{n}", "s2-plan", hidden=True) for n in ["2", "3", "4"])
    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_html(lang, "lagmar", u["title"], META_DESC["lagmar"][lang], [faq_jsonld(lang)])}
</head>
<body class="theme-lagmar">
{sprite_html()}
{nav_html(lang, "lagmar")}
{lagmar_hero_html(lang, u)}
{promo_html(lang)}

<div class="cfg-flow">
<nav class="stepper-bar" aria-label="{esc(m["stepper"][0])} → {esc(m["stepper"][2])}">
  <ol class="stepper wrap" id="stepper">{"".join(f'<li data-step="{i + 1}"{" class=\"on\"" if i == 0 else ""}><a href="#step{i + 1}"><span>{i + 1}</span>{esc(t)}</a></li>' for i, t in enumerate(m["stepper"]))}</ol>
</nav>
<section class="block alt cfg-step" id="step1">
  <div class="wrap">
    <h2 class="h2">{u["step1_title"]}</h2>
    {lagmar_blocks_html(lang, bst)}
    <form id="cfg-search" class="cfg-row" autocomplete="off">
      <label>{u["building_label"]}
        <select id="cfg-building" name="building"><option value="">{u["building_placeholder"]}</option>{building_options}</select>
      </label>
      <label>{u["apt_label"]}
        <input id="cfg-apt" name="apt" type="text" inputmode="numeric" maxlength="4" pattern="[0-9]*" enterkeyhint="search" placeholder="{u["apt_placeholder"]}" aria-describedby="cfg-apt-hint">
      </label>
      <button class="btn btn-primary" type="submit" id="cfg-find">{u["find_btn"]}</button>
    </form>
    <p id="cfg-apt-hint" class="cfg-hint">{u["apt_hint"]}</p>
    <button type="button" class="link-btn" id="cfg-no-number">{m["no_number"]}</button>
    <div id="cfg-found" class="cfg-found" role="status" aria-live="polite" hidden></div>
    <div id="cfg-aptcard" class="aptcard" hidden>
      <figure class="aptcard-plan"><img id="cfg-plan-img" alt="" loading="lazy"><figcaption>{v["your_plan"]}</figcaption></figure>
      <figure class="aptcard-block"><img id="cfg-block-img" alt="" loading="lazy"><figcaption id="cfg-block-cap"></figcaption></figure>
      <div class="aptcard-cta"><button type="button" class="btn btn-primary" id="cfg-to-step2">{m["to_step2"]} {ico("arrow")}</button></div>
    </div>
    <div id="cfg-manual" class="cfg-manual" role="status" aria-live="polite" hidden>
      <p class="cfg-note" id="cfg-notfound-text">{u["not_found_text"]}</p>
      <div class="cfg-row">
        <span>{u["manual_label"]}:</span>
        <button type="button" class="btn btn-ghost cfg-room-btn" data-rooms="2" aria-pressed="false">2</button>
        <button type="button" class="btn btn-ghost cfg-room-btn" data-rooms="3" aria-pressed="false">3</button>
        <button type="button" class="btn btn-ghost cfg-room-btn" data-rooms="4" aria-pressed="false">4</button>
      </div>
    </div>
  </div>
</section>

<section class="block cfg-step" id="step2" hidden>
  <div class="wrap">
    <h2 class="h2">{u["step2_title"]}</h2>
    {preinstall_html(lang)}
    <p class="cfg-note" id="cfg-edge" hidden>{u["edge_hint"]}</p>
    <div class="grid" id="cfg-tariffs" role="radiogroup" aria-label="{esc(u["step2_title"])}"></div>
    <p class="cfg-note" id="cfg-upsell" hidden></p>
    <h3 class="s2-plan-title" id="cfg-opts-title">{m["opt_s2"]}</h3>
    {options_html(lang, interactive=True)}
    <div class="sum" id="cfg-sum">
      <p class="sum-empty" id="sum-empty">{m["pick_pkg_first"]}</p>
      <dl id="sum-rows" hidden>
        <div><dt id="sum-pkg-l">{m["sum_pkg"]}</dt><dd id="sum-pkg"></dd></div>
        <div><dt>{m["sum_opts"]}</dt><dd id="sum-opts"></dd></div>
        <div class="sum-total"><dt>{m["sum_total"]}</dt><dd><s id="sum-old"></s> <b id="sum-total" aria-live="polite"></b></dd></div>
      </dl>
      <p class="sum-caption">{m["promo_caption"]}</p>
      <p class="sum-note">{m["sum_note"]}</p>
    </div>
    <details class="fold price-why"><summary>{m["price_breakdown"]}</summary>{offer_html(lang, pk).replace('class="offer"', 'class="offer offer-inline"', 1)}</details>
    <details class="fold s2-plan"><summary>{m["show_on_plan"]}</summary>{s2_widgets}</details>
  </div>
</section>

<section class="block alt cfg-step" id="step3" hidden>
  <div class="wrap">
    <h2 class="h2">{u["step3_title"]}</h2>
    <div class="s3-grid">
    <div class="s3-main">
    <form id="cfg-form" class="cfg-form" novalidate>
      <input type="text" id="cfg-hp" name="fax_ref" class="cfg-hp" tabindex="-1" aria-hidden="true" autocomplete="new-password">
      <label>{u["name_label"]}<input type="text" id="cfg-name" name="name" required minlength="2" maxlength="80" autocomplete="name"></label>
      <label>{u["phone_label"]}<input type="tel" id="cfg-phone" name="phone" required minlength="6" maxlength="20" autocomplete="tel" inputmode="tel" placeholder="+373 6x xxx xxx" aria-describedby="cfg-phone-hint"></label>
      <p id="cfg-phone-hint" class="cfg-hint">{u["phone_hint"]}</p>
      <label>{u["email_label"]}<input type="email" id="cfg-email" name="email" autocomplete="email" maxlength="120"></label>
      <label class="cfg-consent"><input type="checkbox" id="cfg-consent" required> <span>{u["consent_text"]} <a href="{PRIVACY_URL}" target="_blank" rel="noopener noreferrer">{u["consent_link"]}</a></span></label>
      <button class="btn btn-primary" type="submit" id="cfg-submit">{u["submit_btn"]}</button>
      <p class="cfg-disclaimer">{u["disclaimer"]}</p>
    </form>
    <div class="s3-next">
      <h3>{m["next_title"]}</h3>
      <ul class="checks"><li>{ico("check")}<span>{m["next1"]}</span></li><li>{ico("check")}<span>{m["next2"]}</span></li><li>{ico("check")}<span>{m["next3"]}</span></li></ul>
      <p class="s3-call">{m["call_instead"]} <a href="tel:{PHONE_TEL}">{ico("phone")}{PHONE_DISPLAY}</a> · <a href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener">{ico("chat")}WhatsApp</a></p>
    </div>
    <div id="cfg-result" class="cfg-note cfg-status" role="status" aria-live="polite" hidden></div>
    </div>
    <aside class="recap">
      <h3>{m["recap_title"]}</h3>
      <dl>
        <div><dt>{m["recap_apt"]}</dt><dd id="rc-apt">—</dd></div>
        <div><dt>{m["sum_pkg"]}</dt><dd id="rc-pkg">—</dd></div>
        <div><dt>{m["sum_opts"]}</dt><dd id="rc-opts">{m["recap_none"]}</dd></div>
        <div class="rc-total"><dt>{m["sum_total"]}</dt><dd><s id="rc-old"></s> <b id="rc-total">—</b></dd></div>
      </dl>
      <p class="rc-caption">{m["promo_caption"]}</p>
      <a class="rc-edit" href="#step2">{m["recap_edit"]}</a>
    </aside>
    </div>
  </div>
</section>
</div>


<section class="block alt" id="faq">
  <div class="wrap faq-grid">
    <div class="faq-aside">
      <span class="eyebrow">FAQ</span>
      <h2 class="h2">{u["faq_title"]}</h2>
      <p class="sub">{m["faq_sub"]}</p>
      <div class="cta-row cta-left">
        <a class="btn btn-primary" href="tel:{PHONE_TEL}">{ico("phone")}{PHONE_DISPLAY}</a>
        <a class="btn btn-wa" href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener">{ico("chat")}WhatsApp</a>
      </div>
    </div>
    <div class="faq-list">{faq_html(lang)}</div>
  </div>
</section>

{dealer_band_html(lang, "lagmar")}
{footer_html(lang)}

<script id="apt-data" type="application/json">{_json_for_script(apartments)}</script>
<script id="pk-data" type="application/json">{_json_for_script(pk, lang)}</script>
<script>{js}</script>
<script>{SITE_JS}</script>
</body>
</html>'''


ICON_PATHS = {
    # devices (plan markers / legends)
    "L": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.7.5 1.1 1.3 1.1 2.1V16h5v-.1c0-.8.4-1.6 1.1-2.1A6 6 0 0 0 12 3z"/>',
    "P": '<rect x="4" y="4" width="16" height="16" rx="3"/><rect x="8.5" y="9" width="7" height="5" rx="1"/><path d="M8 17h.01M16 17h.01M8 7h.01M16 7h.01"/>',
    "T": '<path d="M14 14.8V5a2 2 0 0 0-4 0v9.8a4 4 0 1 0 4 0z"/><path d="M12 10v7"/>',
    "W": '<path d="M12 3.5s6 6.4 6 10.8a6 6 0 0 1-12 0C6 9.9 12 3.5 12 3.5z"/><path d="M9.5 15a2.5 2.5 0 0 0 2.5 2.5"/>',
    "S": '<path d="M12 3c.9 3 4.5 4.7 4.5 9a4.5 4.5 0 0 1-9 0c0-2 .9-3.3 2-4.3.2 1.6 1 2.5 2.1 2.7C11 7.9 11 5.6 12 3z"/><path d="M8 21h8"/>',
    "M": '<circle cx="13" cy="4.5" r="1.7"/><path d="M8 21l2.6-6.2L13.5 17v4M6.5 11.5l3.2-3.2h3.9l2.2 3.2H19M11.4 8.6l-1 5.7"/>',
    "C": '<path d="M3.5 4h17M5 4v11M19 4v11M5 7.5h14M5 11h14M5 14.5h14M12 15v3"/><circle cx="12" cy="19.5" r="1.3"/>',
    "A": '<path d="M9 17.5V6l10-2v11.5"/><circle cx="6.5" cy="17.5" r="2.5"/><circle cx="16.5" cy="15.5" r="2.5"/>',
    "Q": '<path d="M3 8.5h10.5a2.8 2.8 0 1 0-2.8-2.8M3 15.5h13.5a2.8 2.8 0 1 1-2.8 2.8M3 12h7"/>',
    "I": '<rect x="6" y="3" width="12" height="18" rx="2.5"/><circle cx="12" cy="9.5" r="2.6"/><path d="M9.5 16.5h5"/>',
    # ui
    "check": '<path d="M5 12.5l4.2 4.2L19 7"/>',
    "play": '<path d="M8 5.5v13l10.5-6.5z"/>',
    "pause": '<path d="M8.5 5v14M15.5 5v14"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "ext": '<path d="M8 16L16 8M9.5 8H16v6.5"/>',
    "shield": '<path d="M12 3l7.5 3v5.5c0 4.6-3.2 8.3-7.5 9.5-4.3-1.2-7.5-4.9-7.5-9.5V6z"/><path d="M8.8 12.2l2.2 2.2 4.2-4.4"/>',
    "wifi": '<path d="M2.5 8.8a14 14 0 0 1 19 0M5.5 12.2a9.5 9.5 0 0 1 13 0M8.6 15.5a5 5 0 0 1 6.8 0"/><circle cx="12" cy="19" r="1"/><path d="M3 3l18 18"/>',
    "tools": '<path d="M14.5 6.5a4 4 0 0 0-5.3 5.2L4 17v3h3l5.3-5.2a4 4 0 0 0 5.2-5.3l-2.6 2.6-2.4-.6-.6-2.4z"/>',
    "pin": '<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>',
    "chat": '<path d="M4 19.5l1.3-3.9A8 8 0 1 1 8.6 19z"/><path d="M9 10.5h.01M12 10.5h.01M15 10.5h.01"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
    "phone": '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
}
ICON_FOR_GROUP = {"light": "L", "climate": "T", "safety": "W", "blinds": "C", "media": "A", "control": "P"}


def sprite_html():
    syms = "".join(
        f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
        f'stroke-linecap="round" stroke-linejoin="round">{v}</symbol>' for k, v in ICON_PATHS.items())
    return f'<svg class="sprite" width="0" height="0" aria-hidden="true" style="position:absolute">{syms}</svg>'


def ico(name, cls="ico"):
    return f'<svg class="{cls}" aria-hidden="true" focusable="false"><use href="#i-{name}"/></svg>'


def mk_icons(letters, lang):
    labels = LAGMAR_VIS[lang]["devices"]
    return "".join(f'<i class="mk mk-{t}" title="{esc(labels[t])}">{ico(t)}</i>' for t in letters)


def tier_chip(lang, tier):
    return f'<span class="tier tier-{tier}">{TIER_CHIP[lang][tier]}</span>'


# assets/grenton/* sizes (width, height); names with an -800 variant get a srcset
G_SIZE = {"app-bedroom": (480, 709), "app-saving": (1000, 666), "bath": (1600, 880), "bedroom": (1600, 880),
          "clu": (800, 800), "hall": (1600, 900), "hallpanels": (800, 928), "hero-poster": (1280, 720),
          "kids": (1000, 1000), "kitchen": (1600, 880), "monolith-hero": (1600, 942), "monolith-wall": (800, 933),
          "multi-wall": (800, 933), "multisensor-poster": (720, 720), "multisensor": (800, 800), "office": (1600, 880),
          "oled": (800, 800), "panel-poster": (960, 540), "salon": (1600, 880), "security": (768, 512),
          "smartpanel": (800, 800), "touch-hero": (1600, 941), "touch-wall": (772, 933)}
G_HAS_800 = {"bath", "bedroom", "hall", "kitchen", "office", "salon", "touch-hero", "monolith-hero"}


def gimg(name, alt, cls="", sizes="(max-width: 700px) 92vw, 45vw", eager=False):
    w, h = G_SIZE[name]
    src = f"../assets/grenton/{name}.webp"
    srcset = f' srcset="../assets/grenton/{name}-800.webp 800w, {src} {w}w" sizes="{sizes}"' if name in G_HAS_800 else ""
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{src}"{srcset} width="{w}" height="{h}" alt="{esc(alt)}"{load}>'


def gvideo(name, poster, label, cls=""):
    w, h = G_SIZE[poster]
    mob = f' data-src-mobile="../assets/grenton/{name}-mobile.mp4"' if name == "hero" else ""
    return (f'<video class="vid {cls}" muted loop playsinline preload="none" data-auto poster="../assets/grenton/{poster}.webp" '
            f'width="{w}" height="{h}" aria-label="{esc(label)}"{mob}><source src="../assets/grenton/{name}.mp4" type="video/mp4"></video>')


def palt(lang, name):
    return PHOTO_ALT[lang].get(name, "Grenton")


def cta_lagmar_html(lang):
    return ""  # merged into the site-wide closing (dealer_band_html)


def simple_hero(eyebrow, h1, lead, media="", extra=""):
    if media:
        return f'''<section class="hero hero-media">
  <div class="wrap hero-media-grid">
    <div><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>{extra}</div>
    <div class="hero-media-visual">{media}</div>
  </div>
</section>'''
    return f'''<section class="hero">
  <div class="wrap">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>'''


SITE_JS = r"""
(function () {
  var d = document, each = function (l, f) { Array.prototype.forEach.call(l, f); };
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var save = navigator.connection && navigator.connection.saveData;
  var hasIO = "IntersectionObserver" in window;

  // reveal on scroll
  if (hasIO && !reduce) {
    d.documentElement.classList.add("js-rv");
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target; el.classList.add("in"); io.unobserve(el);
        var done = function () { el.classList.remove("rv", "in"); };
        el.addEventListener("transitionend", done, { once: true }); setTimeout(done, 900);
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.06 });
    each(d.querySelectorAll(".rv"), function (el) { io.observe(el); });
  }

  // counters
  if (hasIO && !reduce) {
    var co = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        co.unobserve(e.target);
        var el = e.target, to = +el.dataset.count, sep = el.dataset.sep || " ", t0 = null;
        function fmt(v) { return String(v).replace(/\B(?=(\d{3})+(?!\d))/g, sep); }
        function step(ts) { if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / 800); el.textContent = fmt(Math.round(to * (1 - Math.pow(1 - p, 3)))); if (p < 1) requestAnimationFrame(step); }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.5 });
    each(d.querySelectorAll("[data-count]"), function (el) {
      if (el.getBoundingClientRect().top > window.innerHeight) el.textContent = "0";
      co.observe(el);
    });
  }

  // background videos: play only when visible, never for reduced motion / data saver
  if (hasIO && !reduce && !save) {
    var vo = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) { if (v.dataset.userPaused) return;
          if (v.dataset.srcMobile && window.innerWidth < 700 && !v.dataset.swapped) { var so = v.querySelector("source"); if (so) { so.src = v.dataset.srcMobile; v.dataset.swapped = "1"; v.load(); } }
          v.preload = "auto"; var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        else if (!v.paused) v.pause();
      });
    }, { threshold: 0.2 });
    each(d.querySelectorAll("video[data-auto]"), function (v) { vo.observe(v); });
  }

  // swipe rails: dots show position and that there is more to the right
  each(d.querySelectorAll(".rail"), function (r) {
    var items = r.children, n = items.length; if (n < 2) return;
    var dots = d.createElement("div"); dots.className = "rail-dots"; dots.setAttribute("aria-hidden", "true");
    for (var i = 0; i < n; i++) dots.appendChild(d.createElement("i"));
    r.parentNode.insertBefore(dots, r.nextSibling);
    function upd() {
      var w = items[0].getBoundingClientRect().width || 1, gap = 12;
      var k = Math.round(r.scrollLeft / (w + gap)); if (r.scrollLeft + r.clientWidth >= r.scrollWidth - 4) k = n - 1;
      each(dots.children, function (x, j) { x.classList.toggle("on", j === k); });
    }
    r.addEventListener("scroll", upd, { passive: true }); upd();
  });

  // looping background videos get a visible pause / play control
  var VT = { ru: ["Пауза", "Воспроизвести"], ro: ["Pauză", "Redă"], en: ["Pause", "Play"] }[d.documentElement.lang] || ["Pause", "Play"];
  // the Lagmar hero loop shows only once it really plays; the photo underneath stays the fallback
  each(d.querySelectorAll("video.lg-hero-vid"), function (v) { v.addEventListener("playing", function () { v.classList.add("is-on"); }); });
  each(d.querySelectorAll("video.vhero-video, video.hero-media-vid, video.lg-hero-vid"), function (v) {
    var b = d.createElement("button"); b.type = "button"; b.className = "vid-toggle";
    function sync() { var playing = !v.paused; b.setAttribute("aria-label", playing ? VT[0] : VT[1]); b.setAttribute("aria-pressed", playing ? "false" : "true");
      b.innerHTML = '<svg class="ico" aria-hidden="true"><use href="#i-' + (playing ? "pause" : "play") + '"/></svg>'; }
    b.addEventListener("click", function () { if (v.paused) { v.dataset.userPaused = ""; var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); } else { v.dataset.userPaused = "1"; v.pause(); } });
    v.addEventListener("play", sync); v.addEventListener("pause", sync); sync();
    v.parentNode.appendChild(b);
  });

  // package comparison: apartment size switch
  each(d.querySelectorAll("[data-cmp-size]"), function (b) {
    b.addEventListener("click", function () {
      var c = b.closest(".cmp"); c.dataset.size = b.dataset.cmpSize;
      each(c.querySelectorAll("[data-cmp-size]"), function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
    });
  });

  each(d.querySelectorAll("[data-cmp-tier]"), function (b) {
    b.addEventListener("click", function () {
      var c = b.closest(".cmp"); c.dataset.tier = b.dataset.cmpTier;
      each(c.querySelectorAll("[data-cmp-tier]"), function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
    });
  });

  // plan widgets outside the Lagmar configurator
  each(d.querySelectorAll(".planx[data-standalone]"), function (f) {
    each(f.querySelectorAll("[data-set-tier]"), function (b) {
      b.addEventListener("click", function () {
        f.dataset.tier = b.dataset.setTier;
        each(f.querySelectorAll("[data-set-tier]"), function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      });
    });
  });

  // "one day in the apartment"
  var dw = d.getElementById("day-w");
  if (dw) {
    var DATA = JSON.parse(d.getElementById("day-data").textContent), L = DATA.labels, S = DATA.states;
    var cur = 0, timer = null, playBtn = d.getElementById("day-play");
    var $ = function (id) { return d.getElementById(id); };
    function apply(i) {
      cur = i; var s = S[i];
      dw.style.setProperty("--dark", s.dark);
      var on = 0;
      each(dw.querySelectorAll(".dl"), function (el) { var v = s.lights[el.dataset.z] || 0; el.style.opacity = v; if (v) on++; });
      var closed = false;
      each(dw.querySelectorAll(".db"), function (el) { var c = !!s.blinds[el.dataset.b]; el.classList.toggle("closed", c); closed = closed || c; });
      dw.classList.toggle("is-alert", !!s.alert); dw.classList.toggle("is-audio", !!s.audio); dw.classList.toggle("is-guard", !!s.guard);
      $("day-time").textContent = s.time; $("day-scene").textContent = s.title; $("day-text").textContent = s.text;
      $("day-temp").textContent = s.temp; $("day-eco").hidden = !s.eco;
      $("day-light").textContent = on ? L.zones.replace("{n}", on) : L.off;
      $("day-blinds").textContent = closed ? L.closed : L.open;
      $("day-clim").textContent = s.temp + " °C" + (s.eco ? " · " + L.eco : "");
      $("day-toast").hidden = !s.alert;
      each(dw.querySelectorAll("[data-day]"), function (b) { b.setAttribute("aria-selected", +b.dataset.day === i ? "true" : "false"); });
    }
    function setPlay(p) {
      if (p && !timer) timer = setInterval(function () { apply((cur + 1) % S.length); }, 3400);
      if (!p && timer) { clearInterval(timer); timer = null; }
      playBtn.setAttribute("aria-pressed", p ? "true" : "false");
      playBtn.querySelector("use").setAttribute("href", p ? "#i-pause" : "#i-play");
      playBtn.querySelector("span").textContent = p ? L.pause : L.play;
    }
    each(dw.querySelectorAll("[data-day]"), function (b) { b.addEventListener("click", function () { setPlay(false); apply(+b.dataset.day); }); });
    playBtn.addEventListener("click", function () { setPlay(!timer); });
    var side = dw.querySelector(".day-side");
    function lock() {
      side.style.minHeight = "";
      var mx = 0, keep = cur;
      for (var i = 0; i < S.length; i++) { apply(i); mx = Math.max(mx, side.offsetHeight); }
      side.style.minHeight = mx + "px"; apply(keep);
    }
    apply(0); lock();
    var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(lock, 200); });
    if (hasIO && !reduce) {
      var started = false;
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting && !started) { started = true; setPlay(true); }
          else if (!e.isIntersecting && timer) setPlay(false);
        });
      }, { threshold: 0.45 }).observe(dw);
    }
  }
})();
"""


def shell(lang, key, title, body, extra_jsonld=None):
    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_html(lang, key, title, META_DESC[key][lang], extra_jsonld)}
</head>
<body class="theme-lagmar">
{sprite_html()}
{nav_html(lang, key)}
{body}
{dealer_band_html(lang, key)}
{footer_html(lang)}
<script>{SITE_JS}</script>
</body>
</html>'''


# ---------------------------------------------------------------------------
# v3 components

def day_widget_html(lang, cls=""):
    dy = DAY[lang]
    sc = SCENARIOS[lang]["items"]
    w, h = PLAN_SIZE["2"]
    lights = "".join(f'<span class="dl" data-z="{z}" style="left:{x}%;top:{y}%;--s:{s}%"></span>'
                     for z, (x, y, s) in DAY_LIGHTS.items())
    blinds = "".join(
        (f'<span class="db db-h" data-b="{b}" style="left:{x}%;top:{y}%;width:{ln}%"></span>' if o == "h"
         else f'<span class="db db-v" data-b="{b}" style="left:{x}%;top:{y}%;height:{ln}%"></span>')
        for b, (o, x, y, ln) in DAY_BLINDS.items())
    states = []
    for st in DAY_STATES:
        t, title, text, _dev, _tier = sc[st["sc"]]
        states.append(dict(st, time=t, title=title, text=text))
    data = {"labels": {k: dy[k] for k in ("zones", "off", "open", "closed", "eco", "play", "pause")}, "states": states}
    tabs = "".join(
        f'<button type="button" role="tab" data-day="{i}" aria-selected="{"true" if i == 0 else "false"}">'
        f'<span class="t">{s["time"]}</span><span class="n">{s["title"]}</span></button>'
        for i, s in enumerate(states))
    s0 = states[0]
    return f'''<div class="day rv {cls}" id="day-w" style="--dark:{s0["dark"]}">
  <div class="day-stage">
    <div class="day-canvas">
      <img src="../assets/lagmar/plans/plan-2.png" width="{w}" height="{h}" alt="{esc(dy["plan_alt"])}" loading="lazy">
      <span class="day-night"></span>{lights}{blinds}
      <span class="day-pin day-pin-alert" style="left:90%;top:55%">{ico("W")}</span>
      <span class="day-pin day-pin-audio" style="left:24%;top:88%">{ico("A")}</span>
      <span class="day-guard">{ico("shield")}{dy["guard"]}</span>
    </div>
  </div>
  <div class="day-side">
    <div class="day-panel" aria-live="polite">
      <div class="dp-row"><span class="dp-time" id="day-time">{s0["time"]}</span><span class="dp-temp"><b id="day-temp">{s0["temp"]}</b>°C <em id="day-eco" hidden>{dy["eco"]}</em></span></div>
      <div class="dp-scene" id="day-scene">{s0["title"]}</div>
      <div class="dp-dots"><i></i><i></i><i></i><i></i></div>
    </div>
    <p class="day-text" id="day-text">{s0["text"]}</p>
    <ul class="day-chips">
      <li>{ico("L")}<span>{dy["light"]}</span><b id="day-light"></b></li>
      <li>{ico("C")}<span>{dy["blinds"]}</span><b id="day-blinds"></b></li>
      <li>{ico("T")}<span>{dy["climate"]}</span><b id="day-clim"></b></li>
    </ul>
    <div class="day-toast" id="day-toast" hidden>{ico("W")}<div><b>{dy["alert"]}</b><span>{dy["alert_sub"]}</span></div></div>
  </div>
  <div class="day-scrub">
    <div class="day-tabs" role="tablist">{tabs}</div>
    <button type="button" class="day-play" id="day-play" aria-pressed="false">{ico("play")}<span>{dy["play"]}</span></button>
  </div>
  <script id="day-data" type="application/json">{_json_for_script(data, lang)}</script>
</div>'''


def day_section_html(lang, alt=False, more=True):
    dy = DAY[lang]
    more_btn = (f'<a class="btn btn-ghost" href="scenarios.html">{dy["more"]} {ico("arrow")}</a>' if more else "")
    return f'''<section class="block{" alt" if alt else ""} day-sec" id="day">
  <div class="wrap">
    <div class="section-head rv">
      <div><span class="eyebrow">{dy["eyebrow"]}</span><h2 class="h2">{dy["title"]}</h2><p class="sub">{dy["sub"]}</p></div>
      {more_btn}
    </div>
    {day_widget_html(lang)}
  </div>
</section>'''


def compare_html(lang, pk, cta=True):
    c = CMP[lang]
    lab = pk["labels"]
    tiers = ["basic", "comfort", "premium"]

    def cell(v):
        if v == "Y":
            return f'<span class="yes">{ico("check")}<span class="sr">{c["yes"]}</span></span>'
        if v == "N":
            return f'<span class="no" aria-label="{c["no"]}">—</span>'
        return v
    head = "".join(
        f'<th scope="col" class="tc-{t}">{esc(lab[t])}' + (f'<em>{esc(lab["recommended"])}</em>' if t == "comfort" else "") + "</th>"
        for t in tiers)
    rows = "".join(
        f'<tr><th scope="row">{r[0]}</th>' + "".join(f'<td class="tc-{t}">{cell(v)}</td>' for t, v in zip(tiers, r[1:])) + "</tr>"
        for r in c["rows"] if tuple(r[1:]) != ("Y", "Y", "Y"))
    common = [r[0] for r in c["rows"] if tuple(r[1:]) == ("Y", "Y", "Y")]
    common_html = (f'<p class="cmp-all">{ico("check")}<span><b>{c["all"]}:</b> ' + " · ".join(common) + "</span></p>") if common else ""
    price_cells = "".join(
        f'<td class="tc-{t} cmp-price">' + "".join(
            f'<span class="pz pz-{n}">{c["price_from"].replace("{p}", fmt_eur(PRICES[n][t], lang))}</span>' for n in ["2", "3", "4"])
        + "</td>" for t in tiers)
    sizes = "".join(
        f'<button type="button" data-cmp-size="{n}" aria-pressed="{"true" if n == "2" else "false"}">{c["sizes"][n]}</button>'
        for n in ["2", "3", "4"])
    cta_html = (f'<a class="btn btn-primary" href="lagmar.html#step1">{c["cta"]}</a>' if cta else "")
    mtiers = "".join(
        f'<button type="button" data-cmp-tier="{t}" aria-pressed="{"true" if t == "comfort" else "false"}">{esc(lab[t])}</button>'
        for t in tiers)
    return f'''<div class="cmp" data-size="2" data-tier="comfort">
  <div class="cmp-sizes" role="group" aria-label="{c["size_label"]}"><span>{c["size_label"]}:</span>{sizes}</div>
  <div class="cmp-tiers" role="group">{mtiers}</div>
  <table class="cmp-table">
    <thead><tr><th scope="col" class="cmp-feat">{c["feature"]}</th>{head}</tr></thead>
    <tbody>{rows}</tbody>
    <tfoot><tr><th scope="row">{c["price"]}</th>{price_cells}</tr></tfoot>
  </table>
  {common_html}
  <div class="cmp-foot"><p class="cmp-note">{c["price_note"]}</p>{cta_html}</div>
</div>'''


def compare_section_html(lang, pk, alt=False, sid="compare"):
    c = CMP[lang]
    return f'''<section class="block{" alt" if alt else ""}" id="{sid}">
  <div class="wrap">
    <div class="rv"><span class="eyebrow">{c["eyebrow"]}</span><h2 class="h2">{c["title"]}</h2><p class="sub">{c["sub"]}</p></div>
    {compare_html(lang, pk)}
  </div>
</section>'''


def finishes_html(lang):
    g = GAL[lang]
    sw = "".join(f'<li><span class="sw" style="background-image:url(../assets/grenton/mono-{k}.webp)"></span>{n}</li>'
                 for k, n in g["finishes"])
    return f'<div class="finishes"><span>{g["finish_label"]}</span><ul>{sw}</ul></div>'


def gallery_html(lang, alt=True):
    g = GAL[lang]
    it = g["items"]
    h3 = HOME_V3[lang]

    def card(key, media, cls=""):
        t, d = it[key]
        return f'<article class="gal-item rv {cls}"><div class="gal-media">{media}</div><div class="gal-body"><h3>{t}</h3><p>{d}</p></div></article>'
    items = (
        card("panel", gvideo("panel", "panel-poster", "Grenton Smart Panel"), "gal-wide")
        + card("multi", gvideo("multisensor", "multisensor-poster", "Grenton Multisensor"), "gal-dark")
        + card("monolith", gimg("monolith-wall", "Grenton Monolith", sizes="(max-width: 700px) 82vw, 30vw") + finishes_html(lang))
        + card("touch", gimg("touch-wall", "Grenton Touch Panel", sizes="(max-width: 700px) 82vw, 30vw"))
        + card("clu", gimg("clu", "Grenton CLU", sizes="(max-width: 700px) 82vw, 30vw"), "gal-paper")
    )
    return f'''<section class="block{" alt" if alt else ""}" id="products">
  <div class="wrap">
    <div class="section-head rv">
      <div><span class="eyebrow">{g["eyebrow"]}</span><h2 class="h2">{g["title"]}</h2><p class="sub">{g["sub"]}</p></div>
      <a class="btn btn-ghost" href="how.html">{h3["gallery_more"]} {ico("arrow")}</a>
    </div>
    <div class="gal rail">{items}</div>
    <p class="credit">{g["credit"]}</p>
  </div>
</section>'''


def app_html(lang, alt=False, cls=""):
    a = APP[lang]
    lis = "".join(f"<li>{ico('check')}<span>{b}</span></li>" for b in a["bullets"])
    return f'''<section class="block{" alt" if alt else ""} app-sec {cls}" id="app">
  <div class="wrap app-grid">
    <div class="phone-wrap rv">
      <div class="phone"><div class="phone-notch"></div>{gimg("app-bedroom", "myGrenton", sizes="(max-width: 700px) 60vw, 18rem")}</div>
      <div class="float-card fc-app">{ico("W", "ico fc-ico")}<div><b>{DAY[lang]["alert"]}</b><span>{DAY[lang]["alert_sub"]}</span></div></div>
    </div>
    <div class="rv">
      <span class="eyebrow">{a["eyebrow"]}</span>
      <h2 class="h2">{a["title"]}</h2>
      <p class="sub">{a["text"]}</p>
      <ul class="checks">{lis}</ul>
    </div>
  </div>
</section>'''


# ---------------------------------------------------------------------------
# pages

def features_page_html(lang, packages_all):
    f = FEATURES[lang]
    rows = []
    for i, g in enumerate(f["groups"]):
        items = "".join(f'<li><span class="feat-text">{t}</span>{tier_chip(lang, tier)}</li>' for t, tier in g["items"])
        ph = FEATURE_PHOTO[g["id"]]
        rows.append(f'''<article class="frow rv" id="{g["id"]}">
      <div class="frow-media">{gimg(ph, palt(lang, ph))}<span class="frow-ico mk mk-{ICON_FOR_GROUP[g["id"]]}">{ico(ICON_FOR_GROUP[g["id"]])}</span></div>
      <div class="frow-text">
        <h3 class="feat-title">{g["title"]}</h3>
        <p class="feat-benefit">{g["benefit"]}</p>
        <ul class="feat-list">{items}</ul>
      </div>
    </article>''')
    hero_media = gvideo("hero", "hero-poster", HOME_V3[lang]["video_label"], "hero-media-vid")
    body = simple_hero(f["eyebrow"], f["h1"], f["lead"], hero_media) + f'''
<section class="block alt">
  <div class="wrap frows">
    {"".join(rows)}
  </div>
</section>
{compare_section_html(lang, packages_all[lang])}
{cta_lagmar_html(lang)}'''
    return shell(lang, "features", f["title"], body)


def scenarios_page_html(lang):
    sc = SCENARIOS[lang]
    items = []
    for i, (t, title, text, dev, tier) in enumerate(sc["items"]):
        ph = SCENE_PHOTO[i] if i < len(SCENE_PHOTO) else "salon"
        items.append(f'''<li class="scene rv">
      <div class="scene-time">{t}</div>
      <div class="scene-card">
        <div class="scene-body">
          <div class="scene-top"><h3 class="scene-title">{title}</h3>{tier_chip(lang, tier)}</div>
          <p>{text}</p>
          <div class="scene-devices">{mk_icons(dev, lang)}</div>
        </div>
        <div class="scene-photo">{gimg(ph, palt(lang, ph), sizes="(max-width: 600px) 90vw, 16rem")}</div>
      </div>
    </li>''')
    hm = PAGE_HERO_MEDIA["scenarios"]
    body = simple_hero(sc["eyebrow"], sc["h1"], sc["lead"], gimg(hm, palt(lang, hm), sizes="(max-width: 860px) 92vw, 45vw", eager=True)) + f'''
{day_section_html(lang, alt=True, more=False)}
<section class="block">
  <div class="wrap">
    <ol class="timeline">{"".join(items)}</ol>
    <p class="cfg-note scene-note">{sc["note"]}</p>
  </div>
</section>
{cta_lagmar_html(lang)}'''
    return shell(lang, "scenarios", sc["title"], body)


def how_page_html(lang):
    h = HOW[lang]
    visuals = [gimg("clu", "Grenton CLU", sizes="16rem"), None,
               gvideo("multisensor", "multisensor-poster", "Grenton Multisensor"),
               gvideo("panel", "panel-poster", "Grenton Smart Panel")]
    layers = []
    for i, (img, icons, title, text) in enumerate(h["layers"]):
        vis = visuals[i] if i < len(visuals) and visuals[i] else f'<div class="layer-icons">{mk_icons(icons, lang)}</div>'
        layers.append(f'<article class="layer rv" style="--d:{i}"><div class="layer-visual">{vis}</div><h3>{title}</h3><p>{text}</p></article>')
    steps = "".join(f'<li class="step rv" style="--d:{i}"><span class="step-n">{i}</span><h3>{t}</h3><p>{d}</p></li>'
                    for i, (t, d) in enumerate(h["steps"], 1))
    why_ic = ["wifi", "shield", "tools", "check"]
    why = "".join(f'<div class="why rv" style="--d:{i}">{ico(why_ic[i % 4], "ico why-ico")}<h3>{t}</h3><p>{d}</p></div>'
                  for i, (t, d) in enumerate(h["why"]))
    g = GAL[lang]
    t_mono, d_mono = g["items"]["monolith"]
    hm = PAGE_HERO_MEDIA["how"]
    body = simple_hero(h["eyebrow"], h["h1"], h["lead"], gimg(hm, palt(lang, hm), sizes="(max-width: 860px) 92vw, 45vw", eager=True)) + f'''
<section class="block alt" id="interfaces">
  <div class="wrap">
    <h2 class="h2 rv">{h["layers_title"]}</h2>
    <div class="layers">{"".join(layers)}</div>
  </div>
</section>
<section class="mono-band" aria-label="Monolith">
  {gimg("monolith-hero", "Grenton Monolith", "mono-bg", sizes="100vw")}
  <div class="wrap mono-inner rv">
    <span class="eyebrow">{g["eyebrow"]}</span>
    <h2 class="h2">{t_mono}</h2>
    <p class="sub">{d_mono}</p>
    {finishes_html(lang)}
  </div>
</section>
{app_html(lang)}
<section class="block alt">
  <div class="wrap">
    <h2 class="h2 rv">{h["process_title"]}</h2>
    <ol class="steps rail">{steps}</ol>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2 class="h2 rv">{h["why_title"]}</h2>
    <div class="why-grid">{why}</div>
  </div>
</section>
{cta_lagmar_html(lang)}'''
    return shell(lang, "how", h["title"], body)


def home_page_html(lang, packages_all):
    h = HOME_V2[lang]
    h3 = HOME_V3[lang]
    pk = packages_all[lang]
    hl = HOME_LAGMAR[lang]
    v = LAGMAR_VIS[lang]
    trust_ic = ["shield", "wifi", "tools"]
    trust = "".join(f'<li>{ico(trust_ic[i])}{t}</li>' for i, t in enumerate(h["trust"]))

    def floatcard(cls, dd):
        icon, title, sub = dd
        return (f'<div class="float-card {cls}"><span class="mk mk-{icon}">{ico(icon)}</span>'
                f'<div><b>{title}</b><span>{sub}</span></div></div>')

    groups = {g["id"]: g for g in FEATURES[lang]["groups"]}
    outcomes = "".join(
        f'<a class="outcome rv" style="--d:{i}" href="features.html#{gid}">'
        f'<div class="outcome-media">{gimg(FEATURE_PHOTO[gid], palt(lang, FEATURE_PHOTO[gid]), sizes="(max-width: 700px) 80vw, 24vw")}'
        f'<span class="mk mk-{ICON_FOR_GROUP[gid]} outcome-icon">{ico(ICON_FOR_GROUP[gid])}</span></div>'
        f'<div class="outcome-body"><h3>{groups[gid]["title"]}</h3><p>{groups[gid]["benefit"]}</p>'
        f'<span class="more">{h["out_more"]} {ico("arrow")}</span></div></a>'
        for i, gid in enumerate(["light", "climate", "safety", "control"]))
    steps = "".join(f'<li class="step rv" style="--d:{i}"><span class="step-n">{i}</span><h3>{t}</h3><p>{d}</p></li>'
                    for i, (t, d) in enumerate(HOW[lang]["steps"], 1))
    sl_href = SMARTLIGHT_URL[lang] + SMARTLIGHT_UTM
    sl_brands = "".join(f"<li>{b}</li>" for b in SL_BRANDS)
    sep = "," if lang == "en" else " "

    def stat(a, b):
        digits = a.replace(" ", "").replace(",", "").replace(" ", "")
        cnt = f' data-count="{digits}" data-sep="{sep}"' if digits.isdigit() else ""
        return f'<li><b{cnt}>{esc(a)}</b><span>{esc(b)}</span></li>'
    stats = "".join(stat(a, b) for a, b in v["stats"])

    lg = HOME_LG[lang]
    body = f'''<section class="home-lg">
  <img class="home-lg-bg" src="../assets/lagmar/aerial-800.jpg" srcset="../assets/lagmar/aerial-800.jpg 800w, ../assets/lagmar/aerial.jpg 1600w" sizes="100vw" alt="" fetchpriority="high">
  <div class="wrap home-lg-inner">
    <div class="lg-logos"><img src="../assets/lagmar/logo-lagmar.png" alt="Lagmar Smart Home" width="160" height="48"><span class="x">×</span><span class="gr">SmartSpace <small>by Grenton</small></span></div>
    <h1>{lg["h1"]}</h1>
    <p class="lead">{lg["lead"]}</p>
    <div class="cta-row cta-left">
      <a class="btn btn-primary" href="lagmar.html#step1">{lg["cta"]}</a>
      <a class="btn btn-light" href="#film">{lg["film"]} {ico("play")}</a>
    </div>
  </div>
</section>

<section class="vhero" id="film">
  {gvideo("hero", "hero-poster", h3["video_label"], "vhero-video")}
  <div class="wrap vhero-inner">
    <div class="vhero-copy">
      <span class="eyebrow">{h["eyebrow"]}</span>
      <h2 class="vhero-title">{h["h1"]}</h2>
      <p class="lead">{h["lead"]}</p>
      <div class="cta-row cta-left">
        <a class="btn btn-primary" href="features.html">{h["cta2"]}</a>
        <a class="btn btn-light" href="#day">{DAY[lang]["play"]} {ico("play")}</a>
      </div>
      <ul class="trust">{trust}</ul>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <div class="rv"><span class="eyebrow">{h["out_eyebrow"]}</span><h2 class="h2">{h3["out_title"]}</h2></div>
    <div class="outcomes rail">{outcomes}</div>
  </div>
</section>

{day_section_html(lang)}


<section class="block lagmar-block" id="lagmar">
  <div class="wrap split">
    <div class="rv">
      <span class="eyebrow">{h3["lagmar_ref"]} · {hl["eyebrow"]}</span>
      <h2 class="h2">{hl["h2"]}</h2>
      <p class="sub">{hl["p"]}</p>
      <ul class="mini-stats">{stats}</ul>
      <a class="btn btn-primary" href="lagmar.html">{hl["cta"]}</a>
    </div>
    <a href="lagmar.html" class="lagmar-teaser rv"><img class="rounded" src="../assets/lagmar/aerial.jpg" srcset="../assets/lagmar/aerial-800.jpg 800w, ../assets/lagmar/aerial.jpg 1600w" sizes="(max-width: 860px) 92vw, 45vw" alt="Lagmar Smart Home" width="1600" height="828" loading="lazy"><img class="lagmar-teaser-logo" src="../assets/lagmar/logo-lagmar.png" alt="" width="140" height="42"></a>
  </div>
</section>

{gallery_html(lang)}

{app_html(lang, cls="app-home")}

<section class="sl-banner" aria-label="SmartLight">
  <div class="wrap sl-inner">
    <div class="sl-copy rv">
      <span class="sl-wordmark">SMART<b>LIGHT</b></span>
      <span class="sl-eyebrow">{h["sl_eyebrow"]}</span>
      <h2>{h["sl_title"]}</h2>
      <p>{h["sl_text"]}</p>
      <ul class="sl-brands">{sl_brands}</ul>
      <a class="btn sl-btn" href="{sl_href}" rel="noopener">{h["sl_cta"]} {ico("ext")}</a>
    </div>
    <div class="sl-photo rv">
      <img src="../assets/smartlight/banner-960.jpg" srcset="../assets/smartlight/banner-960.jpg 960w, ../assets/smartlight/banner.jpg 1440w" sizes="(max-width: 860px) 100vw, 40vw" width="960" height="1200" alt="Vibia Array — SmartLight" loading="lazy">
      <img class="sl-product" src="../assets/smartlight/taccia.jpg" width="600" height="840" alt="Flos Taccia — SmartLight" loading="lazy">
    </div>
  </div>
</section>'''
    return shell(lang, "home", h["title"], body)



CONTACT_JS = r"""
(function () {
  var d = document, each = function (l, f) { Array.prototype.forEach.call(l, f); };
  var C = JSON.parse(d.getElementById("contact-data").textContent);

  // live open / closed status in Chisinau time
  function nowMD() {
    try {
      var parts = new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Chisinau", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false }).formatToParts(new Date());
      var o = {}; parts.forEach(function (p) { o[p.type] = p.value; });
      return { d: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].indexOf(o.weekday), m: (+o.hour % 24) * 60 + (+o.minute) };
    } catch (e) { var n = new Date(); return { d: (n.getDay() + 6) % 7, m: n.getHours() * 60 + n.getMinutes() }; }
  }
  function mins(t) { var p = t.split(":"); return +p[0] * 60 + +p[1]; }
  var now = nowMD(), H = C.hours, txt = "", open = false;
  if (now.d >= 0) {
    var h = H[now.d];
    if (h[0] && now.m >= mins(h[0]) && now.m < mins(h[1])) { open = true; txt = C.open_now.replace("{t}", h[1]); }
    else {
      for (var k = 0; k < 8; k++) {
        var day = (now.d + k) % 7, hh = H[day];
        if (hh[0] && (k > 0 || now.m < mins(hh[0]))) {
          txt = C.closed_now.replace("{d}", k === 0 ? C.today : k === 1 ? C.tomorrow : C.days_full[day]).replace("{t}", hh[0]); break;
        }
      }
    }
    each(d.querySelectorAll(".open-status"), function (el) { el.classList.toggle("is-open", open); el.querySelector("span").textContent = txt; el.hidden = false; });
    each(d.querySelectorAll('.hours [data-dow="' + now.d + '"]'), function (li) { li.classList.add("today"); });
  }

  // request builder -> WhatsApp / e-mail
  var st = { topic: null, stage: null };
  var nameEl = d.getElementById("b-name"), textEl = d.getElementById("b-text"), out = d.getElementById("b-msg");
  var wa = d.getElementById("b-wa"), mail = d.getElementById("b-mail"), cfg = d.getElementById("b-cfg");
  function compose() {
    var lines = [C.msg_hello];
    if (st.topic) lines.push(C.msg_topic + ": " + C.topics[st.topic]);
    if (st.stage) lines.push(C.msg_stage + ": " + C.stages[st.stage]);
    var t = textEl.value.trim(); if (t) lines.push(t);
    var n = nameEl.value.trim(); if (n) lines.push(C.msg_name + ": " + n);
    var msg = lines.join("\n");
    out.textContent = msg;
    wa.href = "https://wa.me/" + C.wa + "?text=" + encodeURIComponent(msg);
    mail.href = "mailto:" + C.email + "?subject=" + encodeURIComponent(C.mail_subject) + "&body=" + encodeURIComponent(msg);
    cfg.hidden = st.topic !== "lagmar";
  }
  function pick(attr, key) {
    each(d.querySelectorAll("[" + attr + "]"), function (b) {
      b.addEventListener("click", function () {
        var v = b.getAttribute(attr); st[key] = st[key] === v ? null : v;
        each(d.querySelectorAll("[" + attr + "]"), function (x) { x.setAttribute("aria-pressed", x.getAttribute(attr) === st[key] ? "true" : "false"); });
        compose();
      });
    });
  }
  pick("data-topic", "topic"); pick("data-stage", "stage");
  nameEl.addEventListener("input", compose); textEl.addEventListener("input", compose);
  compose();

  // interactive map only on demand (no third-party request before the click)
  var live = d.getElementById("map-live");
  if (live) live.addEventListener("click", function () {
    var card = d.getElementById("mapcard"), f = d.createElement("iframe");
    f.src = C.map_embed; f.title = C.m_live; f.loading = "lazy"; f.referrerPolicy = "no-referrer-when-downgrade"; f.allowFullscreen = true;
    card.appendChild(f); card.classList.add("is-live");
  });
})();
"""


def contact_page_html(lang):
    c = CONTACT_V3[lang]
    lat, lon = GEO
    wa = f"https://wa.me/{WA_NUMBER}"
    gdir = f"https://www.google.com/maps/dir/?api=1&destination={lat},{lon}"
    waze = f"https://waze.com/ul?ll={lat},{lon}&navigate=yes"
    hours = "".join(
        f'<li data-dow="{i}"><span>{c["days"][i]}</span><b>{(o + "–" + cl) if o else c["closed"]}</b></li>'
        for i, (o, cl) in enumerate(HOURS))
    status = '<span class="open-status" hidden><i></i><span></span></span>'
    actions = (f'<div class="cta-row cta-left quick">'
               f'<a class="btn btn-primary" href="tel:{PHONE_TEL}">{ico("phone")}{c["call"]} · {PHONE_DISPLAY}</a>'
               f'<a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{ico("chat")}{c["wa"]}</a>'
               f'<a class="btn btn-ghost" href="mailto:{EMAIL}">{ico("mail")}{c["mail"]}</a></div>')
    media = (gimg(PAGE_HERO_MEDIA["contact"], c["showroom"], sizes="(max-width: 860px) 92vw, 40vw", eager=True)
             + f'<div class="float-card hero-fc"><span class="mk mk-I">{ico("pin")}</span><div><b>{c["showroom"]}</b><span>Strada Pajurii 11</span></div></div>')
    topics = "".join(
        f'<button type="button" class="topic" data-topic="{k}" aria-pressed="false"><span class="mk mk-{icon}">{ico(icon)}</span>'
        f'<span><b>{t}</b><small>{s}</small></span></button>' for k, icon, t, s in c["topics"])
    stages = "".join(f'<button type="button" class="chip" data-stage="{k}" aria-pressed="false">{t}</button>' for k, t in c["stages"])
    social = "".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL)
    steps = "".join(f'<li class="step rv" style="--d:{i}"><span class="step-n">{i}</span><h3>{t}</h3><p>{dd}</p></li>'
                    for i, (t, dd) in enumerate(HOW[lang]["steps"][:3], 1))
    data = {k: c[k] for k in ("open_now", "closed_now", "today", "tomorrow", "days_full", "msg_hello", "msg_topic",
                              "msg_stage", "msg_name", "mail_subject", "m_live")}
    data.update(hours=[list(h) for h in HOURS], topics={k: t for k, _i, t, _s in c["topics"]},
                stages={k: t for k, t in c["stages"]}, wa=WA_NUMBER, email=EMAIL,
                map_embed=f"https://maps.google.com/maps?q={lat},{lon}&z=16&output=embed")
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    ld = {"@context": "https://schema.org", "@type": "LocalBusiness", "name": "SmartSpace", "telephone": PHONE_TEL, "email": EMAIL,
          "address": {"@type": "PostalAddress", "streetAddress": "Strada Pajurii 11", "postalCode": "MD-2059",
                      "addressLocality": "Chișinău", "addressCountry": "MD"},
          "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lon},
          "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": day_names[i], "opens": o, "closes": cl}
                                        for i, (o, cl) in enumerate(HOURS) if o],
          "sameAs": [u for _n, u in SOCIAL]}

    body = simple_hero(c["eyebrow"], c["h1"], c["lead"], media, extra=status + actions) + f'''
<section class="block alt" id="write">
  <div class="wrap">
    <div class="rv"><span class="eyebrow">{c["b_eyebrow"]}</span><h2 class="h2">{c["b_title"]}</h2><p class="sub">{c["b_sub"]}</p></div>
    <div class="builder">
      <div class="bq">
        <h3>{c["q1"]}</h3>
        <div class="topics">{topics}</div>
        <h3>{c["q2"]}</h3>
        <div class="chips">{stages}</div>
        <p class="hint">{c["stage_hint"]}</p>
        <h3>{c["q3"]}</h3>
        <input id="b-name" type="text" maxlength="80" autocomplete="name" placeholder="{esc(c["name_ph"])}" aria-label="{esc(c["name_ph"])}">
        <textarea id="b-text" rows="3" maxlength="600" placeholder="{esc(c["text_ph"])}" aria-label="{esc(c["q3"])}"></textarea>
      </div>
      <div class="bprev">
        <div class="phone-msg">
          <div class="pm-head"><span class="pm-ava">S</span><div><b>SmartSpace</b><small>{PHONE_DISPLAY}</small></div></div>
          <div class="pm-body"><span class="pm-label">{c["preview"]}</span><div class="bubble" id="b-msg"></div></div>
        </div>
        <div class="bactions">
          <a class="btn btn-wa" id="b-wa" href="{wa}" target="_blank" rel="noopener">{ico("chat")}{c["send_wa"]}</a>
          <a class="btn btn-ghost" id="b-mail" href="mailto:{EMAIL}">{ico("mail")}{c["send_mail"]}</a>
          <a class="btn btn-ghost" id="b-cfg" href="lagmar.html#step1" hidden>{c["to_cfg"]} {ico("arrow")}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="block" id="map">
  <div class="wrap map-grid">
    <div class="mapcard" id="mapcard">
      <img class="map-img map-l" src="../assets/img/map-light.webp" width="1110" height="640" alt="{esc(c["m_title"])}" loading="lazy">
      <img class="map-img map-d" src="../assets/img/map-dark.webp" width="1110" height="640" alt="" loading="lazy">
      <span class="map-pin" style="left:50.4%;top:50%"><span class="pin-dot">{ico("pin")}</span></span>
      <div class="map-label"><b>{c["showroom"]}</b><span>Strada Pajurii 11</span></div>
      <button type="button" class="btn btn-light map-live" id="map-live">{ico("pin")}{c["m_live"]}</button>
      <span class="map-attr">© OpenStreetMap</span>
    </div>
    <aside class="map-info rv">
      <span class="eyebrow">{c["m_eyebrow"]}</span>
      <h2 class="h2">{c["m_title"]}</h2>
      <p class="sub">{c["m_sub"]}</p>
      <div class="route"><a class="btn btn-primary" href="{gdir}" target="_blank" rel="noopener">{ico("arrow")}{c["m_route"]}</a><a class="btn btn-ghost" href="{waze}" target="_blank" rel="noopener">{c["m_waze"]}</a></div>
      <div class="info-cols">
        <div><h3>{c["hours"]}</h3>{status}<ul class="hours">{hours}</ul></div>
        <div><h3>{c["write"]}</h3>
          <ul class="links">
            <li>{ico("phone")}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li>{ico("chat")}<a href="{wa}" target="_blank" rel="noopener">WhatsApp</a></li>
            <li>{ico("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
          <h3>{c["social"]}</h3><p class="social">{social}</p>
        </div>
      </div>
      <p class="m-note">{c["m_note"]}</p>
    </aside>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <div class="rv"><span class="eyebrow">{c["after_eyebrow"]}</span><h2 class="h2">{c["after_title"]}</h2></div>
    <ol class="steps steps-3 rail">{steps}</ol>
  </div>
</section>
<script id="contact-data" type="application/json">{_json_for_script(data, lang)}</script>
<script>{CONTACT_JS}</script>'''
    return shell(lang, "contact", c["title"], body, [ld])


def legacy_redirect_html(target):
    return f'''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
<title>→ {target}</title>
</head>
<body><p><a href="{target}">{target}</a></p></body>
</html>'''


# --- typography: glue short words, numbers+units, dashes, phone numbers with no-break spaces ---
NBSP = " "
_SHORT = {  # longest first, so the alternation never stops at a prefix
    "ru": r"для|без|при|как|что|или|над|под|про|обо|во|со|ко|об|на|по|до|за|от|из|не|ни|но|в|и|с|к|о|у|а|я",
    "ro": r"pentru|prin|spre|sau|ale|din|și|în|la|de|pe|cu|că|un|al|nu|să|se|ce|îi|le|ne|vă|o|a|e",
    "en": r"with|your|from|into|and|the|for|our|an|of|in|to|on|at|by|or|no|is|as|it|my|a|I",
}
_SPLIT = re.compile(r"(<script\b.*?</script>|<style\b.*?</style>|<[^>]+>)", re.S | re.I)


def _typo_text(t, lang):
    t = re.sub(r"(?<![\w-])(" + _SHORT[lang] + r") +(?=\S)", lambda m: m.group(1) + NBSP, t, flags=re.I)
    t = re.sub(r" +([—–])", NBSP + r"\1", t)
    t = re.sub(r" +(·)(?= )", NBSP + r"\1", t)
    t = re.sub(r" (же|ли|бы)(?!\w)", NBSP + r"\1", t)
    t = re.sub(r"№ (?=\d)", "№" + NBSP, t)
    t = re.sub(r"(\d) (\d{3})(?!\d)", r"\1" + NBSP + r"\2", t)
    t = re.sub(r"(\d) +(?=[^\s\d])", r"\1" + NBSP, t)
    t = re.sub(r"(\+373)[  ](\d{2})[  ](\d{3})[  ](\d{3})", lambda m: NBSP.join(m.groups()), t)
    return t


_HEAD = re.compile(r"(<h([1-3])\b[^>]*>)(.*?)(</h\2>)", re.S)
_TAG = re.compile(r"(<[^>]+>)")


def _bind_last_words(m):
    """h1-h3 never end on one lonely word: the last two words share a no-break space."""
    open_t, lvl, inner, close_t = m.groups()
    limit = {"1": 16, "2": 18, "3": 16}[lvl]  # longer glued tails split words in narrow cards
    parts = _TAG.split(inner)
    for i in range(len(parts) - 1, -1, -1):
        p = parts[i]
        if p.startswith("<") or not p.strip():
            continue
        body = p.rstrip()
        k = body.rfind(" ")
        prev = body.rfind(" ", 0, k)  # the glued unit must stay short, or the browser splits a word instead
        if k > 0 and len(body) - k - 1 <= 12 and len(body) - prev - 1 <= limit:
            parts[i] = p[:k] + NBSP + p[k + 1:]
        break
    return open_t + "".join(parts) + close_t


def typo(html, lang):
    parts = _SPLIT.split(html)
    for i, part in enumerate(parts):
        if i % 2 == 1:
            continue
        parts[i] = _typo_text(part, lang)
    return _HEAD.sub(_bind_last_words, "".join(parts))


def typo_data(obj, lang):
    if isinstance(obj, str):
        return "".join(p if p.startswith("<") else _typo_text(p, lang) for p in _TAG.split(obj))
    if isinstance(obj, list):
        return [typo_data(x, lang) for x in obj]
    if isinstance(obj, dict):
        return {k: typo_data(v, lang) for k, v in obj.items()}
    return obj


def root_redirect():
    alternates = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE_URL}/{l}/index.html">' for l in LANGS)
    return f'''<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=ro/index.html">
<link rel="canonical" href="{BASE_URL}/ro/index.html">
{alternates}<link rel="alternate" hreflang="x-default" href="{BASE_URL}/ro/index.html">
<title>Grenton — SmartSpace Moldova</title>
</head>
<body>
<p>Redirecting… / <a href="ro/index.html">RO</a> · <a href="ru/index.html">RU</a> · <a href="en/index.html">EN</a></p>
</body>
</html>'''


def not_found_html():
    return f'''<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>404 — SmartSpace · Grenton</title>
<link rel="stylesheet" href="{BASE_URL}/assets/css/style.css">
</head>
<body>
<section class="hero"><div class="wrap">
  <h1>404</h1>
  <p class="lead">Pagina nu există · Страница не найдена · Page not found</p>
  <div class="cta-row">
    <a class="btn btn-primary" href="{BASE_URL}/ro/lagmar.html">RO</a>
    <a class="btn btn-primary" href="{BASE_URL}/ru/lagmar.html">RU</a>
    <a class="btn btn-primary" href="{BASE_URL}/en/lagmar.html">EN</a>
    <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
  </div>
</div></section>
</body>
</html>'''


def sitemap_xml():
    urls = []
    for key in PAGE_ORDER:
        for lang in LANGS:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{BASE_URL}/{l}/{PAGE_FILE[key]}"/>' for l in LANGS)
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}/ro/{PAGE_FILE[key]}"/>'
            urls.append(f"<url><loc>{BASE_URL}/{lang}/{PAGE_FILE[key]}</loc>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">' + "".join(urls) + "</urlset>\n")


def robots_txt():
    return f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n"


_EYEBROW = re.compile(r'<span class="eyebrow">.*?</span>\s*', re.S)




def finalize_html(html, lang):
    """Site-wide markup rules applied to every generated page."""
    html = _EYEBROW.sub("", html)
    if 'id="main"' not in html and "</header>" in html and "<footer" in html:
        i = html.index("</header>") + len("</header>")
        if html[i:].lstrip().startswith("<script>"):
            i = html.index("</script>", i) + len("</script>")
        html = html[:i] + '\n<main id="main" tabindex="-1">' + html[i:]
        j = html.index("<footer")
        k = html.rfind('<section class="closing"', 0, j)
        cut = k if k != -1 else j
        html = html[:cut] + "</main>\n" + html[cut:]
        html = re.sub(r"(<body[^>]*>)", r'\1\n<a class="skip-link" href="#main">' + SKIP_TXT[lang] + "</a>", html, count=1)
    return html


def _load_json(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return json.load(f)


def _write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    apartments = _load_json("assets/data/apartments.json")
    packages_all = _load_json("assets/data/packages.json")
    for lang in LANGS:
        for n, tiers in PACKAGE_SPEC.items():
            for t, spec in tiers.items():
                packages_all[lang][n][t] = [f"{k}: {v}" for k, v in spec_lines(spec, lang)[:-1]]
    vat = {"ru": "без НДС, ориентировочно", "ro": "fără TVA, orientativ", "en": "excl. VAT, indicative"}
    for lang in LANGS:
        pk = packages_all[lang]
        pk["labels"]["price_vat"] = vat[lang]
        pk["price_txt"] = {n: {t: CMP[lang]["price_from"].replace("{p}", fmt_eur(v, lang)) for t, v in tiers.items()}
                           for n, tiers in PRICES.items()}
    for lang in LANGS:
        for key in PAGE_ORDER:
            if key == "lagmar":
                html = lagmar_page_html(lang, apartments, packages_all)
            elif key == "features":
                html = features_page_html(lang, packages_all)
            elif key == "scenarios":
                html = scenarios_page_html(lang)
            elif key == "how":
                html = how_page_html(lang)
            elif key == "home":
                html = home_page_html(lang, packages_all)
            elif key == "contact":
                html = contact_page_html(lang)
            else:
                html = page_html(key, lang)
            html = typo(html, lang)
            html = finalize_html(html, lang)
            assert not any(ch in html for ch in "şţŞŢ"), f"cedilla diacritics in {lang}/{key}"
            _write(f"{lang}/{PAGE_FILE[key]}", html)
        for old, target in LEGACY_REDIRECTS.items():
            _write(f"{lang}/{old}", legacy_redirect_html(target))
    _write("index.html", root_redirect())
    _write("404.html", not_found_html())
    _write("sitemap.xml", sitemap_xml())
    _write("robots.txt", robots_txt())
    print("Built", len(LANGS) * len(PAGE_ORDER), "pages + root redirect, 404, sitemap, robots")


if __name__ == "__main__":
    main()
