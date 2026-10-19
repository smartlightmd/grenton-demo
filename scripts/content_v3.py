"""Copy + data for the v3 visual layer (13.10.2026): video hero, "one day" interactive,
package comparison with "from" prices, product gallery, app mockup — RO/RU/EN.

Media: official Grenton photos/videos (SmartSpace is the official Grenton representative),
Lagmar renders/plans. Prices: SmartSpace unit prices for Grenton modules (2025 quote),
see PRICE_UNITS / PRICE_BOM below — equipment + programming, VAT excluded.
"""
import math

# ---------------------------------------------------------------------------
# Prices: SmartSpace selling prices per Grenton module, EUR excl. VAT (2025 quote)
PRICE_UNITS = {"CLU": 295, "R4": 115, "DIM": 105, "RGBW": 115, "IO": 230, "SP": 230,
               "TP4": 125, "TP8": 135, "RS": 155, "PSU": 51}
# Bill of materials per apartment size / package (Grenton modules only)
PRICE_BOM = {
    "2": {"basic":   {"CLU": 1, "R4": 2, "IO": 1, "SP": 1, "TP4": 1, "PSU": 1},
          "comfort": {"CLU": 1, "R4": 3, "DIM": 1, "RS": 1, "IO": 1, "SP": 1, "TP4": 3, "PSU": 1},
          "premium": {"CLU": 1, "R4": 4, "DIM": 2, "RGBW": 1, "RS": 1, "IO": 2, "SP": 2, "TP4": 2, "TP8": 2, "PSU": 1}},
    "3": {"basic":   {"CLU": 1, "R4": 2, "IO": 1, "SP": 1, "TP4": 2, "PSU": 1},
          "comfort": {"CLU": 1, "R4": 4, "DIM": 1, "RS": 1, "IO": 1, "SP": 1, "TP4": 4, "PSU": 1},
          "premium": {"CLU": 1, "R4": 5, "DIM": 2, "RGBW": 1, "RS": 2, "IO": 2, "SP": 2, "TP4": 3, "TP8": 2, "PSU": 1}},
    "4": {"basic":   {"CLU": 1, "R4": 3, "IO": 1, "SP": 1, "TP4": 2, "PSU": 1},
          "comfort": {"CLU": 1, "R4": 5, "DIM": 2, "RS": 1, "IO": 2, "SP": 1, "TP4": 5, "PSU": 1},
          "premium": {"CLU": 1, "R4": 6, "DIM": 3, "RGBW": 2, "RS": 2, "IO": 2, "SP": 3, "TP4": 4, "TP8": 2, "PSU": 1}},
}
PROGRAMMING_SHARE = 0.30  # programming / commissioning, as in the 2025 quote (~28%)


def package_prices():
    out = {}
    for n, tiers in PRICE_BOM.items():
        out[n] = {}
        for t, bom in tiers.items():
            dev = sum(PRICE_UNITS[k] * q for k, q in bom.items())
            out[n][t] = int(math.ceil(dev * (1 + PROGRAMMING_SHARE) / 100.0) * 100)
    return out


PRICES = package_prices()


def fmt_eur(v, lang):
    s = f"{v:,}".replace(",", " " if lang != "en" else ",")
    return f"{s} €"


# ---------------------------------------------------------------------------
# "One day in a Lagmar apartment" — 46 m² plan (F-27). Positions in % of the plan image.
DAY_LIGHTS = {"bed": (26, 36, 34), "kit": (72, 44, 30), "ver": (67, 17, 18), "liv": (32, 80, 34),
              "hall": (74, 68, 16), "bath": (80, 87, 18)}
