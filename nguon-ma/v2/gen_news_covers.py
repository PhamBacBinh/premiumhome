"""Ảnh bìa bản tin: python3 gen_news_covers.py -> site/assets/img/ban-tin-<no>-{640,1200}.webp"""
import os, sys, asyncio
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from news import POSTS
from playwright.async_api import async_playwright
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, '..', '..', 'tools', 'node_modules', '@fontsource')
def ff(fam, file, w, name):
    p = os.path.join(FONTS, fam, 'files', file)
    return f"@font-face{{font-family:{name};font-weight:{w};src:url(file://{p}) format('woff2')}}"
CSS = ''.join([ff('be-vietnam-pro','be-vietnam-pro-vietnamese-800-normal.woff2',800,'BVX'), ff('be-vietnam-pro','be-vietnam-pro-latin-800-normal.woff2',800,'BVX'),
               ff('be-vietnam-pro','be-vietnam-pro-vietnamese-700-normal.woff2',700,'BVB'), ff('be-vietnam-pro','be-vietnam-pro-latin-700-normal.woff2',700,'BVB')])
TONE = {'green': ('#1F342E', '#E8C981', '#FBF6EC'), 'gold': ('#F6F1E7', '#8A6420', '#14261F'), 'warn': ('#12241E', '#FF8A78', '#FBF6EC')}
LOGO = os.path.join(HERE, 'site', 'assets', 'img', 'arch-mark-dark.svg')
def page(p):
    c = p['cover']; bg, ac, fg = TONE[c['tone']]
    return f'''<html><head><meta charset="utf-8"><style>{CSS}
*{{margin:0;box-sizing:border-box}} body{{width:1200px;height:675px;background:{bg};position:relative;overflow:hidden;font-family:BVB}}
.arch{{position:absolute;right:-90px;top:70px;width:520px;height:760px;border:3px solid {ac}55;border-bottom:none;border-radius:999px 999px 0 0}}
.arch2{{position:absolute;right:-20px;top:150px;width:380px;height:700px;border:2px solid {ac}33;border-bottom:none;border-radius:999px 999px 0 0}}
.tag{{position:absolute;left:70px;top:62px;font-size:22px;letter-spacing:.2em;color:{ac}}}
.mid{{position:absolute;left:66px;top:140px;right:200px;display:flex;flex-direction:column;gap:26px}}
.big{{font-family:BVX;font-weight:800;font-size:{'124' if len(c['big'])<14 else '96'}px;line-height:1.02;color:{ac};letter-spacing:-.02em;white-space:nowrap}}
.lb{{width:760px;font-size:36px;line-height:1.35;color:{fg};padding-left:4px}}
.nt{{position:absolute;left:70px;bottom:58px;font-size:22px;letter-spacing:.06em;color:{fg};opacity:.75}}
.br{{position:absolute;right:56px;bottom:44px;display:flex;align-items:center;gap:12px;background:#F6F1E7;border:2px solid #CBAB6D;border-radius:14px;padding:8px 18px 8px 12px;font-family:BVX;font-size:26px;letter-spacing:.06em;color:#14261F}}
.br img{{height:52px}}
</style></head><body><div class="arch"></div><div class="arch2"></div>
<div class="tag">BẢN TIN NGƯỜI LAO ĐỘNG · BÀI {p['no']}</div><div class="mid"><div class="big">{c['big']}</div><div class="lb">{c['label']}</div></div>
<div class="nt">{c['note']}</div><div class="br"><img src="file://{LOGO}">ELITE HELPERS</div></body></html>'''
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={'width':1200,'height':675})
        for p in POSTS:
            out = os.path.join(HERE, 'site', 'assets', 'img', f"ban-tin-{p['no']}")
            if os.path.exists(out + '-1200.webp') and '--force' not in sys.argv: continue
            tmp = os.path.join(HERE, '_cover.html'); open(tmp, 'w', encoding='utf-8').write(page(p)); await pg.goto('file://' + tmp); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=out + '.png')
            im = Image.open(out + '.png').convert('RGB')
            im.save(out + '-1200.webp', quality=86); im.resize((640, 360), Image.LANCZOS).save(out + '-640.webp', quality=84)
            os.remove(out + '.png'); os.remove(tmp); print('cover', p['no'])
        await b.close()
asyncio.run(main())
