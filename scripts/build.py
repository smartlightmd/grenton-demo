#!/usr/bin/env python3
"""Static site generator for the Grenton showcase (RO/RU/EN) — SmartSpace, official Grenton representative in Moldova."""
import html as _html
import json
import os

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
    "ro": {"home": "Acasă", "lagmar": "Lagmar Smart Home", "system": "Sistem", "control": "Control", "sensors": "Senzori", "contact": "Contact"},
    "ru": {"home": "Главная", "lagmar": "Lagmar Smart Home", "system": "Система", "control": "Управление", "sensors": "Датчики", "contact": "Контакты"},
    "en": {"home": "Home", "lagmar": "Lagmar Smart Home", "system": "System", "control": "Control", "sensors": "Sensors", "contact": "Contact"},
}

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
    "system": {
        "ro": "CLU (Common Logic Unit) — unitatea centrală Grenton: rulează scenariile local, fără internet obligatoriu, și crește de la un apartament la o clădire întreagă.",
        "ru": "CLU (Common Logic Unit) — центральный модуль Grenton: выполняет сценарии локально, без обязательного интернета, масштабируется от квартиры до здания.",
        "en": "CLU (Common Logic Unit) — Grenton's central unit: runs scenes locally with no internet required and scales from one apartment to a whole building.",
    },
    "control": {
        "ro": "Smart Panel, Touch Panel, panourile premium Monolith și aplicația myGrenton — modurile de control al casei inteligente Grenton, la perete sau în buzunar.",
        "ru": "Smart Panel, Touch Panel, премиальные панели Monolith и приложение myGrenton — способы управления умным домом Grenton, на стене или в кармане.",
        "en": "Smart Panel, Touch Panel, the premium Monolith panels and the myGrenton app — ways to control a Grenton smart home, on the wall or in your pocket.",
    },
    "sensors": {
        "ro": "Grenton Multisensor: temperatură, umiditate, luminozitate și mișcare într-un singur senzor — baza scenariilor automate de climă, iluminat și securitate.",
        "ru": "Grenton Multisensor: температура, влажность, освещённость и движение в одном датчике — основа автоматических сценариев климата, света и безопасности.",
        "en": "Grenton Multisensor: temperature, humidity, light and motion in one sensor — the base for automated climate, lighting and security scenes.",
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

PAGES = {}

PAGES["home"] = {
    "ro": {
        "title": "Grenton smart home în Moldova — SmartSpace, reprezentant oficial",
        "eyebrow": "Ecosistem smart home",
        "h1": "Casa ta, controlată dintr-un singur loc",
        "lead": "Grenton este un sistem de automatizare a locuinței produs în Polonia: iluminat, climă, rulouri, muzică și securitate — toate conectate într-un singur ecosistem. SmartSpace instalează și configurează sistemul Grenton în Moldova.",
        "cta_primary": ("Vezi sistemul", "system.html"),
        "cta_secondary": ("Contactează-ne", "contact.html"),
        "cards": [
            ("Un singur creier — CLU", "Unitatea centrală CLU gestionează întreaga locuință — lumini, climă, rulouri, senzori — local, fără cloud obligatoriu."),
            ("Panouri tactile elegante", "Smart Panel, Touch Panel și linia premium Monolith înlocuiesc întrerupătoarele clasice cu un ecran de control intuitiv."),
            ("Aplicație mobilă", "myGrenton îți pune casa în buzunar — control de oriunde, scenarii, notificări."),
        ],
    },
    "ru": {
        "title": "Умный дом Grenton в Молдове — SmartSpace, официальный представитель",
        "eyebrow": "Экосистема умного дома",
        "h1": "Ваш дом — под управлением из одной точки",
        "lead": "Grenton — система домашней автоматизации из Польши: свет, климат, шторы, музыка и безопасность объединены в одну экосистему. SmartSpace устанавливает и настраивает Grenton в Молдове.",
        "cta_primary": ("Смотреть систему", "system.html"),
        "cta_secondary": ("Связаться с нами", "contact.html"),
        "cards": [
            ("Один центральный блок — CLU", "Центральный модуль CLU управляет всем домом — светом, климатом, шторами, датчиками — локально, без обязательного облака."),
            ("Элегантные панели", "Smart Panel, Touch Panel и премиальная линейка Monolith заменяют обычные выключатели интуитивным сенсорным экраном."),
            ("Мобильное приложение", "myGrenton — дом в кармане: управление откуда угодно, сценарии, уведомления."),
        ],
    },
    "en": {
        "title": "Grenton smart home in Moldova — SmartSpace, official representative",
        "eyebrow": "Smart home ecosystem",
        "h1": "Your home, controlled from one place",
        "lead": "Grenton is a Polish-made home automation system: lighting, climate, blinds, audio and security — all connected in one ecosystem. SmartSpace installs and configures Grenton in Moldova.",
        "cta_primary": ("See the system", "system.html"),
        "cta_secondary": ("Contact us", "contact.html"),
        "cards": [
            ("One central unit — CLU", "The CLU central unit runs the whole home — lights, climate, blinds, sensors — locally, no cloud required."),
            ("Elegant touch panels", "Smart Panel, Touch Panel and the premium Monolith line replace classic light switches with an intuitive control screen."),
            ("Mobile app", "myGrenton puts your home in your pocket — control from anywhere, scenes, notifications."),
        ],
    },
}

PAGES["system"] = {
    "ro": {
        "title": "Sistemul Grenton — CLU, unitatea centrală | SmartSpace",
        "eyebrow": "Nucleul sistemului",
        "h1": "CLU — unitatea centrală care leagă totul",
        "lead": "CLU (Common Logic Unit) este creierul instalației Grenton: rulează scenariile, comunică cu modulele de iluminat, climă și cu senzorii și funcționează local, fără conexiune obligatorie la internet.",
        "cta_primary": ("Vezi opțiunile de control", "control.html"),
        "cta_secondary": ("Cere o consultație", "contact.html"),
        "cards": [
            ("Funcționare locală", "Scenariile rulează direct pe CLU — casa continuă să funcționeze chiar dacă internetul cade."),
            ("Scalabil", "De la un apartament la o clădire întreagă — arhitectura modulară Grenton crește odată cu proiectul."),
            ("Integrări", "Compatibil cu module Z-Wave, senzori, sisteme audio și alte protocoale smart home."),
        ],
    },
    "ru": {
        "title": "Система Grenton — центральный модуль CLU | SmartSpace",
        "eyebrow": "Ядро системы",
        "h1": "CLU — центральный блок, который связывает всё",
        "lead": "CLU (Common Logic Unit) — мозг инсталляции Grenton: выполняет сценарии, связывает модули света, климата и датчики и работает локально, без обязательного подключения к интернету.",
        "cta_primary": ("Варианты управления", "control.html"),
        "cta_secondary": ("Заказать консультацию", "contact.html"),
        "cards": [
            ("Локальная работа", "Сценарии выполняются прямо на CLU — дом продолжает работать даже при отключении интернета."),
            ("Масштабируемость", "От квартиры до целого здания — модульная архитектура Grenton растёт вместе с проектом."),
            ("Интеграции", "Совместим с модулями Z-Wave, датчиками, аудиосистемами и другими протоколами умного дома."),
        ],
    },
    "en": {
        "title": "The Grenton system — CLU central unit | SmartSpace",
        "eyebrow": "The core of the system",
        "h1": "CLU — the central unit that ties it all together",
        "lead": "The CLU (Common Logic Unit) is the brain of a Grenton installation: it runs scenes, talks to lighting and climate modules and sensors, and works locally with no internet required.",
        "cta_primary": ("See control options", "control.html"),
        "cta_secondary": ("Request a consultation", "contact.html"),
        "cards": [
            ("Local operation", "Scenes run directly on the CLU — the home keeps working even if the internet goes down."),
            ("Scalable", "From a single apartment to an entire building — Grenton's modular architecture grows with the project."),
            ("Integrations", "Compatible with Z-Wave modules, sensors, audio systems and other smart-home protocols."),
        ],
    },
}

PAGES["control"] = {
    "ro": {
        "title": "Control Grenton — Smart Panel, Touch Panel, Monolith, myGrenton | SmartSpace",
        "eyebrow": "Interfețe de control",
        "h1": "Control intuitiv, la perete sau în buzunar",
        "lead": "Grenton oferă mai multe moduri de a comanda locuința: panouri tactile montate pe perete, întrerupătoare inteligente și o aplicație mobilă — toate sincronizate cu unitatea centrală CLU.",
        "cta_primary": ("Vezi senzorii", "sensors.html"),
        "cta_secondary": ("Cere o ofertă", "contact.html"),
        "cards": [
            ("Smart Panel", "Panou tactil de perete pentru lumină, climă și scenarii — cu finisaje premium (lemn, sticlă)."),
            ("Touch Panel", "Ecran de control compact pentru cameră — acces rapid la funcțiile esențiale."),
            ("Monolith", "Linia premium de panouri tactile Grenton: patru finisaje din metal masiv (Silver, Brass, Titan, Black) într-o formă monolitică."),
            ("myGrenton App", "Control complet al casei de pe telefon — scenarii, notificări, acces de la distanță."),
            ("Întrerupătoare inteligente", "Înlocuiesc întrerupătoarele clasice, integrate direct în ecosistemul Grenton."),
        ],
    },
    "ru": {
        "title": "Управление Grenton — Smart Panel, Touch Panel, Monolith, myGrenton | SmartSpace",
        "eyebrow": "Интерфейсы управления",
        "h1": "Интуитивное управление — на стене или в кармане",
        "lead": "Grenton предлагает несколько способов управлять домом: настенные сенсорные панели, умные выключатели и мобильное приложение — всё синхронизировано с центральным модулем CLU.",
        "cta_primary": ("Смотреть датчики", "sensors.html"),
        "cta_secondary": ("Запросить предложение", "contact.html"),
        "cards": [
            ("Smart Panel", "Настенная сенсорная панель для света, климата и сценариев — с премиальной отделкой (дерево, стекло)."),
            ("Touch Panel", "Компактный экран управления для комнаты — быстрый доступ к основным функциям."),
            ("Monolith", "Премиальная линейка сенсорных панелей Grenton: четыре отделки из цельного металла (Silver, Brass, Titan, Black) в монолитной форме."),
            ("Приложение myGrenton", "Полное управление домом с телефона — сценарии, уведомления, удалённый доступ."),
            ("Умные выключатели", "Заменяют обычные выключатели, интегрированы напрямую в экосистему Grenton."),
        ],
    },
    "en": {
        "title": "Grenton control — Smart Panel, Touch Panel, Monolith, myGrenton | SmartSpace",
        "eyebrow": "Control interfaces",
        "h1": "Intuitive control, on the wall or in your pocket",
        "lead": "Grenton offers several ways to run your home: wall-mounted touch panels, smart switches and a mobile app — all synced with the CLU central unit.",
        "cta_primary": ("See sensors", "sensors.html"),
        "cta_secondary": ("Request a quote", "contact.html"),
        "cards": [
            ("Smart Panel", "A wall-mounted touch panel for lighting, climate and scenes — with premium finishes (wood, glass)."),
            ("Touch Panel", "A compact control screen for a room — fast access to the essential functions."),
            ("Monolith", "Grenton's premium touch-panel line: four solid-metal finishes (Silver, Brass, Titan, Black) in one monolithic form."),
            ("myGrenton App", "Full home control from your phone — scenes, notifications, remote access."),
            ("Smart switches", "Replace classic light switches, integrated directly into the Grenton ecosystem."),
        ],
    },
}

PAGES["sensors"] = {
    "ro": {
        "title": "Senzori Grenton — Multisensor | SmartSpace",
        "eyebrow": "Senzori inteligenți",
        "h1": "Un senzor, mai multe măsurători",
        "lead": "Multisensor Grenton combină în același dispozitiv măsurarea temperaturii, umidității, luminozității și mișcării — datele stau la baza scenariilor automate din CLU.",
        "cta_primary": ("Vezi controlul", "control.html"),
        "cta_secondary": ("Cere o consultație", "contact.html"),
        "cards": [
            ("Temperatură & umiditate", "Bază pentru automatizarea climei — încălzire, ventilație, climatizare adaptate în timp real."),
            ("Luminozitate", "Iluminatul se ajustează automat în funcție de lumina naturală din încăpere."),
            ("Detectarea mișcării", "Declanșează scenarii de securitate sau confort la intrarea într-o cameră."),
        ],
    },
    "ru": {
        "title": "Датчики Grenton — Multisensor | SmartSpace",
        "eyebrow": "Умные датчики",
        "h1": "Один датчик — несколько измерений",
        "lead": "Multisensor Grenton объединяет в одном устройстве измерение температуры, влажности, освещённости и движения — данные используются в автоматических сценариях CLU.",
        "cta_primary": ("Смотреть управление", "control.html"),
        "cta_secondary": ("Заказать консультацию", "contact.html"),
        "cards": [
            ("Температура и влажность", "Основа для автоматизации климата — отопление, вентиляция, кондиционирование в реальном времени."),
            ("Освещённость", "Освещение автоматически подстраивается под уровень естественного света в комнате."),
            ("Датчик движения", "Запускает сценарии безопасности или комфорта при входе в комнату."),
        ],
    },
    "en": {
        "title": "Grenton sensors — Multisensor | SmartSpace",
        "eyebrow": "Smart sensors",
        "h1": "One sensor, several measurements",
        "lead": "The Grenton Multisensor combines temperature, humidity, light level and motion detection in a single device — the data drives the CLU's automated scenes.",
        "cta_primary": ("See control options", "control.html"),
        "cta_secondary": ("Request a consultation", "contact.html"),
        "cards": [
            ("Temperature & humidity", "The base for climate automation — heating, ventilation and cooling adjusted in real time."),
            ("Light level", "Lighting adapts automatically to the natural light available in the room."),
            ("Motion detection", "Triggers security or comfort scenes whenever someone enters a room."),
        ],
    },
}

PAGES["contact"] = {
    "ro": {
        "title": "Contact — SmartSpace, reprezentant oficial Grenton în Moldova",
        "eyebrow": "Hai să vorbim",
        "h1": "Programează o consultație gratuită",
        "lead": "Echipa SmartSpace te ajută să alegi configurația Grenton potrivită pentru proiectul tău — apartament, casă sau clădire.",
        "cta_primary": ("Sună acum", f"tel:{PHONE_TEL}"),
        "cta_secondary": ("Vezi sistemul", "system.html"),
        "cards": [],
    },
    "ru": {
        "title": "Контакты — SmartSpace, официальный представитель Grenton в Молдове",
        "eyebrow": "Давайте обсудим",
        "h1": "Запишитесь на бесплатную консультацию",
        "lead": "Команда SmartSpace поможет подобрать конфигурацию Grenton под ваш проект — квартиру, дом или здание.",
        "cta_primary": ("Позвонить", f"tel:{PHONE_TEL}"),
        "cta_secondary": ("Смотреть систему", "system.html"),
        "cards": [],
    },
    "en": {
        "title": "Contact — SmartSpace, official Grenton representative in Moldova",
        "eyebrow": "Let's talk",
        "h1": "Book a free consultation",
        "lead": "The SmartSpace team helps you choose the right Grenton setup for your project — apartment, house or building.",
        "cta_primary": ("Call now", f"tel:{PHONE_TEL}"),
        "cta_secondary": ("See the system", "system.html"),
        "cards": [],
    },
}

LAGMAR_UI = {
    "ru": {
        "title": "Умный дом Grenton для квартиры в Lagmar Smart Home — конфигуратор | SmartSpace",
        "eyebrow": "Ваш дом в Lagmar Smart Home",
        "h1": "Умный дом для вашей квартиры в Lagmar",
        "lead": "SmartSpace — официальный представитель Grenton — подберёт готовое решение для вашей квартиры в жилом комплексе Lagmar Smart Home. Найдите свою квартиру, выберите комплектацию и получите персональное предложение.",
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
        "error_rate": "Слишком много запросов — попробуйте через несколько минут.",
        "packages_title": "Что входит в пакеты",
        "faq_title": "Вопросы и ответы",
    },
    "ro": {
        "title": "Casă inteligentă Grenton pentru apartamentul tău în Lagmar Smart Home — configurator | SmartSpace",
        "eyebrow": "Apartamentul tău din Lagmar Smart Home",
        "h1": "Casă inteligentă pentru apartamentul tău din Lagmar",
        "lead": "SmartSpace — reprezentant oficial Grenton — îți propune soluția potrivită pentru apartamentul tău din complexul Lagmar Smart Home. Găsește-ți apartamentul, alege pachetul și primește oferta personalizată.",
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
        "error_rate": "Prea multe cereri — încearcă din nou peste câteva minute.",
        "packages_title": "Ce include fiecare pachet",
        "faq_title": "Întrebări frecvente",
    },
    "en": {
        "title": "Grenton smart home for your Lagmar Smart Home apartment — configurator | SmartSpace",
        "eyebrow": "Your home in Lagmar Smart Home",
        "h1": "Smart home for your Lagmar apartment",
        "lead": "SmartSpace — the official Grenton representative — finds the right setup for your apartment in the Lagmar Smart Home complex. Find your apartment, pick a package, and get a personal quote.",
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
        "cta_find": "Найти мою квартиру", "cta_examples": "Пакеты на планировке",
        "complex_eyebrow": "Жилой комплекс", "complex_title": "Lagmar Smart Home — 11 блоков в Кишинёве",
        "complex_text": "Современные дома вокруг зелёных внутренних дворов с зонами отдыха и подземным паркингом. Умный дом здесь — часть проекта: квартиры рассчитаны на систему Grenton, а SmartSpace проектирует, монтирует и обслуживает её.",
        "siteplan_caption": "Генплан комплекса: 11 блоков вокруг зелёных дворов",
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
                    "Q": "Датчик CO₂", "I": "Видеодомофон"},
    },
    "ro": {
        "kicker": "Lagmar Smart Home × Grenton",
        "stats": [("11", "blocuri"), ("1 065", "apartamente"), ("Grenton", "casă inteligentă în fiecare")],
        "cta_find": "Găsește-mi apartamentul", "cta_examples": "Pachetele pe plan",
        "complex_eyebrow": "Complex rezidențial", "complex_title": "Lagmar Smart Home — 11 blocuri în Chișinău",
        "complex_text": "Clădiri moderne în jurul curților interioare verzi, cu zone de odihnă și parcare subterană. Casa inteligentă face parte din proiect: apartamentele sunt gândite pentru sistemul Grenton, iar SmartSpace îl proiectează, îl montează și îl întreține.",
        "siteplan_caption": "Planul general: 11 blocuri în jurul curților verzi",
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
                    "Q": "Senzor CO₂", "I": "Videointerfon"},
    },
    "en": {
        "kicker": "Lagmar Smart Home × Grenton",
        "stats": [("11", "blocks"), ("1,065", "apartments"), ("Grenton", "smart home in every one")],
        "cta_find": "Find my apartment", "cta_examples": "Packages on a floor plan",
        "complex_eyebrow": "Residential complex", "complex_title": "Lagmar Smart Home — 11 blocks in Chișinău",
        "complex_text": "Modern buildings around green inner courtyards with leisure areas and underground parking. The smart home is part of the project: apartments are planned for the Grenton system, which SmartSpace designs, installs and services.",
        "siteplan_caption": "Site plan: 11 blocks around green courtyards",
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
                    "Q": "CO₂ sensor", "I": "Video intercom"},
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
PLAN_SIZE = {"2": (424, 589), "3": (767, 615), "4": (558, 1064)}

