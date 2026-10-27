# -*- coding: utf-8 -*-
"""Tăng tần suất đợt 2: 1/11–4/11/2026. Bài đã hẹn giờ trước đó giữ nguyên (xem tab LichDang)."""
from week_2810 import (LINKS, JOB_LINKS, SIGN, NOFEE, GROUP_NOTE, PAGE_NOTE, PAGE_SHARE, REEL_NOTE, TT_NOTE, STYLE, P, GP, PP, TP, RP, _SC)

def V(*a, scenes, **k):
    """Bài video: cảnh ảnh dọc Meta AI dựng thành video."""
    sc = ['Imagine a vertical 9:16 photorealistic image: ' + s + _SC for s in scenes]
    a = list(a); a[12] = '\n\n'.join(f'Cảnh {i + 1}: ' + s for i, s in enumerate(sc))
    a[13] = a[13].replace('Prompt video', 'Prompt ảnh dựng video') + ' – %d cảnh' % len(sc)
    p = P(*a, **k); p['scenes'] = sc; return p

# ================= CHỦ NHẬT 1/11 =================
D01_G1 = '''Làm việc xa nhà mùa lạnh: 5 cách chị em giữ sức khỏe để yên tâm làm việc 🧣

1️⃣ Mặc ấm nhiều lớp, giữ ấm cổ, ngực và bàn chân, nhất là sáng sớm đi chợ
2️⃣ Uống đủ nước ấm, ăn đủ bữa dù bận việc
3️⃣ Ngủ đủ giấc trong giờ nghỉ đã thỏa thuận với gia đình
4️⃣ Giặt, phơi xong thì lau khô tay, tránh để quần áo ướt trên người
5️⃣ Thấy mệt, sốt, ho kéo dài: báo gia đình và đi khám sớm, đừng cố làm

💡 Chị em khỏe thì mới chăm được cho cả nhà người khác. Gia đình tử tế luôn muốn người hỗ trợ được nghỉ ngơi đúng giờ.

Elite Helpers đồng hành cùng chị em trong suốt thời gian làm việc. ''' + NOFEE + '''

''' + JOB_LINKS + '''

#EliteHelpers #SucKhoeMuaDong #ViecLamHaNoi #GiupViecHaNoi #BaoMau'''
D01_G1_P = ('Vertical 4:5. A Vietnamese woman in her late 40s with a short layered haircut, wearing a thick mustard scarf and a charcoal puffer vest, '
            'holds a warm cup of ginger tea by the kitchen window of a Hanoi house on a misty winter morning, a basket of fresh vegetables on the counter. ' + STYLE)

D01_P1 = '''Lấy chăn đông ra dùng: 5 bước làm sạch, thơm tho cho cả nhà 🛏️

1️⃣ Đọc nhãn chăn: loại nào giặt máy được, loại nào cần giặt khô (chăn lông vũ, lông cừu)
2️⃣ Giặt vỏ chăn, ga gối ở 40–60°C theo nhãn để sạch bụi, mạt
3️⃣ Ruột chăn bông: phơi nắng nhẹ 2–3 tiếng, vỗ đều cho bông tơi
4️⃣ Phơi xong để nguội rồi mới cất hoặc dùng, tránh ẩm ngược
5️⃣ Nhà có bé hoặc ông bà: thay ga mỗi tuần, hút bụi đệm mỗi tháng

💡 Chăn đông cất lâu nên lấy ra trước khi trời rét đậm 1–2 tuần để kịp giặt phơi.

Người hỗ trợ có kinh nghiệm sẽ lo trọn việc đổi mùa trong nhà. Nhắn "ĐỔI MÙA", Elite Helpers tư vấn miễn phí.

''' + LINKS + '''

''' + SIGN + '''

#EliteHelpers #MeoGiaDinh #ChanGaMuaDong #DonDepNhaCua #GiupViecHaNoi'''
D01_P1_PIN = '💬 Nhắn "ĐỔI MÙA" hoặc Zalo 0948 919 598 để được tư vấn người hỗ trợ lo việc nhà'
D01_P1_P = ('Vertical 4:5. A bright Hanoi bedroom on a cool sunny morning: a Vietnamese woman in her early 40s with a sleek low bun and a heather-grey turtleneck '
            'fluffs a thick white winter duvet on a wooden bed, folded cream bed sheets and a wicker basket nearby, sunlight through linen curtains. ' + STYLE)

D01_P2 = '''Sắp xếp tủ quần áo theo mùa: 4 bước gọn gàng, tìm là thấy 👕

1️⃣ Lấy hết đồ ra, chia 3 nhóm: mặc mùa này · cất mùa sau · cho tặng
2️⃣ Đồ mùa hè: giặt sạch, phơi khô, cho vào túi vải hoặc hộp có nắp, dán nhãn
3️⃣ Đồ mùa đông: treo áo khoác dày, gấp áo len, xếp theo từng người
4️⃣ Đặt túi chống ẩm và gỗ thơm ở góc tủ, kiểm tra lại mỗi tháng

💡 Tủ của bé nên xếp theo bộ: áo – quần – tất đặt cùng nhau, sáng đi học lấy nhanh.

Người hỗ trợ gia đình chu đáo sẽ giúp tủ đồ cả nhà luôn gọn. Nhắn "NHÀ GỌN", Elite Helpers tư vấn miễn phí.

''' + LINKS + '''

''' + SIGN + '''

#EliteHelpers #SapXepNhaCua #TuQuanAo #MeoGiaDinh #GiupViecHaNoi'''
D01_P2_PIN = '💬 Nhắn "NHÀ GỌN" hoặc Zalo 0948 919 598 để được tư vấn người hỗ trợ dọn dẹp, sắp xếp nhà'
D01_P2_P = ('Vertical 4:5. A walk-in wardrobe in a premium Hanoi apartment: a Vietnamese woman in her mid 30s with chin-length wavy hair and a camel knit cardigan '
            'places labeled linen storage boxes on an upper shelf while winter coats hang neatly below, warm wood shelves, soft lighting. ' + STYLE)

