# -*- coding: utf-8 -*-
"""Trang tuyển dụng, cẩm nang 2026, trang tiếng Anh, 404 và các tệp meta."""
import os, re, json, shutil, html, hashlib
E = html.escape

# ======================= TUYỂN DỤNG =======================
RECRUIT_FAQ = [
 ('Ứng tuyển vào Elite Helpers có mất phí không?', 'Không. Elite Helpers không thu bất kỳ khoản phí nào của người lao động khi ứng tuyển, phỏng vấn hay được giới thiệu việc làm.'),
 ('Tôi cần chuẩn bị giấy tờ gì?', 'Anh/Chị mang theo căn cước công dân bản gốc khi phỏng vấn để đối chiếu. Website không thu thập số CCCD hay tài khoản ngân hàng. Gia đình không được giữ giấy tờ tùy thân của người lao động; hành vi này bị phạt 10–15 triệu đồng theo Nghị định 283/2026/NĐ-CP.'),
 ('Bao lâu thì được gọi lại?', 'Elite Helpers gọi lại trong 1–2 ngày làm việc sau khi nhận hồ sơ để hẹn phỏng vấn.'),
 ('Tôi có được ký hợp đồng không?', 'Có. Bộ luật Lao động 2019 (Điều 162) yêu cầu hợp đồng với người giúp việc gia đình phải bằng văn bản. Elite Helpers hỗ trợ hai bên thống nhất nội dung hợp đồng: công việc, giờ làm, ngày nghỉ, lương, chỗ ở.'),
 ('Chưa có kinh nghiệm có ứng tuyển được không?', 'Được. Anh/Chị cứ gửi hồ sơ và ghi rõ những việc mình làm được; Elite Helpers sẽ tư vấn vị trí phù hợp.'),
]

def recruit_page(g):
    path = '/tuyen-dung'
    crumbs = [('Trang chủ', '/'), ('Tuyển dụng', None)]
    title = 'Tuyển giúp việc, bảo mẫu, chăm sóc người già tại Hà Nội'
    desc = 'Việc làm giúp việc, bảo mẫu, chăm sóc người già, quản gia, đầu bếp tại Hà Nội. Gia đình uy tín, có hợp đồng, không thu phí. Ứng tuyển online 2 phút.'
    import jobs as J
    main = f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="shell relative pb-20 pt-32 lg:pb-24 lg:pt-40">
    {g['crumbs_html'](crumbs)}
    <span class="eyebrow">Việc làm cho người lao động</span>
    <h1 id="pg-title" class="t-display mt-4" style="max-width:22ch">Tuyển giúp việc, bảo mẫu, chăm sóc người già tại Hà Nội</h1>
    <p class="t-lead mt-6 max-w-[56ch] text-mist">Làm việc cho gia đình Việt Nam, gia đình người nước ngoài và đại sứ quán tại Hà Nội. Có hợp đồng, công việc ổn định, không thu phí người lao động.</p>
    <div class="mt-9 flex flex-wrap gap-3">
      <a class="btn btn-brass" href="#viec-dang-tuyen">Xem việc đang tuyển</a>
      <a class="btn btn-ghost-light" href="#ung-tuyen" data-open="ungvien">Gửi hồ sơ (2 phút)</a>
    </div>
    {J.tabs('jobs')}
  </div>
</section>
{J.jobs_section(g)}
<section id="tim-viec-an-toan" class="on-light bg-linen py-20 lg:py-24" aria-labelledby="at-title">
  <div class="shell">
    <span class="eyebrow">Tìm việc an toàn</span>
    <h2 id="at-title" class="t-h2 mt-3 text-shutter" style="max-width:24ch">Chị em đi làm giúp việc, hãy chọn nơi rõ ràng ngay từ đầu</h2>
    <p class="mt-4 max-w-[60ch] text-ink-soft">Một công việc tốt luôn bắt đầu từ sự minh bạch. Trước khi nhận việc ở bất cứ đâu, chị em hãy dành vài phút đối chiếu những điểm dưới đây.</p>
    <div class="safe2">
      <article class="safe-card safe-warn" aria-labelledby="at-a">
        <img src="assets/img/tim-viec-can-nhac-480.webp" srcset="assets/img/tim-viec-can-nhac-480.webp 480w, assets/img/tim-viec-can-nhac-760.webp 760w" sizes="(min-width:1024px) 560px, 92vw" width="480" height="316" alt="Người phụ nữ đứng giữa văn phòng giới thiệu việc làm, cầm điện thoại và túi hành lý, vẻ băn khoăn" loading="lazy" decoding="async">
        <div class="safe-body">
          <h3 id="at-a">Trước khi nhận việc, hãy <em>cân nhắc</em> nếu…</h3>
          <ul class="safe-list" role="list">
            <li>Tin tuyển đăng đi đăng lại</li>
            <li>Lương báo một đằng, trả một nẻo</li>
            <li>Thu phí trước khi đi làm</li>
            <li>Phải ở trọ chờ việc</li>
            <li>Không rõ thông tin gia đình</li>
            <li>Không có hợp đồng</li>
          </ul>
        </div>
      </article>
      <span class="safe-arrow" aria-hidden="true"></span>
      <article class="safe-card safe-ok" aria-labelledby="at-b">
        <img src="assets/img/tim-viec-an-tam-480.webp" srcset="assets/img/tim-viec-an-tam-480.webp 480w, assets/img/tim-viec-an-tam-760.webp 760w" sizes="(min-width:1024px) 560px, 92vw" width="480" height="316" alt="Người giúp việc trò chuyện vui vẻ cùng chủ nhà bên bàn trà, cùng xem bản thỏa thuận công việc" loading="lazy" decoding="async">
        <div class="safe-body">
          <h3 id="at-b">Ở Elite Helpers,<br>chị em được <em>an tâm</em></h3>
          <ul class="safe-list" role="list">
            <li>Không thu bất kỳ khoản phí nào của người lao động</li>
            <li>Lương đúng như tin đăng</li>
            <li>Không ở trọ chờ việc</li>
            <li>Trao đổi kỹ qua điện thoại, Zalo trước khi gặp</li>
            <li>Gặp gia đình trước khi nhận việc</li>
            <li>Hợp đồng rõ ràng, luôn đồng hành hỗ trợ</li>
          </ul>
        </div>
      </article>
    </div>
    <div class="mt-10 flex flex-wrap gap-3">
      <a class="btn btn-brass" href="#ung-tuyen" data-open="ungvien">Ứng tuyển online (2 phút)</a>
      <a class="btn btn-ghost-dark" href="https://zalo.me/0948919598" target="_blank" rel="noopener" data-track="zalo">Hỏi trước qua Zalo 0948 919 598</a>
    </div>
  </div>
</section>
{__import__('news').teaser_section(g)}
<section class="on-light bg-linen py-20 lg:py-24" aria-labelledby="ql-title">
  <div class="shell grid gap-14 lg:grid-cols-12 lg:gap-12">
    <div class="lg:col-span-6">
      <h2 id="ql-title" class="t-h2 text-shutter">Quyền lợi</h2>
      <ul class="checks" role="list">
        <li>Không thu phí ứng tuyển, phỏng vấn hay giới thiệu việc làm</li>
        <li>Được tư vấn vị trí đúng kinh nghiệm, sở trường</li>
        <li>Gia đình được Elite Helpers tìm hiểu trước; có hợp đồng bằng văn bản</li>
        <li>Thỏa thuận rõ công việc, giờ làm, ngày nghỉ, lương, chỗ ở trước khi bắt đầu</li>
        <li>Có người đồng hành, hỗ trợ trong suốt quá trình làm việc</li>
      </ul>
    </div>
    <div class="lg:col-span-6">
      <h2 class="t-h2 text-shutter">Yêu cầu chung</h2>
      <ul class="checks" role="list">
        <li>Có căn cước công dân, nơi cư trú rõ ràng</li>
        <li>Trung thực, sạch sẽ, có trách nhiệm với công việc</li>
        <li>Đủ sức khỏe làm việc; ưu tiên có kinh nghiệm theo vị trí</li>
        <li>Giao tiếp tiếng Anh là lợi thế với gia đình nước ngoài, đại sứ quán</li>
      </ul>
    </div>
  </div>