PAGE_IMG = {"home": "monolith.png", "system": "clu.jpg", "control": "smart-panel.jpg", "sensors": "audio-integration.png", "contact": "project-1.png", "lagmar": "project-2.png"}
IMG_ALT = {
    "monolith.png": "Grenton Monolith — сенсорная панель / touch panel", "clu.jpg": "Grenton CLU — central unit",
    "smart-panel.jpg": "Grenton Smart Panel", "audio-integration.png": "Grenton — audio integration",
    "project-1.png": "Smart home project", "project-2.png": "Smart home project",
}

PAGE_ORDER = ["home", "lagmar", "system", "control", "sensors", "contact"]
PAGE_FILE = {"home": "index.html", "lagmar": "lagmar.html", "system": "system.html", "control": "control.html",
             "sensors": "sensors.html", "contact": "contact.html"}


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
<meta name="theme-color" content="#fafafa">
<link rel="stylesheet" href="../assets/css/style.css">
{jsonld_html}'''


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
      <img src="../assets/img/favicon-32.png" alt="" width="28" height="28">
      GRENTON <span class="by">by SmartSpace</span>
    </a>
    <nav class="main" aria-label="Main">
      {''.join(links)}
      <div class="langs">{''.join(lang_links)}</div>
    </nav>
  </div>
</header>'''


