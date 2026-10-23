// Social share cards (og:image, 1200x630), RO/RU/EN — Lagmar Smart Home first (owner 20.10.2026).
// Run: node scripts/og_cards.mjs   (needs Playwright + ImageMagick `magick`)
// Output: assets/og/og-home-{lang}.jpg (every page but the calculator), assets/og/og-calc-{lang}.jpg (lagmar.html)
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
  latin: b64("assets/fonts/inter-latin.woff2"),
  ext: b64("assets/fonts/inter-latin-ext.woff2"),
  cyr: b64("assets/fonts/inter-cyrillic.woff2"),
};
const AERIAL = "data:image/jpeg;base64," + b64("assets/lagmar/aerial.jpg");
const LOGO = "data:image/png;base64," + b64("assets/lagmar/logo-lagmar.png");
const NAVY = "#19355b", NAVY2 = "#22446f", RED = "#e32213";

const NB = " ";
const T = {
  ro: {
    sub: `Casă inteligentă în fiecare apartament${NB}— unitatea e${NB}deja montată`,
    cta: `Alege și calculează pentru apartamentul tău`,
    loc: "SmartSpace · Chișinău",
    calc: `Calculează casa inteligentă pentru apartamentul tău`,
    zero: `0${NB}€ pentru unitate${NB}— e${NB}deja montată`,
    rooms: `Apartamente cu 2, 3${NB}și 4${NB}camere`,
    rec: "Recomandat",
  },
  ru: {
    sub: `Умный дом в${NB}каждой квартире${NB}— контроллер уже установлен`,
    cta: `Подберите и${NB}рассчитайте для своей квартиры`,
    loc: "SmartSpace · Кишинёв",
    calc: `Рассчитайте умный дом для своей квартиры`,
    zero: `0${NB}€ за${NB}контроллер${NB}— он${NB}уже стоит`,
    rooms: `Квартиры на${NB}2, 3 и${NB}4${NB}комнаты`,
    rec: "Рекомендуем",
  },
  en: {
    sub: `A smart home in every apartment${NB}— the controller is already in`,
    cta: `Choose and price it for your apartment`,
    loc: "SmartSpace · Chișinău",
    calc: `Price a smart home for your apartment`,
    zero: `0${NB}€ for the controller${NB}— already installed`,
    rooms: `2, 3 and 4-room apartments`,
    rec: "Recommended",
  },
};

const base = `
@font-face{font-family:M;font-weight:400 700;src:url(data:font/woff2;base64,${FONT.cyr}) format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}
@font-face{font-family:M;font-weight:400 700;src:url(data:font/woff2;base64,${FONT.ext}) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+2020,U+20A0-20AB,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:M;font-weight:400 700;src:url(data:font/woff2;base64,${FONT.latin}) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+20AC,U+2122,U+2212}
*{margin:0;padding:0;box-sizing:border-box}
.card{width:1200px;height:630px;position:relative;overflow:hidden;font-family:M,sans-serif;color:#fff;background:${NAVY}}
.chip{position:absolute;top:56px;left:72px;display:flex;align-items:center;gap:14px;background:#fff;color:${NAVY2};
  border-radius:16px;padding:12px 20px;box-shadow:0 10px 30px -12px rgba(0,0,0,.5)}
.chip img{height:40px;width:auto;display:block}
.chip .x{font-weight:700;color:#8a95a8;font-size:20px}
.chip .gr{font-weight:700;font-size:24px;letter-spacing:-.02em}
.foot{position:absolute;left:72px;bottom:56px;display:flex;align-items:center;gap:16px}
.foot b{width:4px;height:44px;background:${RED};border-radius:2px}
.foot .cta{font-size:24px;font-weight:700;letter-spacing:-.01em}
.foot .loc{font-size:16px;font-weight:500;color:rgba(255,255,255,.66);letter-spacing:.04em;margin-top:3px}
h1,h2{text-wrap:balance}
`;

const chip = `<div class="chip"><img src="${LOGO}"><span class="x">×</span><span class="gr">SmartSpace</span></div>`;

