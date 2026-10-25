# -*- coding: utf-8 -*-
"""Trang đăng bài cho từng lịch: media/<ngày>/<slug>.html (tải ảnh/video, sao chép nội dung). Không index."""
import os, json, html
E = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.join(HERE, '..', 'media')
d25 = json.load(open(os.path.join(HERE, 'd2510.json'), encoding='utf-8'))

CAP_2410_TT = '''Nhà bạn có cần người hỗ trợ? 4 dấu hiệu dễ nhận ra 🏡
Bữa tối hay đặt ngoài, cuối tuần chỉ để dọn dẹp, con nhỏ và ông bà cần người bên cạnh, đi làm về đã kiệt sức…
Elite Helpers tư vấn miễn phí, tìm người hợp nếp nhà mình tại Hà Nội.
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn
#EliteHelpers #GiupViecHaNoi #HoTroGiaDinh #BaoMau #ChamSocNguoiGia #HaNoi'''
CAP_2410_GR = '''Đi gặp gia đình lần đầu, chị em nhớ hỏi rõ 5 điều này nhé 🌿

1️⃣ Công việc hằng ngày cụ thể gồm những gì?
2️⃣ Giờ làm, giờ nghỉ và ngày nghỉ trong tháng?
3️⃣ Mức lương, ngày trả lương và khoản BHXH, BHYT?
4️⃣ Chỗ ở, bữa ăn được sắp xếp thế nào?
5️⃣ Thời gian làm thử và hợp đồng ra sao?

Hỏi rõ từ đầu thì hai bên hiểu nhau, làm việc lâu dài và an tâm.

Ở Elite Helpers, mọi điều trên đều được trao đổi kỹ trước khi nhận việc. Không thu bất kỳ khoản phí nào của người lao động.

📞 Zalo 0948 919 598
🌐 Ứng tuyển: giupviecelite.vn/tuyen-dung
👥 Nhóm Zalo việc làm: https://zalo.me/g/rp4oixvilrwfy71i6yan

#EliteHelpers #ViecLamHaNoi #GiupViecHaNoi #ViecLamGiupViec #BaoMau'''
CAP_2410_PG = '''Ở lại hay theo giờ: hình thức nào hợp nhà mình? 🏡

🌙 Ở LẠI phù hợp khi:
◆ Nhà có trẻ nhỏ, ông bà cần người bên cạnh cả ngày
◆ Muốn người hỗ trợ lo trọn nấu ăn, dọn dẹp, giặt là
◆ Có phòng riêng cho người hỗ trợ

☀️ THEO GIỜ phù hợp khi:
◆ Cần dọn dẹp, nấu ăn vào khung giờ cố định
◆ Gia đình muốn giữ không gian riêng
◆ Căn hộ nhỏ, ít thành viên, cần linh hoạt số buổi

Chưa chắc nhà mình hợp hình thức nào? Nhắn "TƯ VẤN", Elite Helpers gợi ý phương án và mức chi phí phù hợp trong 15 phút, hoàn toàn miễn phí.

📞 Zalo 0948 919 598
🌐 giupviecelite.vn
👥 Nhóm Zalo: https://zalo.me/g/rp4oixvilrwfy71i6yan

Elite Helpers – Trao trọn niềm tin, nâng tầm tổ ấm.

#EliteHelpers #GiupViecHaNoi #GiupViecTheoGio #HoTroGiaDinh #BaoMau #ChamSocNguoiGia'''
EN_TOP = '''Hiring home help in Vietnam? 4 rules every family should know 🏡

1️⃣ Written contract – required by Article 162 of Vietnam's 2019 Labour Code
2️⃣ Notify the ward – inform the local People's Committee when employment starts and ends
3️⃣ Insurance amount – pay the social and health insurance amount together with the salary
4️⃣ ID papers – employers must never keep a helper's identity documents

Elite Helpers guides expat families and embassies in Hanoi through every step, with English-speaking helpers and a free first consultation.'''
EN_VI = '''Thuê người giúp việc tại Việt Nam: 4 quy định gia đình cần biết 🏡

1️⃣ Ký hợp đồng bằng văn bản (Điều 162 Bộ luật Lao động 2019)
2️⃣ Thông báo UBND phường, xã khi bắt đầu và kết thúc hợp đồng
3️⃣ Trả kèm khoản BHXH, BHYT cùng kỳ trả lương
4️⃣ Không giữ giấy tờ tùy thân của người giúp việc

Elite Helpers đồng hành cùng gia đình ở từng bước, tư vấn miễn phí.'''
CAP_EN_PAGE = EN_TOP + '''

✉️ lienhe@giupviecelite.vn
🌐 giupviecelite.vn/en
🎵 tiktok.com/@giupviecelite

—————

''' + EN_VI + '''
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn

#EliteHelpers #HanoiExpats #ExpatLife #HomeHelpHanoi #GiupViecHaNoi #Hanoi'''
CAP_EN_LI = EN_TOP + '''

📩 Message us here on LinkedIn, email lienhe@giupviecelite.vn or chat on Zalo: https://zalo.me/g/rp4oixvilrwfy71i6yan
🌐 giupviecelite.vn/en · 📘 facebook.com/EliteHelpersVN · 🎵 tiktok.com/@giupviecelite

—————

''' + EN_VI + '''
📩 Nhắn tin LinkedIn, email lienhe@giupviecelite.vn hoặc Zalo: https://zalo.me/g/rp4oixvilrwfy71i6yan
🌐 giupviecelite.vn · 📘 facebook.com/EliteHelpersVN · 🎵 tiktok.com/@giupviecelite

#EliteHelpers #Hanoi #ExpatsInVietnam #HomeHelp #Vietnam'''

