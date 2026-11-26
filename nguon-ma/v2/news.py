# -*- coding: utf-8 -*-
"""Bản tin người lao động (hiển thị toàn bộ ở trang /tin-tuc: Trang chủ / Tuyển dụng / Tin tức, mỗi bài một trang riêng, mở tab mới).
Thêm bài mới: thêm dict vào đầu POSTS (no tăng dần, chỉ dùng cho tên ảnh; bài đầu danh sách tự gắn nhãn "Tin mới"), tạo ảnh bìa bằng gen_news_covers.py, chạy build.py."""
import html
E = html.escape

POSTS = [
dict(no=7, slug='ngoai-40-tuoi-tim-viec-giup-viec-gia-dinh', date='2026-11-26', date_vi='26/11/2026',
     tag='Thị trường việc làm',
     title='Ngoài 40 tuổi tìm việc: kinh nghiệm chăm nhà là lợi thế với nghề giúp việc gia đình',
     sapo='Nhiều lao động trung niên đang tìm hướng đi mới, trong khi gia đình thành phố ngày càng cần người chăm nhà, chăm trẻ và người cao tuổi. Elite Helpers tóm tắt bức tranh mới nhất và gợi ý cách chị em biến kinh nghiệm của mình thành một công việc ổn định.',
     src_short='VnExpress, Tiền Phong',
     body='''
<h2>Lao động trung niên đang tìm hướng đi mới</h2>
<p>Theo Tiền Phong (26/11/2026), dẫn số liệu của Sở Nội vụ TP.HCM, tính đến 25/10 năm nay Trung tâm Dịch vụ việc làm thành phố đã tiếp nhận hơn <strong>191.300 hồ sơ</strong> đề nghị hưởng trợ cấp thất nghiệp, tăng 6,47% so với cùng kỳ năm 2025. Trong đó, lao động trung niên chiếm <strong>hơn 50%</strong> và tỷ lệ nữ cao hơn nam.</p>
<ul>
<li>Nhiều doanh nghiệp ưu tiên nhân sự trẻ, yêu cầu thêm ngoại ngữ và kỹ năng số.</li>
<li>Trung tâm Dịch vụ việc làm TP.HCM khuyến khích người lao động học các khóa ngắn hạn như nấu ăn, pha chế, trang điểm để mở rộng cơ hội.</li>
<li>Chuyên gia nhân sự khuyên người lao động chủ động học kỹ năng mới và sẵn sàng thử một lĩnh vực khác.</li>
</ul>

<h2>Giúp việc gia đình: nghề cần sự chín chắn</h2>
<p>Trong một bài viết trên VnExpress (24/11/2026), tác giả Khánh Hưng cho rằng dọn nhà, nấu ăn, chăm trẻ hay làm theo giờ có thể giúp lao động ngoài 40 tuổi tiếp tục có thu nhập. Nhu cầu ổn định vì ngày càng nhiều gia đình có cả vợ và chồng đi làm toàn thời gian. Tác giả viết: “Tôi nghĩ giúp việc gia đình là một lựa chọn việc làm đáng được nhìn nhận nghiêm túc hơn.”</p>
<p>Bài viết cũng nêu điều kiện để nghề phát triển bền vững: có đơn vị kết nối lao động, chương trình đào tạo kỹ năng, tiêu chuẩn công việc và thỏa thuận tiền công minh bạch. Đây cũng là những điều chị em nên tìm khi chọn nơi nhận việc.</p>

<h2>Kinh nghiệm nào của chị em là lợi thế?</h2>
<p>Gợi ý của Elite Helpers để chị em tự đối chiếu trước khi ứng tuyển:</p>
<table>
<tr><th>Kinh nghiệm sẵn có</th><th>Vị trí phù hợp</th><th>Nên bổ sung</th></tr>
<tr><td>Nấu cơm gia đình nhiều năm, quen chợ búa</td><td>Giúp việc nấu ăn, quản gia</td><td>Thực đơn theo tuần, an toàn thực phẩm, món ăn cho trẻ nhỏ</td></tr>
<tr><td>Đã nuôi con nhỏ, chăm cháu</td><td>Bảo mẫu, đưa đón trẻ</td><td>Sơ cứu cơ bản, nề nếp sinh hoạt của trẻ</td></tr>
<tr><td>Từng chăm ông bà, cha mẹ</td><td>Chăm sóc người cao tuổi</td><td>Hỗ trợ di chuyển an toàn, theo dõi giờ uống thuốc theo chỉ dẫn của gia đình</td></tr>
<tr><td>Gọn gàng, quen việc nhà</td><td>Giúp việc theo giờ, dọn dẹp</td><td>Dùng máy móc gia dụng hiện đại, phân loại đồ giặt, vệ sinh đồ đạc cao cấp</td></tr>
</table>

<h2>Chuẩn bị gì trước buổi gặp gia đình?</h2>
<ol>
<li><strong>Kể kinh nghiệm bằng việc cụ thể:</strong> ví dụ “nấu cơm cho gia đình 5 người trong 15 năm”, “chăm mẹ chồng sau mổ 6 tháng”.</li>
<li><strong>Nói rõ mong muốn:</strong> làm cả ngày hay theo giờ, ở lại hay về trong ngày, khu vực thuận tiện đi lại.</li>
<li><strong>Hỏi rõ phạm vi công việc:</strong> mấy người trong nhà, có trẻ nhỏ hay người cao tuổi không, giờ giấc mỗi ngày.</li>
<li><strong>Thống nhất bằng văn bản:</strong> lương, ngày nghỉ, cách tính làm thêm giờ, ngày lễ, Tết.</li>
<li><strong>Tự giữ giấy tờ tùy thân:</strong> chỉ cung cấp bản sao khi cần làm hợp đồng.</li>
</ol>

<div class="note"><strong>Ở Elite Helpers:</strong> chị em không phải trả bất kỳ khoản phí nào, được ký hợp đồng bằng văn bản ghi rõ lương, giờ làm, ngày nghỉ và được gặp gia đình trước khi nhận việc. Kinh nghiệm chăm nhà, chăm trẻ, chăm người cao tuổi của chị em được trân trọng; Elite Helpers giới thiệu vị trí phù hợp với sở trường và khu vực sinh sống tại Hà Nội. Xem các vị trí đang tuyển tại <a href="/tuyen-dung">trang Tuyển dụng</a>.</div>
''',
     sources=[('Nhiều người cần tuyển giúp việc đưa đón con, nấu cơm, dọn nhà lương 5 triệu – VnExpress, 24/11/2026', 'https://vnexpress.net/tuyen-dung-nguoi-giup-viec-tra-luong-5-trieu-dong-mot-thang-5148387.html'),
              ('Có bằng cấp, nhiều kinh nghiệm, vì sao khó xin việc? – Tiền Phong, 26/11/2026', 'https://tienphong.vn/co-bang-cap-nhieu-kinh-nghiem-vi-sao-kho-xin-viec-post1897325.tpo')],
     cover=dict(big='Ngoài 40 tuổi', label='kinh nghiệm nấu ăn, chăm trẻ, chăm người cao tuổi là lợi thế khi tìm việc giúp việc gia đình', note='VnExpress 24/11 · Tiền Phong 26/11/2026', tone='gold'),
     prompt='KÊNH: WEBSITE – BẢN TIN. Photorealistic 16:9 photo: a confident Vietnamese woman in her late 40s with a short layered bob and small pearl earrings, wearing a teal polo shirt and a beige linen apron, plating a colourful home-cooked meal (braised fish, stir-fried greens, soup) in a bright modern kitchen of a Hanoi apartment; a young Vietnamese mother in office wear holding a laptop bag pauses beside her and smiles approvingly, a 5-year-old boy in a school uniform peeks at the food; morning sunlight through large windows, potted herbs on the counter, warm cream, soft gold and deep green tones, no readable text, no logo.'),

dict(no=6, slug='nghi-le-24-11-tet-2027-nguoi-giup-viec', date='2026-11-19', date_vi='19/11/2026',
     tag='Nghỉ lễ, Tết',
     title='Nghỉ 24/11 và Tết Đinh Mùi 2027: chị em giúp việc được nghỉ thế nào, đi làm được trả lương ra sao?',
     sapo='Ngày Văn hóa Việt Nam 24/11 năm nay là ngày nghỉ hưởng nguyên lương đầu tiên, còn Tết Đinh Mùi 2027 đã có lịch nghỉ chính thức. Elite Helpers tóm tắt lịch nghỉ và cách tính lương khi chị em đồng ý ở lại làm cùng gia đình.',
     src_short='Chinhphu.vn, Dân trí, VTV, Tuổi Trẻ',
     body='''
<h2>Ngày 24/11: lần đầu có thêm một ngày nghỉ hưởng lương</h2>
<p>Theo Cổng Chính sách (Chinhphu.vn, 18/11/2026), Quốc hội đã thông qua Nghị quyết về phát triển văn hóa Việt Nam ngày 24/4/2026, xác định ngày 24/11 hằng năm là “Ngày Văn hóa Việt Nam”, người lao động được nghỉ và hưởng nguyên lương.</p>
<ul>
<li><strong>Năm 2026:</strong> nghỉ 1 ngày vào <strong>thứ Ba, 24/11/2026</strong>, không hoán đổi ngày làm việc.</li>
<li><strong>Năm 2027:</strong> 24/11 rơi vào thứ Tư, tiếp tục nghỉ 1 ngày (Tuổi Trẻ, 14/10/2026).</li>
<li>Chị em giúp việc nên trao đổi sớm với gia đình: nghỉ trọn ngày, hoặc đồng ý đi làm và nhận lương ngày lễ như mục dưới.</li>
</ul>

<h2>Lịch nghỉ Tết Nguyên đán Đinh Mùi 2027</h2>
<p>Văn phòng Chính phủ đã thông báo phương án nghỉ Tết 7 ngày cho cán bộ, công chức (VTV, 2/10/2026). Với người lao động làm cho gia đình, doanh nghiệp, Bộ luật Lao động 2019 quy định 5 ngày nghỉ Tết hưởng nguyên lương; lịch cụ thể do hai bên thỏa thuận.</p>
<table>
<tr><th>Nội dung</th><th>Thời gian</th></tr>
<tr><td>Nghỉ Tết của cán bộ, công chức</td><td>Thứ Năm 4/2/2027 (28 tháng Chạp) đến hết thứ Tư 10/2/2027 (mùng 5 Tết), <strong>7 ngày</strong></td></tr>
<tr><td>Ngày nghỉ Tết hưởng lương theo luật</td><td><strong>5 ngày</strong> Tết âm lịch</td></tr>
<tr><td>Ví dụ doanh nghiệp nghỉ dài</td><td>Một số công ty cho nghỉ 9–12 ngày, như từ 3/2 đến hết 14/2/2027 (Dân trí, 7/11/2026)</td></tr>
</table>

<h2>Đi làm ngày lễ, Tết: lương ít nhất 300%</h2>
<p>Theo Dân trí (19/11/2026), làm việc vào ngày lễ, Tết cần có <strong>sự đồng ý của người lao động</strong>. Khi đó, chị em được trả ít nhất <strong>300% tiền lương</strong> của ngày làm việc bình thường, chưa kể tiền lương ngày lễ vẫn được hưởng (Điều 98 Bộ luật Lao động 2019). Làm ban đêm (22h–6h) được trả thêm ít nhất 30%.</p>
<p><strong>Ví dụ minh họa của Elite Helpers:</strong> lương 9 triệu đồng/tháng, giả sử tính 26 ngày công, mỗi ngày khoảng 346.000 đồng. Ở lại làm mùng 1 Tết, chị em nhận thêm ít nhất khoảng <strong>1,04 triệu đồng</strong> cho ngày đó, ngoài lương tháng.</p>

<h2>Thưởng Tết: nên ghi rõ từ đầu</h2>
<p>Theo Điều 104 Bộ luật Lao động 2019 (Dân trí dẫn lại), thưởng là khoản do người sử dụng lao động quyết định, không bắt buộc. Vì vậy, cách chắc chắn nhất là thỏa thuận ngay trong hợp đồng:</p>
<ol>
<li><strong>Lịch nghỉ Tết:</strong> nghỉ từ ngày nào đến ngày nào, ngày nào quay lại.</li>
<li><strong>Lương những ngày ở lại làm:</strong> ghi mức cụ thể, tối thiểu theo luật.</li>
<li><strong>Thưởng Tết, tiền tàu xe về quê:</strong> số tiền và thời điểm trả, tốt nhất trước kỳ nghỉ.</li>
<li><strong>Người làm thay:</strong> nếu gia đình cần người trong những ngày chị em nghỉ, thống nhất sớm để cả hai bên yên tâm.</li>
</ol>

<div class="note"><strong>Ở Elite Helpers:</strong> chị em không phải trả bất kỳ khoản phí nào, được ký hợp đồng bằng văn bản ghi rõ lương, ngày nghỉ lễ, Tết và lương làm thêm; được gặp gia đình trước khi nhận việc. Elite Helpers hỗ trợ trao đổi lịch nghỉ Tết với gia đình từ sớm. Xem thêm phần <a href="/tuyen-dung#tim-viec-an-toan">Tìm việc an toàn</a>.</div>
''',
     sources=[('Ngày Văn hóa Việt Nam 24/11: Người lao động được nghỉ, hưởng nguyên lương – Chinhphu.vn, 18/11/2026', 'https://xaydungchinhsach.chinhphu.vn/ngay-24-11-hang-nam-la-ngay-van-hoa-viet-nam-nguoi-lao-dong-duoc-nghi-huong-nguyen-luong-119260113152642414.htm'),
              ('Điều kiện lương, thưởng với người lao động trong ngày Văn hóa VN 24/11 – Dân trí, 19/11/2026', 'https://dantri.com.vn/lao-dong-viec-lam/dieu-kien-luong-thuong-voi-nguoi-lao-dong-trong-ngay-van-hoa-vn-2411-20261118150708522.htm'),
              ('Thương lượng với doanh nghiệp về thời gian nghỉ Tết, tiền thưởng – Dân trí, 7/11/2026', 'https://dantri.com.vn/lao-dong-viec-lam/thuong-luong-voi-doanh-nghiep-ve-thoi-gian-nghi-tet-tien-thuong-20261107085307504.htm'),
              ('Chính phủ chốt nghỉ Tết Nguyên đán 7 ngày: có nơi nghỉ 12 ngày – Tuổi Trẻ, 14/10/2026', 'https://tuoitre.vn/chinh-phu-chot-nghi-tet-nguyen-dan-7-ngay-co-noi-nghi-12-ngay-100261013223051997.htm'),
              ('Chốt nghỉ 7 ngày dịp Tết Nguyên đán năm 2027, nghỉ Quốc khánh 4 ngày – VTV, 2/10/2026', 'https://vtv.vn/chot-nghi-7-ngay-dip-tet-nguyen-dan-nam-2027-nghi-quoc-khanh-4-ngay-100261002184331043.htm')],
     cover=dict(big='Ít nhất 300%', label='tiền lương khi chị em đồng ý đi làm ngày lễ, Tết, chưa kể lương ngày lễ được hưởng', note='Ngày Văn hóa Việt Nam 24/11 · Tết Đinh Mùi 2027', tone='green'),
     prompt='KÊNH: WEBSITE – BẢN TIN. Photorealistic 16:9 photo: a cheerful Vietnamese woman in her mid-40s with shoulder-length wavy hair, wearing a burgundy knit cardigan over a cream blouse, standing at the front door of a modern Hanoi apartment with a small navy rolling suitcase, about to go home for Lunar New Year; an elderly Vietnamese couple in warm sweaters smile and hand her a small wrapped gift box; a blooming pink peach-blossom branch in a ceramic vase and a bowl of kumquats on a side table, soft late-afternoon light, warm grateful mood, cream, deep green and soft gold tones, no readable text, no logo.'),

dict(no=5, slug='bhxh-tu-nguyen-2027-nguoi-giup-viec', date='2026-11-12', date_vi='12/11/2026',
     tag='Bảo hiểm',
     title='BHXH tự nguyện từ 1/1/2027: mức đóng thấp nhất 484.000 đồng, chị em giúp việc nên biết gì?',
     sapo='Từ 1/1/2027, chuẩn nghèo mới được áp dụng nên mức đóng bảo hiểm xã hội tự nguyện thấp nhất tăng từ 330.000 lên 484.000 đồng/tháng, kèm phần hỗ trợ của Nhà nước. Đây là cách để chị em làm theo giờ, làm tự do vẫn có lương hưu và trợ cấp thai sản.',
     src_short='Dân trí, Chinhphu.vn, Thanh Niên',
     body='''
<h2>Mức đóng mới từ 1/1/2027</h2>
<p>Theo Dân trí (9/11/2026), mức đóng BHXH tự nguyện hằng tháng bằng <strong>22% mức thu nhập</strong> do người tham gia tự chọn. Thu nhập chọn thấp nhất bằng chuẩn hộ nghèo khu vực nông thôn, cao nhất bằng 20 lần mức tham chiếu. Nghị định 351/2025/NĐ-CP nâng chuẩn nghèo nông thôn giai đoạn 2027–2030 lên 2.200.000 đồng/người/tháng, nên mức sàn thay đổi như sau:</p>
<table>
<tr><th>Nội dung</th><th>Hiện nay</th><th>Từ 1/1/2027</th></tr>
<tr><td>Thu nhập chọn thấp nhất</td><td>1.500.000đ</td><td><strong>2.200.000đ</strong></td></tr>
<tr><td>Mức đóng thấp nhất/tháng (22%)</td><td>330.000đ</td><td><strong>484.000đ</strong></td></tr>
</table>
<p>Chị em có thể chọn mức thu nhập cao hơn để sau này nhận lương hưu cao hơn, miễn là trong khả năng đóng đều đặn.</p>

<h2>Nhà nước hỗ trợ bao nhiêu?</h2>
<p>Theo Điều 5 Nghị định 159/2025/NĐ-CP, ngân sách hỗ trợ một phần tiền đóng, tính trên mức đóng theo chuẩn hộ nghèo nông thôn. Với chuẩn mới từ 2027, Elite Helpers quy đổi ra số tiền như sau:</p>
<table>
<tr><th>Đối tượng</th><th>Tỷ lệ hỗ trợ</th><th>Quy đổi từ 2027</th></tr>
<tr><td>Hộ nghèo; người sống ở xã đảo, đặc khu</td><td>50%</td><td>242.000đ/tháng</td></tr>
<tr><td>Hộ cận nghèo</td><td>40%</td><td>193.600đ/tháng</td></tr>
<tr><td>Người dân tộc thiểu số</td><td>30%</td><td>145.200đ/tháng</td></tr>
<tr><td>Người tham gia khác</td><td>20%</td><td>96.800đ/tháng</td></tr>
</table>
<p>Theo Chinhphu.vn, thời gian được hỗ trợ tính theo số tháng tham gia thực tế, nhưng không quá 10 năm (120 tháng).</p>

<h2>Ai tham gia được và được hưởng gì?</h2>
<ul>
<li><strong>Đối tượng:</strong> công dân Việt Nam từ đủ 15 tuổi, không thuộc diện BHXH bắt buộc và chưa hưởng lương hưu, trợ cấp BHXH hằng tháng. Phù hợp với chị em làm giúp việc theo giờ, làm tự do.</li>
<li><strong>Lương hưu:</strong> từ 1/7/2025, chỉ cần đủ <strong>15 năm đóng</strong> và đủ tuổi nghỉ hưu là được nhận lương hưu hằng tháng, có thẻ BHYT.</li>
<li><strong>Trợ cấp thai sản:</strong> 2 triệu đồng cho mỗi con khi đã đóng từ đủ 6 tháng trong 12 tháng trước khi sinh (Điều 95 Luật BHXH 2024).</li>
<li><strong>Tử tuất:</strong> gia đình được trợ cấp mai táng khi người tham gia đã đóng từ đủ 60 tháng.</li>
</ul>

<h2>Đóng linh hoạt theo thu nhập</h2>
<p>Chị em được chọn đóng hằng tháng, 3 tháng, 6 tháng, 12 tháng một lần, hoặc nhiều năm một lần (tối đa 5 năm). Người sắp đến tuổi nghỉ hưu còn thiếu không quá 5 năm có thể đóng một lần cho phần còn thiếu để đủ điều kiện lương hưu.</p>

<h2>3 bước để bắt đầu</h2>
<ol>
<li><strong>Chọn mức thu nhập</strong> phù hợp: từ 2.200.000 đồng/tháng trở lên (đóng từ 484.000 đồng/tháng, trước khi trừ phần hỗ trợ).</li>
<li><strong>Đăng ký</strong> tại cơ quan BHXH nơi cư trú, đại lý thu BHXH ở xã, phường, hoặc trên ứng dụng VssID.</li>
<li><strong>Chọn phương thức đóng</strong> hợp với dòng tiền: nhận lương tháng thì đóng tháng, có khoản thưởng cuối năm thì đóng 6 hoặc 12 tháng.</li>
</ol>

<div class="note"><strong>Ở Elite Helpers:</strong> chị em được ký hợp đồng bằng văn bản ghi rõ lương, giờ làm, ngày nghỉ; được gặp gia đình trước khi nhận việc và không phải trả bất kỳ khoản phí nào. Thu nhập ổn định 10–25 triệu đồng/tháng giúp chị em chủ động kế hoạch bảo hiểm, lương hưu lâu dài. Xem thêm phần <a href="/tuyen-dung#tim-viec-an-toan">Tìm việc an toàn</a>.</div>
''',
     sources=[('Điều chỉnh mức đóng, hỗ trợ đóng bảo hiểm xã hội tự nguyện từ ngày 1/1/2027 – Dân trí, 9/11/2026', 'https://dantri.com.vn/noi-vu/dieu-chinh-muc-dong-ho-tro-dong-bao-hiem-xa-hoi-tu-nguyen-tu-ngay-112027-20261108205230384.htm'),
              ('Những điều cần biết về chính sách bảo hiểm xã hội tự nguyện – Chinhphu.vn, 18/9/2025', 'https://xaydungchinhsach.chinhphu.vn/nhung-dieu-can-biet-ve-chinh-sach-bao-hiem-xa-hoi-tu-nguyen-119250913101137277.htm'),
              ('Tham gia BHXH tự nguyện, cần thủ tục gì để hưởng trợ cấp thai sản? – Thanh Niên, 21/12/2025', 'https://thanhnien.vn/tham-gia-bhxh-tu-nguyen-can-thu-tuc-gi-de-huong-tro-cap-thai-san-185251220094400973.htm')],
     cover=dict(big='484.000 đồng', label='mức đóng BHXH tự nguyện thấp nhất mỗi tháng từ 1/1/2027, Nhà nước hỗ trợ thêm', note='Nghị định 351/2025/NĐ-CP · từ 1/1/2027', tone='gold'),
     prompt='KÊNH: WEBSITE – BẢN TIN. Photorealistic 16:9 photo: a Vietnamese woman in her late 30s with a neat low ponytail, wearing a dusty-rose long-sleeve blouse, sitting at the counter of a bright local social-insurance service office in Hanoi, smiling as a friendly female staff member in a light-blue uniform shirt (no logo) explains a form; a smartphone and a small cloth wallet on the counter, a potted green plant nearby, soft morning light through large windows, reassuring hopeful mood, cream, deep green and soft gold tones, no readable text, no logo.'),

dict(no=4, slug='luong-toi-thieu-vung-2027-nguoi-giup-viec', date='2026-11-05', date_vi='05/11/2026',
     tag='Tiền lương',
     title='Từ 1/1/2027, lương tối thiểu vùng tăng: người giúp việc gia đình cần biết gì?',
     sapo='Nghị định 399/2026/NĐ-CP nâng lương tối thiểu vùng thêm 310.000–390.000 đồng/tháng từ 1/1/2027. Quy định áp dụng cả với hộ gia đình, cá nhân thuê người lao động, nên chị em giúp việc cũng nằm trong diện được bảo vệ.',
     src_short='VnExpress, Thanh Niên, Tuổi Trẻ',
     body='''
<h2>Mức lương tối thiểu mới là bao nhiêu?</h2>
<p>Ngày 3/11/2026, các báo đồng loạt đưa tin Chính phủ ban hành Nghị định 399/2026/NĐ-CP, có hiệu lực từ ngày 1/1/2027, thay thế Nghị định 293/2025/NĐ-CP. Mức tăng bình quân khoảng 7,8% so với hiện hành:</p>
<table>
<tr><th>Vùng</th><th>Lương tháng từ 1/1/2027</th><th>Lương giờ</th></tr>
<tr><td>I</td><td><strong>5.700.000đ</strong><br>(hiện 5.310.000đ, +390.000đ)</td><td>27.400đ</td></tr>
<tr><td>II</td><td><strong>5.080.000đ</strong><br>(hiện 4.730.000đ, +350.000đ)</td><td>24.400đ</td></tr>
<tr><td>III</td><td><strong>4.450.000đ</strong><br>(hiện 4.140.000đ, +310.000đ)</td><td>21.400đ</td></tr>
<tr><td>IV</td><td><strong>4.040.000đ</strong><br>(hiện 3.700.000đ, +340.000đ)</td><td>19.400đ</td></tr>
</table>

<h2>Người giúp việc gia đình có được áp dụng không?</h2>
<p>Có. Theo Thanh Niên và Tuổi Trẻ, nghị định áp dụng với người lao động làm việc theo hợp đồng lao động theo Bộ luật Lao động, và người sử dụng lao động bao gồm cả <strong>hộ gia đình, cá nhân có thuê mướn lao động</strong>. Nghĩa là gia đình thuê chị em giúp việc theo hợp đồng cũng phải tuân theo mức sàn này.</p>
<ul>
<li><strong>Lương tháng:</strong> là mức thấp nhất để thỏa thuận và trả cho người làm đủ thời giờ bình thường trong tháng.</li>
<li><strong>Lương giờ:</strong> người làm theo giờ được trả ít nhất bằng mức lương tối thiểu giờ của vùng.</li>
<li><strong>Lương theo ngày, tuần, khoán:</strong> khi quy đổi ra tháng hoặc giờ cũng không được thấp hơn mức của vùng.</li>
<li>Mức áp dụng tính theo <strong>vùng nơi gia đình thuê sinh sống</strong>.</li>
<li>Gia đình không được cắt giảm các chế độ có lợi đã thỏa thuận, như tiền làm thêm giờ, làm ban đêm.</li>
</ul>

<h2>Ý nghĩa thực tế với chị em</h2>
<p>Lương tối thiểu là mức sàn để bảo vệ người lao động. Trên thực tế, thu nhập nghề giúp việc thường cao hơn nhiều: theo VnExpress (27/8/2026), giúp việc theo giờ qua ứng dụng nhận 60.000–100.000 đồng/giờ, gấp hơn hai lần mức sàn 27.400 đồng/giờ của vùng I. Điều quan trọng là mức lương được ghi rõ trong hợp đồng để chị em yên tâm.</p>

<h2>4 việc nên làm trước năm 2027</h2>
<ol>
<li><strong>Xem lại hợp đồng:</strong> mức lương, giờ làm, ngày nghỉ, tiền làm thêm giờ có được ghi bằng văn bản chưa.</li>
<li><strong>Hỏi rõ vùng áp dụng:</strong> gia đình ở xã, phường nào để biết mức sàn tương ứng.</li>
<li><strong>Kiểm tra cách trả lương:</strong> nếu nhận theo ngày hoặc theo giờ, quy đổi xem có thấp hơn mức của vùng không.</li>
<li><strong>Giữ lại chứng từ:</strong> tin nhắn, biên nhận, sao kê chuyển khoản lương mỗi tháng.</li>
</ol>

<div class="note"><strong>Ở Elite Helpers:</strong> lương 10–25 triệu đồng/tháng tùy vị trí, ghi rõ trong hợp đồng bằng văn bản; chị em được gặp gia đình trước khi nhận việc và không phải trả bất kỳ khoản phí nào. Xem thêm phần <a href="/tuyen-dung#tim-viec-an-toan">Tìm việc an toàn</a>.</div>
''',
     sources=[('Lương tối thiểu vùng tăng 310.000-390.000 đồng từ năm 2027 – VnExpress, 3/11/2026', 'https://vnexpress.net/luong-toi-thieu-vung-tang-310-000-390-000-dong-tu-nam-2027-5140183.html'),
              ('Lương tối thiểu vùng chính thức tăng từ 1.1.2027 – Thanh Niên, 3/11/2026', 'https://thanhnien.vn/luong-toi-thieu-vung-chinh-thuc-tang-tu-112027-185261103135733018.htm'),
              ('Tăng lương tối thiểu vùng từ 1-1-2027, cao nhất tăng tới 390.000 đồng – Tuổi Trẻ, 3/11/2026', 'https://tuoitre.vn/tang-luong-toi-thieu-vung-tu-1-1-2027-cao-nhat-tang-toi-390000-dong-100261103131209338.htm'),
              ('Giúp việc theo giờ hút lao động – VnExpress, 27/8/2026', 'https://vnexpress.net/giup-viec-theo-gio-hut-lao-dong-5113556.html')],
     cover=dict(big='5,7 triệu đồng', label='lương tối thiểu tháng vùng I từ 1/1/2027, áp dụng cả với hộ gia đình thuê lao động', note='Nghị định 399/2026/NĐ-CP · từ 1/1/2027', tone='green'),
     prompt='KÊNH: WEBSITE – BẢN TIN. Photorealistic 16:9 photo: a Vietnamese woman in her mid-40s with shoulder-length wavy hair, wearing a soft maroon knit sweater, standing at a tidy kitchen counter in a Hanoi family home in early winter, writing in a small notebook beside a cup of hot tea, a vase with a budding peach-blossom branch in the background, warm late-afternoon light, hopeful confident expression, cream, deep green and soft gold tones, no readable text, no logo.'),

dict(no=3, slug='quang-cao-tuyen-dung-gian-doi-phat-75-trieu', date='2026-10-23', date_vi='23/10/2026',
     tag='Cảnh giác khi tìm việc',
     title='Quảng cáo tuyển dụng gian dối có thể bị phạt tới 75 triệu đồng: người tìm việc cần biết gì?',
     sapo='Từ 10/9/2026, quảng cáo gian dối, hứa hẹn sai sự thật để lôi kéo người lao động có thể bị phạt 50–75 triệu đồng. Đây là lớp bảo vệ mới cho chị em đang tìm việc giúp việc gia đình.',
     src_short='Sức khỏe & Đời sống, VnExpress',
     body='''
<h2>Quy định mới nói gì?</h2>
<p>Theo Nghị định 283/2026/NĐ-CP về xử phạt vi phạm hành chính trong lĩnh vực lao động, có hiệu lực từ ngày 10/9/2026, các hành vi sau trong tuyển dụng có thể bị phạt từ 50 đến 75 triệu đồng:</p>
<ul>
<li>Quảng cáo gian dối, hứa hẹn gian dối để lừa người lao động.</li>
<li>Dụ dỗ, lôi kéo hoặc dùng thủ đoạn khác để lừa gạt người lao động.</li>
<li>Tuyển dụng nhằm bóc lột, cưỡng bức lao động (khi chưa đến mức truy cứu trách nhiệm hình sự).</li>
</ul>
<p>Cũng theo Nghị định này, gia chủ giữ giấy tờ tùy thân của người giúp việc bị phạt 10–15 triệu đồng và buộc phải trả lại giấy tờ.</p>

<h2>6 dấu hiệu chị em nên dừng lại kiểm tra</h2>
<ol>
<li><strong>Thu phí trước khi đi làm</strong>: phí hồ sơ, phí giới thiệu, phí "giữ chỗ".</li>
<li><strong>Lương cao bất thường</strong> nhưng không nói rõ gia đình ở đâu, làm việc gì.</li>
<li><strong>Yêu cầu ở trọ chờ việc</strong>, mất tiền trọ, tiền ăn trong lúc chờ.</li>
<li><strong>Đòi giữ căn cước bản gốc</strong> hoặc giấy tờ tùy thân khác.</li>
<li><strong>Chỉ hứa miệng</strong>, không có hợp đồng bằng văn bản.</li>
<li><strong>Giục đi ngay trong ngày</strong>, không cho thời gian hỏi thêm hay báo người thân.</li>
</ol>

<h2>Trước khi nhận việc, hãy làm 4 việc</h2>
<ul>
<li>Hỏi rõ tên, khu vực sống của gia đình, công việc cụ thể, giờ làm, ngày nghỉ, mức lương.</li>
<li>Gặp gia đình trực tiếp trước khi nhận việc; xin xem trước hợp đồng.</li>
<li>Không chuyển khoản bất kỳ khoản phí nào; luôn tự giữ giấy tờ bản gốc.</li>
<li>Báo cho người thân địa chỉ nơi làm việc và số điện thoại liên hệ.</li>
</ul>
<p>Nếu đã bị thu phí hoặc bị lừa, chị em giữ lại tin nhắn, biên lai, số điện thoại và báo ngay cho công an xã, phường nơi gần nhất.</p>

<div class="note"><strong>Ở Elite Helpers:</strong> không thu bất kỳ khoản phí nào của người lao động, không ở trọ chờ việc, gặp gia đình trước khi nhận việc và ký hợp đồng bằng văn bản. Xem thêm phần <a href="/tuyen-dung#tim-viec-an-toan">Tìm việc an toàn</a>.</div>
''',
     sources=[('Từ 10/9, quảng cáo tuyển dụng gian dối có thể bị phạt tới 75 triệu đồng – Sức khỏe & Đời sống, 4/9/2026', 'https://suckhoedoisong.vn/tu-10-9-quang-cao-tuyen-dung-gian-doi-co-the-bi-phat-toi-75-trieu-dong-169260904092303332.htm'),
              ('Trường hợp nào phải báo UBND xã khi thuê giúp việc gia đình để tránh bị phạt? – VnExpress, 6/8/2026', 'https://vnexpress.net/truong-hop-nao-phai-bao-ubnd-xa-khi-thue-giup-viec-gia-dinh-de-tranh-bi-phat-5105888.html')],
     cover=dict(big='75 triệu đồng', label='mức phạt tối đa với quảng cáo tuyển dụng gian dối, lừa người lao động', note='Nghị định 283/2026/NĐ-CP · từ 10/9/2026', tone='warn'),
     prompt='Photorealistic 16:9 photo, no faces visible: a Vietnamese woman in her 40s seen from behind, sitting on a bench at a bus stop in Hanoi, looking at a job advertisement on her smartphone, a small travel bag beside her, overcast soft light, calm cautious mood, deep green and cream tones, no readable text, no logo.'),

dict(no=2, slug='giup-viec-theo-gio-hut-lao-dong-2026', date='2026-10-23', date_vi='23/10/2026',
     tag='Thị trường việc làm',
     title='Giúp việc theo giờ hút lao động: thu nhập 60.000–100.000 đồng mỗi giờ',
     sapo='Nhiều người chuyển sang làm giúp việc theo giờ, kể cả nhân viên văn phòng làm thêm buổi tối. Thu nhập khá, giờ giấc linh hoạt, nhưng không phải ai cũng hợp với hình thức này.',
     src_short='VnExpress',
     body='''
<h2>Chuyện gì đang diễn ra?</h2>
<p>Theo VnExpress (27/8/2026), giúp việc theo giờ qua ứng dụng đang thu hút nhiều lao động:</p>
<ul>
<li>Tiền công <strong>60.000–100.000 đồng/giờ</strong> tùy diện tích, khối lượng việc, cao gấp đôi nhiều việc phục vụ, bán hàng (khoảng 25.000–30.000 đồng/giờ).</li>
<li>Người trên 50 tuổi nhận ca cố định có thể đạt <strong>8–10 triệu đồng/tháng</strong>.</li>
<li>Một ứng dụng giúp việc có khoảng 3.000 người làm, lượng khách đặt theo giờ tăng khoảng 20%.</li>
<li>Nhóm 40–50 tuổi vẫn đông nhất, nhưng ngày càng có thêm mẹ bỉm sữa, sinh viên, nhân viên văn phòng. Khoảng 70% nhận ca định kỳ, tương đương 8 giờ/ngày.</li>
</ul>
<p>Một bài khác của VnExpress (6/9/2026) cho biết nhân viên văn phòng làm thêm 3–5 ca/tuần, mỗi ca 2–3 tiếng, nhận 170.000–250.000 đồng/ca, thêm 3–5 triệu đồng/tháng. Nhiều người chỉ gắn bó 3–6 tháng vì áp lực thời gian và mệt khi làm hai việc.</p>

<h2>Vì sao gia đình chuyển sang thuê theo giờ?</h2>
<p>Căn hộ chung cư ngày càng nhỏ, nhiều gia đình muốn giữ không gian riêng và tiết kiệm chi phí ăn ở cho người làm. Tuy vậy, gia đình có trẻ nhỏ, có ông bà cần người bên cạnh cả ngày vẫn cần người ở lại.</p>

<h2>Theo giờ hay ở lại: chị em chọn thế nào?</h2>
<table>
<tr><th></th><th>Theo giờ</th><th>Ở lại cùng gia đình</th></tr>
<tr><td>Thu nhập</td><td>Theo số ca, thay đổi theo tháng</td><td>Lương tháng cố định (tại Elite Helpers: 10–25 triệu đồng)</td></tr>
<tr><td>Chỗ ở, đi lại</td><td>Tự lo, di chuyển nhiều nơi</td><td>Có chỗ ở, bữa ăn tại nhà gia đình</td></tr>
<tr><td>Giờ giấc</td><td>Linh hoạt, áp lực xong việc trong ca</td><td>Ổn định, có giờ nghỉ, ngày nghỉ theo hợp đồng</td></tr>
<tr><td>Phù hợp</td><td>Người cần làm thêm, có việc khác</td><td>Người muốn gắn bó lâu dài, thu nhập chắc chắn</td></tr>
</table>

<h2>Làm theo giờ, nhớ giữ an toàn</h2>
<ul>
<li>Từ chối việc nguy hiểm khi làm một mình: trèo ra cửa sổ, leo cao lau quạt trần.</li>
<li>Đọc kỹ hướng dẫn hóa chất tẩy rửa, đeo găng tay, không pha trộn các loại.</li>
<li>Báo người quản lý hoặc người thân lịch làm và địa chỉ từng ca.</li>
</ul>

<div class="note"><strong>Ở Elite Helpers:</strong> có cả việc ở lại và theo giờ tại Hà Nội, tư vấn vị trí đúng sở trường, không thu phí người lao động. Gửi hồ sơ 2 phút để được gọi lại.</div>
''',
     sources=[('Giúp việc theo giờ hút lao động – VnExpress, 27/8/2026', 'https://vnexpress.net/giup-viec-theo-gio-hut-lao-dong-5113556.html'),
              ('Nhân viên văn phòng làm thêm giúp việc theo giờ – VnExpress, 6/9/2026', 'https://vnexpress.net/nhan-vien-van-phong-lam-them-giup-viec-theo-gio-5116976.html')],
     cover=dict(big='60.000–100.000đ', label='tiền công mỗi giờ của người giúp việc theo giờ qua ứng dụng', note='Theo VnExpress · 27/8/2026', tone='gold'),
     prompt='Photorealistic 16:9 photo: a Vietnamese woman around 38 with a short ponytail, wearing a plain light-blue T-shirt and an apron (no company logo), wiping a glass dining table in a bright modern Hanoi apartment, cleaning caddy beside her, mid-morning sunlight, focused calm expression, cream and deep green tones, no readable text, no logo.'),

dict(no=1, slug='nguoi-giup-viec-duoc-bao-ve-the-nao-2026', date='2026-10-23', date_vi='23/10/2026',
     tag='Quyền lợi người lao động',
     title='Từ 10/9/2026, người giúp việc gia đình được pháp luật bảo vệ thế nào?',
     sapo='Nghị định 283/2026/NĐ-CP nâng mức phạt với gia chủ vi phạm quyền lợi người giúp việc: giữ giấy tờ tùy thân hay không trả khoản bảo hiểm có thể bị phạt 10–15 triệu đồng.',
     src_short='VnExpress, VnBusiness',
     body='''
<h2>Bức tranh nghề giúp việc ở Hà Nội</h2>
<p>Theo VnBusiness (12/8/2026), Hà Nội có hơn 13.700 lao động giúp việc gia đình, 94% là nữ. Khoảng 90–95% làm việc không có hợp đồng bằng văn bản, chỉ 3% có bảo hiểm xã hội và 19,5% có bảo hiểm y tế. Gần một nửa người lao động muốn ký hợp đồng nhưng không biết cách làm hoặc gia chủ chưa đồng ý.</p>
<p>Nghị định 283/2026/NĐ-CP, ban hành ngày 15/7/2026 và có hiệu lực từ 10/9/2026, đặt ra mức phạt cụ thể để thay đổi thực trạng này.</p>

<h2>Quyền lợi của chị em và mức phạt nếu gia chủ vi phạm</h2>
<table>
<tr><th>Quyền lợi của người giúp việc</th><th>Gia chủ vi phạm</th></tr>
<tr><td>Có hợp đồng lao động bằng văn bản</td><td>Cảnh cáo; tái phạm phạt 1–3 triệu đồng</td></tr>
<tr><td>Gia chủ thông báo UBND xã, phường trong 10 ngày khi bắt đầu và khi chấm dứt hợp đồng</td><td>Phạt 1–3 triệu đồng</td></tr>
<tr><td>Nhận thêm khoản tiền bằng mức đóng BHXH, BHYT bắt buộc cùng kỳ trả lương để tự tham gia (ví dụ lương 6 triệu, khoản này khoảng 1,29 triệu đồng)</td><td>Phạt 10–15 triệu đồng và phải trả đủ</td></tr>
<tr><td>Tự giữ giấy tờ tùy thân</td><td>Phạt 10–15 triệu đồng, buộc trả lại giấy tờ</td></tr>
<tr><td>Được trả tiền tàu xe về nơi cư trú khi nghỉ việc</td><td>Cảnh cáo, buộc trả</td></tr>
<tr><td>Không bị ngược đãi, quấy rối tình dục, cưỡng bức lao động</td><td>Phạt 50–75 triệu đồng (khi chưa đến mức truy cứu hình sự)</td></tr>
</table>

<h2>Giờ nghỉ chị em được hưởng</h2>
<ul>
<li>Mỗi ngày làm việc được nghỉ ít nhất 8 giờ, trong đó có 6 giờ liên tục.</li>
<li>Mỗi tuần được nghỉ ít nhất 24 giờ liên tục; nếu gia đình không bố trí được nghỉ hằng tuần thì bình quân mỗi tháng được nghỉ ít nhất 4 ngày.</li>
</ul>
<p>Căn cứ: Điều 111 Bộ luật Lao động 2019 và Điều 89 Nghị định 145/2020/NĐ-CP.</p>

<h2>Lưu ý với việc làm theo giờ</h2>
<p>Theo VnExpress (6/8/2026), làm việc nhà theo giờ thông qua công ty không thuộc diện lao động giúp việc gia đình theo Bộ luật Lao động 2019, vì vậy gia đình không phải thông báo UBND xã. Quyền lợi của người làm theo giờ khi đó do hợp đồng với công ty quy định.</p>

<div class="note"><strong>Ở Elite Helpers:</strong> hợp đồng bằng văn bản, khoản BHXH, BHYT ghi rõ trong hợp đồng, hướng dẫn gia đình thông báo UBND xã và không ai giữ giấy tờ tùy thân của chị em.</div>
''',
     sources=[('Trường hợp nào phải báo UBND xã khi thuê giúp việc gia đình để tránh bị phạt? – VnExpress, 6/8/2026', 'https://vnexpress.net/truong-hop-nao-phai-bao-ubnd-xa-khi-thue-giup-viec-gia-dinh-de-tranh-bi-phat-5105888.html'),
              ('Thị trường giúp việc gia đình: Siết chặt quản lý, bước qua thời "thỏa thuận miệng" – VnBusiness, 12/8/2026', 'https://vnbusiness.vn/thi-truong-giup-viec-gia-dinh-siet-chat-quan-ly-buoc-qua-thoi-thoa-thuan-mieng.html'),
              ('Thời giờ làm việc, nghỉ ngơi của người giúp việc gia đình – Luật Minh Khuê', 'https://luatminhkhue.vn/thoi-gian-lam-viec-thoi-gian-nghi-ngoi-cua-lao-dong-la-nguoi-giup-viec-gia-dinh-mau-hop-dong-giup-viec-gia-dinh-moi-nhat-nam-2021.aspx')],
     cover=dict(big='10–15 triệu đồng', label='mức phạt nếu gia chủ giữ giấy tờ tùy thân hoặc không trả khoản BHXH, BHYT cho người giúp việc', note='Nghị định 283/2026/NĐ-CP · từ 10/9/2026', tone='green'),
     prompt='Photorealistic 16:9 photo: a Vietnamese woman in her early 50s with grey-streaked hair in a low bun, wearing a mustard cardigan, sitting at a wooden table in a bright Hanoi townhouse living room, reading a two-page employment contract with a pen in hand, a younger woman in a white blouse sitting opposite pointing at a line, both relaxed and smiling, natural window light, cream and deep green tones, no readable text, no logo.'),
]


