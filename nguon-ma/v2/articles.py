# -*- coding: utf-8 -*-
"""Bài cẩm nang (SEO/GEO/AIO): mỗi bài có Trả lời nhanh, bảng, checklist, FAQ, Article + FAQ + Breadcrumb schema."""
import html
E = html.escape
DATE = '2026-10-19'
DATE_VI = '19/10/2026'

LEGAL = '<a href="/thue-giup-viec-2026">quy định mới khi thuê người giúp việc (Nghị định 283/2026/NĐ-CP)</a>'

ARTICLES = [
# ---------------------------------------------------------------- 1. GIÁ
dict(slug='gia-thue-giup-viec-ha-noi', lang='vi', service='Giúp việc gia đình',
 title='Giá thuê người giúp việc Hà Nội 2026: bảng lương theo vị trí',
 desc='Bảng lương tham khảo 2026 cho giúp việc, bảo mẫu, chăm sóc người già, quản gia, đầu bếp tại Hà Nội, các yếu tố ảnh hưởng và chi phí ngoài lương cần tính.',
 h1='Giá thuê người giúp việc tại Hà Nội 2026: bảng lương tham khảo theo vị trí',
 card='Lương tham khảo từng vị trí, 6 yếu tố làm thay đổi mức lương và các khoản chi phí ngoài lương gia đình cần tính trước.',
 answer='''Mức lương tham khảo tại Elite Helpers năm 2026 (người giúp việc nhận, theo tháng):
<ul>
<li><strong>Giúp việc gia đình:</strong> 10–25 triệu đồng</li>
<li><strong>Bảo mẫu, chăm bé:</strong> 10–25 triệu đồng</li>
<li><strong>Chăm sóc người già:</strong> 10–25 triệu đồng</li>
<li><strong>Đầu bếp gia đình:</strong> 15–35 triệu đồng</li>
<li><strong>Quản gia:</strong> 18–40 triệu đồng</li>
<li><strong>Hỗ trợ ngắn hạn:</strong> báo giá riêng</li>
</ul>
Mức lương có thể thay đổi theo nhu cầu của gia đình: ở lại hay theo giờ, quy mô nhà, yêu cầu chứng chỉ, bằng cấp, ngoại ngữ, kinh nghiệm quản lý. Ngoài lương, gia đình cần tính khoản tiền tương ứng bảo hiểm xã hội, bảo hiểm y tế trả cho người giúp việc theo quy định.''',
 body='''
<h2 id="bang-luong">Bảng lương tham khảo 2026 theo vị trí</h2>
<div class="tbl-wrap"><table>
<thead><tr><th>Vị trí</th><th>Lương tham khảo/tháng</th><th>Phù hợp với</th></tr></thead>
<tbody>
<tr><td><a href="/giup-viec-gia-dinh">Giúp việc gia đình</a></td><td>10–25 triệu đồng</td><td>Căn hộ, nhà phố, biệt thự cần dọn dẹp, giặt là, đi chợ, nấu ăn</td></tr>
<tr><td><a href="/bao-mau-cham-be">Bảo mẫu, chăm bé</a></td><td>10–25 triệu đồng</td><td>Gia đình có trẻ sơ sinh, trẻ nhỏ</td></tr>
<tr><td><a href="/cham-soc-nguoi-gia">Chăm sóc người già</a></td><td>10–25 triệu đồng</td><td>Ông bà cần hỗ trợ sinh hoạt, ăn uống, đi khám</td></tr>
<tr><td><a href="/dau-bep-gia-dinh">Đầu bếp gia đình</a></td><td>15–35 triệu đồng</td><td>Gia đình cần bữa ăn chuẩn vị, thực đơn tuần, tiệc tại nhà</td></tr>
<tr><td><a href="/quan-gia">Quản gia</a></td><td>18–40 triệu đồng</td><td>Biệt thự, dinh thự, gia đình nhiều nhân sự</td></tr>
<tr><td><a href="/ho-tro-ngan-han">Hỗ trợ ngắn hạn</a></td><td>Báo giá riêng</td><td>Dịp Tết, chuyển nhà, thay người tạm thời</td></tr>
</tbody></table></div>
<p><strong>Mức lương có thể thay đổi theo nhu cầu của gia đình</strong>, ví dụ:</p>
<ul>
<li>Làm ở lại hay theo giờ</li>
<li>Diện tích nhà, số thành viên, có trẻ nhỏ hoặc người già cần chăm sóc</li>
<li>Yêu cầu chứng chỉ, kỹ năng, mức độ chuyên nghiệp</li>
<li>Yêu cầu bằng cấp: đại học, cao đẳng</li>
<li>Yêu cầu ngoại ngữ: tiếng Anh, tiếng Trung, tiếng Hàn…</li>
<li>Yêu cầu kinh nghiệm quản lý</li>
</ul>
<p class="note">Mức lương là khoản người hỗ trợ nhận trực tiếp theo hợp đồng giữa gia đình và người lao động. Mức cụ thể được thống nhất sau khi Elite Helpers nắm rõ công việc.</p>

<h2 id="yeu-to">6 yếu tố làm thay đổi mức lương</h2>
<ol>
<li><strong>Kinh nghiệm:</strong> người đã làm nhiều năm cho gia đình có yêu cầu cao, có người giới thiệu, thường ở mức trên của khung.</li>
<li><strong>Ở lại hay theo giờ:</strong> ở lại cùng gia đình tính theo tháng; theo giờ, theo ca tính theo thời lượng thực tế.</li>
<li><strong>Khối lượng công việc:</strong> diện tích nhà, số người, số bữa ăn, có thú cưng hay không.</li>
<li><strong>Ngoại ngữ:</strong> giao tiếp tiếng Anh cho gia đình người nước ngoài, đại sứ quán.</li>
<li><strong>Kỹ năng đặc thù:</strong> chăm trẻ sơ sinh, nấu món Âu, chăm người cao tuổi nằm một chỗ.</li>
<li><strong>Thời gian làm việc:</strong> làm thêm buổi tối, cuối tuần, ngày lễ được thỏa thuận riêng.</li>
</ol>

<h2 id="chi-phi-khac">Chi phí ngoài lương gia đình cần tính trước</h2>
<ul>
<li><strong>Khoản tiền tương ứng bảo hiểm xã hội, bảo hiểm y tế</strong> trả cùng kỳ lương để người giúp việc tự tham gia. Không trả khoản này có thể bị phạt 10–15 triệu đồng. Xem chi tiết tại {LEGAL}.</li>
<li><strong>Chỗ ở, ăn uống</strong> nếu người giúp việc ở lại.</li>
<li><strong>Tiền tàu xe về nơi cư trú</strong> khi kết thúc hợp đồng, theo quy định.</li>
<li><strong>Ngày nghỉ, lễ Tết, thưởng</strong>: ghi rõ trong hợp đồng để tránh hiểu lầm.</li>
</ul>

<h2 id="toi-uu">Cách tối ưu chi phí mà vẫn chọn đúng người</h2>
<ul>
<li>Viết ra danh sách công việc cụ thể theo ngày, theo tuần trước khi tìm người.</li>
<li>Chọn đúng hình thức: nếu chỉ cần dọn dẹp vài buổi, theo giờ tiết kiệm hơn ở lại. Xem <a href="/giup-viec-o-lai-hay-theo-gio">so sánh ở lại và theo giờ</a>.</li>
<li>Luôn gặp mặt và cho làm thử vài ngày trước khi ký hợp đồng.</li>
</ul>''',
 faq=[
  ('Thuê người giúp việc ở Hà Nội bao nhiêu tiền một tháng?', 'Tại Elite Helpers, lương tham khảo năm 2026 cho giúp việc gia đình là 10–25 triệu đồng/tháng, bảo mẫu 10–25 triệu, chăm sóc người già 10–25 triệu, đầu bếp 15–35 triệu, quản gia 18–40 triệu. Mức cụ thể tùy kinh nghiệm, hình thức và khối lượng công việc.'),
  ('Lương trả cho ai?', 'Lương trả trực tiếp cho người giúp việc theo hợp đồng lao động giữa gia đình và người giúp việc.'),
  ('Ngoài lương còn khoản nào bắt buộc không?', 'Có. Gia đình trả thêm khoản tiền tương ứng mức đóng bảo hiểm xã hội bắt buộc và bảo hiểm y tế cùng kỳ lương để người giúp việc tự tham gia, theo Bộ luật Lao động và Nghị định 283/2026/NĐ-CP.'),
  ('Vì sao mức lương của Elite Helpers cao hơn mặt bằng?', 'Vì ứng viên được xác minh lý lịch, phỏng vấn trực tiếp, chọn theo đúng nếp nhà của từng gia đình và được theo dõi trong suốt quá trình làm việc.'),
 ]),
# ---------------------------------------------------------------- 2. BẢO MẪU
dict(slug='kinh-nghiem-thue-bao-mau', lang='vi', service='Bảo mẫu, chăm bé',
 title='Kinh nghiệm thuê bảo mẫu cho trẻ sơ sinh, trẻ nhỏ tại Hà Nội',
 desc='Cách chọn bảo mẫu an toàn: tiêu chí, 10 câu hỏi phỏng vấn, những điều cần quan sát khi làm thử, quy tắc trong nhà và hợp đồng đúng luật.',
 h1='Kinh nghiệm thuê bảo mẫu cho trẻ sơ sinh và trẻ nhỏ',
 card='Tiêu chí chọn bảo mẫu, 10 câu hỏi phỏng vấn, điều cần quan sát khi làm thử và quy tắc an toàn trong nhà.',
 answer='''Để thuê được bảo mẫu phù hợp, gia đình nên:
<ul>
<li>Xác định rõ độ tuổi của bé và công việc đi kèm</li>
<li>Ưu tiên người có kinh nghiệm chăm trẻ cùng độ tuổi</li>
<li>Kiểm tra giấy tờ, nơi cư trú và người giới thiệu</li>
<li>Phỏng vấn trực tiếp bằng câu hỏi tình huống</li>
<li>Cho làm thử vài ngày khi có người lớn ở nhà</li>
<li>Ký hợp đồng bằng văn bản theo quy định</li>
</ul>''',
 body='''
<h2 id="nhu-cau">Bước 1: Xác định nhu cầu trước khi tìm người</h2>
<ul>
<li>Độ tuổi của bé: sơ sinh, dưới 3 tuổi hay đã đi học.</li>
<li>Hình thức: ở lại cùng gia đình hay theo giờ, có cần trông đêm không.</li>
<li>Công việc đi kèm: nấu ăn cho bé, giặt đồ bé, đưa đón đi học, dọn dẹp chung.</li>
<li>Ngôn ngữ: gia đình người nước ngoài có thể cần bảo mẫu giao tiếp tiếng Anh.</li>
</ul>

<h2 id="tieu-chi">Bước 2: Tiêu chí chọn bảo mẫu</h2>
<div class="tbl-wrap"><table>
<thead><tr><th>Tiêu chí</th><th>Vì sao quan trọng</th></tr></thead>
<tbody>
<tr><td>Kinh nghiệm chăm trẻ cùng độ tuổi</td><td>Chăm trẻ sơ sinh (bú, tắm, giấc ngủ) khác hẳn chăm trẻ 3–5 tuổi</td></tr>
<tr><td>Đã có con, tính cách kiên nhẫn</td><td>Hiểu nhịp sinh hoạt của trẻ, bình tĩnh khi bé quấy khóc</td></tr>
<tr><td>Vệ sinh, sức khỏe tốt</td><td>Trẻ nhỏ dễ lây bệnh</td></tr>
<tr><td>Giấy tờ, nơi cư trú rõ ràng</td><td>Biết rõ người sống cùng con mình</td></tr>
<tr><td>Người giới thiệu, gia đình cũ</td><td>Kiểm chứng cách làm việc thực tế</td></tr>
</tbody></table></div>

<h2 id="phong-van">Bước 3: 10 câu hỏi phỏng vấn nên dùng</h2>
<ol>
<li>Chị đã chăm trẻ ở độ tuổi này bao lâu, cho mấy gia đình?</li>
<li>Một ngày chăm bé của chị thường diễn ra thế nào?</li>
<li>Khi bé sốt cao vào ban đêm, chị làm gì?</li>
<li>Bé không chịu ăn, chị xử lý ra sao?</li>
<li>Chị cho bé xem điện thoại, ti vi không?</li>
<li>Chị làm gì khi bé bị hóc, sặc?</li>
<li>Chị nghĩ sao về việc gia đình đặt quy tắc riêng cho bé?</li>
<li>Vì sao chị nghỉ ở gia đình trước?</li>
<li>Chị có thể làm việc lâu dài không, nghỉ Tết bao lâu?</li>
<li>Chị cần gia đình hỗ trợ gì để làm tốt nhất?</li>
</ol>

<h2 id="lam-thu">Bước 4: Làm thử, cần quan sát gì</h2>
<ul>
<li>Cách bảo mẫu bế, cho ăn, tắm và ru bé ngủ.</li>
<li>Sự chủ động: tự sắp xếp đồ của bé, hỏi lại khi chưa rõ.</li>
<li>Vệ sinh: rửa tay, tiệt trùng bình sữa, giữ khu vực của bé sạch sẽ.</li>
<li>Phản ứng của bé sau vài ngày.</li>
</ul>

<h2 id="an-toan">Bước 5: Quy tắc an toàn trong nhà</h2>
<ul>
<li>Dán sẵn số điện thoại của bố mẹ, người thân và cấp cứu 115.</li>
<li>Thống nhất bằng văn bản: giờ ăn, giờ ngủ, thực phẩm không được dùng, thuốc chỉ dùng khi bố mẹ đồng ý.</li>
<li>Nếu lắp camera, thông báo rõ cho bảo mẫu từ đầu. Vừa minh bạch, vừa tôn trọng quyền riêng tư của người lao động.</li>
</ul>

<h2 id="hop-dong">Bước 6: Ký hợp đồng đúng luật</h2>
<p>Hợp đồng với người giúp việc gia đình phải bằng văn bản. Gia đình cũng cần thông báo UBND cấp xã khi bắt đầu và khi kết thúc hợp đồng. Xem đủ các bước tại {LEGAL} và <a href="/mau-hop-dong-giup-viec-gia-dinh.docx" download>tải mẫu hợp đồng</a>.</p>''',
 faq=[
  ('Lương bảo mẫu ở Hà Nội bao nhiêu?', 'Tại Elite Helpers, lương tham khảo cho bảo mẫu, người chăm bé năm 2026 là 10–25 triệu đồng/tháng, tùy kinh nghiệm, độ tuổi của bé, hình thức ở lại hay theo giờ và yêu cầu ngoại ngữ.'),
  ('Nên chọn bảo mẫu đã có con hay chưa có con?', 'Nên ưu tiên người đã có con và có kinh nghiệm chăm trẻ cùng độ tuổi, vì họ hiểu nhịp sinh hoạt của trẻ và bình tĩnh hơn khi bé ốm, quấy khóc.'),
  ('Có nên cho bảo mẫu làm thử không?', 'Có. Gia đình nên cho làm thử vài ngày khi có người lớn ở nhà để quan sát cách chăm bé và phản ứng của bé trước khi ký hợp đồng.'),
  ('Bao lâu thì tìm được bảo mẫu qua Elite Helpers?', 'Thường từ vài ngày đến khoảng một tuần, tùy yêu cầu. Gia đình nhận hồ sơ ứng viên đã được xác minh, phỏng vấn trước khi gặp mặt.'),
 ]),
# ---------------------------------------------------------------- 3. NGƯỜI GIÀ
dict(slug='thue-nguoi-cham-soc-nguoi-gia', lang='vi', service='Chăm sóc người già',
 title='Thuê người chăm sóc người già tại nhà: lưu ý gì? | Elite Helpers',
 desc='Hướng dẫn thuê người chăm sóc người cao tuổi tại nhà ở Hà Nội: đánh giá mức hỗ trợ, phạm vi công việc, tiêu chí chọn người, chuẩn bị nhà an toàn.',
 h1='Thuê người chăm sóc người già tại nhà: những điều gia đình cần lưu ý',
 card='Đánh giá ông bà cần hỗ trợ đến đâu, người chăm sóc làm gì và không làm gì, cách chọn người và chuẩn bị nhà an toàn.',
 answer='Trước khi thuê, gia đình nên <strong>đánh giá mức độ ông bà cần hỗ trợ</strong> (tự đi lại, cần hỗ trợ một phần hay nằm một chỗ), <strong>thống nhất phạm vi công việc</strong> (sinh hoạt, ăn uống, vệ sinh, nhắc thuốc theo chỉ định của bác sĩ, đưa đi khám), chọn người <strong>kiên nhẫn, có kinh nghiệm với người cao tuổi</strong> và cho <strong>làm thử</strong>. Người chăm sóc tại nhà hỗ trợ sinh hoạt, không thay thế điều dưỡng hay chỉ định của bác sĩ.',
 body='''
<h2 id="danh-gia">Bước 1: Ông bà cần hỗ trợ đến mức nào?</h2>
<div class="tbl-wrap"><table>
<thead><tr><th>Mức độ</th><th>Biểu hiện</th><th>Hình thức thường phù hợp</th></tr></thead>
<tbody>
<tr><td>Tự chủ phần lớn</td><td>Tự đi lại, cần người nấu ăn, trò chuyện, đi cùng khi ra ngoài</td><td>Theo giờ hoặc ban ngày</td></tr>
<tr><td>Cần hỗ trợ một phần</td><td>Đi lại khó, cần giúp tắm rửa, thay đồ, nhắc thuốc</td><td>Ở lại cùng gia đình</td></tr>
<tr><td>Nằm một chỗ</td><td>Cần trở mình, vệ sinh, ăn uống tại giường</td><td>Ở lại, có thể cần thêm điều dưỡng theo chỉ định y tế</td></tr>
</tbody></table></div>

<h2 id="pham-vi">Bước 2: Người chăm sóc làm gì và không làm gì</h2>
<ul>
<li><strong>Làm:</strong> hỗ trợ ăn uống, vệ sinh cá nhân, đi lại; nhắc giờ uống thuốc theo đơn; đưa đi khám; trò chuyện, đi dạo; giữ phòng ở sạch sẽ.</li>
<li><strong>Không tự ý làm:</strong> đổi thuốc, chỉnh liều, thực hiện thủ thuật y tế. Những việc này cần bác sĩ hoặc điều dưỡng.</li>
</ul>

<h2 id="tieu-chi">Bước 3: Tiêu chí chọn người chăm sóc</h2>
<ul>
<li>Kinh nghiệm chăm người cao tuổi, đặc biệt người có mức độ hỗ trợ tương tự.</li>
<li>Kiên nhẫn, nhẹ nhàng, biết lắng nghe.</li>
<li>Sức khỏe tốt để đỡ, dìu ông bà an toàn.</li>
<li>Giấy tờ, nơi cư trú rõ ràng, có người giới thiệu.</li>
</ul>

<h2 id="nha-an-toan">Bước 4: Chuẩn bị nhà ở an toàn</h2>
<ul>
<li>Thảm chống trơn và tay vịn ở nhà tắm, nhà vệ sinh.</li>
<li>Đèn ngủ ở lối đi ban đêm, dọn gọn dây điện, đồ dễ vấp.</li>
<li>Sổ theo dõi hằng ngày: ăn uống, giấc ngủ, thuốc, dấu hiệu bất thường.</li>
<li>Danh sách số điện thoại người thân, bác sĩ, cấp cứu 115.</li>
</ul>

<h2 id="hop-dong">Bước 5: Hợp đồng và thủ tục</h2>
<p>Ký hợp đồng bằng văn bản, ghi rõ giờ làm, ngày nghỉ, việc ban đêm. Thực hiện đúng {LEGAL}.</p>''',
 faq=[
  ('Thuê người chăm sóc người già tại nhà bao nhiêu tiền?', 'Tại Elite Helpers, lương tham khảo cho người chăm sóc người già năm 2026 là 10–25 triệu đồng/tháng, tùy mức độ ông bà cần hỗ trợ, hình thức ở lại hay theo giờ và kinh nghiệm của người chăm sóc.'),
  ('Người chăm sóc có trông ban đêm không?', 'Có thể, nếu thỏa thuận trước. Với hình thức ở lại, gia đình nên ghi rõ việc ban đêm và thời gian nghỉ bù trong hợp đồng.'),
  ('Người chăm sóc có thay được điều dưỡng không?', 'Không. Người chăm sóc tại nhà hỗ trợ sinh hoạt hằng ngày. Việc chuyên môn y tế cần bác sĩ hoặc điều dưỡng theo chỉ định.'),
  ('Elite Helpers xác minh người chăm sóc thế nào?', 'Mỗi ứng viên được xác minh giấy tờ tùy thân, nơi cư trú, kinh nghiệm làm việc và phỏng vấn trực tiếp. Gia đình gặp mặt và cho làm thử trước khi quyết định.'),
 ]),
# ---------------------------------------------------------------- 4. Ở LẠI HAY THEO GIỜ
dict(slug='giup-viec-o-lai-hay-theo-gio', lang='vi', service='Giúp việc gia đình',
 title='Giúp việc ở lại hay theo giờ: nên chọn loại nào? | Elite Helpers',
 desc='So sánh giúp việc ở lại và theo giờ về chi phí, mức linh hoạt, sự riêng tư và loại gia đình phù hợp, kèm 5 câu hỏi giúp chọn đúng hình thức.',
 h1='Giúp việc ở lại hay theo giờ: nên chọn hình thức nào?',
 card='Bảng so sánh chi phí, linh hoạt, riêng tư và 5 câu hỏi giúp gia đình chọn đúng hình thức ngay từ đầu.',
 answer='Chọn <strong>giúp việc ở lại</strong> khi gia đình cần người hỗ trợ cả ngày, có trẻ nhỏ hoặc người cao tuổi, nhà rộng và có phòng riêng cho người giúp việc. Chọn <strong>theo giờ</strong> khi chỉ cần dọn dẹp, nấu ăn vài buổi mỗi tuần, nhà nhỏ hoặc gia đình muốn giữ sự riêng tư. Nhiều gia đình kết hợp cả hai: một người ở lại và một người theo giờ cho việc nặng định kỳ.',
 body='''
<h2 id="so-sanh">Bảng so sánh nhanh</h2>
<div class="tbl-wrap"><table>
<thead><tr><th>Tiêu chí</th><th>Ở lại cùng gia đình</th><th>Theo giờ, theo ca</th></tr></thead>
<tbody>
<tr><td>Thời gian hỗ trợ</td><td>Cả ngày, có mặt khi cần</td><td>Theo buổi đã hẹn</td></tr>
<tr><td>Cách tính chi phí</td><td>Lương tháng, cộng chỗ ở, ăn uống</td><td>Theo giờ hoặc theo ca thực tế</td></tr>
<tr><td>Riêng tư</td><td>Ít hơn, cần phòng riêng cho người giúp việc</td><td>Cao hơn</td></tr>
<tr><td>Phù hợp</td><td>Có trẻ nhỏ, người cao tuổi, nhà rộng, bố mẹ đi làm cả ngày</td><td>Căn hộ, gia đình ít người, cần dọn dẹp định kỳ</td></tr>
<tr><td>Hợp đồng</td><td>Bắt buộc bằng văn bản</td><td>Bắt buộc bằng văn bản nếu là quan hệ lao động giúp việc gia đình</td></tr>
</tbody></table></div>

<h2 id="cau-hoi">5 câu hỏi giúp chọn đúng</h2>
<ol>
<li>Nhà có trẻ nhỏ, người cao tuổi cần người bên cạnh cả ngày không?</li>
<li>Mỗi tuần thực sự cần bao nhiêu giờ cho việc nhà?</li>
<li>Nhà có phòng riêng, khu vệ sinh riêng cho người ở lại không?</li>
<li>Gia đình có cần người nấu bữa tối hằng ngày không?</li>
<li>Gia đình đặt nặng sự riêng tư đến mức nào?</li>
</ol>

<h2 id="ket-hop">Khi nào nên kết hợp</h2>
<p>Biệt thự, nhà nhiều tầng hoặc gia đình đông người thường có một người ở lại lo việc hằng ngày, thêm người theo giờ cho tổng vệ sinh, giặt rèm, lau kính định kỳ. Với gia đình cần điều phối nhiều người, xem dịch vụ <a href="/quan-gia">quản gia</a>.</p>

<h2 id="chi-phi">Chi phí tham khảo</h2>
<p>Xem bảng lương từng vị trí tại <a href="/gia-thue-giup-viec-ha-noi">giá thuê người giúp việc tại Hà Nội 2026</a>. Dù chọn hình thức nào, gia đình cũng cần thực hiện {LEGAL}.</p>''',
 faq=[
  ('Giúp việc theo giờ có phải ký hợp đồng không?', 'Nếu là quan hệ lao động giúp việc gia đình, Bộ luật Lao động 2019 yêu cầu hợp đồng bằng văn bản, kể cả khi làm theo giờ.'),
  ('Giúp việc ở lại có được nghỉ hằng tuần không?', 'Có. Ngày nghỉ hằng tuần, nghỉ lễ Tết và nghỉ hằng năm được thỏa thuận trong hợp đồng theo quy định của Bộ luật Lao động.'),
  ('Elite Helpers có cung cấp cả hai hình thức không?', 'Có. Elite Helpers giới thiệu người giúp việc ở lại và theo giờ, theo ca tại Hà Nội và một số khu vực lân cận.'),
 ]),
# ---------------------------------------------------------------- 5. EN EXPAT GUIDE
dict(slug='hiring-helper-hanoi-expat-guide', lang='en', service='Household staff',
 title='Hiring a Housekeeper or Nanny in Hanoi: 2026 Expat Guide',
 desc='How expat families in Hanoi hire housekeepers, nannies and elderly caregivers in 2026: reference salaries, legal rules, contracts and the hiring process.',
 h1='Hiring a housekeeper or nanny in Hanoi: a 2026 guide for expat families',
 card='',
 answer='''To hire household staff in Hanoi in 2026: agree the duties and schedule, interview and trial the candidate, sign a <strong>written contract</strong> (required by Article 162 of the 2019 Labour Code), <strong>notify the commune-level People's Committee</strong> when employment starts and ends, and pay the helper the <strong>social and health insurance amounts</strong> with the salary. Reference monthly salaries with Elite Helpers:
<ul>
<li><strong>Housekeeper:</strong> 10–25 million VND</li>
<li><strong>Nanny:</strong> 10–25 million VND</li>
<li><strong>Elderly caregiver:</strong> 10–25 million VND</li>
<li><strong>Family cook:</strong> 15–35 million VND</li>
<li><strong>House manager:</strong> 18–40 million VND</li>
</ul>''',
 body='''
<h2 id="salaries">Reference salaries in 2026</h2>
<div class="tbl-wrap"><table>
<thead><tr><th>Role</th><th>Monthly salary (paid to the helper)</th></tr></thead>
<tbody>
<tr><td>Housekeeper (live-in or part-time)</td><td>10–25 million VND</td></tr>
<tr><td>Nanny</td><td>10–25 million VND</td></tr>
<tr><td>Elderly caregiver</td><td>10–25 million VND</td></tr>
<tr><td>Family cook</td><td>15–35 million VND</td></tr>
<tr><td>House manager</td><td>18–40 million VND</td></tr>
<tr><td>Short-term help</td><td>Quoted separately</td></tr>
</tbody></table></div>
<p class="note">The exact figure depends on experience, English level, live-in or part-time, and workload.</p>

<h2 id="legal">Legal basics for employers</h2>
<ul>
<li><strong>Written contract</strong> with the domestic worker (Article 162, Labour Code 2019).</li>
<li><strong>Notify the commune-level People's Committee</strong> where the helper works, when employment starts and ends.</li>
<li><strong>Pay the social and health insurance amounts</strong> together with the salary so the helper can join insurance.</li>
<li><strong>Never keep the helper's ID papers.</strong></li>
<li>Since 10 September 2026, Article 28 of Decree 283/2026/ND-CP fines employers for violations: 1–3 million VND for not notifying the commune, 10–15 million VND for keeping ID papers or not paying the insurance amounts. Details in Vietnamese: <a href="/thue-giup-viec-2026" lang="vi">Thuê người giúp việc năm 2026</a>.</li>
</ul>

<h2 id="process">How hiring works with Elite Helpers</h2>
<ol>
<li><strong>Tell us your needs:</strong> duties, hours, live-in or part-time, English level, start date.</li>
<li><strong>Receive vetted profiles:</strong> ID, residence and work history checked; interviewed in person.</li>
<li><strong>Meet and trial:</strong> meet the candidate and arrange a short trial at home.</li>
<li><strong>Contract and follow-up:</strong> we help both sides agree the contract and follow up afterwards.</li>
</ol>

<h2 id="tips">Practical tips from experienced families</h2>
<ul>
<li>Write a simple house manual: daily routine, cleaning products, food rules, children's schedule.</li>
<li>Test English with real situations, for example explaining a child's allergy or a recipe.</li>
<li>Agree days off, Tet holiday and any bonus in writing from the start.</li>
<li>If you install cameras, tell the helper clearly before they start.</li>
</ul>
<p><a href="/en">Learn more about Elite Helpers in English</a> or send a request through our English form.</p>''',
 faq=[
  ('How much does a housekeeper cost in Hanoi?', 'With Elite Helpers, reference monthly salaries in 2026 are 10–25 million VND for a housekeeper, 10–25 million for a nanny, 10–25 million for an elderly caregiver, 15–35 million for a family cook and 18–40 million for a house manager.'),
  ('Do I need a contract with my helper in Vietnam?', 'Yes. Article 162 of the 2019 Labour Code requires a written contract with a domestic worker, and employers must notify the commune-level People\'s Committee when employment starts and ends.'),
  ('Can I find an English-speaking nanny in Hanoi?', 'Yes. Elite Helpers introduces nannies, housekeepers and house managers with basic to good English, checked at interview.'),
  ('Which areas of Hanoi do you cover?', 'Central Hanoi, including Tay Ho, Ba Dinh, Hoan Kiem, Dong Da, Cau Giay, Nam Tu Liem and Long Bien, plus nearby Bac Ninh and Hung Yen.'),
 ]),
]