DAY_BLINDS = {"bed": ("h", 5, 9.6, 36), "liv": ("v", 2.2, 76, 21)}  # (orientation, x, y, length %)
# sc = index in SCENARIOS items; dark = night overlay 0..1; lights = brightness per zone
DAY_STATES = [
    {"sc": 0, "dark": .32, "lights": {"bed": .75, "bath": 1}, "blinds": {"bed": 0, "liv": 0}, "temp": 22, "eco": False},
    {"sc": 1, "dark": 0, "lights": {}, "blinds": {"bed": 0, "liv": 0}, "temp": 18, "eco": True, "guard": True},
    {"sc": 2, "dark": 0, "lights": {}, "blinds": {"bed": 0, "liv": 0}, "temp": 18, "eco": True, "guard": True, "alert": True},
    {"sc": 3, "dark": .45, "lights": {"hall": 1, "kit": .9, "liv": .8}, "blinds": {"bed": 0, "liv": 0}, "temp": 22, "eco": False},
    {"sc": 4, "dark": .78, "lights": {"liv": .7}, "blinds": {"bed": 1, "liv": 1}, "temp": 22, "eco": False, "audio": True},
    {"sc": 5, "dark": .84, "lights": {"hall": .5}, "blinds": {"bed": 1, "liv": 1}, "temp": 20, "eco": False},
]

DAY = {
    "ru": {"eyebrow": "Интерактив", "title": "Один день в квартире Lagmar 46 м²",
           "sub": "Выберите время — и посмотрите, что квартира делает сама. Свет, шторы и климат меняются по сценариям, без единого выключателя.",
           "light": "Свет", "blinds": "Шторы", "climate": "Климат", "open": "открыты", "closed": "закрыты",
           "zones": "{n} из 6 зон", "off": "выключен", "eco": "эко", "guard": "Квартира под охраной датчиков",
           "alert": "Протечка на кухне — вода перекрыта", "alert_sub": "уведомление пришло на телефон",
           "audio": "Музыка в гостиной", "play": "Смотреть день", "pause": "Пауза",
           "plan_alt": "Квартира Lagmar 46 м²: свет и шторы по времени суток", "more": "Все сценарии"},
    "ro": {"eyebrow": "Interactiv", "title": "O zi într-un apartament Lagmar de 46 m²",
           "sub": "Alege ora — și vezi ce face apartamentul singur. Lumina, rulourile și clima se schimbă după scenarii, fără niciun întrerupător.",
           "light": "Lumină", "blinds": "Rulouri", "climate": "Climă", "open": "deschise", "closed": "închise",
           "zones": "{n} din 6 zone", "off": "stinsă", "eco": "eco", "guard": "Senzorii păzesc apartamentul",
           "alert": "Scurgere în bucătărie — apa e oprită", "alert_sub": "notificarea a ajuns pe telefon",
           "audio": "Muzică în living", "play": "Vezi ziua", "pause": "Pauză",
           "plan_alt": "Apartament Lagmar de 46 m²: lumina și rulourile în funcție de oră", "more": "Toate scenariile"},
    "en": {"eyebrow": "Interactive", "title": "One day in a 46 m² Lagmar apartment",
           "sub": "Pick a time and watch what the apartment does on its own. Light, blinds and climate follow scenes — no switches needed.",
           "light": "Light", "blinds": "Blinds", "climate": "Climate", "open": "open", "closed": "closed",
           "zones": "{n} of 6 zones", "off": "off", "eco": "eco", "guard": "Sensors are watching the apartment",
           "alert": "Kitchen leak — water shut off", "alert_sub": "a notification reached your phone",
           "audio": "Music in the living room", "play": "Play the day", "pause": "Pause",
           "plan_alt": "46 m² Lagmar apartment: light and blinds by time of day", "more": "All scenes"},
}