def cover_img(p, cls=''):
    n = p['no']
    return (f'<img{cls} src="assets/img/ban-tin-{n}-640.webp" srcset="assets/img/ban-tin-{n}-640.webp 640w, assets/img/ban-tin-{n}-1200.webp 1200w" '
            f'sizes="(min-width:1024px) 720px, 92vw" width="640" height="360" alt="{E(p["cover"]["big"])}: {E(p["cover"]["label"])}" loading="lazy" decoding="async">')


def list_section(g, page=False):
    items = ''
    for i, p in enumerate(POSTS):
        items += f'''
      <article class="nw-item">
        <a href="/{p['slug']}" target="_blank" rel="noopener" data-track="news_open">
          <span class="nw-tag">{'<b class="nw-new">Tin mới</b>' if i == 0 else ''}{E(p['tag'])}</span>
          <h3>{E(p['title'])}</h3>
          <p>{E(p['sapo'])}</p>
          {cover_img(p)}
        </a>
        <div class="nw-meta">{p['date_vi']} · Tổng hợp từ {E(p['src_short'])}</div>
      </article>'''
    head = '' if page else '''
    <span class="eyebrow">Bản tin người lao động · cập nhật hằng tuần</span>
    <h2 id="bt-title" class="t-h2 mt-3 text-shutter" style="max-width:26ch">Tin tức, quyền lợi và kinh nghiệm tìm việc</h2>
    <p class="mt-4 max-w-[60ch] text-ink-soft">Elite Helpers tổng hợp quy định mới và tin tức về nghề giúp việc từ các báo chính thống. Bấm vào bài để đọc đầy đủ.</p>'''
    return f'''<section id="ban-tin" class="on-light bg-paper py-16 lg:py-20"{'' if page else ' aria-labelledby="bt-title"'} aria-label="Danh sách bài">
  <div class="shell">{head}
    <div class="nw-list">{items}
    </div>
  </div>
</section>'''


