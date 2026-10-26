# -*- coding: utf-8 -*-
"""Tin tuyển dụng (mục /tuyen-dung). Mỗi tin có trang riêng /<slug> và nút "Ứng tuyển ngay" mở form ứng viên
với vị trí, hình thức chọn sẵn; mã tin được ghi vào ô Ghi chú của hồ sơ (trang quản trị và Apps Script giữ nguyên).

Thêm tin mới: thêm dict vào ĐẦU JOBS rồi chạy build.py.
- code: mã tin, dạng EH-<viết tắt vị trí>-<ngày tháng>, ví dụ EH-BM-2510 (BM bảo mẫu, GV giúp việc, NG người già, QG quản gia, DB đầu bếp, NH ngắn hạn).
- position: đúng 1 trong 5 lựa chọn của form: Giúp việc gia đình | Bảo mẫu, chăm bé | Chăm sóc người già | Quản gia | Đầu bếp gia đình
- mode: Ở lại cùng gia đình | Theo giờ / theo ca | Cả hai
- status: 'open' (đang tuyển) hoặc 'closed' (đã tuyển: giữ trang, ẩn nút ứng tuyển, không gửi dữ liệu JobPosting cho Google).
- valid: ngày hết hạn tin (yyyy-mm-dd); quá hạn thì tự hiện như đã tuyển.
"""
import html, json
from datetime import date
E = html.escape

JOBS = [
dict(code='EH-BM-2610', slug='tuyen-bao-mau-cham-be-toan-thoi-gian-gamuda-hoang-mai', status='open', urgent=False,
     date='2026-10-26', date_vi='26/10/2026', valid='2026-11-30',
     title='Bảo mẫu chăm bé toàn thời gian, ở lại cùng gia đình tại KĐT Gamuda, Hoàng Mai',
     position='Bảo mẫu, chăm bé', mode='Ở lại cùng gia đình',
     area='KĐT Gamuda, Hoàng Mai, Hà Nội', locality='Hoàng Mai', region='Hà Nội',
     salary='15–25 triệu đồng/tháng', sal_min=15000000, sal_max=25000000, salary_note='Có thưởng tháng lương 13',
     summary='Chăm bé toàn thời gian: ăn, ngủ, tắm, vệ sinh, chơi cùng bé. Ưu tiên người gắn bó lâu dài.',
     duties=['Chăm bé ăn, ngủ, tắm, vệ sinh', 'Chơi cùng bé, theo dõi nếp sinh hoạt hằng ngày'],
     family='', reqs=['Đã có kinh nghiệm chăm trẻ toàn thời gian', 'Tận tâm, sạch sẽ, gắn bó lâu dài'],
     off='Trao đổi cụ thể khi phỏng vấn.'),
dict(code='EH-BM-2510', slug='tuyen-bao-mau-cham-be-so-sinh-ocean-park-2', status='open', urgent=True,
     date='2026-10-25', date_vi='25/10/2026', valid='2026-11-30',
     title='Bảo mẫu chăm bé sơ sinh, ở lại cùng gia đình tại Vinhomes Ocean Park 2',
     position='Bảo mẫu, chăm bé', mode='Ở lại cùng gia đình',
     area='Vinhomes Ocean Park 2, Văn Giang, Hưng Yên (gần Gia Lâm, Hà Nội)', locality='Văn Giang', region='Hưng Yên',
     salary='18–25 triệu đồng/tháng', sal_min=18000000, sal_max=25000000, salary_note='Tùy năng lực, có thưởng tháng 13',
     summary='Chăm bé sơ sinh 1 tháng tuổi theo phương pháp EASY, nấu 2 bữa trưa, tối cho gia đình 3 người.',
     duties=['Chăm bé sơ sinh 1 tháng tuổi theo phương pháp EASY',
             'Rèn nếp sinh hoạt, chuẩn bị ăn dặm khi bé lớn hơn',
             'Nấu 2 bữa trưa, tối cho gia đình'],
     family='Hai vợ chồng và 1 bé. Bố mẹ làm việc tại nhà nên luôn có người hỗ trợ. Nhà có máy móc hỗ trợ dọn dẹp và có người dọn theo giờ hằng tuần.',
     reqs=['Có kinh nghiệm chăm trẻ sơ sinh, thành thạo phương pháp EASY',
           'Nấu ăn ngon',
           'Yêu trẻ, quý động vật (nhà có 2 bé mèo)'],
     off='Được gộp ngày nghỉ để về quê, trao đổi cụ thể khi phỏng vấn.'),
]