const home = (t) => `<!doctype html><meta charset="utf-8"><style>${base}
.ph{position:absolute;top:0;right:0;width:620px;height:630px;overflow:hidden}
.photo{position:absolute;top:0;right:0;width:620px;height:630px;object-fit:cover;object-position:40% 50%;transform:scale(1.32);transform-origin:62% 8%}
.fade{position:absolute;top:0;right:0;width:620px;height:630px;background:linear-gradient(90deg,${NAVY} 0%,rgba(20,42,75,.55) 30%,rgba(20,42,75,0) 62%)}
h1{position:absolute;left:68px;top:170px;width:640px;font-size:88px;font-weight:700;letter-spacing:-.035em;line-height:1}
h2{position:absolute;left:72px;top:368px;width:600px;font-size:31px;font-weight:700;line-height:1.25;color:rgba(255,255,255,.92)}
</style><div class="card"><div class="ph"><img class="photo" src="${AERIAL}"><div class="fade"></div></div>${chip}
<h1>Lagmar Smart${NB}Home</h1><h2>${t.sub}</h2>
<div class="foot"><b></b><div><div class="cta">${t.cta}</div><div class="loc">${t.loc}</div></div></div></div>`;

const calc = (t) => `<!doctype html><meta charset="utf-8"><style>${base}
.card{background:radial-gradient(760px 520px at 100% 0%, ${NAVY2} 0%, transparent 70%), ${NAVY}}
.col{position:absolute;left:72px;top:160px;width:650px;display:flex;flex-direction:column;align-items:flex-start;gap:26px}
.col h1{margin-left:-4px;font-size:60px;font-weight:700;letter-spacing:-.03em;line-height:1.06}
.zero{display:inline-flex;align-items:center;gap:10px;font-size:22px;font-weight:700;
  background:rgba(139,224,173,.14);color:#a6ecc2;border:1px solid rgba(139,224,173,.35);border-radius:999px;padding:10px 18px}
.zero i{width:10px;height:10px;border-radius:50%;background:#8be0ad}
.rooms{margin-top:-12px;font-size:19px;font-weight:500;color:rgba(255,255,255,.66)}
.tiers{position:absolute;right:72px;top:150px;width:330px;display:flex;flex-direction:column;gap:16px}
.tier{border:1px solid rgba(255,255,255,.18);border-radius:16px;padding:22px 26px;font-size:28px;font-weight:700;
  display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.04)}
.tier.rec{border-color:${RED};background:rgba(227,34,19,.16)}
.tier span{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#fff;background:${RED};border-radius:999px;padding:6px 11px}
</style><div class="card">${chip}
<div class="col"><h1>${t.calc}</h1><div class="zero"><i></i>${t.zero}</div><div class="rooms">${t.rooms}</div></div>
<div class="tiers"><div class="tier">Basic</div><div class="tier rec">Comfort<span>${t.rec}</span></div><div class="tier">Premium</div></div>
<div class="foot"><b></b><div><div class="cta">Lagmar Smart Home</div><div class="loc">${t.loc}</div></div></div></div>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 2 });
for (const lang of Object.keys(T)) {
  for (const [name, tpl] of [["home", home], ["calc", calc]]) {
    await page.setContent(tpl(T[lang]), { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    const bad = await page.evaluate(() => {
      const box = (s) => document.querySelector(s)?.getBoundingClientRect();
      const out = [...document.querySelectorAll(".chip,h1,h2,.zero,.rooms,.tiers,.foot")].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.right > 1200 - 40 || r.bottom > 630 - 28;
      }).map((e) => e.className || e.tagName);
      // text column must not run into the right-hand visual
      const t = box(".tiers"), h = box("h1");
      if (t && h && h.right > t.left - 24) out.push("h1-into-tiers");
      const z = box(".zero"), r = box(".rooms"), f = box(".foot"), h2 = box("h2");
      if (z && h && z.top < h.bottom + 16) out.push("zero-into-h1");
      if (r && f && r.bottom > f.top - 16) out.push("rooms-into-foot");
      if (h2 && h && h2.top < h.bottom + 12) out.push("h2-into-h1");
      if (h2 && f && h2.bottom > f.top - 16) out.push("h2-into-foot");
      return out;
    });
    if (bad.length) throw new Error(`${name}-${lang}: layout problem: ${bad}`);
    const png = path.join(OUT, `og-${name}-${lang}.png`);
    await page.locator(".card").screenshot({ path: png });
    const jpg = png.replace(/\.png$/, ".jpg");
    execFileSync("magick", [png, "-resize", "1200x630", "-strip", "-quality", "84", jpg]);
    fs.unlinkSync(png);
    console.log("rendered", path.relative(ROOT, jpg), fs.statSync(jpg).size, "bytes");
  }
}
await browser.close();