def teaser_section(g):
    """Ô dẫn sang trang Tin tức (đặt trong /tuyen-dung): 3 tiêu đề mới nhất."""
    NEW = '<b class="nw-new">Tin mới</b>'
    li = ''.join(f'<li><a href="/{p["slug"]}">{NEW if i == 0 else ""}{E(p["title"])}</a><small>{p["date_vi"]}</small></li>' for i, p in enumerate(POSTS[:3]))
    return f'''<section id="tin-tuc" class="on-light bg-paper py-16 lg:py-20" aria-labelledby="tt-title">
  <div class="shell">
    <div class="td-teaser">
      <div><span class="eyebrow">Tin tức</span><h2 id="tt-title" class="t-h2 mt-3 text-shutter">Tin tức cho người lao động</h2>
        <p class="mt-3 text-ink-soft">Quy định mới, quyền lợi và kinh nghiệm tìm việc, cập nhật hằng tuần.</p>
        <a class="btn btn-ghost-dark mt-6" href="/tin-tuc">Xem tất cả tin tức</a></div>
      <ul class="td-teaser-list" role="list">{li}</ul>
    </div>
  </div>
</section>'''


def post_page(g, p, idx):
    SITE = g['SITE']; path = '/' + p['slug']
    crumbs = [('Trang chủ', '/'), ('Tuyển dụng', '/tuyen-dung'), ('Tin tức', '/tin-tuc')]
    newer = POSTS[idx - 1] if idx > 0 else None
    older = POSTS[idx + 1] if idx + 1 < len(POSTS) else None
    nav = '<nav class="nw-nav" aria-label="Bài trong chuỗi">'
    nav += (f'<a href="/{older["slug"]}"><small>← Bài trước</small>{E(older["title"])}</a>' if older else '<span></span>')
    nav += (f'<a class="r" href="/{newer["slug"]}"><small>Bài tiếp theo →</small>{E(newer["title"])}</a>' if newer else '<span></span>')
    nav += '</nav>'
    srcs = '<h2>Nguồn tham khảo</h2><ul class="nw-src">' + ''.join(
        f'<li><a href="{E(u)}" target="_blank" rel="noopener nofollow">{E(t)}</a></li>' for t, u in p['sources']) + '</ul>'
    others = ''.join(f'<li><a href="/{x["slug"]}">{E(x["title"])}</a></li>' for x in POSTS if x is not p)
    main = f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="shell relative pb-14 pt-32 lg:pb-16 lg:pt-40">
    {g['crumbs_html'](crumbs)}
    <span class="eyebrow">{'Tin mới · ' if idx == 0 else ''}{E(p['tag'])} · {p['date_vi']}</span>
    <h1 id="pg-title" class="t-display mt-4" style="max-width:26ch;font-size:clamp(2rem,1.4rem + 2.4vw,3.2rem)">{E(p['title'])}</h1>
    <p class="byline">Biên soạn: <b>Elite Helpers</b> · Tổng hợp từ {E(p['src_short'])}</p>
  </div>