def dealer_band_html(lang):
    d = DEALER_BAND[lang]
    return f'''<section class="dealer-band">
  <div class="wrap">
    <h2>{d["h"]}</h2>
    <p>{d["p"]}</p>
    <a class="btn btn-accent" href="contact.html">{d["cta"]}</a>
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
        items = "".join(f'<div class="card"><div class="body"><h3>{h}</h3><p>{b}</p></div></div>' for h, b in p["cards"])
        cards_html = f'<section class="block"><div class="wrap"><div class="grid">{items}</div></div></section>'

    extra = ""
    if key == "contact":
        c = CONTACT_INFO[lang]
        extra = f'''<section class="block">
  <div class="wrap">
    <div class="grid">
      <div class="card"><div class="body"><h3>📍 {c["addr"]}</h3><p>{c["note"]}</p></div></div>
      <div class="card"><div class="body"><h3>📞 <a href="tel:{PHONE_TEL}">{c["phone"]}</a></h3><p>SmartSpace</p></div></div>
    </div>
  </div>
</section>'''
    if key == "home":
        hl = HOME_LAGMAR[lang]
        extra = f'''<section class="block lagmar-block" id="lagmar">
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

    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_html(lang, key, p["title"], META_DESC[key][lang])}
</head>
<body>
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
<section class="block alt">
  <div class="wrap split">
    <img src="../assets/img/{img}" alt="{IMG_ALT.get(img, 'Grenton')}" loading="lazy">
    {badges_html(lang)}
  </div>
