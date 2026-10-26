# -*- coding: utf-8 -*-
"""Tin tuyển dụng (mục /tuyen-dung).

Nguồn dữ liệu chính: tab TinTuyenDung trong Google Sheets, sửa tại /quan-tri → mục "Tin tuyển dụng" (Apps Script bản 18).
Website đọc tin qua Apps Script (action=jobs) mỗi lần mở trang. Danh sách SEED dưới đây chỉ là bản dự phòng in sẵn
trong HTML (hiển thị khi chưa kết nối được Apps Script hoặc tab TinTuyenDung còn trống) và là dữ liệu mẫu để
"Đưa tin mẫu lên hệ thống" trên trang quản trị.

- /tuyen-dung: thẻ tin gọn (bấm mở tab mới trang chi tiết), nút Ứng tuyển trên từng thẻ.
- /viec-lam/?ma=<Mã tin>: trang chi tiết (JavaScript dựng từ dữ liệu, có JobPosting cho Google Việc làm).
- Nút "Ứng tuyển" mở form ứng viên chọn sẵn vị trí, hình thức; mã tin ghi vào đầu ô Ghi chú của hồ sơ.

Trường dữ liệu (trùng tên cột Apps Script):
ma, trangThai (Đang tuyển | Tạm ẩn | Đã tuyển), nhan (Tuyển gấp | Hot | Mới | trống), thuTu, tenViTri,
viTri (Giúp việc gia đình | Bảo mẫu, chăm bé | Chăm sóc người già | Quản gia | Đầu bếp gia đình | Hỗ trợ ngắn hạn),
hinhThuc (Ở lại cùng gia đình | Theo giờ / theo ca | Cả hai), luongTu, luongDen (triệu/tháng), luongGhiChu,
ngayNghi, thang13, diaDiem, tinh, thoiGianCan, thoiGianLam, moTa, yeuCau, quyenLoi (mỗi dòng 1 ý, "- " thành gạch đầu dòng),
ngayDang, hanTin (yyyy-mm-dd).
"""
import html, json
from datetime import date
E = html.escape