D01_T1 = '''Lấy chăn đông ra dùng: 5 bước làm sạch 🛏️
Đọc nhãn · giặt vỏ chăn 40–60°C · phơi ruột chăn · để nguội mới cất · thay ga mỗi tuần.
Elite Helpers kết nối người hỗ trợ gia đình tại Hà Nội.
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn
#EliteHelpers #MeoGiaDinh #ChanGaMuaDong #GiupViecHaNoi #HaNoi'''
D01_G2 = '''Nấu cháo ăn dặm cho bé: 4 nguyên tắc vệ sinh bảo mẫu nào cũng cần nhớ 🥣

1️⃣ Rửa tay bằng xà phòng trước khi sơ chế và trước khi cho bé ăn
2️⃣ Thớt, dao riêng cho đồ sống và đồ chín; dụng cụ của bé tráng nước sôi
3️⃣ Nấu chín kỹ, để nguội vừa ăn; thử nhiệt độ bằng mu bàn tay
4️⃣ Cháo thừa sau bữa không cho bé ăn lại; phần nấu sẵn cất ngăn mát, dùng trong ngày

💡 Thực đơn, độ đặc loãng và món mới cho bé: luôn làm theo hướng dẫn của bố mẹ và bác sĩ dinh dưỡng của bé.

Elite Helpers ưu tiên chị em có kinh nghiệm chăm bé ăn dặm. ''' + NOFEE + '''

''' + JOB_LINKS + '''

#EliteHelpers #BaoMau #AnDam #KyNangChamTre #ViecLamHaNoi'''
D01_G2_P = ('Vertical 4:5. A clean bright kitchen with sage tiles: a Vietnamese nanny in her early 30s with a neat French braid and a dusty-blue sweater '
            'stirs a small pot of rice porridge while a separate color-coded cutting board set and sterilized baby bowls sit on the counter. ' + STYLE)
D01_T2 = '''Sắp xếp tủ quần áo theo mùa: 4 bước 👕
Chia 3 nhóm · đồ hè vào hộp có nhãn · đồ đông treo và gấp theo người · túi chống ẩm.
Elite Helpers kết nối người hỗ trợ gia đình tại Hà Nội.
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn
#EliteHelpers #SapXepNhaCua #MeoGiaDinh #GiupViecHaNoi'''
D01_T3 = '''Cháo ăn dặm cho bé: 4 nguyên tắc vệ sinh 🥣
Rửa tay · thớt dao riêng · nấu chín, thử nhiệt độ · không cho bé ăn lại cháo thừa.
Elite Helpers đồng hành cùng chị em, không thu phí người lao động.
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn/tuyen-dung
#EliteHelpers #BaoMau #AnDam #ViecLamHaNoi'''

# ================= THỨ HAI 2/11 =================
D02_G1 = '''Làm việc với ông bà khó tính: 5 câu nói giúp chị em ghi điểm ngay từ tuần đầu 👵

1️⃣ "Dạ, bà chỉ cho cháu cách bà thích nhé" – hỏi trước khi làm theo ý mình
2️⃣ "Cháu làm thế này đã vừa ý ông chưa ạ?" – hỏi lại sau mỗi việc mới
3️⃣ "Dạ, cháu nhớ rồi, lần sau cháu sửa" – nhận góp ý nhẹ nhàng, không cãi
4️⃣ "Ông kể tiếp chuyện hồi xưa cho cháu nghe đi ạ" – dành thời gian trò chuyện
5️⃣ "Cháu báo con ông bà một chút để cả nhà cùng biết ạ" – việc lớn thì báo gia chủ

💡 Ông bà khó tính thường vì muốn mọi việc đúng nếp cũ. Kiên nhẫn 1–2 tuần, chị em sẽ được quý mến.

Elite Helpers giới thiệu kỹ tính cách, thói quen của ông bà trước khi chị em nhận việc. ''' + NOFEE + '''

''' + JOB_LINKS + '''

#EliteHelpers #ChamSocNguoiGia #KinhNghiemLamViec #GiupViecHaNoi #ViecLamHaNoi'''
D02_G1_P = ('Vertical 4:5. In a traditional Hanoi tube house living room with wooden furniture, a patient Vietnamese woman in her mid 40s with a long low ponytail '
            'and a forest-green cardigan listens attentively to a stern-looking elderly grandmother in a lavender áo bà ba who points at a teapot set, morning light. ' + STYLE)

D02_P1 = '''Đầu tuần họp 10 phút với người hỗ trợ: 4 nội dung giúp cả tuần trơn tru 🗓️

1️⃣ Lịch cả nhà tuần này: ai đi công tác, bé thi, ông bà đi khám
2️⃣ Thực đơn tuần và danh sách đi chợ
3️⃣ Việc đặc biệt: dọn kho, giặt rèm, đón khách
4️⃣ Góp ý hai chiều: tuần trước điều gì tốt, điều gì cần chỉnh

💡 Họp cùng một giờ mỗi sáng thứ Hai, ghi ra một tờ giấy dán ở bếp. Người hỗ trợ chủ động hơn, bố mẹ đỡ phải nhắc.

Elite Helpers hướng dẫn gia đình cách giao việc rõ ràng ngay từ ngày đầu. Nhắn "GIAO VIỆC" để được tư vấn miễn phí.

''' + LINKS + '''

''' + SIGN + '''

#EliteHelpers #QuanLyGiaDinh #KinhNghiemThueGiupViec #GiupViecHaNoi #HoTroGiaDinh'''
D02_P1_PIN = '💬 Nhắn "GIAO VIỆC" hoặc Zalo 0948 919 598 để nhận mẫu họp đầu tuần với người hỗ trợ'
D02_P1_P = ('Vertical 4:5. Monday morning at a marble kitchen island in a Hanoi apartment: a Vietnamese mother in her late 30s with a sharp bob in a navy blouse '
            'and a warm Vietnamese woman in her early 50s with grey-streaked hair in a knot and a maroon knit top review a weekly planner sheet together over coffee. ' + STYLE)