GROUPS = 'Group của mình + 3 nhóm Hà Nội: GIÚP VIỆC THEO GIỜ TẠI HÀ NỘI · Giúp việc tìm người – Người tìm giúp việc HN · HỘI TÌM NGƯỜI GIÚP VIỆC TẠI HÀ NỘI'
POSTS = [
 dict(day='2026-10-24', slug='tiktok-1200', when='Thứ Bảy 24/10 · 12:00', ch='TIKTOK', title='4 dấu hiệu cần người hỗ trợ',
      media=['EliteHelpers_TikTok_V7_4DauHieu.mp4'], note='Ảnh bìa: khung đầu · Video chữ, KHÔNG cần nhãn AI · Vị trí: Hà Nội', items=[('Nội dung đăng', CAP_2410_TT)]),
 dict(day='2026-10-24', slug='group-1215', when='Thứ Bảy 24/10 · 12:15', ch='FACEBOOK GROUP', title='5 câu nên hỏi khi gặp gia đình',
      media=['EliteHelpers_2410_Group_5CauHoi.jpg'], note=GROUPS, items=[('Nội dung đăng', CAP_2410_GR)]),
 dict(day='2026-10-24', slug='page-2000', when='Thứ Bảy 24/10 · 20:00 (20:15 chia sẻ sang Group)', ch='FACEBOOK PAGE', title='Ở lại hay theo giờ?',
      media=['EliteHelpers_2410_Page_OLaiTheoGio.jpg'], note='Đăng Page, 20:15 bấm Chia sẻ lên Group của mình', items=[('Nội dung đăng', CAP_2410_PG), ('Bình luận ghim', '💬 Nhắn "TƯ VẤN" hoặc Zalo 0948 919 598 để được gợi ý hình thức phù hợp nhà mình')]),
 dict(day='2026-10-25', slug='group-1215', when='Chủ nhật 25/10 · 12:15', ch='FACEBOOK GROUP', title='Hồ sơ nhận việc: 5 thứ nên có sẵn',
      media=['EliteHelpers_2510_Group_HoSoNhanViec.jpg'], note=GROUPS, items=[('Nội dung đăng', d25[0]['cap']), ('Prompt ảnh – kênh Facebook Group (tùy chọn)', d25[0]['prompt'])]),
 dict(day='2026-10-25', slug='tiktok-1900', when='Chủ nhật 25/10 · 19:00', ch='TIKTOK', title='4 điều giúp người hỗ trợ gắn bó lâu dài',
      media=['EliteHelpers_TikTok_V8_GanBoLauDai.mp4'], note='Ảnh bìa: khung đầu · Video chữ, KHÔNG cần nhãn AI · Vị trí: Hà Nội', items=[('Nội dung đăng', d25[1]['cap']), ('Prompt ảnh – kênh TikTok (tùy chọn)', d25[1]['prompt'])]),
 dict(day='2026-10-25', slug='page-2000', when='Chủ nhật 25/10 · 20:00 (20:15 chia sẻ sang Group)', ch='FACEBOOK PAGE', title='Bảng việc trong tuần',
      media=['EliteHelpers_2510_Page_BangViecTuan.jpg'], note='Đăng Page, 20:15 bấm Chia sẻ lên Group của mình', items=[('Nội dung đăng', d25[2]['cap']), ('Bình luận ghim', d25[2]['pin']), ('Prompt ảnh – kênh Facebook Page (tùy chọn)', d25[2]['prompt'])]),
 dict(day='2026-10-27', slug='page-linkedin-0900', when='Thứ Ba 27/10 · 09:00 (song ngữ)', ch='FACEBOOK PAGE + LINKEDIN', title='Hiring home help: 4 rules',
      media=['../2026-10-24/EliteHelpers_2410_Page_EN_4Rules.jpg'], note='Cùng một ảnh cho cả Page và LinkedIn. LinkedIn: không ghi số điện thoại.',
      items=[('Nội dung Facebook Page', CAP_EN_PAGE), ('Nội dung LinkedIn', CAP_EN_LI)]),
 dict(day='2026-10-25', slug='group-vin2-1930', when='Chủ nhật 25/10 · 19:30', ch='FACEBOOK GROUP + NHÓM ZALO', title='Tuyển gấp bảo mẫu chăm bé sơ sinh – Ocean Park 2',
      media=['EliteHelpers_2510_Group_TuyenBaoMau_OceanPark2.jpg'], note='Group của mình + 3 nhóm Hà Nội + nhóm Zalo việc làm. Không ghi số điện thoại của gia đình.', items=[('Nội dung đăng', '🍼 TUYỂN GẤP BẢO MẪU CHĂM BÉ SƠ SINH – VINHOMES OCEAN PARK 2\n\n📍 Văn Giang, Hưng Yên (gần Gia Lâm, Hà Nội)\n💰 Thu nhập: 18–25 triệu/tháng, tùy năng lực + thưởng tháng 13\n🏡 Ở lại cùng gia đình\n\n👶 Công việc:\n◆ Chăm bé sơ sinh 1 tháng tuổi theo phương pháp EASY\n◆ Rèn nếp sinh hoạt, chuẩn bị ăn dặm khi bé lớn hơn\n◆ Nấu 2 bữa trưa, tối cho gia đình\n\n🏠 Gia đình: 2 vợ chồng và 1 bé, bố mẹ làm việc tại nhà nên luôn có người hỗ trợ. Nhà có máy móc hỗ trợ dọn dẹp và có người dọn theo giờ hằng tuần.\n\n✅ Yêu cầu: có kinh nghiệm chăm trẻ sơ sinh, thành thạo EASY, nấu ăn ngon, yêu trẻ, quý động vật (nhà có 2 bé mèo).\n🗓 Ngày nghỉ: được gộp để về quê, trao đổi cụ thể khi phỏng vấn.\n\nElite Helpers không thu bất kỳ khoản phí nào của người lao động. Trao đổi kỹ qua Zalo, gặp gia đình trước khi nhận việc, hợp đồng rõ ràng.\n\n📲 Nhắn ngay Zalo 0948 919 598 (Elite Helpers)\n🌐 Ứng tuyển 2 phút: giupviecelite.vn/tuyen-dung\n👥 Nhóm Zalo việc làm: https://zalo.me/g/rp4oixvilrwfy71i6yan\n\n#EliteHelpers #TuyenBaoMau #ChamBeSoSinh #EASY #OceanPark #ViecLamHaNoi #GiupViecHaNoi'), ('Bình luận ghim', '📲 Chị em quan tâm nhắn Zalo 0948 919 598 kèm: họ tên, năm sinh, số năm chăm bé sơ sinh, đã làm EASY chưa. Elite Helpers gọi lại trong ngày.')]),
]