</section>
<section class="on-light bg-paper py-20 lg:py-24" aria-labelledby="qtut-title">
  <div class="shell">
    <h2 id="qtut-title" class="t-h2 text-shutter">Quy trình ứng tuyển</h2>
    <ol class="steps-sm" role="list">
      <li><b>Gửi hồ sơ online</b><span>Điền form 2 phút trên website hoặc nhắn Zalo.</span></li>
      <li><b>Phỏng vấn</b><span>Elite Helpers gọi lại trong 1–2 ngày, hẹn phỏng vấn trực tiếp.</span></li>
      <li><b>Gặp gia đình, làm thử</b><span>Gặp gia đình phù hợp, làm thử để hai bên cùng đánh giá.</span></li>
      <li><b>Ký hợp đồng, bắt đầu</b><span>Ký hợp đồng bằng văn bản, được theo dõi, hỗ trợ khi làm việc.</span></li>
    </ol>
  </div>
</section>
<section class="on-light bg-linen py-20 lg:py-24" aria-labelledby="fq-title">
  <div class="shell grid gap-12 lg:grid-cols-12 lg:gap-10">
    <div class="lg:col-span-4"><h2 id="fq-title" class="t-h2 text-shutter">Hỏi đáp cho người ứng tuyển</h2></div>
    <div class="faq lg:col-span-8">
{g['faq_html'](RECRUIT_FAQ)}
    </div>
  </div>
</section>
<section class="on-dark bg-lacquer py-20 text-paper lg:py-24" aria-labelledby="cta-title">
  <div class="shell">
    <h2 id="cta-title" class="t-h2">Sẵn sàng làm việc cùng Elite Helpers?</h2>
    <div class="mt-8 flex flex-wrap gap-3">
      <a class="btn btn-brass" href="#ung-tuyen" data-open="ungvien">Gửi hồ sơ ứng tuyển</a>
      <a class="btn btn-ghost-light" href="tel:0948919598" data-track="call">Gọi 0948 919 598</a>
    </div>
  </div>
</section>'''
    SITE = g['SITE']
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': SITE + path + '#webpage', 'url': SITE + path, 'name': title, 'description': desc, 'inLanguage': 'vi',
         'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#org'}},
        g['crumbs_ld'](crumbs, path), g['faq_ld'](RECRUIT_FAQ, path)]}
    return 'tuyen-dung.html', path, g['page'](title, desc, path, main, ld)

def news_page(g):
    import jobs as J, news as N
    path = '/tin-tuc'
    crumbs = [('Trang chủ', '/'), ('Tuyển dụng', '/tuyen-dung'), ('Tin tức', None)]
    title = 'Tin tức cho người lao động giúp việc, bảo mẫu, chăm sóc người già'
    desc = 'Bản tin hằng tuần của Elite Helpers: quy định mới, quyền lợi, mức lương và kinh nghiệm tìm việc giúp việc gia đình, bảo mẫu, chăm sóc người già tại Hà Nội.'
    main = f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="shell relative pb-16 pt-32 lg:pb-20 lg:pt-40">
    {g['crumbs_html'](crumbs)}
    <span class="eyebrow">Bản tin người lao động · cập nhật hằng tuần</span>
    <h1 id="pg-title" class="t-display mt-4" style="max-width:22ch">Tin tức, quyền lợi và kinh nghiệm tìm việc</h1>
    <p class="t-lead mt-6 max-w-[56ch] text-mist">Elite Helpers tổng hợp quy định mới và tin tức về nghề giúp việc từ các báo chính thống. Bấm vào bài để đọc đầy đủ.</p>
    {J.tabs('news')}
  </div>
</section>
{N.list_section(g, page=True)}
<section class="on-dark bg-lacquer py-20 text-paper lg:py-24" aria-labelledby="cta-title">
  <div class="shell">
    <h2 id="cta-title" class="t-h2">Đang tìm việc giúp việc, bảo mẫu, chăm sóc người già?</h2>
    <div class="mt-8 flex flex-wrap gap-3">
      <a class="btn btn-brass" href="/tuyen-dung#viec-dang-tuyen">Xem việc đang tuyển</a>
      <a class="btn btn-ghost-light" href="#ung-tuyen" data-open="ungvien">Gửi hồ sơ (2 phút)</a>
    </div>
  </div>
</section>'''
    SITE = g['SITE']
    items = [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + '/' + p['slug'], 'name': p['title']} for i, p in enumerate(N.POSTS)]
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'CollectionPage', '@id': SITE + path + '#webpage', 'url': SITE + path, 'name': title, 'description': desc, 'inLanguage': 'vi',
         'isPartOf': {'@id': SITE + '/#website'}, 'mainEntity': {'@type': 'ItemList', 'itemListElement': items}},
        g['crumbs_ld'](crumbs, path)]}
    return 'tin-tuc.html', path, g['page'](title, desc, path, main, ld)

# ======================= CẨM NANG 2026 =======================
GUIDE_FAQ = [
 ('Thuê người giúp việc có bắt buộc ký hợp đồng không?', 'Có. Điều 162 Bộ luật Lao động 2019 quy định hợp đồng với người giúp việc gia đình phải bằng văn bản. Theo Nghị định 283/2026/NĐ-CP, không giao kết hợp đồng bằng văn bản bị cảnh cáo, tái phạm bị phạt 1–3 triệu đồng.'),
 ('Phải thông báo cho cơ quan nào khi thuê người giúp việc?', 'Gia đình thông báo cho UBND cấp xã (xã, phường, đặc khu) nơi người giúp việc làm việc khi bắt đầu và khi chấm dứt hợp đồng. Không thông báo bị phạt 1–3 triệu đồng theo Nghị định 283/2026/NĐ-CP, có hiệu lực từ 10/9/2026.'),
 ('Gia đình có phải đóng bảo hiểm xã hội cho người giúp việc không?', 'Gia đình trả cho người giúp việc khoản tiền tương ứng với mức đóng bảo hiểm xã hội bắt buộc và bảo hiểm y tế, cùng kỳ trả lương, để người giúp việc tự tham gia. Không trả khoản này bị phạt 10–15 triệu đồng và phải truy trả.'),
 ('Có được giữ căn cước của người giúp việc không?', 'Không. Giữ giấy tờ tùy thân của người giúp việc bị phạt 10–15 triệu đồng và buộc trả lại giấy tờ.'),
]

def guide_page(g):
    path = '/thue-giup-viec-2026'
    crumbs = [('Trang chủ', '/'), ('Cẩm nang', '/cam-nang'), ('Thuê người giúp việc 2026', None)]
    title = 'Thuê người giúp việc 2026: quy định mới và mẫu hợp đồng'
    desc = 'Từ 10/9/2026, chủ nhà bị phạt nếu không ký hợp đồng, không báo UBND xã, giữ giấy tờ người giúp việc (Điều 28 NĐ 283/2026). Checklist 7 việc, mẫu hợp đồng.'
    main = f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="shell relative pb-16 pt-32 lg:pb-20 lg:pt-40">
    {g['crumbs_html'](crumbs)}
    <span class="eyebrow">Cẩm nang · Cập nhật 13/10/2026</span>
    <h1 id="pg-title" class="t-display mt-4" style="max-width:24ch">Thuê người giúp việc năm 2026: 7 việc gia đình cần làm để đúng luật</h1>
    <p class="t-lead mt-6 max-w-[60ch] text-mist">Từ ngày 10/9/2026, Nghị định 283/2026/NĐ-CP xử phạt chủ nhà nếu không ký hợp đồng bằng văn bản, không thông báo UBND cấp xã, giữ giấy tờ tùy thân hoặc không trả khoản bảo hiểm cho người giúp việc. Bài viết tóm tắt những việc gia đình cần làm, kèm mẫu hợp đồng tham khảo.</p>
    <p class="byline">Biên soạn: <b>Đội ngũ Elite Helpers</b> · Đối chiếu với văn bản gốc Nghị định 283/2026/NĐ-CP · Cập nhật 13/10/2026</p>
  </div>