# ---------------------------------------------------------------------------
# Package comparison. Values: "Y" = included, "N" = not included, otherwise text.
CMP = {
    "ru": {"eyebrow": "Сравнение", "title": "Три пакета — одна система, которая растёт вместе с вами",
           "sub": "Начните с Basic и добавляйте модули позже — без замены уже установленного.",
           "size_label": "Квартира", "sizes": {"2": "2 комнаты", "3": "3 комнаты", "4": "4 комнаты"},
           "feature": "Что входит",
           "rows": [
               ("Свет", "группами", "по комнатам + диммирование", "весь свет + декоративная подсветка"),
               ("Панели управления", "Smart Panel + Touch Panel у входа", "в каждой комнате", "во всех зонах"),
               ("Отопление", "термостат + график", "своя температура в каждой зоне", "зоны + контроль CO₂ и влажности"),
               ("Защита от протечки", "датчики + уведомление", "+ автоперекрытие воды", "+ автоперекрытие воды"),
               ("Моторизованные шторы", "N", "2–4 окна", "все окна"),
               ("Датчики движения и дыма", "N", "Y", "Y"),
               ("Сценарии", "«Ухожу», «Я дома»", "+ «Утро», «Ночь», «Отпуск»", "+ «Кино» и личные сцены"),
               ("Приложение myGrenton, работа без интернета", "Y", "Y", "Y"),
           ],
           "price": "Ориентировочно", "price_from": "от {p}",
           "price_note": "Оборудование Grenton и программирование, без НДС. Датчики, приводы штор, аудио и монтаж — в персональном предложении после осмотра квартиры.",
           "cta": "Получить точный расчёт на мою квартиру", "yes": "есть", "no": "нет", "all": "Во всех пакетах"},
    "ro": {"eyebrow": "Comparație", "title": "Trei pachete — un singur sistem care crește odată cu tine",
           "sub": "Începe cu Basic și adaugă module mai târziu — fără a înlocui ce e deja montat.",
           "size_label": "Apartament", "sizes": {"2": "2 camere", "3": "3 camere", "4": "4 camere"},
           "feature": "Ce include",
           "rows": [
               ("Lumină", "pe grupuri", "pe camere + reglaj de intensitate", "toată lumina + iluminat decorativ"),
               ("Panouri de comandă", "Smart Panel + Touch Panel la intrare", "în fiecare cameră", "în toate zonele"),
               ("Încălzire", "termostat + program", "temperatură proprie în fiecare zonă", "zone + control CO₂ și umiditate"),
               ("Protecție la scurgeri", "senzori + notificare", "+ oprirea automată a apei", "+ oprirea automată a apei"),
               ("Rulouri motorizate", "N", "2–4 ferestre", "toate ferestrele"),
               ("Senzori de mișcare și fum", "N", "Y", "Y"),
               ("Scenarii", "„Plec”, „Sunt acasă”", "+ „Dimineața”, „Noaptea”, „Concediu”", "+ „Film” și scene personale"),
               ("Aplicația myGrenton, funcționează fără internet", "Y", "Y", "Y"),
           ],
           "price": "Orientativ", "price_from": "de la {p}",
           "price_note": "Echipamente Grenton și programare, fără TVA. Senzorii, motoarele rulourilor, audio și montajul — în oferta personală după vizita la apartament.",
           "cta": "Primește calculul exact pentru apartamentul meu", "yes": "da", "no": "nu", "all": "În toate pachetele"},
    "en": {"eyebrow": "Compare", "title": "Three packages — one system that grows with you",
           "sub": "Start with Basic and add modules later — nothing installed has to be replaced.",
           "size_label": "Apartment", "sizes": {"2": "2 rooms", "3": "3 rooms", "4": "4 rooms"},
           "feature": "What's included",
           "rows": [
               ("Lighting", "in groups", "per room + dimming", "all lights + accent lighting"),
               ("Control panels", "Smart Panel + Touch Panel at the door", "in every room", "in all zones"),
               ("Heating", "thermostat + schedule", "own temperature in every zone", "zones + CO₂ and humidity control"),
               ("Leak protection", "sensors + notification", "+ automatic water shut-off", "+ automatic water shut-off"),
               ("Motorised blinds", "N", "2–4 windows", "all windows"),
               ("Motion and smoke sensors", "N", "Y", "Y"),
               ("Scenes", "“Leaving”, “I'm home”", "+ “Morning”, “Night”, “Holiday”", "+ “Movie” and personal scenes"),
               ("myGrenton app, works without internet", "Y", "Y", "Y"),
           ],
           "price": "Indicative", "price_from": "from {p}",
           "price_note": "Grenton equipment and programming, excl. VAT. Sensors, blind motors, audio and installation are in your personal offer after we visit the apartment.",
           "cta": "Get an exact quote for my apartment", "yes": "yes", "no": "no", "all": "In every package"},
}