D02_P2 = '''Bàn giao lịch uống thuốc, lịch khám của ông bà cho người chăm sóc: 5 điều gia đình nên làm 💊

1️⃣ Lập bảng: tên thuốc, liều, giờ uống theo đúng đơn bác sĩ; dán ở chỗ dễ thấy
2️⃣ Dùng hộp chia thuốc theo ngày, gia đình chuẩn bị sẵn mỗi tuần
3️⃣ Ghi lịch tái khám, số điện thoại bác sĩ và người thân cần gọi khi cấp cứu
4️⃣ Dặn rõ những dấu hiệu cần báo ngay: chóng mặt, khó thở, ngã, bỏ ăn
5️⃣ Người chăm sóc không tự ý thêm, bớt hay đổi thuốc

💡 Việc dùng thuốc luôn theo chỉ định của bác sĩ. Người chăm sóc giúp nhắc giờ, ghi sổ và báo gia đình.

Elite Helpers kết nối người chăm sóc ông bà cẩn thận, biết ghi chép. Nhắn "ÔNG BÀ" để được tư vấn miễn phí.

''' + LINKS + '''

''' + SIGN + '''

#EliteHelpers #ChamSocNguoiGia #OngBa #NguoiCaoTuoi #GiupViecHaNoi'''
D02_P2_PIN = '💬 Nhắn "ÔNG BÀ" hoặc Zalo 0948 919 598 để được tư vấn người chăm sóc ông bà tại nhà'
D02_P2_P = ('Vertical 4:5. In a calm Hanoi living room, a Vietnamese daughter in her early 40s with long hair tucked behind ears and a beige trench sweater shows a '
            'weekly pill organizer and a handwritten schedule card to a kind caregiver in her late 40s with a short curly bob and an olive quilted vest; '
            'an elderly grandfather reads a newspaper in an armchair behind them. ' + STYLE)
D02_T1 = '''Đầu tuần họp 10 phút với người hỗ trợ 🗓️
Lịch cả nhà · thực đơn tuần · việc đặc biệt · góp ý hai chiều. Ghi ra tờ giấy dán ở bếp.
Elite Helpers kết nối người hỗ trợ hợp nếp nhà tại Hà Nội.
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn
#EliteHelpers #QuanLyGiaDinh #GiaDinh #GiupViecHaNoi #HaNoi'''
D02_T2 = '''Ông bà khó tính: 5 câu nói giúp chị em ghi điểm 👵
Hỏi cách ông bà thích · hỏi lại sau việc mới · nhận góp ý nhẹ nhàng · trò chuyện · việc lớn báo gia chủ.
Elite Helpers đồng hành cùng chị em, không thu phí người lao động.
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn/tuyen-dung
#EliteHelpers #ChamSocNguoiGia #KinhNghiemLamViec #ViecLamHaNoi'''

# ================= THỨ BA 3/11 (song ngữ) =================
D03_G1 = '''Trải giường, gấp khăn chuẩn khách sạn: 4 bước nhỏ, gia chủ khen ngay 🛎️

1️⃣ Ga bọc đệm: kéo căng 4 góc, góc giường gấp vuông như phong bì
2️⃣ Chăn: đặt cách đầu giường một gang tay, gập mép trên xuống 20–30 cm
3️⃣ Gối: vỗ phồng, xếp gối lớn phía sau, gối nhỏ phía trước
4️⃣ Khăn tắm: gấp ba theo chiều dọc rồi cuộn hoặc gấp đôi, xếp cùng chiều trên kệ

💡 Làm giống nhau mỗi ngày, phòng ngủ luôn gọn đẹp như khách sạn. Đây là kỹ năng được các gia đình cao cấp đánh giá cao.

Elite Helpers kết nối chị em với các gia đình cao cấp tại Hà Nội. ''' + NOFEE + '''

''' + JOB_LINKS + '''

#EliteHelpers #KyNangDonPhong #QuanGia #GiupViecHaNoi #ViecLamHaNoi'''
D03_G1_P = ('Vertical 4:5. An elegant master bedroom in a Hanoi villa: a young Vietnamese woman in her late 20s with a sleek high ponytail and a soft white '
            'long-sleeve top smooths a crisp white duvet with a neat folded hem, rolled towels stacked on a walnut bench, brass bedside lamps. ' + STYLE)

D03_P1 = '''Mẹ đi làm lại sau sinh: lộ trình 2 tuần bàn giao bé cho bảo mẫu, mẹ yên tâm, bé quen dần 👶

📅 TUẦN 1
◆ Ngày 1–2: bảo mẫu quan sát mẹ chăm bé, ghi nếp ăn ngủ
◆ Ngày 3–4: bảo mẫu cho bé ăn, tắm, mẹ ở bên cạnh
◆ Ngày 5–7: mẹ ra ngoài 2–3 tiếng, bảo mẫu nhắn tin cập nhật

📅 TUẦN 2
◆ Mẹ đi làm nửa ngày, bảo mẫu chăm trọn ca
◆ Cuối tuần: cả nhà cùng xem sổ ghi chép, chỉnh lại nếp

💡 Bé quen người mới cần thời gian. Bắt đầu trước ngày đi làm ít nhất 2 tuần là đẹp nhất.

Elite Helpers kết nối bảo mẫu có kinh nghiệm chăm bé dưới 1 tuổi. Nhắn "BẢO MẪU" để được tư vấn miễn phí.

''' + LINKS + '''

''' + SIGN + '''

#EliteHelpers #BaoMau #MeDiLam #ChamBe #GiupViecHaNoi'''
D03_P1_PIN = '💬 Nhắn "BẢO MẪU" hoặc Zalo 0948 919 598 để được tư vấn bảo mẫu phù hợp với bé'
D03_P1_P = ('Vertical 4:5. A sunlit Hanoi nursery: a young Vietnamese mother in her early 30s in a smart grey blazer ready for work hands her smiling 8-month-old '
            'baby to a gentle nanny in her late 30s with a soft wavy bob and a lilac cardigan, a wooden crib and a notebook on a dresser. ' + STYLE)