</section>
<article class="on-light bg-paper py-16 lg:py-24">
  <div class="shell">
    <div class="prose">
      <nav class="toc" aria-label="Mục lục"><b>Nội dung chính</b>
        <ol>
          <li><a href="#tom-tat">Tóm tắt nhanh</a></li>
          <li><a href="#muc-phat">Bảng mức phạt từ 10/9/2026</a></li>
          <li><a href="#checklist">7 việc cần làm khi thuê người giúp việc</a></li>
          <li><a href="#hop-dong">Hợp đồng cần có những nội dung gì</a></li>
          <li><a href="#mau-hop-dong">Tải mẫu hợp đồng</a></li>
          <li><a href="#hoi-dap-cn">Hỏi đáp</a></li>
        </ol>
      </nav>

      <h2 id="tom-tat">Tóm tắt nhanh</h2>
      <ul>
        <li>Hợp đồng với người giúp việc gia đình <strong>bắt buộc bằng văn bản</strong> (Điều 162 Bộ luật Lao động 2019).</li>
        <li>Gia đình <strong>thông báo UBND cấp xã</strong> nơi người giúp việc làm việc khi bắt đầu và khi chấm dứt hợp đồng.</li>
        <li>Gia đình <strong>trả khoản tiền bảo hiểm xã hội, bảo hiểm y tế</strong> cùng kỳ trả lương để người giúp việc tự tham gia.</li>
        <li><strong>Không giữ giấy tờ tùy thân</strong> của người giúp việc.</li>
        <li>Từ <strong>10/9/2026</strong>, các vi phạm trên bị xử phạt theo <a href="https://hethongphapluat.com/nghi-dinh-283-2026-nd-cp-quy-dinh-xu-phat-vi-pham-hanh-chinh-trong-linh-vuc-lao-dong-bao-hiem-xa-hoi-nguoi-lao-dong-viet-nam-di-lam-viec-o-nuoc-ngoai-theo-hop-dong/dieu-28" rel="noopener" target="_blank"><strong>Điều 28 Nghị định 283/2026/NĐ-CP</strong></a> (Vi phạm quy định về lao động là người giúp việc gia đình).</li>
      </ul>

      <h2 id="muc-phat">Bảng mức phạt với chủ nhà từ 10/9/2026</h2>
      <div class="tbl-wrap"><table>
        <thead><tr><th>Hành vi của người sử dụng lao động</th><th>Mức xử lý</th></tr></thead>
        <tbody>
          <tr><td>Không giao kết hợp đồng lao động bằng văn bản với người giúp việc</td><td>Cảnh cáo; tái phạm phạt 1–3 triệu đồng</td></tr>
          <tr><td>Không trả tiền tàu xe về nơi cư trú khi kết thúc hợp đồng (trừ khi người giúp việc tự chấm dứt trước hạn)</td><td>Cảnh cáo; tái phạm phạt 1–3 triệu đồng</td></tr>
          <tr><td>Không thông báo UBND cấp xã khi bắt đầu hoặc chấm dứt việc sử dụng người giúp việc</td><td>Phạt 1–3 triệu đồng</td></tr>
          <tr><td>Giữ giấy tờ tùy thân của người giúp việc</td><td>Phạt 10–15 triệu đồng, buộc trả lại giấy tờ</td></tr>
          <tr><td>Không trả khoản tiền tương ứng bảo hiểm xã hội, bảo hiểm y tế để người giúp việc tự tham gia</td><td>Phạt 10–15 triệu đồng, buộc truy trả</td></tr>
          <tr><td>Ngược đãi, quấy rối tình dục, cưỡng bức lao động, dùng vũ lực với người giúp việc (chưa đến mức truy cứu hình sự)</td><td>Phạt 50–75 triệu đồng</td></tr>
        </tbody>
      </table></div>
      <p class="note">Căn cứ: Điều 28 Nghị định 283/2026/NĐ-CP (ban hành 15/7/2026, hiệu lực 10/9/2026), gồm khoản 1 (cảnh cáo), khoản 2 (1–3 triệu đồng, gồm cả tái phạm sau cảnh cáo), khoản 3 (10–15 triệu đồng), khoản 4 (50–75 triệu đồng) và khoản 5 (biện pháp khắc phục hậu quả). Mức phạt áp dụng với cá nhân vi phạm. <a href="https://storage-vnportal.vnpt.vn/qnm-ubnd/7872/Nghị%20định/283_2026_ND-CP_15072026_1-signed.pdf" rel="noopener" target="_blank">Xem toàn văn nghị định (PDF có chữ ký số)</a>.</p>

      <h2 id="checklist">7 việc cần làm khi thuê người giúp việc</h2>
      <ol>
        <li><strong>Thống nhất công việc trước khi nhận người:</strong> phạm vi việc, giờ làm, ngày nghỉ, lương, chỗ ở, ăn uống.</li>
        <li><strong>Kiểm tra giấy tờ tùy thân bản gốc</strong> để đối chiếu, chụp lại nếu người giúp việc đồng ý, rồi trả ngay. Không giữ giấy tờ.</li>
        <li><strong>Cho làm thử</strong> vài ngày để hai bên cùng đánh giá.</li>
        <li><strong>Ký hợp đồng bằng văn bản</strong>, mỗi bên giữ một bản. Người giúp việc từ 15 đến dưới 18 tuổi cần có sự đồng ý bằng văn bản của người đại diện theo pháp luật.</li>
        <li><strong>Thông báo UBND cấp xã</strong> nơi người giúp việc làm việc. Nhớ thông báo lại khi chấm dứt hợp đồng.</li>
        <li><strong>Trả lương đúng hạn</strong> kèm khoản tiền tương ứng bảo hiểm xã hội bắt buộc, bảo hiểm y tế; lưu chứng từ trả lương.</li>
        <li><strong>Khi kết thúc hợp đồng:</strong> thanh toán đủ lương, trả tiền tàu xe về nơi cư trú theo quy định, thông báo UBND cấp xã.</li>
      </ol>

      <h2 id="hop-dong">Hợp đồng với người giúp việc cần có những nội dung gì</h2>
      <p>Theo Điều 162 Bộ luật Lao động 2019, ngoài nội dung chủ yếu của hợp đồng lao động, hợp đồng với người giúp việc gia đình cần có:</p>
      <ul>
        <li>Hình thức trả lương, kỳ hạn trả lương;</li>
        <li>Thời giờ làm việc hằng ngày;</li>
        <li>Chỗ ở (nếu người giúp việc ở lại).</li>
      </ul>
      <p>Thời hạn hợp đồng do hai bên thỏa thuận. Mỗi bên có quyền đơn phương chấm dứt hợp đồng bất kỳ khi nào nhưng phải báo trước 15 ngày. Gia đình nên ghi thêm: mô tả công việc, ngày nghỉ hằng tuần, nghỉ lễ Tết, thời gian làm thử, cách xử lý khi làm hỏng hoặc mất tài sản.</p>

      <h2 id="mau-hop-dong">Tải mẫu hợp đồng lao động giúp việc gia đình</h2>
      <p>Elite Helpers soạn sẵn mẫu hợp đồng tham khảo, định dạng Word để gia đình điền và chỉnh sửa:</p>
      <p><a class="btn btn-brass" style="text-decoration:none;color:var(--color-lacquer)" href="/mau-hop-dong-giup-viec-gia-dinh.docx" download data-track="download_contract">Tải mẫu hợp đồng (.docx)</a></p>
      <p class="note">Mẫu hợp đồng và nội dung bài viết mang tính tham khảo, không thay thế tư vấn pháp lý. Với trường hợp đặc thù (người giúp việc là người nước ngoài, dưới 18 tuổi, làm cho nhiều hộ), gia đình nên hỏi luật sư hoặc UBND cấp xã.</p>

      <h2>Elite Helpers hỗ trợ gia đình thế nào?</h2>
      <p>Khi gia đình nhận người qua Elite Helpers, ứng viên đã được xác minh giấy tờ và phỏng vấn trực tiếp. Elite Helpers hướng dẫn hai bên thống nhất nội dung hợp đồng và nhắc gia đình các thủ tục cần làm theo quy định mới. Xem các dịch vụ: <a href="/giup-viec-gia-dinh">giúp việc gia đình</a>, <a href="/bao-mau-cham-be">bảo mẫu</a>, <a href="/cham-soc-nguoi-gia">chăm sóc người già</a>, <a href="/quan-gia">quản gia</a>, <a href="/dau-bep-gia-dinh">đầu bếp gia đình</a>.</p>

      <h2>Nguồn tham khảo</h2>
      <ul>
        <li>Bộ luật Lao động 2019, Mục 2 Chương XI (Điều 161–165) về lao động là người giúp việc gia đình.</li>
        <li>Nghị định 145/2020/NĐ-CP hướng dẫn Bộ luật Lao động về điều kiện lao động và quan hệ lao động.</li>
        <li><a href="https://storage-vnportal.vnpt.vn/qnm-ubnd/7872/Nghị%20định/283_2026_ND-CP_15072026_1-signed.pdf" rel="noopener" target="_blank">Toàn văn Nghị định 283/2026/NĐ-CP</a> quy định xử phạt vi phạm hành chính trong lĩnh vực lao động, bảo hiểm xã hội, người lao động Việt Nam đi làm việc ở nước ngoài theo hợp đồng (ban hành 15/7/2026, hiệu lực 10/9/2026). Bản PDF có chữ ký số, đăng trên cổng thông tin UBND tỉnh.</li>
        <li><a href="https://hethongphapluat.com/nghi-dinh-283-2026-nd-cp-quy-dinh-xu-phat-vi-pham-hanh-chinh-trong-linh-vuc-lao-dong-bao-hiem-xa-hoi-nguoi-lao-dong-viet-nam-di-lam-viec-o-nuoc-ngoai-theo-hop-dong/dieu-28" rel="noopener" target="_blank">Điều 28 Nghị định 283/2026/NĐ-CP: Vi phạm quy định về lao động là người giúp việc gia đình</a></li>
        <li><a href="https://vnexpress.net/phat-tien-nguoi-thue-giup-viec-gia-dinh-ma-khong-bao-ubnd-xa-5105165.html" rel="noopener" target="_blank">VnExpress: Phạt tiền người thuê giúp việc gia đình mà không báo UBND xã</a></li>
        <li><a href="https://tuoitre.vn/thue-nguoi-giup-viec-nhung-khong-thong-bao-cho-ubnd-xa-co-the-bi-phat-toi-3-trieu-dong-10026072211565164.htm" rel="noopener" target="_blank">Tuổi Trẻ: Thuê người giúp việc nhưng không thông báo cho UBND xã có thể bị phạt tới 3 triệu đồng</a></li>
        <li><a href="https://dantri.com.vn/lao-dong-viec-lam/bi-phat-den-3-trieu-dong-neu-thue-nguoi-giup-viec-ma-khong-bao-ubnd-xa-20260722094957494.htm" rel="noopener" target="_blank">Dân trí: Bị phạt đến 3 triệu đồng nếu thuê người giúp việc mà không báo UBND xã</a></li>
      </ul>
    </div>
  </div>
