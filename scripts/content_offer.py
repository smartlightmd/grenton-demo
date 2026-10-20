"""Lagmar package offer model (14.10.2026): one exact spec per package -> features, bill of materials, price.

Everything shown on the site (what is included, which devices, how many, unit price, total) is derived
from PACKAGE_SPEC by build_bom(), so the three can never drift apart.

Unit prices: SmartSpace selling prices, EUR excl. VAT.
  * Grenton modules and panels — our 2025 quote (Casa Doni, «Automatizare - Grenton.pdf»).
  * Sensors / valve — see SENSOR_PRICES (source noted per item; None = priced in the personal offer).
Programming & commissioning: 30 % of equipment (2025 quote: 2 150 € on 7 761 € of devices ≈ 28 %).

Pre-installed by Lagmar (owner, 20.10.2026): every apartment already has a CLU, a 24 V power supply and a
2-channel relay in the panel. The resident does not pay for them; we connect and program them, so the
programming share is taken on the whole system, pre-installed CLU + PSU included.
"""
import math

UNIT = {  # code: (price EUR, article)
    "CLU": (295, "CLU-300-E-00"),
    "PSU": (51, "PSU-241-2-01"),
    "R4": (115, "Relay x4, DIN, TF-Bus"),
    "R2": (None, "Relay x2, DIN, TF-Bus"),  # only ever pre-installed by Lagmar
    "DIM": (105, "Dimmer, DIN, TF-Bus"),
    "RGBW": (115, "LED RGBW, DIN, TF-Bus"),
    "RS": (155, "Roller Shutter, DIN, TF-Bus"),
    "IO": (230, "I/O 8/8, DIN, TF-Bus"),
    "SP": (230, "Smart Panel, OLED, TF-Bus"),
    "TP4": (125, "Touch Panel 4B, TF-Bus"),
    "TP8": (135, "Touch Panel 8B, TF-Bus"),
}
# Sensors and the water valve are not in the 2025 quote; None means "in the personal offer".
SENSOR_PRICES = {"LEAK": None, "VALVE": None, "SMOKE": None, "MOTION": None, "MULTI": None}
PROGRAMMING_SHARE = 0.30
PREINSTALLED = [("CLU", 1), ("PSU", 1), ("R2", 1)]  # in every Lagmar apartment, paid by the developer
PRE_RELAY_CH = 2

# l = on/off light groups, d = dimmable groups, led = LED-strip zones, s = switched sockets,
# b = motorised blinds, h = heating zones, sp/tp4/tp8 = panels, leak/valve/smoke/motion/multi = sensors
PACKAGE_SPEC = {
    "2": {
        "basic":   dict(l=5, d=0, led=0, s=2, b=0, h=1, sp=1, tp4=1, tp8=0, leak=2, valve=0, smoke=0, motion=0, multi=0),
        "comfort": dict(l=5, d=2, led=0, s=4, b=2, h=2, sp=1, tp4=3, tp8=0, leak=2, valve=1, smoke=1, motion=1, multi=0),
        "premium": dict(l=6, d=3, led=2, s=6, b=3, h=2, sp=2, tp4=2, tp8=1, leak=2, valve=1, smoke=1, motion=2, multi=1),
    },
    "3": {
        "basic":   dict(l=7, d=0, led=0, s=3, b=0, h=1, sp=1, tp4=2, tp8=0, leak=2, valve=0, smoke=0, motion=0, multi=0),
        "comfort": dict(l=7, d=3, led=0, s=6, b=3, h=3, sp=1, tp4=4, tp8=0, leak=2, valve=1, smoke=1, motion=2, multi=0),
        "premium": dict(l=8, d=4, led=3, s=8, b=4, h=3, sp=2, tp4=3, tp8=1, leak=3, valve=1, smoke=2, motion=2, multi=1),
    },
    "4": {
        "basic":   dict(l=9, d=0, led=0, s=4, b=0, h=2, sp=1, tp4=2, tp8=0, leak=3, valve=0, smoke=0, motion=0, multi=0),
        "comfort": dict(l=9, d=4, led=0, s=8, b=4, h=4, sp=1, tp4=5, tp8=0, leak=3, valve=1, smoke=2, motion=2, multi=0),
        "premium": dict(l=10, d=5, led=4, s=10, b=5, h=4, sp=3, tp4=4, tp8=1, leak=3, valve=1, smoke=2, motion=3, multi=2),
    },
}


def build_bom(spec):
    """Spec -> list of (code, qty) we supply on top of the Lagmar pre-install. Channel rules follow how we size
    Grenton cabinets; the pre-installed relay covers the first 2 switched channels, the pre-installed PSU the first 24."""
    relay_ch = spec["l"] + spec["s"] + spec["valve"]
    io_in = spec["leak"] + spec["smoke"] + spec["motion"]
    io_out = spec["h"]
    psu_need = 1 if relay_ch + spec["d"] + spec["b"] <= 24 else 2
    bom = [("PSU", psu_need - 1),
           ("R4", math.ceil(max(0, relay_ch - PRE_RELAY_CH) / 4)),
           ("DIM", spec["d"]),
           ("RGBW", math.ceil(spec["led"] / 4)),
           ("RS", math.ceil(spec["b"] / 3)),
           ("IO", max(math.ceil(io_in / 8), math.ceil(io_out / 8)) if (io_in or io_out) else 0),
           ("SP", spec["sp"]), ("TP4", spec["tp4"]), ("TP8", spec["tp8"]),
           ("LEAK", spec["leak"]), ("VALVE", spec["valve"]), ("SMOKE", spec["smoke"]),
           ("MOTION", spec["motion"]), ("MULTI", spec["multi"])]
    return [(c, q) for c, q in bom if q]


def unit_price(code):
    return UNIT[code][0] if code in UNIT else SENSOR_PRICES.get(code)


def price_package(spec):
    bom = build_bom(spec)
    priced = [(c, q, unit_price(c)) for c, q in bom]
    equipment = sum(q * p for _c, q, p in priced if p is not None)
    pre_value = sum(q * unit_price(c) for c, q in PREINSTALLED if unit_price(c) is not None)
    programming = int(math.ceil((equipment + pre_value) * PROGRAMMING_SHARE / 10.0) * 10)
    total = equipment + programming
    unpriced = [c for c, _q, p in priced if p is None]
    return {"bom": priced, "pre": PREINSTALLED, "pre_value": pre_value, "equipment": equipment,
            "programming": programming, "total": total, "unpriced": unpriced}


OFFER = {n: {t: price_package(s) for t, s in tiers.items()} for n, tiers in PACKAGE_SPEC.items()}
PRICES = {n: {t: OFFER[n][t]["total"] for t in tiers} for n, tiers in OFFER.items()}
EQUIPMENT = {n: {t: OFFER[n][t]["equipment"] for t in tiers} for n, tiers in OFFER.items()}  # promo base

if __name__ == "__main__":
    for n in OFFER:
        for t in OFFER[n]:
            o = OFFER[n][t]
            print(n, t, o["equipment"], o["programming"], o["total"], o["unpriced"], [(c, q) for c, q, _p in o["bom"]])
