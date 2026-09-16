// Social share cards (og:image, 1200x630) for the Grenton demo, RO/RU/EN.
// Run: node scripts/og_cards.mjs   (needs Playwright + ImageMagick `magick`)
// Output: assets/og/og-grenton-{lang}.jpg, assets/og/og-lagmar-{lang}.jpg
import fs from "fs";
import path from "path";
import { execFileSync } from "child_process";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_PATH || "playwright");

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const OUT = path.join(ROOT, "assets/og");
fs.mkdirSync(OUT, { recursive: true });

const b64 = (p) => fs.readFileSync(path.join(ROOT, p)).toString("base64");
const FONT = {
  latin: b64("assets/fonts/manrope-latin.woff2"),
  ext: b64("assets/fonts/manrope-latin-ext.woff2"),
  cyr: b64("assets/fonts/manrope-cyrillic.woff2"),
};
const CLU = "data:image/jpeg;base64," + b64("assets/img/clu.jpg");
const ACCENT = "#ed0f40";

const T = {
  ro: {
    rep: "Reprezentant oficial Grenton",
    home: "Casa ta, controlată dintr-un singur loc",
    loc: "Chișinău · Moldova",
    cfg: "Configurator Grenton",
    lagmar: "Casă inteligentă pentru apartamentul tău",
    rooms: "Apartamente cu 2, 3 și 4 camere",
    rec: "Recomandat",
  },
  ru: {
    rep: "Официальный представитель Grenton",
    home: "Ваш дом — под управлением из одной точки",
    loc: "Кишинёв · Молдова",
    cfg: "Конфигуратор Grenton",
    lagmar: "Умный дом для вашей квартиры",
    rooms: "Квартиры на 2, 3 и 4 комнаты",
    rec: "Рекомендуем",
  },
  en: {
    rep: "Official Grenton representative",
    home: "Your home, controlled from one place",
    loc: "Chișinău · Moldova",
    cfg: "Grenton configurator",
    lagmar: "Smart home for your apartment",
    rooms: "2, 3 and 4-room apartments",
    rec: "Recommended",
  },
};

const base = `
@font-face{font-family:M;font-weight:500 800;src:url(data:font/woff2;base64,${FONT.cyr}) format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}
@font-face{font-family:M;font-weight:500 800;src:url(data:font/woff2;base64,${FONT.ext}) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+2020,U+20A0-20AB,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:M;font-weight:500 800;src:url(data:font/woff2;base64,${FONT.latin}) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+20AC,U+2122,U+2212}
*{margin:0;padding:0;box-sizing:border-box}
.card{width:1200px;height:630px;position:relative;overflow:hidden;font-family:M,sans-serif;color:#fff;
  background:radial-gradient(900px 520px at 8% 110%, ${ACCENT}2e 0%, transparent 60%), #111827}
.eyebrow{position:absolute;top:64px;left:72px;display:flex;align-items:center;gap:12px;
  font-size:15px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.72)}
.eyebrow i{width:8px;height:8px;border-radius:50%;background:${ACCENT}}
.foot{position:absolute;left:72px;bottom:62px;display:flex;align-items:center;gap:16px}
.foot b{width:4px;height:44px;background:${ACCENT};border-radius:2px}
.foot .who{font-size:24px;font-weight:800;letter-spacing:-.01em}
.foot .loc{font-size:15px;font-weight:500;color:rgba(255,255,255,.6);letter-spacing:.06em;margin-top:2px}
`;

const grenton = (t) => `<!doctype html><meta charset="utf-8"><style>${base}
.photo{position:absolute;top:0;right:0;width:450px;height:630px;object-fit:contain;background:#fff;padding:40px 30px}
.wm{position:absolute;left:68px;top:150px;font-size:104px;font-weight:800;letter-spacing:-.035em;line-height:1}
.h{position:absolute;left:72px;top:282px;width:580px;font-size:36px;font-weight:700;line-height:1.22;letter-spacing:-.01em;color:rgba(255,255,255,.92)}
</style><div class="card"><img class="photo" src="${CLU}">
<div class="eyebrow"><i></i>${t.rep}</div><div class="wm">Grenton</div><div class="h">${t.home}</div>
<div class="foot"><b></b><div><div class="who">SmartSpace</div><div class="loc">${t.loc}</div></div></div></div>`;

const lagmar = (t) => `<!doctype html><meta charset="utf-8"><style>${base}
.wm{position:absolute;left:68px;top:148px;width:640px;font-size:74px;font-weight:800;letter-spacing:-.03em;line-height:1.02}
.h{position:absolute;left:72px;top:332px;width:600px;font-size:32px;font-weight:700;line-height:1.24;color:rgba(255,255,255,.92)}
.rooms{position:absolute;left:72px;top:420px;font-size:19px;font-weight:500;color:rgba(255,255,255,.62)}
.tiers{position:absolute;right:72px;top:150px;width:330px;display:flex;flex-direction:column;gap:16px}
.tier{border:1px solid rgba(255,255,255,.16);border-radius:16px;padding:22px 26px;font-size:28px;font-weight:800;
  display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.03)}
.tier.rec{border-color:${ACCENT};background:${ACCENT}1f}
.tier span{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#fff;background:${ACCENT};border-radius:999px;padding:6px 11px}
</style><div class="card">
<div class="eyebrow"><i></i>${t.cfg}</div><div class="wm">Lagmar Smart Home</div><div class="h">${t.lagmar}</div><div class="rooms">${t.rooms}</div>
<div class="tiers"><div class="tier">Basic</div><div class="tier rec">Comfort<span>${t.rec}</span></div><div class="tier">Premium</div></div>
<div class="foot"><b></b><div><div class="who">SmartSpace</div><div class="loc">${t.loc}</div></div></div></div>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 2 });
for (const lang of Object.keys(T)) {
  for (const [name, tpl] of [["grenton", grenton], ["lagmar", lagmar]]) {
    await page.setContent(tpl(T[lang]), { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    const overflow = await page.evaluate(() =>
      [...document.querySelectorAll(".wm,.h,.rooms,.tiers,.foot,.eyebrow")].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.right > 1200 - 40 || r.bottom > 630 - 30;
      }).map((e) => e.className));
    if (overflow.length) throw new Error(`${name}-${lang}: element outside safe area: ${overflow}`);
    const png = path.join(OUT, `og-${name}-${lang}.png`);
    await page.locator(".card").screenshot({ path: png });
    const jpg = png.replace(/\.png$/, ".jpg");
    execFileSync("magick", [png, "-resize", "1200x630", "-strip", "-quality", "84", jpg]);
    fs.unlinkSync(png);
    console.log("rendered", path.relative(ROOT, jpg), fs.statSync(jpg).size, "bytes");
  }
}
await browser.close();