# ---------------------------------------------------------------------------
# Product gallery
GAL = {
    "ru": {"eyebrow": "Продукция Grenton", "title": "То, что вы увидите на стене",
           "sub": "Панели — единственное, что видно в интерьере. Всё остальное спрятано в электрощите.",
           "credit": "Фото и видео: Grenton",
           "items": {
               "panel": ("Smart Panel", "OLED-экран, 4 сенсорные кнопки и датчик температуры. Свет, климат и сценарии с одной панели."),
               "touch": ("Touch Panel", "4 или 8 кнопок с подсветкой и иконками — замена ряду обычных выключателей."),
               "monolith": ("Monolith", "Премиальная линейка из металла: цельная поверхность без видимых кнопок."),
               "multi": ("Multisensor", "Один датчик на потолке: температура, влажность, освещённость, движение и качество воздуха."),
               "clu": ("CLU — мозг системы", "Хранит и выполняет все сценарии прямо в квартире, даже без интернета."),
           },
           "finishes": [("black", "Чёрный"), ("titan", "Титан"), ("silver", "Серебро"), ("gold", "Золото")],
           "finish_label": "Отделки Monolith"},
    "ro": {"eyebrow": "Produse Grenton", "title": "Ce vei vedea pe perete",
           "sub": "Panourile sunt singurul lucru vizibil în interior. Restul stă ascuns în tabloul electric.",
           "credit": "Foto și video: Grenton",
           "items": {
               "panel": ("Smart Panel", "Ecran OLED, 4 butoane tactile și senzor de temperatură. Lumină, climă și scenarii de pe un singur panou."),
               "touch": ("Touch Panel", "4 sau 8 butoane iluminate cu pictograme — în locul unui șir de întrerupătoare."),
               "monolith": ("Monolith", "Linia premium din metal: o suprafață unitară, fără butoane vizibile."),
               "multi": ("Multisensor", "Un singur senzor pe tavan: temperatură, umiditate, lumină, mișcare și calitatea aerului."),
               "clu": ("CLU — creierul sistemului", "Păstrează și rulează toate scenariile chiar în apartament, și fără internet."),
           },
           "finishes": [("black", "Negru"), ("titan", "Titan"), ("silver", "Argintiu"), ("gold", "Auriu")],
           "finish_label": "Finisaje Monolith"},
    "en": {"eyebrow": "Grenton products", "title": "What you'll see on the wall",
           "sub": "Panels are the only part visible in your interior. Everything else is hidden in the switchboard.",
           "credit": "Photos and video: Grenton",
           "items": {
               "panel": ("Smart Panel", "OLED screen, 4 touch buttons and a temperature sensor. Light, climate and scenes from one panel."),
               "touch": ("Touch Panel", "4 or 8 backlit buttons with icons — instead of a row of ordinary switches."),
               "monolith": ("Monolith", "The premium metal line: one seamless surface with no visible buttons."),
               "multi": ("Multisensor", "One ceiling sensor: temperature, humidity, light level, motion and air quality."),
               "clu": ("CLU — the brain", "Stores and runs every scene right in the apartment, even without internet."),
           },
           "finishes": [("black", "Black"), ("titan", "Titanium"), ("silver", "Silver"), ("gold", "Gold")],
           "finish_label": "Monolith finishes"},
}