</article>
<section class="on-light bg-linen py-20 lg:py-24" aria-labelledby="hoi-dap-cn">
  <div class="shell grid gap-12 lg:grid-cols-12 lg:gap-10">
    <div class="lg:col-span-4"><h2 id="hoi-dap-cn" class="t-h2 text-shutter">Hỏi đáp nhanh</h2></div>
    <div class="faq lg:col-span-8">
{g['faq_html'](GUIDE_FAQ)}
    </div>
  </div>
</section>
{g['cta_block'](None, h='Cần người giúp việc được tuyển chọn kỹ, đúng quy định?')}'''
    SITE = g['SITE']
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Article', '@id': SITE + path + '#article', 'headline': 'Thuê người giúp việc năm 2026: 7 việc gia đình cần làm để đúng luật',
         'description': desc, 'url': SITE + path, 'inLanguage': 'vi', 'datePublished': '2026-10-13', 'dateModified': '2026-10-13',
         'author': {'@id': SITE + '/#org'},
         'publisher': {'@id': SITE + '/#org'}, 'image': SITE + '/og-thue-giup-viec-2026.jpg',
         'citation': [{'@type': 'Legislation', 'name': 'Nghị định 283/2026/NĐ-CP', 'legislationDate': '2026-07-15', 'url': 'https://storage-vnportal.vnpt.vn/qnm-ubnd/7872/Nghị%20định/283_2026_ND-CP_15072026_1-signed.pdf'},
                      {'@type': 'Legislation', 'name': 'Bộ luật Lao động 2019'}],
         'mainEntityOfPage': SITE + path, 'about': ['Nghị định 283/2026/NĐ-CP', 'Bộ luật Lao động 2019', 'Lao động giúp việc gia đình']},
        g['crumbs_ld'](crumbs, path), g['faq_ld'](GUIDE_FAQ, path)]}
    return 'thue-giup-viec-2026.html', path, g['page'](title, desc, path, main, ld, og_type='article', og=SITE + '/og-thue-giup-viec-2026.jpg', og_alt='Thuê người giúp việc 2026: 7 việc cần làm để đúng luật, Nghị định 283/2026/NĐ-CP')

# ======================= ENGLISH =======================
EN_FAQ = [
 ('What services does Elite Helpers offer?', 'Elite Helpers places housekeepers (live-in or part-time), nannies, elderly caregivers, house managers, family cooks and short-term helpers with families in Hanoi. Each role is matched to the family\'s home, schedule and specific needs.'),
 ('Do your helpers speak English?', 'Yes, on request. We introduce housekeepers, nannies and house managers with basic to good English who are used to international households and cuisine. English level is checked at interview.'),
 ('How are candidates screened?', 'Every candidate has their ID, residence and work history verified and is interviewed in person before being introduced. The family then meets the candidate and arranges a trial period before deciding.'),
 ('How much does a helper cost in Hanoi?', 'Reference monthly salaries with Elite Helpers (paid to the helper): housekeeper 10–25 million VND, nanny 10–25 million VND, elderly caregiver 10–25 million VND, family cook 15–35 million VND, house manager 18–40 million VND. Short-term help is quoted separately based on tasks and duration. The exact figure depends on experience, live-in or part-time, English level and workload.'),
 ('Do I need a contract with my helper?', 'Yes. Article 162 of Vietnam\'s 2019 Labour Code requires a written contract with a domestic worker. Employers must also notify the commune-level People\'s Committee when employment starts and ends. Since 10 September 2026, Decree 283/2026/ND-CP fines employers 1–3 million VND for not notifying, and 10–15 million VND for keeping the worker\'s ID papers or not paying the social and health insurance amounts.'),
 ('Which areas do you cover?', 'Central Hanoi, including Tay Ho, Ba Dinh, Hoan Kiem, Dong Da, Cau Giay, Nam Tu Liem and Long Bien, and nearby areas such as Bac Ninh and Hung Yen.'),
 ('Do you work with embassies?', 'Yes. We provide discreet, well-mannered staff for embassies, ambassadors\' residences and international organisations, including house managers, cooks and housekeepers.'),
 ('How fast will you reply?', 'We reply to requests within the same working day. We are available from 8:00 to 21:00 every day via Zalo, phone or email.'),
]
EN_SVC = [
 ('Housekeeper (live-in or part-time)', 'Cleaning, laundry and ironing, grocery shopping and daily family meals for apartments, townhouses and villas.', 'giup-viec-gia-dinh'),
 ('Nanny', 'Care for newborns and young children: feeding, bathing, naps, hygiene, school runs, play and learning. English-speaking nannies on request.', 'bao-mau-cham-be'),
 ('Elderly caregiver', 'Daily support for seniors: meals, personal hygiene, medication reminders, doctor visits and companionship.', 'cham-soc-nguoi-gia'),
 ('House manager', 'Runs the household: supervises staff, manages supplies and expenses, receives guests and prepares events.', 'quan-gia'),
 ('Family cook', 'Vietnamese, Asian and Western dishes, children\'s meals, vegetarian or special diets, weekly menus and home parties.', 'dau-bep-gia-dinh'),
 ('Short-term helper', 'Help for Tet holidays, moving house, hosting guests or covering while your regular helper is away.', 'ho-tro-ngan-han'),
]

EN_HEADER = '''<a href="#content" class="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[90] focus:rounded-full focus:bg-brass focus:px-5 focus:py-3 focus:text-lacquer">Skip to content</a>
<svg width="0" height="0" class="absolute" aria-hidden="true" focusable="false">
  <symbol id="mark" viewBox="0 0 40 50"><image href="assets/img/arch-mark.svg" x="0" y="0" width="40" height="50" preserveAspectRatio="xMidYMid meet"/></symbol>
  <symbol id="i-chat" viewBox="0 0 24 24"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h13A1.5 1.5 0 0 1 20 5.5v9a1.5 1.5 0 0 1-1.5 1.5H10l-4.5 4v-4h0A1.5 1.5 0 0 1 4 14.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></symbol>
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M5.5 3.5h3l1.5 4-2 1.3a11 11 0 0 0 6.2 6.2l1.3-2 4 1.5v3a2 2 0 0 1-2.1 2A16.5 16.5 0 0 1 3.5 5.6a2 2 0 0 1 2-2.1Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></symbol>
</svg>
<div class="progress" id="progress" aria-hidden="true"></div>
<header class="site-head fixed inset-x-0 top-0 z-50 text-paper" id="siteHead">
  <div class="shell flex h-[72px] items-center justify-between gap-6">
    <a href="/en" class="flex items-center gap-3" aria-label="Elite Helpers home">
      <svg class="h-10 w-8 shrink-0 text-paper" aria-hidden="true"><use href="#mark"/></svg>
      <span class="brand-stack"><span class="wordmark text-[1rem] sm:text-[1.15rem]">ELITE HELPERS</span><span class="visits-head" data-visits hidden aria-hidden="true"></span></span>
    </a>
    <nav aria-label="Main" class="hidden lg:block">
      <ul class="flex items-center gap-8 text-[.94rem]">
        <li><a class="nav-link" href="#services">Services</a></li>
        <li><a class="nav-link" href="#who">Who we serve</a></li>
        <li><a class="nav-link" href="#process">Process</a></li>
        <li><a class="nav-link" href="#faq">FAQ</a></li>
        <li><a class="nav-link" href="#contact">Contact</a></li>
      </ul>
    </nav>
    <div class="flex items-center gap-2">
      <a class="lang-link" href="/" hreflang="vi" lang="vi" title="Tiếng Việt">VI<span class="sr-only"> – Tiếng Việt</span></a>
      <a class="btn btn-brass btn-sm hidden sm:inline-flex" href="#contact">Get in touch</a>
    </div>
  </div>
