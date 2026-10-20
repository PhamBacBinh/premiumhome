# -*- coding: utf-8 -*-
"""Build giupviecelite.vn v2: subpages, JSON-LD, llms.txt, sitemap, flat dist/."""
import os, re, json, shutil, html, hashlib
from bs4 import BeautifulSoup
from content import SERVICES, SVC, PROCESS, SITE
import pages_extra as X

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'site')
GEN = os.path.join(ROOT, 'gen')          # generated pages (structured paths)
DIST = os.path.join(ROOT, 'dist')        # flat output for GitHub upload
TODAY = '2026-10-19'
VER = '20261020d'
E = html.escape

home = open(os.path.join(SRC, 'index.html'), encoding='utf-8').read()

# ---------------- shared chunks from home ----------------
body_start = home.index('<body>') + len('<body>')
header_end = home.index('</header>') + len('</header>')
TOP = home[body_start:header_end]
foot_start = home.index('<!-- ===================== FOOTER')
BOTTOM = home[foot_start:home.index('</body>')]
POLICY = home[home.index('<!-- ===================== CHÍNH SÁCH'):home.index('</main>')]
HEAD_COMMON = '''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#1F342E">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="assets/fonts/be-vietnam-pro-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/be-vietnam-pro-vietnamese-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/app.css?v=%s">
<script>document.documentElement.classList.replace('no-js','js');if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('js-motion');</script>''' % VER

def sub_anchors(chunk):
    """Section anchors of the home page -> absolute (/#x) for subpages."""
    for a in ['dich-vu', 'doi-tuong', 'cam-ket', 'quy-trinh', 'hoi-dap', 've-chung-toi']:
        chunk = chunk.replace(f'href="#{a}"', f'href="/#{a}"')
    chunk = chunk.replace('href="#top" class="flex items-center gap-3"', 'href="/" class="flex items-center gap-3"')
    chunk = chunk.replace('aria-label="Elite Helpers, về đầu trang"', 'aria-label="Elite Helpers, về trang chủ"')
    chunk = chunk.replace(' data-spy>', '>')
    return chunk

TOP_SUB = sub_anchors(TOP)
BOTTOM_SUB = sub_anchors(BOTTOM)

ORG_ID = SITE + '/#org'
LOGO = SITE + '/logo-square-512.png'
OG = SITE + '/og-giup-viec-elite.jpg'

ORG_MIN = {'@type': ['EmploymentAgency', 'LocalBusiness'], '@id': ORG_ID, 'name': 'Elite Helpers', 'alternateName': 'Giúp việc Elite',
           'description': 'Dịch vụ kết nối người giúp việc, bảo mẫu, chăm sóc người già, quản gia, đầu bếp gia đình cao cấp tại Hà Nội.',
           'url': SITE + '/', 'logo': SITE + '/logo-square-512.png', 'image': SITE + '/og-giup-viec-elite.jpg',
           'telephone': '+84948919598', 'email': 'lienhe@giupviecelite.vn', 'priceRange': '$$',
           'address': {'@type': 'PostalAddress', 'addressLocality': 'Hà Nội', 'addressRegion': 'Hà Nội', 'addressCountry': 'VN'},
           'areaServed': {'@type': 'City', 'name': 'Hà Nội'},
           'sameAs': ['https://www.facebook.com/EliteHelpersVN']}
WEBSITE_MIN = {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'Elite Helpers', 'alternateName': 'Giúp việc Elite', 'publisher': {'@id': ORG_ID}}

def with_org(ld):
    ids = {n.get('@id') for n in ld.get('@graph', [])}
    if ORG_ID not in ids: ld['@graph'].append(ORG_MIN)
    if SITE + '/#website' not in ids: ld['@graph'].append(WEBSITE_MIN)
    return ld

def head(title, desc, path, lang='vi', alt=None, ld=None, og_type='website', og=None, og_alt=None):
    url = SITE + path
    og = og or OG
    alts = ''
    if alt:
        for hl, href in alt:
            alts += f'<link rel="alternate" hreflang="{hl}" href="{SITE + href}">\n'
    ldj = ''
    if ld:
        ld = with_org(ld)
        ldj = '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, separators=(',', ':')) + '\n</script>'
    return f'''<!doctype html>
<html lang="{lang}" class="no-js">
<head>
{HEAD_COMMON}
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
{alts}<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="{'vi_VN' if lang == 'vi' else 'en_US'}">
<meta property="og:site_name" content="Elite Helpers">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{E(og_alt or title)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og}">
{ldj}
</head>
<body>'''