# Vị trí tuyển thường xuyên (không gắn gia đình cụ thể)
REGULAR = [
    ('Giúp việc gia đình', 'Giúp việc gia đình', 'Ở lại hoặc theo giờ: dọn dẹp, giặt là, đi chợ, nấu ăn.', '10–25 triệu đồng/tháng'),
    ('Bảo mẫu, chăm bé', 'Bảo mẫu, chăm bé', 'Chăm trẻ sơ sinh, trẻ nhỏ; ưu tiên người đã có con, có kinh nghiệm.', '10–25 triệu đồng/tháng'),
    ('Chăm sóc người già', 'Chăm sóc người già', 'Hỗ trợ sinh hoạt, ăn uống, nhắc thuốc, đưa đi khám cho ông bà.', '10–25 triệu đồng/tháng'),
    ('Quản gia', 'Quản gia', 'Điều phối việc nhà ở biệt thự, dinh thự; ưu tiên biết tiếng Anh.', '18–40 triệu đồng/tháng'),
    ('Đầu bếp gia đình', 'Đầu bếp gia đình', 'Nấu món Việt, Á, Âu; lên thực đơn, nấu tiệc tại nhà.', '15–35 triệu đồng/tháng'),
    ('Hỗ trợ ngắn hạn, dịp Tết', '', 'Làm theo đợt từ vài ngày đến vài tuần, dịp Tết thu nhập cao.', 'Báo theo từng đợt'),
]


def is_open(j, today=None):
    today = today or date.today().isoformat()
    return j['status'] == 'open' and j['valid'] >= today


def apply_attrs(code='', title='', pos='', mode=''):
    """Thuộc tính cho nút mở form ứng viên với tin được chọn sẵn (app.js đọc data-job-*)."""
    a = ' data-open="ungvien"'
    if code: a += f' data-job-code="{E(code)}"'
    if title: a += f' data-job-title="{E(title)}"'
    if pos: a += f' data-job-pos="{E(pos)}"'
    if mode: a += f' data-job-mode="{E(mode)}"'
    return a


def apply_btn(j, cls='btn btn-green', label='Ứng tuyển ngay'):
    return f'<a class="{cls}" href="#ung-tuyen"{apply_attrs(j["code"], j["title"], j["position"], j["mode"])} data-track="job_apply">{label}</a>'


def job_card(j):
    op = is_open(j)
    badge = ('<b class="jb-hot">Tuyển gấp</b>' if j.get('urgent') else '<b class="jb-open">Đang tuyển</b>') if op else '<b class="jb-done">Đã tuyển</b>'
    acts = (apply_btn(j) + f'<a class="btn btn-ghost-dark" href="/{j["slug"]}">Xem chi tiết</a>') if op else \
        f'<a class="btn btn-ghost-dark" href="/{j["slug"]}">Xem tin</a>'
    return f'''
      <article class="jb-card{'' if op else ' is-done'}" id="{E(j['code'])}" aria-labelledby="t-{E(j['code'])}">
        <div class="jb-top">{badge}<span class="jb-code">Mã tin {E(j['code'])} · {j['date_vi']}</span></div>
        <h3 id="t-{E(j['code'])}"><a href="/{j['slug']}">{E(j['title'])}</a></h3>
        <ul class="jb-facts" role="list">
          <li><span>Thu nhập</span><b>{E(j['salary'])}</b></li>
          <li><span>Hình thức</span>{E(j['mode'])}</li>
          <li><span>Nơi làm</span>{E(j['area'])}</li>
        </ul>
        <p class="jb-sum">{E(j['summary'])}</p>
        <div class="jb-acts">{acts}</div>
      </article>'''