</header>'''

def en_footer(g):
    return '''<footer class="on-dark bg-lacquer pb-28 pt-16 text-mist md:pb-12" aria-label="Footer">
  <div class="shell">
    <div class="rule-top flex flex-col gap-2 pt-6 text-[.85rem] sm:flex-row sm:justify-between">
      <p>&copy; <span data-year>2026</span> Elite Helpers (Giúp việc Elite) · Hanoi, Vietnam<br>lienhe@giupviecelite.vn · +84 948 919 598</p>
      <p><button type="button" class="link-quiet" data-cookie-settings>Cookie settings</button> · <a class="link-quiet" href="/" hreflang="vi" lang="vi">Tiếng Việt</a></p>
    </div>
  </div>
</footer>
<div class="mbar fixed inset-x-0 bottom-0 z-40 grid grid-cols-2 bg-brass md:hidden">
  <a class="flex items-center justify-center gap-2 bg-lacquer py-4 font-medium text-brass" href="https://zalo.me/0948919598" target="_blank" rel="noopener" data-track="zalo"><svg class="h-5 w-5" aria-hidden="true"><use href="#i-chat"/></svg>Zalo</a>
  <a class="flex items-center justify-center gap-2 py-4 font-medium text-lacquer" href="tel:+84948919598" data-track="call"><svg class="h-5 w-5" aria-hidden="true"><use href="#i-phone"/></svg>Call us</a>