def page(title, desc, path, main, ld=None, lang='vi', alt=None, og_type='website', top=None, bottom=None, og=None, og_alt=None):
    return (head(title, desc, path, lang, alt, ld, og_type, og, og_alt) + (top or TOP_SUB) +
            '\n<main id="noi-dung">\n' + main + '\n' + (POLICY if lang == 'vi' else '') + '\n</main>\n\n' + (bottom or BOTTOM_SUB) + '</body>\n</html>\n')

def crumbs_html(items):
    out = []
    for i, (name, href) in enumerate(items):
        if i: out.append('<span aria-hidden="true">/</span>')
        out.append(f'<a href="{href}">{E(name)}</a>' if href else f'<span aria-current="page">{E(name)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + ''.join(out) + '</nav>'

def crumbs_ld(items, path):
    return {'@type': 'BreadcrumbList', '@id': SITE + path + '#breadcrumb', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + (h if h else path)} for i, (n, h) in enumerate(items)]}

def faq_ld(items, path):
    return {'@type': 'FAQPage', '@id': SITE + path + '#faq', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub('<[^>]+>', '', a)}} for q, a in items]}

def faq_html(items, gid='faq'):
    return '\n'.join(f'''      <details name="{gid}">
        <summary><span>{E(q)}</span><span class="pm" aria-hidden="true"></span></summary>
        <div class="ans"><p>{a}</p></div>
      </details>''' for q, a in items)

def li(items):
    return '\n'.join(f'<li>{E(x)}</li>' for x in items)

def cta_block(service=None, h='Cần tìm người phù hợp cho gia đình?', p='Gửi yêu cầu trong 2 phút, Elite Helpers liên hệ lại trong ngày làm việc. Tư vấn miễn phí.'):
    ds = f' data-service="{E(service)}"' if service else ''
    return f'''<section class="on-dark bg-lacquer py-20 text-paper lg:py-24" aria-labelledby="cta-title">
  <div class="shell">
    <h2 id="cta-title" class="t-h2" style="max-width:22ch">{h}</h2>
    <p class="mt-4 max-w-[52ch] text-mist">{p}</p>
    <div class="mt-8 flex flex-wrap gap-3">
      <a class="btn btn-brass" href="#tim-nguoi" data-open="khach"{ds}>Gửi yêu cầu tư vấn</a>
      <a class="btn btn-ghost-light" href="https://zalo.me/0948919598" target="_blank" rel="noopener" data-track="zalo">Nhắn Zalo 0948 919 598</a>
    </div>
  </div>
</section>'''

def salary_ld(s):
    nums = [int(x) for x in re.findall(r'(\d+)–(\d+) triệu', s.get('salary', '')) for x in x]
    if not nums: return {}
    lo, hi = min(nums) * 1000000, max(nums) * 1000000
    return {'offers': {'@type': 'Offer', 'priceCurrency': 'VND', 'priceSpecification': {'@type': 'UnitPriceSpecification', 'minPrice': lo, 'maxPrice': hi, 'priceCurrency': 'VND', 'unitText': 'tháng (lương người hỗ trợ)'}}}

def salary_html(s):
    if s.get('salary'):
        return f'<p class="mt-4 text-ink-soft"><b class="text-ink">Mức lương tham khảo: {s["salary"]}</b> (người hỗ trợ nhận). Mức cụ thể tùy kinh nghiệm, hình thức ở lại hay theo giờ và khối lượng công việc. <a class="underline" href="/#hoi-dap-11">Xem bảng lương các vị trí</a>.</p>'
    if s['slug'] == 'ho-tro-ngan-han':
        return '<p class="mt-4 text-ink-soft"><b class="text-ink">Chi phí:</b> báo giá riêng theo công việc, thời gian và địa điểm. <a class="underline" href="/#tim-nguoi" data-open="khach" data-service="Hỗ trợ ngắn hạn">Gửi yêu cầu để nhận báo giá</a>.</p>'
    return ''

def steps_html():
    return '<ol class="steps-sm" role="list">' + ''.join(f'<li><b>{E(a)}</b><span>{E(b)}</span></li>' for a, b in PROCESS) + '</ol>'