D03_G2 = '''Bảo quản thực phẩm tươi sống đúng cách: tủ mát, tủ đông chị em cần nhớ 🥩

❄️ NGĂN ĐÔNG (≤ -18°C)
◆ Chia thịt, cá thành phần vừa nấu 1 bữa, cho vào túi hoặc hộp kín
◆ Ghi ngày cấp đông lên túi
◆ Rã đông bằng ngăn mát từ tối hôm trước, không rã đông ngoài bàn cả buổi

🥬 NGĂN MÁT (khoảng 0–5°C)
◆ Rau lau khô, bọc giấy rồi cho vào hộp
◆ Đồ sống để ngăn dưới, đồ chín để ngăn trên
◆ Thực phẩm đã rã đông không cấp đông lại

💡 Gia chủ yên tâm nhất khi bếp sạch và thực phẩm luôn tươi. Đây là điểm cộng lớn khi phỏng vấn.

Elite Helpers kết nối chị em với các gia đình tốt tại Hà Nội. ''' + NOFEE + '''

''' + JOB_LINKS + '''

#EliteHelpers #AnToanThucPham #KinhNghiemLamViec #GiupViecHaNoi #ViecLamHaNoi'''
D03_G2_P = ('Vertical 4:5. A modern Hanoi kitchen: a Vietnamese woman in her early 40s with a shoulder-length straight cut and a teal knit top portions fresh '
            'fish and pork into labeled glass containers beside an open freezer drawer, a roll of labels and a marker on the counter. ' + STYLE)

D03_EN = '''Hosting a dinner at home in Hanoi? 5 ways your helper can make it effortless 🍷

1️⃣ Agree on the menu and guest count 3 days ahead
2️⃣ Prep vegetables, sauces and desserts the day before
3️⃣ Set the table together once, take a photo as the standard
4️⃣ During dinner: refill water, clear plates quietly between courses
5️⃣ After guests leave: kitchen first, living room the next morning

Elite Helpers connects expat families in Hanoi with experienced helpers and family cooks, including English-speaking options.'''
D03_VI = '''Mở tiệc tại nhà: 5 cách người hỗ trợ giúp buổi tối thật nhẹ nhàng 🍷

1️⃣ Chốt thực đơn và số khách trước 3 ngày
2️⃣ Sơ chế rau, nước sốt, món tráng miệng từ hôm trước
3️⃣ Bày bàn mẫu một lần, chụp ảnh làm chuẩn
4️⃣ Trong bữa: rót nước, thu dọn đĩa nhẹ nhàng giữa các món
5️⃣ Khách về: dọn bếp trước, phòng khách để sáng hôm sau

Elite Helpers kết nối người hỗ trợ và đầu bếp gia đình có kinh nghiệm.'''
D03_P2 = D03_EN + '''

✉️ lienhe@giupviecelite.vn · 🌐 giupviecelite.vn/en

—————

''' + D03_VI + '''

''' + LINKS + '''

#EliteHelpers #HanoiExpats #DinnerParty #DauBepGiaDinh #GiupViecHaNoi'''
D03_P2_PIN = '💬 Message us or Zalo 0948 919 598 · Nhắn "ĐẦU BẾP" để được tư vấn đầu bếp gia đình'
D03_P2_P = ('Vertical 4:5. An elegant dining room in a Tay Ho villa set for a dinner party: a European couple in their 40s welcome guests while a poised '
            'Vietnamese woman in her late 30s with a neat chignon and a black knit top arranges a platter of spring rolls on a long candlelit table, '
            'deep green walls, brass candlesticks. ' + STYLE)

D03_T1 = '''Mẹ đi làm lại: lộ trình 2 tuần bàn giao bé cho bảo mẫu 👶
Quan sát · làm cùng mẹ · mẹ ra ngoài 2–3 tiếng · đi làm nửa ngày · cùng xem sổ ghi chép.
Elite Helpers kết nối bảo mẫu có kinh nghiệm tại Hà Nội.
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn
#EliteHelpers #BaoMau #MeDiLam #ChamBe #HaNoi'''
D03_T2 = '''Hosting at home: 5 ways your helper helps 🍷 Mở tiệc tại nhà nhẹ nhàng hơn
Menu 3 days ahead · prep the day before · photo of the table · quiet service · kitchen first.
Elite Helpers · Hanoi · lienhe@giupviecelite.vn · Zalo 0948 919 598
#EliteHelpers #HanoiExpats #DinnerParty #GiupViecHaNoi'''

# ================= THỨ TƯ 4/11 =================
D04_G1 = '''BHXH, BHYT của người giúp việc gia đình: ai trả, chị em tham gia thế nào? 🩺

Theo Bộ luật Lao động 2019 (Chương XI về lao động giúp việc gia đình):

1️⃣ Gia đình trả cho chị em khoản tiền bảo hiểm xã hội, bảo hiểm y tế theo quy định, cùng kỳ trả lương
2️⃣ Chị em dùng khoản này để tự tham gia BHXH tự nguyện và mua BHYT (thường theo hộ gia đình tại nơi cư trú)
3️⃣ Khoản tiền này nên ghi rõ trong hợp đồng: số tiền mỗi tháng, ngày trả
4️⃣ Từ 10/9/2026, theo Nghị định 283/2026/NĐ-CP, gia chủ không trả khoản này có thể bị phạt 10–15 triệu đồng và phải truy trả đủ

📌 Mẹo nhỏ: giữ biên nhận đóng BHXH, BHYT. Khi ốm đau cần khám chữa bệnh, thẻ BHYT giúp chị em đỡ rất nhiều chi phí.

Ở Elite Helpers, khoản BHXH, BHYT được trao đổi rõ và ghi vào hợp đồng trước khi nhận việc. ''' + NOFEE + '''

''' + JOB_LINKS + '''

#EliteHelpers #QuyenLoiNguoiLaoDong #BHYT #BHXH #GiupViecHaNoi'''
D04_G1_P = ('Vertical 4:5. At a ward service counter in Hanoi, a Vietnamese woman in her late 40s with shoulder-length hair clipped back and a rust-orange '
            'cardigan smiles holding a newly issued health insurance card and a receipt, a folder of documents under her arm, bright modern office. ' + STYLE)