</section>
{cards_html}
{extra}
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
  var state = { building: "", apt: "", floor: null, rooms: null, roomsActual: null, area: null, tariff: null };

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
      $("cfg-building").value = tile.dataset.block;
      Array.prototype.forEach.call(document.querySelectorAll(".blk"), function (x) { x.setAttribute("aria-pressed", x === tile ? "true" : "false"); });
      show($("cfg-found"), false); show($("cfg-manual"), false); resetBelow();
      $("cfg-apt").focus();
    });
  });
  function markBlock(b) {
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
      var pr = document.createElement("p"); pr.className = "tariff-price"; pr.textContent = PK.labels.price_note || "";
      var ul = document.createElement("ul"); ul.className = "tariff-list";
      (cat[tier] || []).forEach(function (t) { var li = document.createElement("li"); li.textContent = t; ul.appendChild(li); });
      body.appendChild(h3); body.appendChild(pr); body.appendChild(ul); card.appendChild(body);
      card.addEventListener("click", function () {
        Array.prototype.forEach.call(wrap.querySelectorAll(".tariff-card"), function (c) { c.setAttribute("aria-checked", "false"); });
        card.setAttribute("aria-checked", "true");
        state.tariff = tier;
        setTier($("s2-" + state.rooms), tier);
        show($("step3"), true);
        scrollTo($("step3"));
      });
      wrap.appendChild(card);
    });
    $("cfg-upsell").textContent = "✨ " + PK.labels.upsell_title + ": " + PK.labels.upsell;
  }

  function showStep2(roomsActual, area, floor) {
    state.roomsActual = roomsActual; state.rooms = clipRooms(roomsActual); state.area = area || null; state.floor = floor;
    show($("cfg-edge"), roomsActual < 2 || roomsActual > 4);
    renderTariffs(state.rooms);
    ["2", "3", "4"].forEach(function (k) { show($("s2-" + k), String(state.rooms) === k); });
    setTier($("s2-" + state.rooms), "comfort");
    show($("step2"), true);
    scrollTo($("step2"));
  }

  function doFind() {
    var b = $("cfg-building").value;
    var n = normNum($("cfg-apt").value);
    resetBelow();
    show($("cfg-manual"), false); show($("cfg-found"), false);
    state.building = b; state.apt = n;
    if (!b) { $("cfg-found").textContent = UI.choose_building; show($("cfg-found"), true); $("cfg-building").focus(); return; }
    if (!n) { show($("cfg-manual"), true); return; }
    var found = null;
    for (var i = 0; i < APTS.length; i++) { if (APTS[i].b === b && normNum(APTS[i].n) === n) { found = APTS[i]; break; } }
    if (found) {
      var fl = String(found.f) === "0" ? UI.floor_ground : (UI.floor_word + " " + found.f);
      $("cfg-found").textContent = UI.found_prefix + " " + UI.building_label + " " + b + " · " + fl + " · " + found.r + " " + UI.rooms_word + " · " + fmtArea(found.a) + " " + UI.area_word;
      show($("cfg-found"), true);
      markBlock(b);
      showAptCard(found);
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
  function validQuoteUrl(u) { return typeof u === "string" && /^https:\/\/app\.smartspace\.md\/q\/[A-Za-z0-9_-]{10,}$/.test(u); }

  $("cfg-form").addEventListener("submit", function (ev) {
    ev.preventDefault();
    var btn = $("cfg-submit");
    if ($("cfg-hp").value) { showResult(successNode(null)); show($("cfg-form"), false); return; }
    if (!state.tariff || !state.rooms) { showResult(errorNode(UI.tariff_required, false)); scrollTo($("step2")); return; }
    var phone = normPhone($("cfg-phone").value);
    if (!phone) { showResult(errorNode(UI.error_phone, false)); $("cfg-phone").focus(); return; }
    btn.disabled = true; btn.textContent = UI.sending;
    var payload = {
      name: $("cfg-name").value.trim(), phone: phone, email: $("cfg-email").value.trim() || null,
      building: state.building || null, floor: state.floor, apartment_number: state.apt || null,
      rooms: state.rooms, rooms_actual: state.roomsActual, area_m2: state.area, tariff: state.tariff,
      lang: LANG, source: "grenton-demo", page_url: location.href, consent: true
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


def _json_for_script(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def packages_static_html(lang, pk):
    lab = pk["labels"]
    out = []
    for i, n in enumerate(["2", "3", "4"]):
        tiers = "".join(
            f'<div class="pk-tier"><h3>{esc(lab[t])}</h3><ul>' + "".join(f"<li>{esc(x)}</li>" for x in pk[n][t]) + "</ul></div>"
            for t in ["basic", "comfort", "premium"])
        out.append(f'<details class="pk"{" open" if i == 0 else ""}><summary>{esc(lab["size_title"].replace("{n}", n))}</summary><div class="pk-grid">{tiers}</div></details>')
    return "".join(out) + f'<p class="cfg-note">{esc(lab["why_comfort"])}</p><p class="cfg-note">{esc(lab["why_premium"])}</p><p class="cfg-footnote">{esc(lab["footnote"])}</p>'


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
        f'<span class="mk mk-{t}" data-t="{tiers}" style="left:{x}%;top:{y}%" title="{esc(v["devices"][t])}"><i>{t}</i></span>'
        for t, x, y, tiers in PLAN_MARKERS[n])
    tier_btns = "".join(
        f'<button type="button" class="planx-tier" data-set-tier="{t}" aria-pressed="{"true" if t == "comfort" else "false"}">{esc(lab[t])}</button>'
        for t in ["basic", "comfort", "premium"])
    legend = []
    for t in DEVICE_ORDER:
        cnt = {k: sum(1 for m in PLAN_MARKERS[n] if m[0] == t and k in m[3]) for k in "bcp"}
        if not any(cnt.values()):
            continue
        legend.append(f'<li class="lg-{t}" data-has="{"".join(k for k in "bcp" if cnt[k])}"><i class="mk mk-{t}"><i>{t}</i></i>'
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
    stats = "".join(f'<li><b>{esc(a)}</b><span>{esc(b)}</span></li>' for a, b in v["stats"])
    return f'''<section class="lg-hero">
  <img class="lg-hero-bg" src="../assets/lagmar/hero.jpg" srcset="../assets/lagmar/hero-960.jpg 960w, ../assets/lagmar/hero.jpg 1920w" sizes="100vw" alt="Lagmar Smart Home" fetchpriority="high">
  <div class="wrap lg-hero-inner">
    <div class="lg-logos"><img src="../assets/lagmar/logo-lagmar.png" alt="Lagmar Smart Home" width="160" height="48"><span class="x">×</span><span class="gr">GRENTON <small>by SmartSpace</small></span></div>
    <h1>{u["h1"]}</h1>
    <p class="lead">{u["lead"]}</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="#step1">{v["cta_find"]}</a>
      <a class="btn btn-light" href="#examples">{v["cta_examples"]}</a>
    </div>
    <ul class="lg-stats">{stats}</ul>
    <noscript><p class="lead"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p></noscript>
  </div>
</section>'''


def lagmar_complex_html(lang):
    v = LAGMAR_VIS[lang]
    return f'''<section class="block lg-complex" id="complex">
  <div class="wrap">
    <div class="split">
      <div>
        <span class="eyebrow">{v["complex_eyebrow"]}</span>
        <h2 class="h2">{v["complex_title"]}</h2>
        <p class="sub">{v["complex_text"]}</p>
      </div>
      <img class="rounded" src="../assets/lagmar/aerial.jpg" width="1600" height="828" alt="Lagmar Smart Home" loading="lazy">
    </div>
    <div class="lg-gallery">
      <img src="../assets/lagmar/collage.jpg" width="888" height="843" alt="Lagmar Smart Home" loading="lazy">
      <figure><img src="../assets/lagmar/siteplan.jpg" width="1600" height="898" alt="{esc(v["siteplan_caption"])}" loading="lazy"><figcaption>{v["siteplan_caption"]}</figcaption></figure>
    </div>
  </div>
</section>'''


def lagmar_blocks_html(lang):
    v = LAGMAR_VIS[lang]
    tiles = "".join(
        f'<button type="button" class="blk" data-block="{b}" aria-pressed="false"><img src="../assets/lagmar/blocks/{b}.jpg" width="330" height="508" alt="{esc(v["block_word"])} {b}" loading="lazy"><span>{b}</span></button>'
        for b in BUILDINGS)
    return f'<p class="cfg-note"><b>{v["blocks_title"]}.</b> {v["blocks_sub"]}</p><div class="blk-row">{tiles}</div>'


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
    ui_js = dict(u, block_word=v["block_word"], your_plan=v["your_plan"], your_block=v["your_block"])
    building_options = "".join(f'<option value="{b}">{b}</option>' for b in BUILDINGS)
    js = (LAGMAR_JS.replace("__LANG__", lang).replace("__UI__", _json_for_script(ui_js)).replace("__API__", API_URL)
          .replace("__PHONE_DISPLAY__", PHONE_DISPLAY).replace("__PHONE_TEL__", PHONE_TEL)
          .replace("__PLAN_BASE__", PLAN_IMG_BASE))
    s2_widgets = "".join(plan_widget_html(lang, n, pk, f"s2-{n}", "s2-plan", hidden=True) for n in ["2", "3", "4"])
    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_html(lang, "lagmar", u["title"], META_DESC["lagmar"][lang], [faq_jsonld(lang)])}
</head>
<body class="theme-lagmar">
{nav_html(lang, "lagmar")}
{lagmar_hero_html(lang, u)}

<section class="block alt cfg-step" id="step1">
  <div class="wrap">
    <h2 class="h2">{u["step1_title"]}</h2>
    {lagmar_blocks_html(lang)}
    <form id="cfg-search" class="cfg-row" autocomplete="off">
      <label>{u["building_label"]}
        <select id="cfg-building" name="building"><option value="">{u["building_placeholder"]}</option>{building_options}</select>
      </label>
      <label>{u["apt_label"]}
        <input id="cfg-apt" name="apt" type="text" inputmode="numeric" enterkeyhint="search" placeholder="{u["apt_placeholder"]}" aria-describedby="cfg-apt-hint">
      </label>
      <button class="btn btn-primary" type="submit" id="cfg-find">{u["find_btn"]}</button>
    </form>
    <p id="cfg-apt-hint" class="cfg-hint">{u["apt_hint"]}</p>
    <div id="cfg-found" class="cfg-note cfg-status" role="status" aria-live="polite" hidden></div>
    <div id="cfg-aptcard" class="aptcard" hidden>
      <figure class="aptcard-plan"><img id="cfg-plan-img" alt="" loading="lazy"><figcaption>{v["your_plan"]}</figcaption></figure>
      <figure class="aptcard-block"><img id="cfg-block-img" alt="" loading="lazy"><figcaption id="cfg-block-cap"></figcaption></figure>
    </div>
    <div id="cfg-manual" class="cfg-manual" role="status" aria-live="polite" hidden>
      <p class="cfg-note">{u["not_found_text"]}</p>
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
    <p class="cfg-note" id="cfg-edge" hidden>{u["edge_hint"]}</p>
    <div class="grid" id="cfg-tariffs" role="radiogroup" aria-label="{esc(u["step2_title"])}"></div>
    <p class="cfg-note" id="cfg-upsell"></p>
    <h3 class="s2-plan-title">{v["s2_plan_title"]}</h3>
    {s2_widgets}
  </div>
</section>

<section class="block alt cfg-step" id="step3" hidden>
  <div class="wrap">
    <h2 class="h2">{u["step3_title"]}</h2>
    <form id="cfg-form" class="cfg-form" novalidate>
      <input type="text" id="cfg-hp" name="fax_ref" class="cfg-hp" tabindex="-1" aria-hidden="true" autocomplete="new-password">
      <label>{u["name_label"]}<input type="text" id="cfg-name" name="name" required minlength="2" maxlength="80" autocomplete="name"></label>
      <label>{u["phone_label"]}<input type="tel" id="cfg-phone" name="phone" required minlength="6" maxlength="20" autocomplete="tel" inputmode="tel" placeholder="+373 6x xxx xxx" aria-describedby="cfg-phone-hint"></label>
      <p id="cfg-phone-hint" class="cfg-hint">{u["phone_hint"]}</p>
      <label>{u["email_label"]}<input type="email" id="cfg-email" name="email" autocomplete="email" maxlength="120"></label>
      <label class="cfg-consent"><input type="checkbox" id="cfg-consent" required> <span>{u["consent_text"]} <a href="{PRIVACY_URL}" target="_blank" rel="noopener noreferrer">{u["consent_link"]}</a></span></label>
      <p class="cfg-disclaimer">{u["disclaimer"]}</p>
      <button class="btn btn-primary" type="submit" id="cfg-submit">{u["submit_btn"]}</button>
    </form>
    <div id="cfg-result" class="cfg-note cfg-status" role="status" aria-live="polite" hidden></div>
  </div>
</section>

{lagmar_examples_html(lang, pk)}

{lagmar_complex_html(lang)}

<section class="block" id="packages">
  <div class="wrap">
    <h2 class="h2">{u["packages_title"]}</h2>
    {packages_static_html(lang, pk)}
  </div>
</section>

<section class="block alt" id="faq">
  <div class="wrap">
    <h2 class="h2">{u["faq_title"]}</h2>
    {faq_html(lang)}
  </div>
</section>

{dealer_band_html(lang)}
{footer_html(lang)}

<script id="apt-data" type="application/json">{_json_for_script(apartments)}</script>
<script id="pk-data" type="application/json">{_json_for_script(pk)}</script>
<script>{js}</script>
</body>
</html>'''


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
        for key in PAGE_ORDER:
            html = lagmar_page_html(lang, apartments, packages_all) if key == "lagmar" else page_html(key, lang)
            assert not any(ch in html for ch in "şţŞŢ"), f"cedilla diacritics in {lang}/{key}"
            _write(f"{lang}/{PAGE_FILE[key]}", html)
    _write("index.html", root_redirect())
    _write("404.html", not_found_html())
    _write("sitemap.xml", sitemap_xml())
    _write("robots.txt", robots_txt())
    print("Built", len(LANGS) * len(PAGE_ORDER), "pages + root redirect, 404, sitemap, robots")


if __name__ == "__main__":
    main()