# ---------------- service pages ----------------
GUIDE_LINK = {
    'giup-viec-gia-dinh': 'Đọc thêm: <a class="underline" href="/giup-viec-o-lai-hay-theo-gio">nên chọn ở lại hay theo giờ</a>, <a class="underline" href="/gia-thue-giup-viec-ha-noi">bảng lương 2026</a>. ',
    'bao-mau-cham-be': 'Đọc thêm: <a class="underline" href="/kinh-nghiem-thue-bao-mau">kinh nghiệm thuê bảo mẫu</a>. ',
    'cham-soc-nguoi-gia': 'Đọc thêm: <a class="underline" href="/thue-nguoi-cham-soc-nguoi-gia">thuê người chăm sóc người già cần lưu ý gì</a>. ',
    'quan-gia': 'Đọc thêm: <a class="underline" href="/gia-thue-giup-viec-ha-noi">bảng lương các vị trí 2026</a>. ',
    'dau-bep-gia-dinh': 'Đọc thêm: <a class="underline" href="/gia-thue-giup-viec-ha-noi">bảng lương các vị trí 2026</a>. ',
    'ho-tro-ngan-han': 'Đọc thêm: <a class="underline" href="/giup-viec-o-lai-hay-theo-gio">so sánh ở lại và theo giờ</a>. ',
}
def service_page(s):
    path = '/' + s['slug']
    crumbs = [('Trang chủ', '/'), ('Dịch vụ', '/dich-vu'), (s['name'], None)]
    rel = ''.join(f'''<a class="card" href="/{r}"><h3>{E(SVC[r]['name'])}</h3><p>{E(SVC[r]['desc'][:150].rsplit(' ', 1)[0])}…</p><span class="more">Xem dịch vụ →</span></a>''' for r in s['related'])
    main = f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="pointer-events-none absolute inset-0" aria-hidden="true" style="background:radial-gradient(60% 70% at 78% 45%, rgba(53,84,73,.75), transparent 70%)"></div>
  <div class="shell relative grid items-center gap-14 pb-20 pt-32 lg:grid-cols-12 lg:gap-8 lg:pb-24 lg:pt-40">
    <div class="lg:col-span-7">
      {crumbs_html(crumbs)}
      <span class="eyebrow">{E(s['tag'])}</span>
      <h1 id="pg-title" class="t-display mt-4" style="max-width:19ch">{E(s['h1'])}</h1>
      <p class="t-lead mt-6 max-w-[52ch] text-mist">{E(s['lead'])}</p>
      <div class="mt-9 flex flex-wrap gap-3">
        <a class="btn btn-brass" href="#tim-nguoi" data-open="khach" data-service="{E(s['name'])}">Yêu cầu tư vấn</a>
        <a class="btn btn-ghost-light" href="tel:0948919598" data-track="call">Gọi 0948 919 598</a>
      </div>
    </div>
    <div class="lg:col-span-5">
      <div class="arch-frame mx-auto w-[min(76vw,430px)] lg:ml-auto lg:mr-2">
        <div class="arch aspect-[4/5] bg-shutter">
          <img src="assets/img/{s['img']}-720.webp" width="720" height="900" alt="{E(s['name'])} – Elite Helpers Hà Nội" fetchpriority="high" decoding="async">
        </div>
      </div>
    </div>
  </div>
</section>

<section class="on-light bg-paper py-20 lg:py-28" aria-labelledby="cv-title">
  <div class="shell grid gap-14 lg:grid-cols-12 lg:gap-12">
    <div class="lg:col-span-7">
      <h2 id="cv-title" class="t-h2 text-shutter">Công việc {E(s['name'].lower())} đảm nhận</h2>
      <ul class="checks" role="list">{li(s['tasks'])}</ul>
    </div>
    <div class="lg:col-span-5">
      <h2 class="t-h2 text-shutter">Phù hợp với</h2>
      <ul class="checks" role="list">{li(s['fit'])}</ul>
    </div>
  </div>
</section>

<section class="on-light bg-linen py-20 lg:py-28" aria-labelledby="tc-title">
  <div class="shell grid gap-14 lg:grid-cols-12 lg:gap-12">
    <div class="lg:col-span-7">
      <h2 id="tc-title" class="t-h2 text-shutter">Tiêu chí Elite Helpers chọn người</h2>
      <ul class="checks" role="list">{li(s['criteria'])}</ul>
    </div>
    <div class="lg:col-span-5">
      <h2 class="t-h2 text-shutter">Hình thức và chi phí</h2>
      <p class="mt-5 text-ink-soft">{E(s['modes'])}</p>
      {salary_html(s)}
    </div>
  </div>
</section>