D04_P1 = '''Bé biếng ăn: 5 điều bố mẹ và bảo mẫu nên thống nhất để bữa ăn nhẹ nhàng hơn 🍚

1️⃣ Giờ ăn cố định, mỗi bữa khoảng 30 phút, hết giờ thì dọn
2️⃣ Không vừa ăn vừa xem điện thoại, tivi
3️⃣ Không ép, không dọa; khen khi bé tự xúc
4️⃣ Đổi món, đổi cách chế biến; cho bé cùng nhặt rau, bày đĩa
5️⃣ Ghi sổ lượng ăn mỗi ngày để cả nhà cùng theo dõi

💡 Bé sụt cân, mệt mỏi hay biếng ăn kéo dài, bố mẹ nên cho bé đi khám bác sĩ nhi để được tư vấn.

Bảo mẫu có kinh nghiệm sẽ cùng bố mẹ giữ một cách làm thống nhất. Nhắn "BẢO MẪU" để được tư vấn miễn phí.

''' + LINKS + '''

''' + SIGN + '''

#EliteHelpers #BeBiengAn #BaoMau #ChamBe #GiupViecHaNoi'''
D04_P1_PIN = '💬 Nhắn "BẢO MẪU" hoặc Zalo 0948 919 598 để được tư vấn bảo mẫu có kinh nghiệm chăm bé'
D04_P1_P = ('Vertical 4:5. A cheerful Hanoi dining nook: a 3-year-old Vietnamese boy in a yellow sweater proudly feeds himself with a small spoon at a toddler table '
            'while a kind nanny in her mid 30s with a curly pixie cut and a coral sweater claps softly beside him, colorful small bowls, no screens. ' + STYLE)

D04_P2 = '''Lắp camera trong nhà khi có người hỗ trợ: dùng đúng luật, giữ được niềm tin 📹

1️⃣ Thông báo rõ cho người hỗ trợ có camera và vị trí lắp, tốt nhất ghi trong hợp đồng
2️⃣ Chỉ lắp ở khu vực chung: phòng khách, bếp, lối vào, phòng chơi của bé
3️⃣ Không lắp trong phòng ngủ riêng, nhà tắm, nhà vệ sinh của người hỗ trợ
4️⃣ Hình ảnh chỉ để gia đình theo dõi, không đăng lên mạng hay chia sẻ cho người khác
5️⃣ Có vấn đề thì trao đổi trực tiếp, bình tĩnh, dựa trên sự việc

⚖️ Bộ luật Dân sự 2015 (Điều 38) bảo vệ quyền về đời sống riêng tư; hình ảnh của một người là dữ liệu cá nhân theo Luật Bảo vệ dữ liệu cá nhân (hiệu lực từ 1/1/2026).

💡 Camera giúp gia đình yên tâm; sự minh bạch giúp người hỗ trợ yên tâm. Hai bên cùng tôn trọng thì gắn bó lâu dài.

Elite Helpers tư vấn gia đình thỏa thuận rõ ràng trước khi người hỗ trợ bắt đầu làm việc. Nhắn "HỢP ĐỒNG" để được tư vấn miễn phí.

''' + LINKS + '''

''' + SIGN + '''

#EliteHelpers #AnTamTaiNha #KinhNghiemThueGiupViec #GiupViecHaNoi #HoTroGiaDinh'''
D04_P2_PIN = '💬 Nhắn "HỢP ĐỒNG" hoặc Zalo 0948 919 598 để được tư vấn thỏa thuận khi lắp camera'
D04_P2_P = ('Vertical 4:5. A bright Hanoi apartment living room with a small white security camera mounted high in a corner: a Vietnamese father in his early 40s '
            'in a grey polo explains a printed agreement to a relaxed Vietnamese woman in her early 40s with a low bun and a sage-green linen shirt, '
            'both seated on a sofa, toys neatly stored. ' + STYLE)

D04_T1 = '''Bé biếng ăn: 5 điều bố mẹ và bảo mẫu nên thống nhất 🍚
Giờ ăn cố định · không màn hình · không ép · đổi món, cho bé cùng làm · ghi sổ lượng ăn.
Elite Helpers kết nối bảo mẫu tận tâm tại Hà Nội.
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn
#EliteHelpers #BeBiengAn #BaoMau #ChamBe #HaNoi'''
D04_REEL = '''Chiều đón bé, tối cơm ấm 🌇

Bố mẹ về đến nhà, bé đã tắm thơm, bữa cơm đã dọn, ông bà có người trò chuyện. Nhịp sống ấy đến từ một người hỗ trợ hợp nếp nhà, tận tâm và đáng tin.

Elite Helpers kết nối gia đình Hà Nội với người hỗ trợ phù hợp. Nhắn "TƯ VẤN" để được gợi ý miễn phí.

''' + LINKS + '''

''' + SIGN + '''

#EliteHelpers #GiaDinhHaNoi #BuaComGiaDinh #BaoMau #GiupViecHaNoi'''
D04_REEL_PIN = '💬 Nhắn "TƯ VẤN" hoặc Zalo 0948 919 598, Elite Helpers gợi ý người hỗ trợ hợp nếp nhà trong 15 phút'
D04_T2 = '''BHXH, BHYT của người giúp việc: ai trả? 🩺
Gia đình trả khoản BHXH, BHYT cùng kỳ lương để chị em tự tham gia (BLLĐ 2019). Không trả có thể bị phạt 10–15 triệu (NĐ 283/2026).
Elite Helpers: hợp đồng rõ ràng, không thu phí người lao động.
📞 Zalo 0948 919 598 · 🌐 giupviecelite.vn/tuyen-dung
#EliteHelpers #BHYT #QuyenLoiNguoiLaoDong #ViecLamHaNoi'''

