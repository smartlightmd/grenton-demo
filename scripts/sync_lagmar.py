"""Sync apartments of Lagmar Smart Home 1 and Smart Home 2 from the lagmar.md data source (our project).

Source: the public get-apartments function lagmar.md itself uses (profitbase cache), one call per project.
Writes assets/data/apts-sh1.json and apts-sh2.json:
  [{"b": block, "n": number as on lagmar.md (P101, 507), "f": floor (0 = ground), "r": rooms, "a": m2, "p": plan id}]
The plan image is PLAN_URL + p + ".jpg" (every apartment has its own plan). Run: python scripts/sync_lagmar.py
"""
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://rysffqfskegppczifyjd.supabase.co/functions/v1/get-apartments?projectId={}"
PLAN_URL = "https://pb21648.profitbase.ru/uploads/preset/21648/"
PROJECTS = {"sh1": "57386", "sh2": "57421"}


def fetch(pid):
    req = urllib.request.Request(API.format(pid), headers={"User-Agent": "SmartSpace-sync/1.0"})
    j = json.loads(urllib.request.urlopen(req, timeout=60).read())
    return j["data"]["data"]


def compact(rows):
    out = []
    for x in rows:
        if x.get("typePurpose") not in (None, "residential"):
            continue
        preset = x.get("preset") or ""
        pid = preset[len(PLAN_URL):-4] if preset.startswith(PLAN_URL) and preset.endswith(".jpg") else ""
        out.append({"b": (x.get("houseName") or "").strip().upper(), "n": (x.get("number") or "").replace(" ", "").upper(),
                    "f": int(x.get("floor") or 0), "r": int(x.get("rooms_amount") or 0),
                    "a": round(float((x.get("area") or {}).get("area_total") or 0), 2), "p": pid})
    out = [x for x in out if x["b"] and x["n"]]
    out.sort(key=lambda x: (x["b"], x["f"], x["n"]))
    return out


def main():
    for key, pid in PROJECTS.items():
        rows = compact(fetch(pid))
        assert len(rows) > 500, (key, len(rows))
        dupes = len(rows) - len({(x["b"], x["n"]) for x in rows})
        path = os.path.join(ROOT, "assets", "data", f"apts-{key}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, separators=(",", ":"))
        blocks = sorted({x["b"] for x in rows})
        print(f"{key}: {len(rows)} apartments, blocks {''.join(blocks)}, with plan {sum(1 for x in rows if x['p'])}, "
              f"duplicate numbers {dupes}, {os.path.getsize(path) // 1024} KB")


if __name__ == "__main__":
    sys.exit(main())