for a in ARTICLES:
    a['body'] = a['body'].replace('{LEGAL}', LEGAL)


def plain(h):
    import re
    h = h.replace('<li>', ' – ')
    return re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', h)).replace(' :', ':').strip()


def article_page(g, a):
    SITE = g['SITE']; path = '/' + a['slug']; vi = a['lang'] == 'vi'
    crumbs = [('Trang chủ', '/'), ('Cẩm nang', '/cam-nang'), (a['h1'].split(':')[0], None)] if vi else \
             [('Home', '/en'), ('Guide', None)]
    upd = ('Cẩm nang · Cập nhật ' + DATE_VI) if vi else ('Guide · Updated 19 October 2026')
    by = ('Biên soạn: <b>Đội ngũ Elite Helpers</b> · Hà Nội') if vi else ('Written by <b>the Elite Helpers team</b> · Hanoi')
    qa = 'Trả lời nhanh' if vi else 'Quick answer'
    faq_h = 'Hỏi đáp nhanh' if vi else 'FAQ'
    related = ''
    if vi:
        others = [x for x in ARTICLES if x['lang'] == 'vi' and x['slug'] != a['slug']][:3]
        related = '<h2>Bài liên quan</h2><ul>' + ''.join(f'<li><a href="/{x["slug"]}">{E(x["h1"])}</a></li>' for x in others) + \
                  '<li><a href="/thue-giup-viec-2026">Thuê người giúp việc năm 2026: 7 việc cần làm để đúng luật</a></li></ul>'
    main = f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="shell relative pb-16 pt-32 lg:pb-20 lg:pt-40">
    {g['crumbs_html'](crumbs)}
    <span class="eyebrow">{upd}</span>
    <h1 id="pg-title" class="t-display mt-4" style="max-width:24ch">{E(a['h1'])}</h1>
    <p class="byline">{by}</p>
  </div>