SEED = [
dict(ma='EH-GV-2610', trangThai='Đang tuyển', nhan='Mới', thuTu='', ngayDang='2026-10-26', hanTin='2026-11-30',
     tenViTri='Giúp việc gia đình làm ở lại tại Tây Hồ', viTri='Giúp việc gia đình', hinhThuc='Ở lại cùng gia đình',
     luongTu='15', luongDen='20', luongGhiChu='Theo kinh nghiệm', ngayNghi='', thang13='',
     diaDiem='Tây Hồ, Hà Nội', tinh='Hà Nội', thoiGianCan='', thoiGianLam='Ở lại cùng gia đình, làm việc lâu dài',
     moTa='Gia đình 4 người lớn và 1 bé 2 tuổi. Nhà 3 tầng, khoảng 100 m²/tầng, có sân vườn.\n- Dọn dẹp nhà cửa\n- Giặt giũ quần áo\n- Chăm sóc sân vườn\n- Cho thú cưng ăn',
     yeuCau='- Có kinh nghiệm giúp việc bài bản\n- Sạch sẽ, gọn gàng, ngăn nắp\n- Quen dùng máy móc gia đình\n- Ưu tiên người đã được đào tạo và làm Housekeeping tại khách sạn',
     quyenLoi=''),
dict(ma='EH-BM-2610', trangThai='Đang tuyển', nhan='', thuTu='', ngayDang='2026-10-26', hanTin='2026-11-30',
     tenViTri='Bảo mẫu chăm bé toàn thời gian tại KĐT Gamuda, Hoàng Mai', viTri='Bảo mẫu, chăm bé', hinhThuc='Ở lại cùng gia đình',
     luongTu='15', luongDen='25', luongGhiChu='Tùy kinh nghiệm và kỹ năng', ngayNghi='Được gộp để về quê, trao đổi cụ thể khi gặp gia đình', thang13='Có',
     diaDiem='KĐT Gamuda Gardens, Hoàng Mai, Hà Nội', tinh='Hà Nội', thoiGianCan='', thoiGianLam='Ở lại cùng gia đình, chăm bé toàn thời gian',
     moTa='- Chăm bé ăn uống, giấc ngủ, tắm rửa, vệ sinh cá nhân\n- Chuẩn bị bữa ăn, đồ dùng riêng; giặt, gấp quần áo của bé\n- Chơi cùng bé, đọc sách, rèn nề nếp sinh hoạt theo lứa tuổi\n- Theo dõi sức khỏe, thói quen của bé và trao đổi với bố mẹ mỗi ngày',
     yeuCau='- Đã có kinh nghiệm chăm trẻ toàn thời gian, vững nghề\n- Sức khỏe tốt, sạch sẽ, kiên nhẫn, yêu trẻ\n- Trung thực, sẵn sàng gắn bó lâu dài',
     quyenLoi='- Bao ăn ở\n- Môi trường văn minh, an toàn'),
dict(ma='EH-BM-2510', trangThai='Đang tuyển', nhan='Tuyển gấp', thuTu='', ngayDang='2026-10-25', hanTin='2026-11-30',
     tenViTri='Bảo mẫu chăm bé sơ sinh tại Vinhomes Ocean Park 2', viTri='Bảo mẫu, chăm bé', hinhThuc='Ở lại cùng gia đình',
     luongTu='18', luongDen='25', luongGhiChu='Tùy năng lực', ngayNghi='Được gộp để về quê, trao đổi cụ thể khi phỏng vấn', thang13='Có',
     diaDiem='Vinhomes Ocean Park 2, Văn Giang, Hưng Yên (gần Gia Lâm, Hà Nội)', tinh='Hưng Yên', thoiGianCan='', thoiGianLam='Ở lại cùng gia đình',
     moTa='Gia đình 2 vợ chồng và 1 bé. Bố mẹ làm việc tại nhà nên luôn có người hỗ trợ; nhà có máy móc hỗ trợ dọn dẹp và người dọn theo giờ hằng tuần.\n- Chăm bé sơ sinh 1 tháng tuổi theo phương pháp EASY\n- Rèn nếp sinh hoạt, chuẩn bị ăn dặm khi bé lớn hơn\n- Nấu 2 bữa trưa, tối cho gia đình',
     yeuCau='- Có kinh nghiệm chăm trẻ sơ sinh, thành thạo phương pháp EASY\n- Nấu ăn ngon\n- Yêu trẻ, quý động vật (nhà có 2 bé mèo)',
     quyenLoi=''),
]

# Trang cũ của từng tin (đã chia sẻ link) → chuyển sang trang chi tiết mới
OLD_SLUGS = {'tuyen-bao-mau-cham-be-so-sinh-ocean-park-2': 'EH-BM-2510',
             'tuyen-bao-mau-cham-be-toan-thoi-gian-gamuda-hoang-mai': 'EH-BM-2610'}

# Vị trí tuyển thường xuyên (không gắn gia đình cụ thể)
REGULAR = [
    ('Giúp việc gia đình', 'Giúp việc gia đình', 'Ở lại hoặc theo giờ: dọn dẹp, giặt là, đi chợ, nấu ăn.', '10–25 triệu đồng/tháng'),
    ('Bảo mẫu, chăm bé', 'Bảo mẫu, chăm bé', 'Chăm trẻ sơ sinh, trẻ nhỏ; ưu tiên người đã có con, có kinh nghiệm.', '10–25 triệu đồng/tháng'),
    ('Chăm sóc người già', 'Chăm sóc người già', 'Hỗ trợ sinh hoạt, ăn uống, nhắc thuốc, đưa đi khám cho ông bà.', '10–25 triệu đồng/tháng'),
    ('Quản gia', 'Quản gia', 'Điều phối việc nhà ở biệt thự, dinh thự; ưu tiên biết tiếng Anh.', '18–40 triệu đồng/tháng'),
    ('Đầu bếp gia đình', 'Đầu bếp gia đình', 'Nấu món Việt, Á, Âu; lên thực đơn, nấu tiệc tại nhà.', '15–35 triệu đồng/tháng'),
    ('Hỗ trợ ngắn hạn, dịp Tết', '', 'Làm theo đợt từ vài ngày đến vài tuần, dịp Tết thu nhập cao.', 'Báo theo từng đợt'),
]
FORM_POS = ['Giúp việc gia đình', 'Bảo mẫu, chăm bé', 'Chăm sóc người già', 'Quản gia', 'Đầu bếp gia đình']