def jobs_section(g):
    opened = [j for j in JOBS if is_open(j)]
    closed = [j for j in JOBS if not is_open(j)][:4]
    cards = ''.join(job_card(j) for j in opened + closed)
    if not opened:
        cards = '''
      <div class="jb-empty"><p><b>Elite Helpers đang cập nhật tin mới.</b> Chị em gửi hồ sơ trước, khi có gia đình phù hợp Elite Helpers gọi lại ngay.</p>
        <a class="btn btn-green" href="#ung-tuyen" data-open="ungvien">Gửi hồ sơ ứng tuyển</a></div>''' + cards
    reg = ''.join(f'''
      <div class="card jb-reg"><h3>{E(n)}</h3><p>{E(d)}</p><p class="jb-reg-sal">{E(s)}</p>
        <a class="jb-link" href="#ung-tuyen"{apply_attrs('', 'Vị trí thường xuyên: ' + n, pos)} data-track="job_apply">Ứng tuyển vị trí này →</a></div>'''
                  for n, pos, d, s in REGULAR)
    return f'''<section id="viec-dang-tuyen" class="on-light bg-paper py-20 lg:py-24" aria-labelledby="vdt-title">
  <div class="shell">
    <span class="eyebrow">Tin tuyển dụng · {len(opened)} việc đang tuyển</span>
    <h2 id="vdt-title" class="t-h2 mt-3 text-shutter">Việc đang tuyển</h2>
    <p class="mt-4 max-w-[60ch] text-ink-soft">Mỗi tin là một gia đình cụ thể Elite Helpers đã trao đổi trước. Bấm <b>Ứng tuyển ngay</b>, form tự chọn sẵn vị trí, chị em chỉ cần điền thông tin trong 2 phút.</p>
    <div class="jb-list">{cards}
    </div>
  </div>
</section>
<section id="vi-tri" class="on-light bg-linen py-20 lg:py-24" aria-labelledby="vt-title">
  <div class="shell">
    <h2 id="vt-title" class="t-h2 text-shutter">Vị trí tuyển thường xuyên</h2>
    <p class="mt-4 max-w-[60ch] text-ink-soft">Chưa thấy tin phù hợp? Gửi hồ sơ theo vị trí, Elite Helpers giới thiệu khi có gia đình đúng kinh nghiệm và khu vực của chị em.</p>
    <div class="cards c3">{reg}
    </div>
  </div>
</section>'''


def tabs(cur):
    cur_attr = ' aria-current="page"'
    a = lambda href, label, k: f'<a href="{href}"{cur_attr if k == cur else ""}>{label}</a>'
    return f'<nav class="td-tabs" aria-label="Mục tuyển dụng">{a("/tuyen-dung", "Việc đang tuyển", "jobs")}{a("/tin-tuc", "Tin tức", "news")}</nav>'


def job_page(g, j, others):
    SITE = g['SITE']; path = '/' + j['slug']
    op = is_open(j)
    crumbs = [('Trang chủ', '/'), ('Tuyển dụng', '/tuyen-dung'), ('Mã tin ' + j['code'], None)]
    li = lambda xs: ''.join(f'<li>{E(x)}</li>' for x in xs)
    acts = (f'''<div class="mt-9 flex flex-wrap gap-3">
      {apply_btn(j, 'btn btn-brass', 'Ứng tuyển ngay (2 phút)')}
      <a class="btn btn-ghost-light" href="https://zalo.me/0948919598" target="_blank" rel="noopener" data-track="zalo">Hỏi qua Zalo 0948 919 598</a>
    </div>''' if op else '''<p class="jb-closed-note">Vị trí này đã tuyển đủ. Chị em xem các việc khác đang tuyển hoặc gửi hồ sơ để Elite Helpers giới thiệu gia đình phù hợp.</p>
    <div class="mt-6 flex flex-wrap gap-3"><a class="btn btn-brass" href="/tuyen-dung">Xem việc đang tuyển</a><a class="btn btn-ghost-light" href="#ung-tuyen" data-open="ungvien">Gửi hồ sơ</a></div>''')
    more = [o for o in others if o is not j and is_open(o)][:3]
    more_html = ('<h2>Việc khác đang tuyển</h2><ul>' + ''.join(f'<li><a href="/{o["slug"]}">{E(o["title"])}</a> · {E(o["salary"])}</li>' for o in more) + '</ul>') if more else ''
    main = f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="shell relative pb-16 pt-32 lg:pb-20 lg:pt-40">
    {g['crumbs_html'](crumbs)}
    <span class="eyebrow">{'Tuyển gấp · ' if op and j.get('urgent') else ('' if op else 'Đã tuyển · ')}Đăng ngày {j['date_vi']}</span>
    <h1 id="pg-title" class="t-display mt-4" style="max-width:24ch;font-size:clamp(2rem,1.4rem + 2.4vw,3.2rem)">{E(j['title'])}</h1>
    <ul class="jb-hero-facts" role="list">
      <li><span>Thu nhập</span><b>{E(j['salary'])}</b><small>{E(j['salary_note'])}</small></li>
      <li><span>Hình thức</span><b>{E(j['mode'])}</b></li>
      <li><span>Nơi làm</span><b>{E(j['area'])}</b></li>
    </ul>
    {acts}
  </div>