CSS = '''*{box-sizing:border-box;margin:0}body{font-family:-apple-system,"Segoe UI",Roboto,sans-serif;background:#F6F1E7;color:#14261F;padding:16px 16px 40px;max-width:640px;margin:0 auto}
.hd{display:flex;align-items:center;gap:10px;background:#1F342E;color:#FBF6EC;border-radius:14px;padding:12px 14px}.hd b{color:#E8C981;letter-spacing:.06em}
.ch{display:inline-block;margin-top:14px;background:#CBAB6D;color:#14261F;font-weight:800;letter-spacing:.08em;padding:6px 12px;border-radius:999px;font-size:14px}
h1{font-size:22px;margin-top:8px;line-height:1.3}.when{color:#5A6560;margin-top:4px;font-size:15px}.note{margin-top:10px;background:#EFE6D2;border-left:4px solid #8A6420;border-radius:8px;padding:10px 12px;font-size:14px;line-height:1.45}
.media{margin-top:16px}.media img,.media video{width:100%;border-radius:12px;display:block;background:#000}
.btn{display:block;width:100%;text-align:center;margin-top:10px;padding:14px;border-radius:12px;font-size:17px;font-weight:700;text-decoration:none;border:0;cursor:pointer;font-family:inherit}
.dl{background:#1F342E;color:#E8C981}.cp{background:#CBAB6D;color:#14261F}.cp.ok{background:#22a35a;color:#fff}
h2{font-size:17px;margin-top:22px}textarea{width:100%;margin-top:8px;border:1.5px solid #CBAB6D;border-radius:10px;padding:12px;font-size:15px;line-height:1.5;font-family:inherit;background:#fff;color:#14261F}
.tip{margin-top:18px;font-size:13px;color:#5A6560;line-height:1.5}'''
JS = '''document.querySelectorAll('.cp').forEach(b=>b.addEventListener('click',async()=>{const t=document.getElementById(b.dataset.t);
try{await navigator.clipboard.writeText(t.value)}catch(e){t.focus();t.select();t.setSelectionRange(0,99999);document.execCommand('copy')}
b.classList.add('ok');const o=b.textContent;b.textContent='✓ Đã sao chép';setTimeout(()=>{b.classList.remove('ok');b.textContent=o},2000)}));'''