</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/js/app.js?v=%s" defer></script>
''' % g['VER']

def en_page(g):
    path = '/en'
    title = 'Housekeepers, Nannies & Elderly Care in Hanoi | Elite Helpers'
    desc = 'Vetted housekeepers, nannies, elderly caregivers, house managers and family cooks for expats and embassies in Hanoi. English-speaking staff on request.'
    svc = ''.join(f'<div class="card"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b, _ in EN_SVC)
    faq = g['faq_html'](EN_FAQ)
    main = f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="pointer-events-none absolute inset-0" aria-hidden="true" style="background:radial-gradient(60% 70% at 78% 45%, rgba(53,84,73,.75), transparent 70%)"></div>
  <div class="shell relative grid items-center gap-14 pb-20 pt-32 lg:grid-cols-12 lg:gap-8 lg:pb-24 lg:pt-40">
    <div class="lg:col-span-7">
      <span class="eyebrow">Premium household staffing in Hanoi</span>
      <h1 id="pg-title" class="t-display mt-4" style="max-width:20ch">Housekeepers, nannies and elderly caregivers in Hanoi</h1>
      <p class="t-lead mt-6 max-w-[52ch] text-mist">Elite Helpers matches expat families, Vietnamese families and embassies in Hanoi with carefully vetted household staff. English-speaking helpers available on request.</p>
      <div class="mt-9 flex flex-wrap gap-3">
        <a class="btn btn-brass" href="https://zalo.me/0948919598" target="_blank" rel="noopener" data-track="zalo">Message us on Zalo</a>
        <a class="btn btn-ghost-light" href="mailto:lienhe@giupviecelite.vn?subject=Helper%20request%20-%20Elite%20Helpers">Email us</a>
      </div>
    </div>
    <div class="lg:col-span-5">
      <div class="arch-frame mx-auto w-[min(76vw,430px)] lg:ml-auto lg:mr-2">
        <div class="arch aspect-[4/5] bg-shutter"><img src="assets/img/phong-khach-760.webp" width="760" height="950" alt="Housekeeper arranging cushions in a Hanoi villa living room" fetchpriority="high" decoding="async"></div>
      </div>
    </div>
  </div>
</section>
<section id="services" class="on-light bg-paper py-20 lg:py-28" aria-labelledby="sv-title">
  <div class="shell">
    <h2 id="sv-title" class="t-h2 text-shutter">Services</h2>
    <p class="mt-4 max-w-[60ch] text-ink-soft">New to hiring in Vietnam? Read our <a class="underline" href="/hiring-helper-hanoi-expat-guide">2026 guide for expat families</a>.</p>
    <p class="mt-4 max-w-[60ch] text-ink-soft">Whether you need a live-in housekeeper, a nanny for a newborn or someone to care for an elderly parent, we match each candidate to your household size, routine and expectations.</p>
    <div class="cards c3">{svc}</div>
  </div>
</section>
<section id="who" class="on-light bg-linen py-20 lg:py-28" aria-labelledby="wh-title">
  <div class="shell grid gap-14 lg:grid-cols-12 lg:gap-12">
    <div class="lg:col-span-6">
      <h2 id="wh-title" class="t-h2 text-shutter">Who we serve</h2>
      <ul class="checks" role="list">
        <li>Expatriate families relocating to or living in Hanoi</li>
        <li>Embassies, ambassadors' residences and diplomatic households</li>
        <li>International organisations and representative offices</li>
        <li>Vietnamese families, from apartments to villas</li>
      </ul>
    </div>
    <div class="lg:col-span-6">
      <h2 class="t-h2 text-shutter">Our standards</h2>
      <ul class="checks" role="list">
        <li>ID, residence and work history verified for every candidate</li>
        <li>In-person interview on skills, manners and attitude</li>
        <li>Meet the candidate and arrange a trial before deciding</li>
        <li>Discreet, respectful staff; your information stays private</li>
        <li>Ongoing follow-up with both family and helper</li>
      </ul>
    </div>
  </div>
</section>
<section id="process" class="on-light bg-paper py-20 lg:py-24" aria-labelledby="pr-title">
  <div class="shell">
    <h2 id="pr-title" class="t-h2 text-shutter">How it works</h2>
    <ol class="steps-sm" role="list">
      <li><b>Tell us your needs</b><span>Chat on Zalo, call or email: duties, hours, budget and special requirements.</span></li>
      <li><b>Meet candidates</b><span>We send profiles of vetted, interviewed candidates.</span></li>
      <li><b>Trial period</b><span>Meet in person and arrange a trial before deciding.</span></li>
      <li><b>Start with support</b><span>We help with the written contract and follow up throughout.</span></li>
    </ol>
  </div>
</section>
<section id="faq" class="on-light bg-linen py-20 lg:py-24" aria-labelledby="fq-title">
  <div class="shell grid gap-12 lg:grid-cols-12 lg:gap-10">
    <div class="lg:col-span-4"><h2 id="fq-title" class="t-h2 text-shutter">Frequently asked questions</h2></div>
    <div class="faq lg:col-span-8">
{faq}
    </div>
  </div>
</section>
<section id="contact" class="on-dark bg-lacquer py-20 text-paper lg:py-24" aria-labelledby="ct-title">
  <div class="shell">
    <h2 id="ct-title" class="t-h2">Find the right helper for your home</h2>
    <p class="mt-4 max-w-[56ch] text-mist">Free consultation. Send the form below or message us directly. We reply within the same working day, 8:00–21:00 every day.</p>
    <div class="mt-8 flex flex-wrap gap-3">
      <a class="btn btn-brass" href="https://zalo.me/0948919598" target="_blank" rel="noopener" data-track="zalo">Zalo +84 948 919 598</a>
      <a class="btn btn-ghost-light" href="tel:+84948919598" data-track="call">Call +84 948 919 598</a>
      <a class="btn btn-ghost-light" href="mailto:lienhe@giupviecelite.vn?subject=Helper%20request%20-%20Elite%20Helpers">lienhe@giupviecelite.vn</a>
    </div>
    <form class="en-form" data-simple-form novalidate aria-labelledby="ct-title">
      <div class="row">
        <div><label for="enName">Your name *</label><input id="enName" name="name" required autocomplete="name" maxlength="60"></div>
        <div><label for="enPhone">Phone / WhatsApp / Zalo *</label><input id="enPhone" name="phone" type="tel" required autocomplete="tel" inputmode="tel" maxlength="20" placeholder="+84 ..."></div>
      </div>
      <div class="row">
        <div><label for="enEmail">Email</label><input id="enEmail" name="email" type="email" autocomplete="email" maxlength="80"></div>
        <div><label for="enService">Service</label><select id="enService" name="service"><option>Housekeeper</option><option>Nanny</option><option>Elderly caregiver</option><option>House manager</option><option>Family cook</option><option>Short-term helper</option><option>Not sure yet</option></select></div>
      </div>
      <div class="row">
        <div><label for="enArea">Area in Hanoi</label><input id="enArea" name="area" maxlength="80" placeholder="e.g. Tay Ho, Ba Dinh"></div>
        <div><label for="enStart">Start date</label><input id="enStart" name="start" maxlength="40" placeholder="e.g. early November"></div>
      </div>
      <div><label for="enNote">Tell us about your needs</label><textarea id="enNote" name="note" rows="4" maxlength="1500" placeholder="Household size, children's ages, hours, live-in or part-time, English level needed..."></textarea></div>
      <input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <label class="chk"><input type="checkbox" name="agree" required> <span>I agree that Elite Helpers may use these details to contact me about my request, as described in our <a class="underline" href="/#chinh-sach-bao-mat" lang="vi">privacy policy</a> (Vietnamese).</span></label>
      <label class="chk"><input type="checkbox" name="optin" value="Yes"> <span>Send me helpful updates and offers from Elite Helpers by Zalo/email (optional, unsubscribe anytime).</span></label>
      <div><button type="submit" class="btn btn-brass">Send request</button></div>
      <p class="msg" data-msg role="status" tabindex="-1" hidden></p>
      <p class="text-[.8rem] text-mist">This form is protected by Google reCAPTCHA.</p>
    </form>
  </div>
</section>'''
    footer = en_footer(g)
    SITE = g['SITE']
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': SITE + path + '#webpage', 'url': SITE + path, 'name': title, 'description': desc, 'inLanguage': 'en',
         'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#org'}},
        {'@type': 'ItemList', 'name': 'Household staffing services in Hanoi', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'item': {'@type': 'Service', 'name': a, 'description': b, 'provider': {'@id': SITE + '/#org'}, 'areaServed': {'@type': 'City', 'name': 'Hanoi'}}}
            for i, (a, b, _) in enumerate(EN_SVC)]},
        g['faq_ld'](EN_FAQ, path)]}
    alt = [('vi', '/'), ('en', '/en'), ('x-default', '/')]
    html_ = g['page'](title, desc, path, main, ld, lang='en', alt=alt, top=EN_HEADER, bottom=footer)
    return 'en.html', path, html_.replace('<main id="noi-dung">', '<main id="content">')