</section>
<article class="on-light bg-paper py-14 lg:py-20 jb-detail">
  <div class="shell"><div class="prose">
    <h2>Công việc</h2><ul>{li(j['duties'])}</ul>
    {('<h2>Về gia đình</h2><p>' + E(j['family']) + '</p>') if j.get('family') else ''}
    <h2>Yêu cầu</h2><ul>{li(j['reqs'])}</ul>
    <h2>Ngày nghỉ</h2><p>{E(j['off'])}</p>
    <div class="note"><strong>Ở Elite Helpers:</strong> không thu bất kỳ khoản phí nào của người lao động. Trao đổi kỹ qua Zalo, gặp gia đình trước khi nhận việc, hợp đồng bằng văn bản và luôn có người đồng hành.</div>
    {('<p class="jb-apply-row">' + apply_btn(j) + '</p>') if op else ''}
    <p class="jb-code-line">Mã tin: <b>{E(j['code'])}</b> · Đăng ngày {j['date_vi']}</p>
    {more_html}
    <p><a href="/tuyen-dung#viec-dang-tuyen">← Xem tất cả việc đang tuyển</a></p>
  </div></div>
</article>'''
    ld_graph = [{'@type': 'WebPage', '@id': SITE + path + '#webpage', 'url': SITE + path, 'name': j['title'], 'inLanguage': 'vi',
                 'isPartOf': {'@id': SITE + '/#website'}}, g['crumbs_ld'](crumbs, path)]
    if op:
        desc = ('<p>' + E(j['summary']) + '</p><p><b>Công việc:</b></p><ul>' + li(j['duties']) + '</ul>' + (('<p><b>Gia đình:</b> ' + E(j['family']) + '</p>') if j.get('family') else '') +
                '<p><b>Yêu cầu:</b></p><ul>' + li(j['reqs']) + '</ul><p><b>Ngày nghỉ:</b> ' + E(j['off']) + '</p><p>Elite Helpers không thu phí người lao động.</p>')
        ld_graph.append({'@type': 'JobPosting', '@id': SITE + path + '#job', 'title': j['title'], 'description': desc,
                         'identifier': {'@type': 'PropertyValue', 'name': 'Elite Helpers', 'value': j['code']},
                         'datePosted': j['date'], 'validThrough': j['valid'] + 'T23:59:00+07:00', 'employmentType': 'FULL_TIME',
                         'directApply': True, 'hiringOrganization': {'@id': SITE + '/#org'},
                         'jobLocation': {'@type': 'Place', 'address': {'@type': 'PostalAddress', 'addressLocality': j['locality'], 'addressRegion': j['region'], 'addressCountry': 'VN'}},
                         'baseSalary': {'@type': 'MonetaryAmount', 'currency': 'VND', 'value': {'@type': 'QuantitativeValue', 'minValue': j['sal_min'], 'maxValue': j['sal_max'], 'unitText': 'MONTH'}}})
    ld = {'@context': 'https://schema.org', '@graph': ld_graph}
    desc_meta = f"{j['title']}. Thu nhập {j['salary']}, {j['mode'].lower()}. {j['summary']} Ứng tuyển online 2 phút, không thu phí."
    return j['slug'] + '.html', path, g['page'](j['title'] + ' | Tuyển dụng Elite Helpers', desc_meta[:300], path, main, ld)


def all_jobs(g):
    return [job_page(g, j, JOBS) for j in JOBS]