</section>
<article class="on-light bg-paper py-14 lg:py-20">
  <div class="shell"><div class="prose">
    <p class="nw-sapo">{E(p['sapo'])}</p>
    {cover_img(p, ' class="nw-cover"').replace('loading="lazy"', 'loading="eager" fetchpriority="high"')}
    {p['body']}
    {srcs}
    {nav}
    <h2>Tin tức khác</h2><ul>{others}<li><a href="/tin-tuc">Xem tất cả tin tức</a></li></ul>
  </div></div>
</article>
<section class="on-dark bg-lacquer py-20 text-paper lg:py-24" aria-labelledby="cta-title">
  <div class="shell">
    <h2 id="cta-title" class="t-h2">Tìm việc giúp việc, bảo mẫu, chăm sóc người già tại Hà Nội?</h2>
    <p class="t-lead mt-4 max-w-[56ch] text-mist">Có hợp đồng, gặp gia đình trước khi nhận việc, không thu phí người lao động.</p>
    <div class="mt-8 flex flex-wrap gap-3">
      <a class="btn btn-brass" href="/tuyen-dung#viec-dang-tuyen">Xem việc đang tuyển</a>
      <a class="btn btn-ghost-light" href="#ung-tuyen" data-open="ungvien">Gửi hồ sơ (2 phút)</a>
      <a class="btn btn-ghost-light" href="https://zalo.me/0948919598" target="_blank" rel="noopener" data-track="zalo">Hỏi qua Zalo 0948 919 598</a>
    </div>
  </div>
</section>'''
    art = {'@type': 'NewsArticle', '@id': SITE + path + '#article', 'headline': p['title'], 'description': p['sapo'],
           'url': SITE + path, 'inLanguage': 'vi', 'datePublished': p['date'], 'dateModified': p['date'],
           'image': SITE + f'/ban-tin-{p["no"]}-1200.webp', 'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'},
           'mainEntityOfPage': SITE + path, 'isBasedOn': [u for _, u in p['sources']]}
    ld = {'@context': 'https://schema.org', '@graph': [art, g['crumbs_ld'](crumbs, path)]}
    return p['slug'] + '.html', path, g['page'](p['title'] + ' | Elite Helpers', p['sapo'], path, main, ld, og_type='article')


def all_posts(g):
    return [post_page(g, p, i) for i, p in enumerate(POSTS)]