# ======================= 404 =======================
def notfound_page(g):
    main = '''<section id="top" class="on-dark bg-lacquer text-paper" style="min-height:70vh" aria-labelledby="pg-title">
  <div class="shell pb-20 pt-32 lg:pt-40">
    <span class="eyebrow">Lỗi 404</span>
    <h1 id="pg-title" class="t-display mt-4" style="max-width:20ch">Không tìm thấy trang này</h1>
    <p class="t-lead mt-6 max-w-[52ch] text-mist">Trang có thể đã được đổi địa chỉ. Quý khách có thể quay về trang chủ hoặc xem các dịch vụ bên dưới.</p>
    <div class="mt-9 flex flex-wrap gap-3">
      <a class="btn btn-brass" href="/">Về trang chủ</a>
      <a class="btn btn-ghost-light" href="/#tim-nguoi">Gửi yêu cầu tư vấn</a>
    </div>
    <ul class="checks mt-10" role="list">
      <li><a class="link-quiet underline" href="/giup-viec-gia-dinh">Giúp việc gia đình</a></li>
      <li><a class="link-quiet underline" href="/bao-mau-cham-be">Bảo mẫu, chăm bé</a></li>
      <li><a class="link-quiet underline" href="/cham-soc-nguoi-gia">Chăm sóc người già</a></li>
      <li><a class="link-quiet underline" href="/tuyen-dung">Tuyển dụng</a></li>
      <li><a class="link-quiet underline" href="/en" lang="en">English</a></li>
    </ul>
  </div>
</section>'''
    h = g['page']('Không tìm thấy trang | Elite Helpers', 'Trang không tồn tại. Quay về trang chủ Elite Helpers (Giúp việc Elite).', '/404', main)
    h = h.replace('<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">', '<meta name="robots" content="noindex">')
    h = re.sub(r'<link rel="canonical"[^>]*>\n|<meta property="og:url"[^>]*>\n', '', h)
    # 404 may be served from any path: make asset URLs absolute
    h = h.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/')
    return '404.html', '/404', h

# ======================= TRANG MỤC LỤC: DỊCH VỤ, CẨM NANG =======================
def hub_hero(g, crumbs, eyebrow, h1, lead):
    return f'''<section id="top" class="on-dark relative overflow-hidden bg-lacquer text-paper" aria-labelledby="pg-title">
  <div class="shell relative pb-16 pt-32 lg:pb-20 lg:pt-40">
    {g['crumbs_html'](crumbs)}
    <span class="eyebrow">{eyebrow}</span>
    <h1 id="pg-title" class="t-display mt-4" style="max-width:22ch">{h1}</h1>
    <p class="t-lead mt-6 max-w-[58ch] text-mist">{lead}</p>
  </div>
</section>'''

def services_hub(g):
    from content import SERVICES
    SITE = g['SITE']; path = '/dich-vu'
    crumbs = [('Trang chủ', '/'), ('Dịch vụ', None)]
    title = 'Dịch vụ giúp việc, bảo mẫu, chăm sóc người già Hà Nội'
    desc = 'Sáu dịch vụ của Elite Helpers tại Hà Nội: giúp việc gia đình, bảo mẫu, chăm sóc người già, quản gia, đầu bếp, hỗ trợ ngắn hạn, kèm mức lương tham khảo.'
    cards = ''
    for s in SERVICES:
        sal = s.get('salary') or 'báo giá riêng theo công việc'
        cards += f'''<a class="card" href="/{s['slug']}"><h2>{E(s['name'])}</h2><p>{E(s['desc'])}</p><p><b>Lương tham khảo:</b> {E(sal)}</p><span class="more">Xem chi tiết →</span></a>'''
    main = hub_hero(g, crumbs, 'Dịch vụ · Elite Helpers Hà Nội', 'Dịch vụ người hỗ trợ gia đình cao cấp tại Hà Nội',
                    'Mỗi dịch vụ có tiêu chí tuyển chọn, quy trình xác minh và mức lương tham khảo riêng. Gia đình gặp mặt và cho làm thử trước khi quyết định.') + f'''
<section class="on-light bg-paper py-16 lg:py-24" aria-label="Danh sách dịch vụ">
  <div class="shell"><div class="cards c3 hub">{cards}</div>
  <p class="mt-8 text-ink-soft">Mức lương là khoản người hỗ trợ nhận theo tháng; mức cụ thể tùy kinh nghiệm, hình thức ở lại hay theo giờ và khối lượng công việc. Xem thêm <a class="underline" href="/#hoi-dap-11">bảng lương các vị trí</a>.</p></div>
</section>
{g['cta_block'](None)}'''
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'CollectionPage', '@id': SITE + path + '#webpage', 'url': SITE + path, 'name': title, 'description': desc, 'inLanguage': 'vi',
         'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#org'}, 'breadcrumb': {'@id': SITE + path + '#breadcrumb'},
         'mainEntity': {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + '/' + s['slug'], 'name': s['name']} for i, s in enumerate(SERVICES)]}},
        g['crumbs_ld'](crumbs, path)]}
    return 'dich-vu.html', path, g['page'](title, desc, path, main, ld)

def guides_hub(g):
    SITE = g['SITE']; path = '/cam-nang'
    import articles as A
    art_cards = ''.join(f'''<a class="card" href="/{a['slug']}"{' lang="en" hreflang="en"' if a['lang']=='en' else ''}><h2>{E(a['h1'])}</h2><p>{E(a['card'] or a['desc'])}</p><p><b>{'Cập nhật ' + A.DATE_VI if a['lang']=='vi' else 'English · Updated Oct 2026'}</b></p><span class="more">{'Đọc bài →' if a['lang']=='vi' else 'Read →'}</span></a>''' for a in A.ARTICLES)
    crumbs = [('Trang chủ', '/'), ('Cẩm nang', None)]
    title = 'Cẩm nang thuê người giúp việc, bảo mẫu tại Hà Nội | Elite Helpers'
    desc = 'Cẩm nang thuê người giúp việc, bảo mẫu, chăm sóc người già tại Hà Nội: bảng lương 2026, kinh nghiệm chọn người, quy định pháp luật mới, mẫu hợp đồng.'
    main = hub_hero(g, crumbs, 'Cẩm nang · Elite Helpers', 'Cẩm nang thuê người giúp việc tại Hà Nội',
                    'Thông tin thực tế, cập nhật theo quy định mới, giúp gia đình thuê người hỗ trợ đúng luật và yên tâm.') + f'''
<section class="on-light bg-paper py-16 lg:py-24" aria-label="Danh sách bài viết">
  <div class="shell"><div class="cards c3 hub">
    <a class="card" href="/thue-giup-viec-2026"><h2>Thuê người giúp việc năm 2026: 7 việc cần làm để đúng luật</h2><p>Bảng mức phạt theo Điều 28 Nghị định 283/2026/NĐ-CP, checklist 7 việc gia đình cần làm, nội dung bắt buộc của hợp đồng.</p><p><b>Cập nhật 13/10/2026</b></p><span class="more">Đọc bài →</span></a>
    {art_cards}
    <a class="card" href="/mau-hop-dong-giup-viec-gia-dinh.docx" download data-track="download_contract"><h2>Mẫu hợp đồng lao động giúp việc gia đình</h2><p>Mẫu tham khảo định dạng Word, căn cứ Bộ luật Lao động 2019 và Nghị định 145/2020/NĐ-CP, để gia đình điền và chỉnh sửa.</p><span class="more">Tải mẫu (.docx) →</span></a>
    <a class="card" href="/#hoi-dap"><h2>Hỏi đáp thường gặp</h2><p>Chi phí, quy trình, thời gian tìm người, làm thử, đổi người và các câu hỏi khác về dịch vụ của Elite Helpers.</p><span class="more">Xem hỏi đáp →</span></a>
  </div></div>
</section>
{g['cta_block'](None)}'''
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'CollectionPage', '@id': SITE + path + '#webpage', 'url': SITE + path, 'name': title, 'description': desc, 'inLanguage': 'vi',
         'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#org'}, 'breadcrumb': {'@id': SITE + path + '#breadcrumb'},
         'hasPart': [{'@type': 'Article', '@id': SITE + '/thue-giup-viec-2026#article', 'url': SITE + '/thue-giup-viec-2026', 'headline': 'Thuê người giúp việc năm 2026: 7 việc gia đình cần làm để đúng luật'}] +
                    [{'@type': 'Article', '@id': SITE + '/' + a['slug'] + '#article', 'url': SITE + '/' + a['slug'], 'headline': a['h1'], 'inLanguage': a['lang']} for a in A.ARTICLES]},
        g['crumbs_ld'](crumbs, path)]}
    return 'cam-nang.html', path, g['page'](title, desc, path, main, ld)