APP = {
    "ru": {"eyebrow": "Приложение myGrenton", "title": "Вся квартира — в телефоне",
           "text": "Те же сценарии, что на панелях, — из любой точки мира. Приложение показывает, что включено, и присылает уведомления о протечке, дыме и звонке в домофон.",
           "bullets": ["Свет, шторы и температура по комнатам", "Сценарии одной кнопкой: «Ухожу», «Ночь», «Кино»", "Уведомления о протечке и дыме", "Видеодомофон: ответить гостю из офиса"]},
    "ro": {"eyebrow": "Aplicația myGrenton", "title": "Tot apartamentul — în telefon",
           "text": "Aceleași scenarii ca pe panouri — de oriunde în lume. Aplicația arată ce e aprins și trimite notificări despre scurgeri, fum și apeluri la interfon.",
           "bullets": ["Lumină, rulouri și temperatură pe camere", "Scenarii dintr-o atingere: „Plec”, „Noaptea”, „Film”", "Notificări despre scurgeri și fum", "Videointerfon: răspunzi oaspetelui din birou"]},
    "en": {"eyebrow": "myGrenton app", "title": "The whole apartment in your pocket",
           "text": "The same scenes as on the panels — from anywhere in the world. The app shows what's on and sends notifications about leaks, smoke and intercom calls.",
           "bullets": ["Light, blinds and temperature per room", "One-tap scenes: “Leaving”, “Night”, “Movie”", "Leak and smoke notifications", "Video intercom: answer a visitor from the office"]},
}

# Photos for benefit groups / scenes (assets/grenton/*)
FEATURE_PHOTO = {"light": "salon", "climate": "bedroom", "safety": "bath", "blinds": "office",
                 "media": "touch-hero", "control": "touch-wall"}
SCENE_PHOTO = ["bedroom", "hall", "security", "kitchen", "touch-hero", "kids", "app-saving"]

PHOTO_ALT = {
    "ru": {"salon": "Гостиная со сценой света", "bedroom": "Спальня с панелью Grenton", "bath": "Ванная с панелью управления климатом",
           "office": "Кабинет с моторизованными шторами", "touch-hero": "Гостиная с панелями Touch Panel",
           "hallpanels": "Прихожая с панелями Grenton", "hall": "Прихожая", "security": "Уведомление в приложении myGrenton",
           "kids": "Детская комната", "kitchen": "Кухня"},
    "ro": {"salon": "Living cu scenă de lumină", "bedroom": "Dormitor cu panou Grenton", "bath": "Baie cu panou de climă",
           "office": "Birou cu rulouri motorizate", "touch-hero": "Living cu panouri Touch Panel",
           "hallpanels": "Hol cu panouri Grenton", "hall": "Hol", "security": "Notificare în aplicația myGrenton",
           "kids": "Camera copiilor", "kitchen": "Bucătărie"},
    "en": {"salon": "Living room with a lighting scene", "bedroom": "Bedroom with a Grenton panel", "bath": "Bathroom with a climate panel",
           "office": "Study with motorised blinds", "touch-hero": "Living room with Touch Panels",
           "hallpanels": "Hallway with Grenton panels", "hall": "Hallway", "security": "Notification in the myGrenton app",
           "kids": "Children's room", "kitchen": "Kitchen"},
}

# Home hero over video + section copy for the new rhythm
HOME_V3 = {
    "ru": {"video_label": "Интерьеры с панелями Grenton", "out_title": "Что изменится в первую же неделю",
           "lagmar_ref": "Наш объект", "gallery_more": "Как устроена система"},
    "ro": {"video_label": "Interioare cu panouri Grenton", "out_title": "Ce se schimbă din prima săptămână",
           "lagmar_ref": "Proiectul nostru", "gallery_more": "Cum e construit sistemul"},
    "en": {"video_label": "Interiors with Grenton panels", "out_title": "What changes in the very first week",
           "lagmar_ref": "Our project", "gallery_more": "How the system works"},
}