# ---------- định dạng (giữ khớp với hàm cùng tên trong app.js) ----------
def num(v):
    try:
        f = float(str(v).replace(',', '.'))
        return ('%g' % f).replace('.', ',')
    except Exception:
        return ''

def salary(j):
    a, b = num(j.get('luongTu')), num(j.get('luongDen'))
    if a and b: return f'{a}–{b} triệu/tháng'
    if a: return f'Từ {a} triệu/tháng'
    if b: return f'Đến {b} triệu/tháng'
    return 'Thỏa thuận'

def is_open(j, today=None):
    today = today or date.today().isoformat()
    return j['trangThai'] == 'Đang tuyển' and (not j.get('hanTin') or j['hanTin'] >= today)

def date_vi(iso):
    return f'{iso[8:10]}/{iso[5:7]}/{iso[:4]}' if iso and len(iso) >= 10 else ''

def ordered(jobs):
    vis = [j for j in jobs if j['trangThai'] != 'Tạm ẩn']
    op = sorted([j for j in vis if is_open(j)], key=lambda j: (float(j['thuTu']) if num(j.get('thuTu')) else 9e9, ''.join(chr(0x10FFFF - ord(c)) for c in j.get('ngayDang', ''))))
    done = sorted([j for j in vis if not is_open(j)], key=lambda j: j.get('ngayDang', ''), reverse=True)[:4]
    return op, done


def apply_attrs(code='', title='', pos='', mode=''):
    """Thuộc tính cho nút mở form ứng viên với tin được chọn sẵn (app.js đọc data-job-*)."""
    a = ' data-open="ungvien"'
    if code: a += f' data-job-code="{E(code)}"'
    if title: a += f' data-job-title="{E(title)}"'
    if pos: a += f' data-job-pos="{E(pos)}"'
    if mode: a += f' data-job-mode="{E(mode)}"'
    return a


def badge(j, op):
    if not op: return '<b class="jl-b jl-done">Đã tuyển</b>'
    n = j.get('nhan') or ''
    cls = {'Tuyển gấp': 'jl-hot', 'Hot': 'jl-hot', 'Mới': 'jl-new'}.get(n, 'jl-new')
    return f'<b class="jl-b {cls}">{E(n)}</b>' if n else ''


def card(j):
    """Thẻ tin gọn. Cả thẻ là liên kết mở tab mới; nút Ứng tuyển nằm trên lớp liên kết."""
    op = is_open(j)
    pos = j['viTri'] if j.get('viTri') in FORM_POS else ''
    apply = (f'<a class="jl-apply" href="#ung-tuyen"{apply_attrs(j["ma"], j["tenViTri"], pos, j.get("hinhThuc", ""))} data-track="job_apply">Ứng tuyển</a>' if op else '')
    meta = ' · '.join(x for x in [j.get('hinhThuc', ''), 'Có tháng lương 13' if (j.get('thang13') or '').lower().startswith('có') else ''] if x)
    return f'''<article class="jl-card{'' if op else ' is-done'}" id="{E(j['ma'])}">
  <span class="jl-logo" aria-hidden="true"><img src="/arch-mark.svg" alt="" width="34" height="40" loading="lazy"></span>
  <div class="jl-body">
    <h3><a class="jl-link" href="/viec-lam/?ma={E(j['ma'])}" target="_blank" rel="noopener" data-track="job_open">{E(j['tenViTri'])}</a></h3>
    <p class="jl-sal">{E(salary(j))}</p>
    <p class="jl-loc">{E(j.get('diaDiem', ''))}</p>
    {f'<p class="jl-meta">{E(meta)}</p>' if meta else ''}
  </div>
  <div class="jl-side">{badge(j, op)}{apply}</div>
</article>'''


