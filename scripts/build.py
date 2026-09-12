#!/usr/bin/env python3
"""Static site generator for the Grenton demo (RO/RU/EN) — SmartSpace dealer showcase."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANGS = ["ro", "ru", "en"]
LANG_LABEL = {"ro": "RO", "ru": "RU", "en": "EN"}

NAV_LABELS = {
    "ro": {"home": "Acasă", "system": "Sistem", "control": "Control", "sensors": "Senzori", "contact": "Contact"},
    "ru": {"home": "Главная", "system": "Система", "control": "Управление", "sensors": "Сенсоры", "contact": "Контакты"},
    "en": {"home": "Home", "system": "System", "control": "Control", "sensors": "Sensors", "contact": "Contact"},
}

SITE_TITLE = "Grenton — SmartSpace Moldova"

FOOTER = {
    "ro": "Acest site este un demo informativ realizat de SmartSpace, reprezentant oficial Grenton în Moldova. Fotografiile produselor aparțin Grenton sp. z o.o.",
    "ru": "Этот сайт — информационный демо-стенд SmartSpace, официального представителя Grenton в Молдове. Фотографии продуктов принадлежат Grenton sp. z o.o.",
    "en": "This site is an informational demo built by SmartSpace, the official Grenton dealer in Moldova. Product photos belong to Grenton sp. z o.o.",
}

DEALER_BAND = {
    "ro": {
        "h": "SmartSpace — dealer oficial Grenton în Moldova",
        "p": "Consultanță, proiectare, montaj și service pentru sistemul Grenton — de la un singur apartament până la clădiri întregi.",
        "cta": "Solicită o ofertă",
    },
    "ru": {
        "h": "SmartSpace — официальный дилер Grenton в Молдове",
        "p": "Консультация, проектирование, монтаж и сервис системы Grenton — от одной квартиры до целых зданий.",
        "cta": "Запросить предложение",
    },
    "en": {
        "h": "SmartSpace — official Grenton dealer in Moldova",
        "p": "Consulting, design, installation and service for the Grenton system — from a single apartment to entire buildings.",
        "cta": "Request a quote",
    },
}

CONTACT_INFO = {
    "ro": {"addr": "Strada Pajurii 11, MD-2059 Chișinău", "phone": "+373 78 202 020", "note": "Programare vizită / consultație gratuită"},
    "ru": {"addr": "Strada Pajurii 11, MD-2059 Кишинёв", "phone": "+373 78 202 020", "note": "Запись на визит / бесплатная консультация"},
    "en": {"addr": "Strada Pajurii 11, MD-2059 Chișinău", "phone": "+373 78 202 020", "note": "Book a visit / free consultation"},
}

PAGES = {}

# ---------------- HOME ----------------
PAGES["home"] = {
    "ro": {
        "title": "Grenton Smart Home — prezentare SmartSpace",
        "eyebrow": "Ecosistem smart home",
        "h1": "Casa ta, controlată dintr-un singur loc",
        "lead": "Grenton este un sistem de automatizare a locuinței produs în Polonia: iluminat, climă, rulouri, muzică și securitate — toate conectate într-un singur ecosistem. SmartSpace instalează și configurează sistemul Grenton în Moldova.",
        "cta_primary": ("Vezi sistemul", "system.html"),
        "cta_secondary": ("Contactează-ne", "contact.html"),
        "cards": [
            ("Un singur controler", "Monolith gestionează întreaga locuință — lumini, climă, rulouri, senzori — fără cloud obligatoriu."),
            ("Panouri tactile elegante", "Smart Panel și Touch Panel înlocuiesc întrerupătoarele clasice cu un ecran de control intuitiv."),
            ("Aplicație mobilă", "myGrenton îți pune casa în buzunar — control de oriunde, scenarii, notificări."),
        ],
    },
    "ru": {
        "title": "Grenton Smart Home — обзор от SmartSpace",
        "eyebrow": "Экосистема умного дома",
        "h1": "Ваш дом — под управлением из одной точки",
        "lead": "Grenton — система домашней автоматизации из Польши: свет, климат, шторы, музыка и безопасность объединены в одну экосистему. SmartSpace устанавливает и настраивает Grenton в Молдове.",
        "cta_primary": ("Смотреть систему", "system.html"),
        "cta_secondary": ("Связаться с нами", "contact.html"),
        "cards": [
            ("Один контроллер", "Monolith управляет всем домом — светом, климатом, шторами, датчиками — без обязательного облака."),
            ("Элегантные панели", "Smart Panel и Touch Panel заменяют обычные выключатели интуитивным сенсорным экраном."),
            ("Мобильное приложение", "myGrenton — дом в кармане: управление откуда угодно, сценарии, уведомления."),
        ],
    },
    "en": {
        "title": "Grenton Smart Home — overview by SmartSpace",
        "eyebrow": "Smart home ecosystem",
        "h1": "Your home, controlled from one place",
        "lead": "Grenton is a Polish-made home automation system: lighting, climate, blinds, audio and security — all connected in one ecosystem. SmartSpace installs and configures Grenton in Moldova.",
        "cta_primary": ("See the system", "system.html"),
        "cta_secondary": ("Contact us", "contact.html"),
        "cards": [
            ("One controller", "Monolith runs the whole home — lights, climate, blinds, sensors — with no cloud dependency required."),
            ("Elegant touch panels", "Smart Panel and Touch Panel replace classic light switches with an intuitive control screen."),
            ("Mobile app", "myGrenton puts your home in your pocket — control from anywhere, scenes, notifications."),
        ],
    },
}

# ---------------- SYSTEM ----------------
PAGES["system"] = {
    "ro": {
        "title": "Sistemul Grenton — Monolith",
        "eyebrow": "Nucleul sistemului",
        "h1": "Monolith — controlerul care leagă totul",
        "lead": "Monolith este creierul instalației Grenton: procesează scenariile, comunică cu modulele de lumină, climă și senzorii, și poate funcţiona local, fără conexiune obligatorie la internet.",
        "cta_primary": ("Vezi opțiunile de control", "control.html"),
        "cta_secondary": ("Cere o consultație", "contact.html"),
        "cards": [
            ("Funcționare locală", "Scenariile rulează direct pe controler — casa continuă să funcționeze chiar dacă internetul cade."),
            ("Scalabil", "De la un apartament la o clădire întreagă — arhitectura modulară Grenton crește odată cu proiectul."),
            ("Integrări", "Compatibil cu module Z-Wave, senzori, sisteme audio și alte protocoale smart home."),
        ],
    },
    "ru": {
        "title": "Система Grenton — Monolith",
        "eyebrow": "Ядро системы",
        "h1": "Monolith — контроллер, который связывает всё",
        "lead": "Monolith — мозг инсталляции Grenton: обрабатывает сценарии, общается с модулями света, климата и датчиками, и может работать локально, без обязательного подключения к интернету.",
        "cta_primary": ("Варианты управления", "control.html"),
        "cta_secondary": ("Заказать консультацию", "contact.html"),
        "cards": [
            ("Локальная работа", "Сценарии выполняются прямо на контроллере — дом продолжает работать даже при отключении интернета."),
            ("Масштабируемость", "От квартиры до целого здания — модульная архитектура Grenton растёт вместе с проектом."),
            ("Интеграции", "Совместим с модулями Z-Wave, датчиками, аудиосистемами и другими протоколами умного дома."),
        ],
    },
    "en": {
        "title": "The Grenton system — Monolith",
        "eyebrow": "The core of the system",
        "h1": "Monolith — the controller that ties it all together",
        "lead": "Monolith is the brain of a Grenton installation: it runs scenes and talks to lighting, climate modules and sensors, and can operate locally without a mandatory internet connection.",
        "cta_primary": ("See control options", "control.html"),
        "cta_secondary": ("Request a consultation", "contact.html"),
        "cards": [
            ("Local operation", "Scenes run directly on the controller — the home keeps working even if the internet goes down."),
            ("Scalable", "From a single apartment to an entire building — Grenton's modular architecture grows with the project."),
            ("Integrations", "Compatible with Z-Wave modules, sensors, audio systems and other smart-home protocols."),
        ],
    },
}

# ---------------- CONTROL ----------------
PAGES["control"] = {
    "ro": {
        "title": "Control Grenton — Smart Panel, Touch Panel, myGrenton",
        "eyebrow": "Interfețe de control",
        "h1": "Control intuitiv, la perete sau în buzunar",
        "lead": "Grenton oferă mai multe moduri de a comanda locuința: panouri tactile montate pe perete, întrerupătoare inteligente și o aplicație mobilă — toate sincronizate cu Monolith.",
        "cta_primary": ("Vezi senzorii", "sensors.html"),
        "cta_secondary": ("Cere o ofertă", "contact.html"),
        "cards": [
            ("Smart Panel", "Panou tactil de perete pentru lumină, climă și scenarii — cu finisaje premium (lemn, sticlă)."),
            ("Touch Panel", "Ecran de control compact pentru cameră — acces rapid la funcțiile esențiale."),
            ("myGrenton App", "Control complet al casei de pe telefon — scenarii, notificări, acces de la distanță."),
            ("Întrerupătoare inteligente", "Înlocuiesc întrerupătoarele clasice, integrate direct în ecosistemul Grenton."),
        ],
    },
    "ru": {
        "title": "Управление Grenton — Smart Panel, Touch Panel, myGrenton",
        "eyebrow": "Интерфейсы управления",
        "h1": "Интуитивное управление — на стене или в кармане",
        "lead": "Grenton предлагает несколько способов управлять домом: настенные сенсорные панели, умные выключатели и мобильное приложение — всё синхронизировано с Monolith.",
        "cta_primary": ("Смотреть сенсоры", "sensors.html"),
        "cta_secondary": ("Запросить предложение", "contact.html"),
        "cards": [
            ("Smart Panel", "Настенная сенсорная панель для света, климата и сценариев — с премиальной отделкой (дерево, стекло)."),
            ("Touch Panel", "Компактный экран управления для комнаты — быстрый доступ к основным функциям."),
            ("Приложение myGrenton", "Полное управление домом с телефона — сценарии, уведомления, удалённый доступ."),
            ("Умные выключатели", "Заменяют обычные выключатели, интегрированы напрямую в экосистему Grenton."),
        ],
    },
    "en": {
        "title": "Grenton control — Smart Panel, Touch Panel, myGrenton",
        "eyebrow": "Control interfaces",
        "h1": "Intuitive control, on the wall or in your pocket",
        "lead": "Grenton offers several ways to run your home: wall-mounted touch panels, smart switches and a mobile app — all synced with Monolith.",
        "cta_primary": ("See sensors", "sensors.html"),
        "cta_secondary": ("Request a quote", "contact.html"),
        "cards": [
            ("Smart Panel", "A wall-mounted touch panel for lighting, climate and scenes — with premium finishes (wood, glass)."),
            ("Touch Panel", "A compact control screen for a room — fast access to the essential functions."),
            ("myGrenton App", "Full home control from your phone — scenes, notifications, remote access."),
            ("Smart switches", "Replace classic light switches, integrated directly into the Grenton ecosystem."),
        ],
    },
}

# ---------------- SENSORS ----------------
PAGES["sensors"] = {
    "ro": {
        "title": "Senzori Grenton — Multisensor",
        "eyebrow": "Senzori inteligenți",
        "h1": "Un senzor, mai multe măsurători",
        "lead": "Multisensor Grenton combină în același dispozitiv măsurarea temperaturii, umidității, luminozității și mișcării — datele alimentează scenariile automate din Monolith.",
        "cta_primary": ("Vezi controlul", "control.html"),
        "cta_secondary": ("Cere o consultație", "contact.html"),
        "cards": [
            ("Temperatură & umiditate", "Bază pentru automatizarea climei — încălzire, ventilație, climatizare adaptate în timp real."),
            ("Luminozitate", "Iluminatul se ajustează automat în funcție de lumina naturală din încăpere."),
            ("Detecție mișcare", "Declanșează scenarii de securitate sau confort la intrarea într-o cameră."),
        ],
    },
    "ru": {
        "title": "Сенсоры Grenton — Multisensor",
        "eyebrow": "Умные сенсоры",
        "h1": "Один сенсор — несколько измерений",
        "lead": "Multisensor Grenton объединяет в одном устройстве измерение температуры, влажности, освещённости и движения — данные питают автоматические сценарии в Monolith.",
        "cta_primary": ("Смотреть управление", "control.html"),
        "cta_secondary": ("Заказать консультацию", "contact.html"),
        "cards": [
            ("Температура и влажность", "Основа для автоматизации климата — отопление, вентиляция, кондиционирование в реальном времени."),
            ("Освещённость", "Освещение автоматически подстраивается под уровень естественного света в комнате."),
            ("Детекция движения", "Запускает сценарии безопасности или комфорта при входе в комнату."),
        ],
    },
    "en": {
        "title": "Grenton sensors — Multisensor",
        "eyebrow": "Smart sensors",
        "h1": "One sensor, several measurements",
        "lead": "The Grenton Multisensor combines temperature, humidity, light level and motion detection in a single device — the data feeds Monolith's automated scenes.",
        "cta_primary": ("See control options", "control.html"),
        "cta_secondary": ("Request a consultation", "contact.html"),
        "cards": [
            ("Temperature & humidity", "The base for climate automation — heating, ventilation and cooling adjusted in real time."),
            ("Light level", "Lighting adapts automatically to the natural light available in the room."),
            ("Motion detection", "Triggers security or comfort scenes whenever someone enters a room."),
        ],
    },
}

# ---------------- CONTACT ----------------
PAGES["contact"] = {
    "ro": {
        "title": "Contact — SmartSpace, dealer oficial Grenton",
        "eyebrow": "Hai să vorbim",
        "h1": "Programează o consultație gratuită",
        "lead": "Echipa SmartSpace te ajută să alegi configurația Grenton potrivită pentru proiectul tău — apartament, casă sau clădire.",
        "cta_primary": ("Sună acum", "tel:+37378202020"),
        "cta_secondary": ("Vezi sistemul", "system.html"),
        "cards": [],
    },
    "ru": {
        "title": "Контакты — SmartSpace, официальный дилер Grenton",
        "eyebrow": "Давайте обсудим",
        "h1": "Запишитесь на бесплатную консультацию",
        "lead": "Команда SmartSpace поможет подобрать конфигурацию Grenton под ваш проект — квартиру, дом или здание.",
        "cta_primary": ("Позвонить", "tel:+37378202020"),
        "cta_secondary": ("Смотреть систему", "system.html"),
        "cards": [],
    },
    "en": {
        "title": "Contact — SmartSpace, official Grenton dealer",
        "eyebrow": "Let's talk",
        "h1": "Book a free consultation",
        "lead": "The SmartSpace team helps you choose the right Grenton setup for your project — apartment, house or building.",
        "cta_primary": ("Call now", "tel:+37378202020"),
        "cta_secondary": ("See the system", "system.html"),
        "cards": [],
    },
}

PAGE_IMG = {
    "home": "monolith.png",
    "system": "monolith.png",
    "control": "smart-panel.jpg",
    "sensors": "audio-integration.png",
    "contact": "project-1.png",
}

PAGE_ORDER = ["home", "system", "control", "sensors", "contact"]
PAGE_FILE = {"home": "index.html", "system": "system.html", "control": "control.html",
             "sensors": "sensors.html", "contact": "contact.html"}


def nav_html(lang, current):
    labels = NAV_LABELS[lang]
    links = []
    for key in PAGE_ORDER:
        cls = " active" if key == current else ""
        links.append(f'<a class="{cls.strip()}" href="{PAGE_FILE[key]}">{labels[key]}</a>')
    lang_links = []
    for l in LANGS:
        cls = " active" if l == lang else ""
        lang_links.append(f'<a class="{cls.strip()}" href="../{l}/{PAGE_FILE[current]}">{LANG_LABEL[l]}</a>')
    return f'''<header class="site">
  <div class="wrap bar">
    <a class="brand" href="index.html">
      <img src="../../assets/img/favicon-32.png" alt="Grenton">
      GRENTON <span class="by">by SmartSpace</span>
    </a>
    <nav class="main">
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
    <div>SmartSpace · Chișinău, Moldova</div>
    <div class="disclaimer">{FOOTER[lang]}</div>
  </div>
</footer>'''


def page_html(key, lang):
    p = PAGES[key][lang]
    img = f"../../assets/img/{PAGE_IMG[key]}"
    cards_html = ""
    if p["cards"]:
        items = "".join(
            f'<div class="card"><div class="body"><h3>{h}</h3><p>{b}</p></div></div>'
            for h, b in p["cards"]
        )
        cards_html = f'<section class="block"><div class="wrap"><div class="grid">{items}</div></div></section>'

    contact_extra = ""
    if key == "contact":
        c = CONTACT_INFO[lang]
        contact_extra = f'''<section class="block">
  <div class="wrap">
    <div class="grid">
      <div class="card"><div class="body"><h3>📍 {c["addr"]}</h3><p>{c["note"]}</p></div></div>
      <div class="card"><div class="body"><h3>📞 {c["phone"]}</h3><p>SmartSpace</p></div></div>
    </div>
  </div>
</section>'''

    primary_label, primary_href = p["cta_primary"]
    secondary_label, secondary_href = p["cta_secondary"]

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]}</title>
<link rel="icon" href="../../assets/img/favicon-32.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&display=swap">
<link rel="stylesheet" href="../../assets/css/style.css">
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
    <img src="{img}" alt="Grenton">
    <div class="badge-row">
      <span class="badge">Grenton</span>
      <span class="badge">SmartSpace · Moldova</span>
      <span class="badge">Official dealer</span>
    </div>
  </div>
</section>
{cards_html}
{contact_extra}
{dealer_band_html(lang)}
{footer_html(lang)}
</body>
</html>'''


def root_redirect():
    return '''<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=ro/index.html">
<title>Grenton — SmartSpace Moldova</title>
</head>
<body>
<p>Redirecting… / <a href="ro/index.html">RO</a> · <a href="ru/index.html">RU</a> · <a href="en/index.html">EN</a></p>
</body>
</html>'''


def main():
    for lang in LANGS:
        lang_dir = os.path.join(ROOT, lang)
        os.makedirs(lang_dir, exist_ok=True)
        for key in PAGE_ORDER:
            with open(os.path.join(lang_dir, PAGE_FILE[key]), "w", encoding="utf-8") as f:
                f.write(page_html(key, lang))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(root_redirect())
    print("Built", len(LANGS) * len(PAGE_ORDER), "pages +root redirect")


if __name__ == "__main__":
    main()