def page(p):
    m = ''
    for f in p['media']:
        name = os.path.basename(f)
        tag = f'<video src="{E(f)}" controls playsinline preload="metadata"></video>' if f.endswith('.mp4') else f'<img src="{E(f)}" alt="">'
        m += f'<div class="media">{tag}<a class="btn dl" href="{E(f)}" download="{E(name)}">⬇ Tải {"video" if f.endswith(".mp4") else "ảnh"} về máy</a></div>'
    its = ''
    for i, (h, txt) in enumerate(p['items']):
        if not txt: continue
        rows = max(6, min(30, txt.count('\n') + 3))
        its += f'<h2>{E(h)}</h2><textarea id="t{i}" readonly rows="{rows}">{E(txt)}</textarea><button class="btn cp" data-t="t{i}">📋 Sao chép {E(h.lower())}</button>'
    return f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{E(p['ch'])} · {E(p['title'])}</title><style>{CSS}</style></head><body>
<div class="hd"><b>ELITE HELPERS</b><span>· Trang đăng bài</span></div>
<span class="ch">{E(p['ch'])}</span><h1>{E(p['title'])}</h1><div class="when">{E(p['when'])}</div><div class="note">{E(p['note'])}</div>
{m}{its}
<p class="tip">iPhone: bấm "Tải về máy" → chọn Tải về, ảnh/video nằm trong ứng dụng Tệp (hoặc giữ tay trên ảnh → Lưu vào Ảnh). Bấm "Sao chép" rồi dán vào ô đăng bài.</p>
<script>{JS}</script></body></html>'''

for p in POSTS:
    d = os.path.join(MEDIA, p['day']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, p['slug'] + '.html'), 'w', encoding='utf-8').write(page(p))
    print(f"https://giupviecelite.vn/media/{p['day']}/{p['slug']}.html")