</section>
<article class="on-light bg-paper py-16 lg:py-24">
  <div class="shell"><div class="prose">
    <div class="answer" role="note"><b>{qa}</b><div class="ans-body">{a['answer']}</div></div>
    {a['body']}
    {related}
  </div></div>
</article>
<section class="on-light bg-linen py-20 lg:py-24" aria-labelledby="faq-a">
  <div class="shell grid gap-12 lg:grid-cols-12 lg:gap-10">
    <div class="lg:col-span-4"><h2 id="faq-a" class="t-h2 text-shutter">{faq_h}</h2></div>
    <div class="faq lg:col-span-8">
{g['faq_html'](a['faq'])}
    </div>
  </div>
</section>'''
    import re
    plain_answer = plain(a['answer'])
    art = {'@type': 'Article', '@id': SITE + path + '#article', 'headline': a['h1'], 'description': a['desc'], 'abstract': plain_answer,
           'url': SITE + path, 'inLanguage': a['lang'], 'datePublished': DATE, 'dateModified': DATE,
           'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'}, 'image': SITE + '/og-giup-viec-elite.jpg',
           'mainEntityOfPage': SITE + path, 'about': {'@type': 'Service', 'name': a['service'], 'provider': {'@id': SITE + '/#org'}, 'areaServed': {'@type': 'City', 'name': 'Hà Nội' if vi else 'Hanoi'}}}
    graph = [art, g['faq_ld'](a['faq'], path)]
    if vi: graph.insert(1, g['crumbs_ld'](crumbs, path))
    ld = {'@context': 'https://schema.org', '@graph': graph}
    if vi:
        html_ = g['page'](a['title'], a['desc'], path, main + '\n' + g['cta_block'](a['service'], h='Cần người phù hợp cho gia đình?'), ld, og_type='article')
    else:
        import pages_extra as X
        top = X.EN_HEADER
        for h in ['services', 'who', 'process', 'faq', 'contact']:
            top = top.replace(f'href="#{h}"', f'href="/en#{h}"')
        cta = '''<section class="on-dark bg-lacquer py-20 text-paper lg:py-24"><div class="shell"><h2 class="t-h2">Find the right helper for your home</h2>
<div class="mt-8 flex flex-wrap gap-3"><a class="btn btn-brass" href="/en#contact">Send a request</a><a class="btn btn-ghost-light" href="https://zalo.me/0948919598" target="_blank" rel="noopener" data-track="zalo">Zalo +84 948 919 598</a></div></div></section>'''
        html_ = g['page'](a['title'], a['desc'], path, main + '\n' + cta, ld, lang='en', og_type='article', top=top, bottom=X.en_footer(g))
        html_ = html_.replace('<main id="noi-dung">', '<main id="content">')
    return a['slug'] + '.html', path, html_


def all_articles(g):
    return [article_page(g, a) for a in ARTICLES]