<section class="on-light bg-paper py-20 lg:py-24" aria-labelledby="qt-title">
  <div class="shell">
    <h2 id="qt-title" class="t-h2 text-shutter">Quy trình 4 bước</h2>
    {steps_html()}
  </div>
</section>

<section class="on-light bg-linen py-20 lg:py-24" aria-labelledby="fq-title">
  <div class="shell grid gap-12 lg:grid-cols-12 lg:gap-10">
    <div class="lg:col-span-4"><h2 id="fq-title" class="t-h2 text-shutter">Hỏi đáp về {E(s['name'].lower())}</h2>
      <p class="mt-4 text-ink-soft">{GUIDE_LINK.get(s['slug'], '')}Xem thêm <a class="underline" href="/thue-giup-viec-2026">cẩm nang thuê giúp việc 2026</a> về hợp đồng và quy định mới.</p></div>
    <div class="faq lg:col-span-8">
{faq_html(s['faq'])}
    </div>
  </div>
</section>

<section class="on-light bg-paper py-20 lg:py-24" aria-labelledby="rl-title">
  <div class="shell">
    <h2 id="rl-title" class="t-h2 text-shutter">Dịch vụ liên quan</h2>
    <div class="cards c3">{rel}</div>
  </div>
</section>

{cta_block(s['name'], h=f'Cần {s["name"].lower()} cho gia đình?')}'''
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': SITE + path + '#webpage', 'url': SITE + path, 'name': s['title'], 'description': s['desc'],
         'inLanguage': 'vi', 'isPartOf': {'@id': SITE + '/#website'}, 'breadcrumb': {'@id': SITE + path + '#breadcrumb'}},
        {'@type': 'Service', '@id': SITE + path + '#service', 'name': s['name'], 'serviceType': s['name'], 'url': SITE + path,
         'description': s['lead'], 'provider': {'@id': ORG_ID}, 'areaServed': {'@type': 'City', 'name': 'Hà Nội'},
         'image': SITE + f"/{s['img']}-720.webp", **salary_ld(s)},
        crumbs_ld(crumbs, path), faq_ld(s['faq'], path)]}
    return page(s['title'], s['desc'], path, main, ld)

# ---------------- home JSON-LD (generated from visible content) ----------------
def home_ld():
    soup = BeautifulSoup(home, 'html.parser')
    faqs = []
    for d in soup.select('#hoi-dap details'):
        q = d.summary.get_text(' ', strip=True); a = re.sub(r'\s+([,.;:])', r'\1', d.select_one('.ans').get_text(' ', strip=True))
        faqs.append((q, a))
    svcs = []
    for s in SERVICES:
        li_ = soup.select_one('#' + s['slug'])
        ps = li_.select('p.mt-2')
        svcs.append({'@type': 'Offer', 'itemOffered': {'@type': 'Service', '@id': SITE + '/' + s['slug'] + '#service', 'name': s['name'],
                     'description': ps[0].get_text(' ', strip=True), 'url': SITE + '/' + s['slug']}})
    org = {'@type': ['EmploymentAgency', 'LocalBusiness'], '@id': ORG_ID, 'name': 'Elite Helpers', 'alternateName': ['Giúp việc Elite', 'Elite Helpers - Hỗ trợ gia đình cao cấp'],
           'description': 'Elite Helpers (Giúp việc Elite) là dịch vụ kết nối người hỗ trợ gia đình cao cấp tại Hà Nội: giúp việc gia đình, bảo mẫu, chăm sóc người già, quản gia, đầu bếp gia đình và hỗ trợ ngắn hạn.',
           'url': SITE + '/', 'logo': {'@type': 'ImageObject', 'url': LOGO, 'width': 512, 'height': 512}, 'image': OG,
           'telephone': '+84948919598', 'email': 'lienhe@giupviecelite.vn',
           'address': {'@type': 'PostalAddress', 'addressLocality': 'Hà Nội', 'addressRegion': 'Hà Nội', 'addressCountry': 'VN'},
           'areaServed': [{'@type': 'City', 'name': 'Hà Nội'}, {'@type': 'AdministrativeArea', 'name': 'Bắc Ninh'}, {'@type': 'AdministrativeArea', 'name': 'Hưng Yên'}],
           'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'opens': '08:00', 'closes': '21:00'}],
           'knowsLanguage': ['vi', 'en'], 'priceRange': '$$',
           'contactPoint': [{'@type': 'ContactPoint', 'telephone': '+84948919598', 'email': 'lienhe@giupviecelite.vn', 'contactType': 'customer service', 'availableLanguage': ['Vietnamese', 'English'], 'areaServed': 'VN'}],
           'sameAs': ['https://www.facebook.com/EliteHelpersVN'],
           'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Dịch vụ người hỗ trợ gia đình', 'itemListElement': svcs}}
    title = soup.title.get_text()
    desc = soup.find('meta', attrs={'name': 'description'})['content']
    return {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'Elite Helpers', 'alternateName': 'Giúp việc Elite', 'inLanguage': ['vi', 'en'], 'publisher': {'@id': ORG_ID}},
        {'@type': 'WebPage', '@id': SITE + '/#webpage', 'url': SITE + '/', 'name': title, 'description': desc, 'inLanguage': 'vi', 'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': ORG_ID}, 'primaryImageOfPage': OG},
        org, faq_ld(faqs, '/')]}, faqs

# ---------------- write ----------------
def build():
    shutil.rmtree(GEN, ignore_errors=True)
    shutil.copytree(SRC, GEN, ignore=shutil.ignore_patterns('index.orig.html', 'llms.txt', 'sitemap.xml', 'robots.txt'))
    ld, faqs = home_ld()
    h = home.replace('<!--JSONLD-->', '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, separators=(',', ':')) + '\n</script>')
    h = h.replace('assets/css/app.css?v=202610121240', f'assets/css/app.css?v={VER}').replace('assets/js/app.js?v=202610121240', f'assets/js/app.js?v={VER}')
    global BOTTOM_SUB
    BOTTOM_SUB = BOTTOM_SUB.replace('assets/js/app.js?v=202610121240', f'assets/js/app.js?v={VER}')
    open(os.path.join(GEN, 'index.html'), 'w', encoding='utf-8').write(h)
    pages = {'index.html': '/'}
    for s in SERVICES:
        open(os.path.join(GEN, s['slug'] + '.html'), 'w', encoding='utf-8').write(service_page(s))
        pages[s['slug'] + '.html'] = '/' + s['slug']
    for fn, path, html_ in X.extra_pages(globals()):
        open(os.path.join(GEN, fn), 'w', encoding='utf-8').write(html_)
        if fn not in ('404.html', 'quan-tri.html'): pages[fn] = path
    X.write_meta_files(globals(), pages, faqs)
    return pages

ESBUILD = os.path.join(ROOT, '..', '..', 'tools', 'node_modules', '.bin', 'esbuild')

def minify_dist():
    """Nén CSS/JS và bỏ chú thích HTML trong dist/ (mã nguồn trong site/ giữ nguyên để dễ sửa)."""
    import subprocess
    for fn in ('app.css', 'app.js'):
        f = os.path.join(DIST, fn)
        subprocess.run([ESBUILD, f, '--minify', '--legal-comments=none', '--target=es2019,safari13', '--allow-overwrite', '--outfile=' + f, '--log-level=warning'], check=True)
    for dp, _, fns in os.walk(DIST):
        for fn in fns:
            if fn.endswith('.html'):
                f = os.path.join(dp, fn)
                t = open(f, encoding='utf-8').read()
                t = re.sub(r'<!--(?!\[if).*?-->', '', t, flags=re.S)
                t = re.sub(r'\n[ \t]*\n+', '\n', t)
                open(f, 'w', encoding='utf-8').write(t)
    add_admin_csp()

def add_admin_csp():
    """Trang quản trị: chỉ cho chạy đúng đoạn script của trang (theo mã băm) và script từ Apps Script."""
    import base64
    f = os.path.join(DIST, 'quan-tri', 'index.html')
    t = open(f, encoding='utf-8').read()
    hashes = []
    for m in re.finditer(r'<script>(.*?)</script>', t, flags=re.S):
        hashes.append("'sha256-" + base64.b64encode(hashlib.sha256(m.group(1).encode('utf-8')).digest()).decode() + "'")
    csp = ("default-src 'none'; script-src " + ' '.join(hashes) + " https://script.google.com https://script.googleusercontent.com; "
           "style-src 'unsafe-inline'; img-src 'self' data:; manifest-src 'self'; connect-src 'none'; base-uri 'none'; form-action 'none'")
    t = t.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta http-equiv="Content-Security-Policy" content="' + csp + '">', 1)
    open(f, 'w', encoding='utf-8').write(t)

if __name__ == '__main__':
    p = build()
    minify_dist()
    print('pages:', len(p))