POSTS = [
 # 1/11
 P('2026-11-01','group-0700','Chủ nhật 1/11 · 07:00','FACEBOOK GROUP','Giữ sức khỏe khi làm việc xa nhà mùa lạnh','EliteHelpers_0111_Group_SucKhoe.jpg','page',
   'SỨC KHỎE CHỊ EM','Làm việc xa nhà mùa lạnh','5 cách giữ sức khỏe',GROUP_NOTE,D01_G1,D01_G1_P,GP,chips=['Mặc ấm nhiều lớp','Ăn đủ bữa','Mệt thì báo sớm']),
 P('2026-11-01','page-0730','Chủ nhật 1/11 · 07:30','FACEBOOK PAGE','Chăn đông: 5 bước làm sạch','EliteHelpers_0111_Page_ChanDong.jpg','page',
   'ĐỔI MÙA','Lấy chăn đông ra dùng','5 bước làm sạch, thơm tho',PAGE_NOTE,D01_P1,D01_P1_P,PP,pin=D01_P1_PIN,chips=['Đọc nhãn','Giặt 40–60°C','Phơi ruột chăn']),
 P('2026-11-01','page-1130','Chủ nhật 1/11 · 11:30','FACEBOOK PAGE','Tủ quần áo theo mùa: 4 bước','EliteHelpers_0111_Page_TuDo.jpg','page',
   'MẸO NHÀ CỬA','Tủ quần áo theo mùa','4 bước gọn gàng',PAGE_NOTE,D01_P2,D01_P2_P,PP,pin=D01_P2_PIN,chips=['Chia 3 nhóm','Hộp có nhãn','Túi chống ẩm']),
 V('2026-11-01','tiktok-1200','Chủ nhật 1/11 · 12:00','TIKTOK','Chăn đông: 5 bước (video)','EliteHelpers_TikTok_0111_ChanDong.mp4','tiktok',
   'ĐỔI MÙA','Lấy chăn đông ra dùng','5 bước làm sạch',TT_NOTE,D01_T1,'',TP,points=['Đọc nhãn chăn','Giặt vỏ chăn 40–60°C','Phơi ruột chăn, vỗ tơi','Để nguội mới cất','Thay ga mỗi tuần'],
   scenes=['A Vietnamese woman in her early 40s with a sleek low bun and a heather-grey turtleneck fluffs a thick white winter duvet on a wooden bed in a bright Hanoi bedroom.',
           'Close-up of a duvet cover care label and neatly folded fresh cream bed sheets in a wicker basket on a sunny balcony with a clothes rack.']),
 P('2026-11-01','group-1215','Chủ nhật 1/11 · 12:15','FACEBOOK GROUP','Cháo ăn dặm: 4 nguyên tắc vệ sinh','EliteHelpers_0111_Group_AnDam.jpg','page',
   'KỸ NĂNG CHĂM TRẺ','Cháo ăn dặm cho bé','4 nguyên tắc vệ sinh',GROUP_NOTE,D01_G2,D01_G2_P,GP,chips=['Rửa tay','Thớt dao riêng','Không ăn lại cháo thừa']),
 V('2026-11-01','tiktok-1900','Chủ nhật 1/11 · 19:00','TIKTOK','Tủ quần áo theo mùa (video)','EliteHelpers_TikTok_0111_TuDo.mp4','tiktok',
   'MẸO NHÀ CỬA','Tủ quần áo theo mùa','4 bước gọn gàng',TT_NOTE,D01_T2,'',TP,points=['Chia 3 nhóm đồ','Đồ hè vào hộp có nhãn','Đồ đông treo, gấp theo người','Túi chống ẩm, gỗ thơm'],
   scenes=['A Vietnamese woman in her mid 30s with chin-length wavy hair and a camel knit cardigan places labeled linen storage boxes on an upper shelf of a walk-in wardrobe.',
           'Neatly arranged winter coats and folded sweaters sorted by family member in a warm wooden wardrobe, a small sachet of cedar blocks in the corner.']),
 V('2026-11-01','tiktok-2130','Chủ nhật 1/11 · 21:30','TIKTOK','Cháo ăn dặm: 4 nguyên tắc (video)','EliteHelpers_TikTok_0111_AnDam.mp4','tiktok',
   'KỸ NĂNG CHĂM TRẺ','Cháo ăn dặm cho bé','4 nguyên tắc vệ sinh',TT_NOTE,D01_T3,'',TP,points=['Rửa tay trước khi nấu','Thớt dao riêng sống, chín','Nấu chín, thử nhiệt độ','Không ăn lại cháo thừa'],
   scenes=['A Vietnamese nanny in her early 30s with a neat French braid and a dusty-blue sweater washes her hands at a kitchen sink with sage tiles.',
           'A Vietnamese nanny in her early 30s with a neat French braid and a dusty-blue sweater gently feeds a 9-month-old baby in a high chair with a small spoon of warm rice porridge, a sterilized baby bowl on the tray.']),
 # 2/11
 P('2026-11-02','group-0700','Thứ Hai 2/11 · 07:00','FACEBOOK GROUP','Ông bà khó tính: 5 câu nói ghi điểm','EliteHelpers_0211_Group_OngBaKhoTinh.jpg','page',
   'CHĂM SÓC ÔNG BÀ','Ông bà khó tính','5 câu nói giúp ghi điểm',GROUP_NOTE,D02_G1,D02_G1_P,GP,chips=['Hỏi trước khi làm','Nhận góp ý','Trò chuyện']),
 P('2026-11-02','page-0730','Thứ Hai 2/11 · 07:30','FACEBOOK PAGE','Họp 10 phút đầu tuần','EliteHelpers_0211_Page_HopDauTuan.jpg','page',
   'QUẢN LÝ GIA ĐÌNH','Họp 10 phút đầu tuần','4 nội dung cho cả tuần',PAGE_NOTE,D02_P1,D02_P1_P,PP,pin=D02_P1_PIN,chips=['Lịch cả nhà','Thực đơn tuần','Góp ý hai chiều']),
 P('2026-11-02','page-1130','Thứ Hai 2/11 · 11:30','FACEBOOK PAGE','Bàn giao lịch thuốc, lịch khám của ông bà','EliteHelpers_0211_Page_LichThuoc.jpg','page',
   'CHĂM SÓC ÔNG BÀ','Bàn giao lịch thuốc','5 điều gia đình nên làm',PAGE_NOTE,D02_P2,D02_P2_P,PP,pin=D02_P2_PIN,chips=['Theo đơn bác sĩ','Hộp chia thuốc','Dấu hiệu cần báo']),
 V('2026-11-02','tiktok-1200','Thứ Hai 2/11 · 12:00','TIKTOK','Họp 10 phút đầu tuần (video)','EliteHelpers_TikTok_0211_HopDauTuan.mp4','tiktok',
   'QUẢN LÝ GIA ĐÌNH','Họp 10 phút đầu tuần','4 nội dung cho cả tuần',TT_NOTE,D02_T1,'',TP,points=['Lịch cả nhà tuần này','Thực đơn, đi chợ','Việc đặc biệt','Góp ý hai chiều'],
   scenes=['A Vietnamese mother in her late 30s with a sharp bob in a navy blouse and a warm woman in her early 50s with grey-streaked hair in a knot review a weekly planner at a marble kitchen island over coffee.',
           'Close-up of a handwritten weekly plan sheet with a menu list pinned on a kitchen cork board, morning light.']),
 V('2026-11-02','tiktok-2130','Thứ Hai 2/11 · 21:30','TIKTOK','Ông bà khó tính (video)','EliteHelpers_TikTok_0211_OngBa.mp4','tiktok',
   'CHĂM SÓC ÔNG BÀ','Ông bà khó tính','5 câu nói giúp ghi điểm',TT_NOTE,D02_T2,'',TP,points=['Hỏi cách ông bà thích','Hỏi lại sau việc mới','Nhận góp ý nhẹ nhàng','Dành thời gian trò chuyện','Việc lớn báo gia chủ'],
   scenes=['A patient Vietnamese woman in her mid 40s with a long low ponytail and a forest-green cardigan listens to a stern elderly grandmother in a lavender áo bà ba in a traditional Hanoi living room.',
           'A Vietnamese woman in her mid 40s with a long low ponytail and a forest-green cardigan and an elderly grandmother in a lavender áo bà ba laugh together while pouring tea from a clay teapot at a wooden table.']),
 # 3/11
 P('2026-11-03','group-0700','Thứ Ba 3/11 · 07:00','FACEBOOK GROUP','Trải giường, gấp khăn chuẩn khách sạn','EliteHelpers_0311_Group_TraiGiuong.jpg','page',
   'KỸ NĂNG DỌN PHÒNG','Chuẩn khách sạn','4 bước trải giường, gấp khăn',GROUP_NOTE,D03_G1,D03_G1_P,GP,chips=['Góc phong bì','Gập mép chăn','Khăn cùng chiều']),
 P('2026-11-03','page-1130','Thứ Ba 3/11 · 11:30','FACEBOOK PAGE','Mẹ đi làm lại: lộ trình 2 tuần','EliteHelpers_0311_Page_MeDiLam.jpg','page',
   'CHĂM BÉ','Mẹ đi làm lại','lộ trình 2 tuần bàn giao bé',PAGE_NOTE,D03_P1,D03_P1_P,PP,pin=D03_P1_PIN,chips=['Quan sát','Làm cùng mẹ','Nửa ngày']),
 V('2026-11-03','tiktok-1200','Thứ Ba 3/11 · 12:00','TIKTOK','Mẹ đi làm lại (video)','EliteHelpers_TikTok_0311_MeDiLam.mp4','tiktok',
   'CHĂM BÉ','Mẹ đi làm lại','lộ trình 2 tuần',TT_NOTE,D03_T1,'',TP,points=['Ngày 1–2: quan sát','Ngày 3–4: làm cùng mẹ','Ngày 5–7: mẹ ra ngoài','Tuần 2: đi làm nửa ngày'],
   scenes=['A young Vietnamese mother in her early 30s in a grey blazer cuddles her 8-month-old baby while a gentle nanny in her late 30s with a soft wavy bob and lilac cardigan watches and takes notes in a sunlit nursery.',
           'A gentle Vietnamese nanny in her late 30s with a soft wavy bob and lilac cardigan happily holds a smiling baby by the window while a young mother in a grey blazer waves goodbye at the nursery door with her work bag.']),
 P('2026-11-03','group-1215','Thứ Ba 3/11 · 12:15','FACEBOOK GROUP','Bảo quản thực phẩm tươi sống','EliteHelpers_0311_Group_BaoQuan.jpg','page',
   'AN TOÀN THỰC PHẨM','Bảo quản thực phẩm','tủ mát, tủ đông đúng cách',GROUP_NOTE,D03_G2,D03_G2_P,GP,chips=['Chia phần 1 bữa','Ghi ngày','Không cấp đông lại']),
 P('2026-11-03','page-2000','Thứ Ba 3/11 · 20:00 song ngữ (20:15 chia sẻ sang Group)','FACEBOOK PAGE','Hosting at home: 5 ways','EliteHelpers_0311_Page_TiecTaiGia_EN.jpg','page',
   'FOR EXPAT FAMILIES','Hosting at home','5 ways your helper can help',PAGE_SHARE,D03_P2,D03_P2_P,PP,pin=D03_P2_PIN,sub='Mở tiệc tại nhà: 5 cách người hỗ trợ giúp bạn',chips=['Menu 3 days ahead','Prep the day before','Quiet service']),
 V('2026-11-03','tiktok-2130','Thứ Ba 3/11 · 21:30 song ngữ','TIKTOK','Hosting at home (video)','EliteHelpers_TikTok_0311_TiecTaiGia_EN.mp4','tiktok',
   'FOR EXPAT FAMILIES','Hosting at home','5 ways your helper helps',TT_NOTE,D03_T2,'',TP,sub='Mở tiệc tại nhà nhẹ nhàng hơn',points=['Menu 3 days ahead','Prep the day before','Photo of the table setup','Quiet service','Kitchen first'],
   scenes=['A poised Vietnamese woman in her late 30s with a neat chignon and a black knit top arranges a platter of fresh spring rolls in a Tay Ho villa kitchen before a dinner party.',
           'A long candlelit dinner table with deep green walls and brass candlesticks, a European couple in their 40s laughing with guests.']),
 # 4/11
 P('2026-11-04','group-0700','Thứ Tư 4/11 · 07:00','FACEBOOK GROUP','BHXH, BHYT của người giúp việc','EliteHelpers_0411_Group_BHYT.jpg','page',
   'QUYỀN LỢI NGƯỜI LAO ĐỘNG','BHXH, BHYT','ai trả, chị em tham gia thế nào?',GROUP_NOTE,D04_G1,D04_G1_P,GP,chips=['Trả cùng kỳ lương','Ghi trong hợp đồng','NĐ 283/2026']),
 P('2026-11-04','page-0730','Thứ Tư 4/11 · 07:30','FACEBOOK PAGE','Bé biếng ăn: 5 điều thống nhất','EliteHelpers_0411_Page_BiengAn.jpg','page',
   'CHĂM BÉ','Bé biếng ăn','5 điều bố mẹ và bảo mẫu thống nhất',PAGE_NOTE,D04_P1,D04_P1_P,PP,pin=D04_P1_PIN,chips=['Giờ ăn cố định','Không màn hình','Không ép']),
 P('2026-11-04','page-1130','Thứ Tư 4/11 · 11:30','FACEBOOK PAGE','Camera trong nhà: đúng luật, giữ niềm tin','EliteHelpers_0411_Page_Camera.jpg','page',
   'AN TÂM TẠI NHÀ','Camera trong nhà','dùng đúng luật, giữ niềm tin',PAGE_NOTE,D04_P2,D04_P2_P,PP,pin=D04_P2_PIN,chips=['Thông báo rõ','Khu vực chung','Không chia sẻ']),
 V('2026-11-04','tiktok-1200','Thứ Tư 4/11 · 12:00','TIKTOK','Bé biếng ăn (video)','EliteHelpers_TikTok_0411_BiengAn.mp4','tiktok',
   'CHĂM BÉ','Bé biếng ăn','5 điều nên thống nhất',TT_NOTE,D04_T1,'',TP,points=['Giờ ăn cố định 30 phút','Không xem màn hình','Không ép, khen khi tự xúc','Đổi món, cho bé cùng làm','Ghi sổ lượng ăn'],
   scenes=['A 3-year-old Vietnamese boy in a yellow sweater feeds himself with a small spoon at a toddler table while a nanny in her mid 30s with a curly pixie cut and coral sweater claps softly.',
           'A 3-year-old Vietnamese boy in a yellow sweater and a nanny with a curly pixie cut and coral sweater arrange cucumber and carrot slices into a smiley face on a small plate at a sunny kitchen counter.']),
 V('2026-11-04','reel-2000','Thứ Tư 4/11 · 20:00 Reel (20:15 chia sẻ sang Group)','FACEBOOK PAGE · REEL','Reel: Chiều đón bé, tối cơm ấm','EliteHelpers_Reel_0411_ChieuToi.mp4','reel',
   'ELITE HELPERS','Chiều đón bé','tối cơm ấm',REEL_NOTE,D04_REEL,'',RP,pin=D04_REEL_PIN,
   scenes=['A caring Vietnamese woman in her early 40s with a sleek shoulder-length cut and a sand-colored trench coat picks up a smiling 6-year-old girl at a Hanoi school gate in golden afternoon light.',
           'In a warm Hanoi apartment, a Vietnamese woman in her early 40s with a sleek shoulder-length cut and a beige sweater wraps a 6-year-old girl in a fluffy towel after a bath, soft lamp light.',
           'A Vietnamese family (parents in their late 30s, the girl and a grandmother) sit down to a steaming home-cooked dinner while a Vietnamese woman in her early 40s with a sleek shoulder-length cut places the last dish on the table.']),
 V('2026-11-04','tiktok-2130','Thứ Tư 4/11 · 21:30','TIKTOK','BHXH, BHYT của người giúp việc (video)','EliteHelpers_TikTok_0411_BHYT.mp4','tiktok',
   'QUYỀN LỢI NGƯỜI LAO ĐỘNG','BHXH, BHYT','ai trả cho người giúp việc?',TT_NOTE,D04_T2,'',TP,points=['Gia đình trả cùng kỳ lương','Chị em tự tham gia BHXH, BHYT','Ghi rõ trong hợp đồng','Không trả: phạt 10–15 triệu'],
   scenes=['A Vietnamese woman in her late 40s with shoulder-length hair clipped back and a rust-orange cardigan receives her monthly salary envelope and a receipt from a smiling homeowner at a dining table.',
           'A Vietnamese woman in her late 40s with hair clipped back and a rust-orange cardigan smiles at a ward service counter holding a new health insurance card, a folder under her arm.']),
]