def jobs_section(g):
    op, done = ordered(SEED)
    cards = ''.join(card(j) for j in op + done)
    reg = ''.join(f'''
      <div class="card jb-reg"><h3>{E(n)}</h3><p>{E(d)}</p><p class="jb-reg-sal">{E(s)}</p>
        <a class="jb-link" href="#ung-tuyen"{apply_attrs('', 'Vị trí thường xuyên: ' + n, pos)} data-track="job_apply">Ứng tuyển vị trí này →</a></div>'''
                  for n, pos, d, s in REGULAR)
    seed = json.dumps(SEED, ensure_ascii=False).replace('</', '<\\/')
    return f'''<section id="viec-dang-tuyen" class="on-light bg-paper py-16 lg:py-20" aria-labelledby="vdt-title">
  <div class="shell">
    <div class="jl-head">
      <h2 id="vdt-title" class="t-h2 text-shutter">Việc đang tuyển</h2>
      <p class="jl-count" data-jobs-count>{len(op)} việc đang tuyển</p>
    </div>
    <p class="mt-3 max-w-[60ch] text-ink-soft">Bấm vào tin để xem chi tiết (mở tab mới). Nút <b>Ứng tuyển</b> mở form chọn sẵn vị trí, chị em chỉ cần điền 2 phút.</p>
    <div class="jl-list" data-jobs-list>{cards}
    </div>
    <script type="application/json" id="jobs-seed">{seed}</script>
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


def detail_page(g):
    """/viec-lam/?ma=…: khung trang, app.js dựng nội dung tin từ Apps Script (dự phòng: dữ liệu SEED)."""
    path = '/viec-lam'
    crumbs = [('Trang chủ', '/'), ('Tuyển dụng', '/tuyen-dung'), ('Chi tiết tin', None)]
    seed = json.dumps(SEED, ensure_ascii=False).replace('</', '<\\/')
    main = f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="shell relative pb-14 pt-32 lg:pb-16 lg:pt-40" data-job-hero>
    {g['crumbs_html'](crumbs)}
    <span class="eyebrow" data-job-eyebrow>Tin tuyển dụng</span>
    <h1 id="pg-title" class="t-display mt-4 jd-title" data-job-title>Đang tải tin tuyển dụng…</h1>
    <div data-job-top></div>
  </div>
</section>
<article class="on-light bg-paper py-12 lg:py-16 jb-detail">
  <div class="shell"><div class="jd-wrap" data-job-body>
    <noscript><p>Vui lòng bật JavaScript để xem tin, hoặc xem <a href="/tuyen-dung">danh sách việc đang tuyển</a>.</p></noscript>
  </div></div>
  <script type="application/json" id="jobs-seed">{seed}</script>
</article>'''
    ld = {'@context': 'https://schema.org', '@graph': [g['crumbs_ld'](crumbs, path)]}
    return 'viec-lam.html', path, g['page']('Tin tuyển dụng | Elite Helpers', 'Chi tiết tin tuyển dụng giúp việc, bảo mẫu, chăm sóc người già tại Hà Nội. Ứng tuyển online 2 phút, không thu phí người lao động.', path, main, ld)


def redirect_page(g, slug, ma):
    to = f'/viec-lam/?ma={ma}'
    html_ = f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tin tuyển dụng {ma} | Elite Helpers</title>
<link rel="canonical" href="{g['SITE']}{to}">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace({json.dumps(to)}+location.hash)</script>
</head><body><p>Tin đã chuyển sang <a href="{to}">trang mới</a>.</p></body></html>
'''
    return slug + '.html', '/' + slug, html_


def all_jobs(g):
    return [detail_page(g)] + [redirect_page(g, s, m) for s, m in OLD_SLUGS.items()]


def seed_json():
    return json.dumps(SEED, ensure_ascii=False)