def admin_page(g):
    here = os.path.dirname(os.path.abspath(__file__))
    return 'quan-tri.html', '/quan-tri', open(os.path.join(here, 'admin_page.html'), encoding='utf-8').read()

def extra_pages(g):
    import articles as A
    return [services_hub(g), guides_hub(g), recruit_page(g), news_page(g), guide_page(g), en_page(g), notfound_page(g), admin_page(g)] + A.all_articles(g) + __import__('news').all_posts(g) + __import__('jobs').all_jobs(g)

# ======================= META FILES + FLATTEN =======================
def write_meta_files(g, pages, home_faqs):
    from content import SERVICES
    SITE, GEN, DIST, TODAY = g['SITE'], g['GEN'], g['DIST'], g['TODAY']
    # ---- llms.txt (generated from visible content) ----
    L = ['# Elite Helpers (Giúp việc Elite)', '',
         '> Elite Helpers (Giúp việc Elite) là dịch vụ kết nối người hỗ trợ gia đình cao cấp tại Hà Nội: giúp việc gia đình, bảo mẫu, chăm sóc người già, quản gia, đầu bếp gia đình và hỗ trợ ngắn hạn. Ứng viên được xác minh lý lịch, phỏng vấn trực tiếp và làm thử trước khi gia đình quyết định.', '',
         'Website: https://giupviecelite.vn · Hotline/Zalo: 0948 919 598 (https://zalo.me/0948919598) · Email: lienhe@giupviecelite.vn · Giờ làm việc: 8:00–21:00 tất cả các ngày · Khu vực: Hà Nội và lân cận · Fanpage: https://www.facebook.com/EliteHelpersVN', '',
         '## Dịch vụ', '']
    for s in SERVICES:
        L.append(f"- [{s['name']}]({SITE}/{s['slug']}): {s['lead']}")
    L += ['', '## Trang khác', '',
          f'- [Tất cả dịch vụ và mức lương tham khảo]({SITE}/dich-vu)',
          f'- [Cẩm nang thuê người giúp việc]({SITE}/cam-nang)',
          *[f"- [{a['h1']}]({SITE}/{a['slug']}): {__import__('articles').plain(a['answer'])}" for a in __import__('articles').ARTICLES],
          f'- [Tuyển dụng người giúp việc, bảo mẫu, chăm sóc người già]({SITE}/tuyen-dung): tin tuyển dụng đang mở, ứng tuyển trực tiếp từng tin, không thu phí.',
          *[f"- [{j['title']}]({SITE}/{j['slug']}): {j['salary']}, {j['mode'].lower()}, {j['area']}." for j in __import__('jobs').JOBS if __import__('jobs').is_open(j)],
          f'- [Tin tức cho người lao động]({SITE}/tin-tuc): bản tin hằng tuần về quy định, quyền lợi và kinh nghiệm tìm việc.',
          f'- [Cẩm nang thuê người giúp việc năm 2026]({SITE}/thue-giup-viec-2026): quy định mới theo Nghị định 283/2026/NĐ-CP, checklist, mẫu hợp đồng.',
          f'- [English: Housekeepers, nannies & elderly caregivers in Hanoi]({SITE}/en)', '',
          '## Câu hỏi thường gặp', '']
    for q, a in home_faqs:
        L += [f'### {q}', a, '']
    L += ['## Liên hệ', '', f'- [Gửi yêu cầu tìm người hỗ trợ]({SITE}/#tim-nguoi)', f'- [Gửi hồ sơ ứng tuyển]({SITE}/#ung-tuyen)', f'- [Chính sách bảo vệ dữ liệu cá nhân]({SITE}/#chinh-sach-bao-mat)', '']
    open(os.path.join(GEN, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(L))
    # ---- sitemap.xml ----
    urls = []
    for fn, path in pages.items():
        loc = SITE + path if path != '/' else SITE + '/'
        extra = ''
        if path in ('/', '/en'):
            extra = f'\n    <xhtml:link rel="alternate" hreflang="vi" href="{SITE}/"/>\n    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/en"/>\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>'
        prio = '1.0' if path == '/' else ('0.9' if path.strip('/') in [s['slug'] for s in SERVICES] else '0.8')
        urls.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>{prio}</priority>{extra}\n  </url>')
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(urls) + '\n</urlset>\n'
    open(os.path.join(GEN, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
    # ---- robots.txt ----
    rb = open(os.path.join(g['SRC'], 'robots.txt'), encoding='utf-8').read()
    rb = re.sub(r'^#.*\n', '# Elite Helpers (Giúp việc Elite) - cho phép mọi công cụ tìm kiếm và trợ lý AI đọc nội dung công khai\n', rb, count=1)
    open(os.path.join(GEN, 'robots.txt'), 'w', encoding='utf-8').write(rb)
    # ---- manifest ----
    mf = json.load(open(os.path.join(g['SRC'], 'site.webmanifest'), encoding='utf-8'))
    mf['name'] = 'Elite Helpers (Giúp việc Elite) - Người hỗ trợ gia đình cao cấp tại Hà Nội'; mf['short_name'] = 'Elite Helpers'
    mf['start_url'] = '/'; mf['scope'] = '/'
    for ic in mf['icons']: ic['src'] = '/' + ic['src'].replace('assets/img/', '')
    json.dump(mf, open(os.path.join(GEN, 'site.webmanifest'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    # ---- IndexNow key ----
    key = hashlib.sha1(b'giupviecelite.vn-indexnow').hexdigest()[:32]
    open(os.path.join(GEN, key + '.txt'), 'w').write(key)
    g['INDEXNOW_KEY'] = key
    # ---- flatten into dist/: trang con thành thư mục slug/index.html (chạy cả /slug và /slug/) ----
    slugs = sorted({p.strip('/') for p in pages.values() if p != '/'}, key=len, reverse=True)
    def slashify(t):
        for sl in slugs:
            t = re.sub(r'(giupviecelite\.vn|href=")/' + re.escape(sl) + r'(?=["#?)\s<])', r'\1/' + sl + '/', t)
        return t
    def absolutize(t):
        t = re.sub(r'(?<=["\s,(])assets/', '/assets/', t)
        t = t.replace('href="apple-touch-icon.png"', 'href="/apple-touch-icon.png"').replace('href="site.webmanifest"', 'href="/site.webmanifest"')
        return t
    page_files = {fn for fn in pages if fn != 'index.html'} | {'quan-tri.html'}
    shutil.rmtree(DIST, ignore_errors=True); os.makedirs(DIST)
    for dp, _, fns in os.walk(GEN):
        for fn in fns:
            src = os.path.join(dp, fn)
            if fn in ('CNAME',): continue
            if dp == GEN and fn in page_files:
                os.makedirs(os.path.join(DIST, fn[:-5]), exist_ok=True)
                dst = os.path.join(DIST, fn[:-5], 'index.html')
            else:
                dst = os.path.join(DIST, fn)
            assert not os.path.exists(dst), 'duplicate ' + fn
            if fn.endswith(('.html', '.css', '.webmanifest', '.js', '.txt', '.xml')) and not fn.startswith(g['INDEXNOW_KEY']):
                t = open(src, encoding='utf-8').read()
                if fn.endswith('.html'): t = absolutize(t)
                t = t.replace('/assets/img/', '/').replace('/assets/fonts/', '/').replace('/assets/css/', '/').replace('/assets/js/', '/')
                t = t.replace('assets/img/', '').replace('assets/fonts/', '').replace('assets/css/', '').replace('assets/js/', '')
                t = t.replace('url(../fonts/', 'url(')
                if fn.endswith(('.html', '.txt', '.xml')): t = slashify(t)
                open(dst, 'w', encoding='utf-8').write(t)
            else:
                shutil.copy(src, dst)
