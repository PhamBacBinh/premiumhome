import asyncio, re, json
from playwright.async_api import async_playwright
B='http://127.0.0.1:8765'
PAGES=['/','/dich-vu/','/giup-viec-gia-dinh/','/bao-mau-cham-be/','/cham-soc-nguoi-gia/','/quan-gia/','/dau-bep-gia-dinh/','/ho-tro-ngan-han/','/tuyen-dung/','/cam-nang/','/thue-giup-viec-2026/','/gia-thue-giup-viec-ha-noi/','/kinh-nghiem-thue-bao-mau/','/thue-nguoi-cham-soc-nguoi-gia/','/giup-viec-o-lai-hay-theo-gio/','/hiring-helper-hanoi-expat-guide/','/en/','/quan-tri/','/khong-ton-tai']
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        seen=set(); bad=[]
        for path in PAGES:
            pg=await b.new_page(viewport={'width':390,'height':844})
            errs=[]; fails=[]
            pg.on('pageerror',lambda e: errs.append(str(e)))
            pg.on('console',lambda m: errs.append('console:'+m.text) if m.type=='error' else None)
            pg.on('response',lambda r: fails.append(f'{r.status} {r.url}') if r.status>=400 and '127.0.0.1' in r.url and 'khong-ton-tai' not in r.url else None)
            await pg.goto(B+path, wait_until='networkidle')
            h1=(await pg.locator('h1').first.inner_text()) if await pg.locator('h1').count() else ''
            n_h1=await pg.locator('h1').count()
            lds=await pg.eval_on_selector_all('script[type="application/ld+json"]','e=>e.map(x=>x.textContent)')
            for t in lds: json.loads(t)
            links=await pg.eval_on_selector_all('a[href]','e=>e.map(a=>a.getAttribute("href"))')
            for l in links:
                if l.startswith('/') and not l.startswith('//'): seen.add(l.split('#')[0] or '/')
            # open form if exists
            ok_form=''
            if await pg.locator("main [data-open=\"khach\"]:visible").count():
                await pg.locator("main [data-open=\"khach\"]:visible").first.click(); await pg.wait_for_timeout(400)
                ok_form = 'form-open' if await pg.locator('#dlg-khach[open]').count() else 'FORM-FAIL'
            print(f'{path:24} h1x{n_h1} ld{len(lds)} {ok_form} | {h1[:60]!r} | err={errs[:2]} fail={fails[:3]}')
            await pg.close()
        # check internal links
        for l in sorted(x for x in seen if not x.endswith(".docx")):
            pg=await b.new_page(); r=await pg.goto(B+l); 
            if r.status!=200: bad.append((l,r.status))
            await pg.close()
        print('internal links', len(seen), 'bad', bad)
        await b.close()
asyncio.run(main())
