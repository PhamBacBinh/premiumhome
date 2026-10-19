---
title: Premium Home - Prototype website mới
author: PhuongVM
last_saved_by: PhuongVM
tags: [premium-home, website, prototype, tailwind-css, spa, seo, geo]
---

# Premium Home - Prototype website mới

Bản prototype làm lại website Premium Home (người hỗ trợ gia đình cao cấp tại Hà Nội) trên nền HTML, JavaScript thuần và Tailwind CSS v4. Toàn bộ nội dung của bản hiện tại được giữ nguyên, bổ sung phần Hỏi đáp và dữ liệu cấu trúc phục vụ SEO, GEO/AIO.

## Cấu trúc thư mục

```
site/                     Thư mục deploy (GitHub Pages, Netlify, Vercel, hosting tĩnh bất kỳ)
  index.html              Trang duy nhất (SPA), toàn bộ nội dung nằm sẵn trong HTML
  assets/css/app.css      CSS đã biên dịch từ Tailwind (minify)
  assets/js/app.js        Điều hướng SPA, hiệu ứng cuộn, form nhiều bước
  assets/fonts/           Font tự host: Cormorant Garamond, Be Vietnam Pro (subset Việt + Latin)
  assets/img/             Ảnh AVIF + WebP nhiều kích thước, logo, icon, ảnh chia sẻ mạng xã hội
  robots.txt, sitemap.xml, llms.txt, site.webmanifest, favicon.svg
src/app.css               Nguồn Tailwind (design tokens, component)
package.json              Lệnh build CSS
```

## Chạy thử

- Cách nhanh: mở `site/index.html` bằng trình duyệt.
- Có máy chủ cục bộ (khuyến nghị, giống môi trường thật): `npm run serve` rồi mở http://localhost:5173

## Chỉnh giao diện

1. `npm install`
2. `npm run watch:css` trong lúc sửa `site/index.html` hoặc `src/app.css`
3. `npm run build:css` trước khi deploy

Tailwind quét class trong `site/index.html` và `site/assets/js/app.js`. Màu, font, easing khai báo trong khối `@theme` của `src/app.css`.

## Điều hướng kiểu SPA

| Địa chỉ | Hành vi |
|---|---|
| `#tim-nguoi` | Mở form yêu cầu tìm người hỗ trợ |
| `#ung-tuyen` | Mở form ứng tuyển |
| `#chinh-sach-bao-mat` | Mở chính sách bảo vệ dữ liệu cá nhân |
| `#dich-vu`, `#doi-tuong`, `#cam-ket`, `#quy-trinh`, `#hoi-dap`, `#dang-ky` | Cuộn tới section |

Nút Back của trình duyệt đóng form, link chia sẻ mở đúng form. Bấm "Yêu cầu tư vấn" ở từng dịch vụ sẽ mở form với dịch vụ đó được chọn sẵn.

## Kết nối form với backend

Form đang ở chế độ prototype: không gửi dữ liệu đi đâu, chỉ ghi ra console trình duyệt. Khi có API, điền URL vào `CONFIG.FORM_ENDPOINT` trong `site/assets/js/app.js`. Script gửi `POST` JSON và coi mọi mã HTTP 2xx là thành công; nếu lỗi, form chuyển sang phương án dự phòng (sao chép nội dung và gửi qua Zalo) như bản cũ.

Trường dữ liệu form khách hàng (`formType = khach`): `client`, `service`, `mode`, `area`, `start`, `name`, `phone`, `email`, `contactTime`, `lang`, `house`, `note`.

Trường dữ liệu form ứng viên (`formType = ungvien`): `name`, `phone`, `birthYear`, `hometown`, `currentAddress`, `position`, `mode`, `salary`, `start`, `expYears`, `experience` (gộp đã làm, nơi làm, giặt là, chăm sóc, nhà cửa, mô tả), `cooking`, `language`, `note`.

Cả hai form gửi kèm `consent`, `consentAt` (ISO 8601) và `page`. Trường nhiều lựa chọn được nối bằng dấu phẩy. Ô `website` là bẫy bot, có giá trị thì bỏ qua.

Lưu ý: mục 4 của Chính sách bảo vệ dữ liệu cá nhân đang ghi dữ liệu được lưu trên Google Sheets. Khi chuyển sang database mới cần cập nhật lại mục này cho đúng thực tế.

## Đo lường

Các sự kiện được đẩy vào `window.dataLayer`, dùng ngay được với Google Tag Manager / GA4: `dialog_open`, `form_step`, `form_error`, `form_submit`, `form_fallback`, `click_call`, `click_zalo`, `copy_phone`, `menu_open`.

## SEO và GEO/AIO đã làm

- HTML ngữ nghĩa, một H1, mỗi section có H2, nội dung có sẵn trong HTML (không phụ thuộc JavaScript để hiển thị).
- Title, meta description, canonical, Open Graph, Twitter Card, ảnh chia sẻ 1200x630.
- JSON-LD: `EmploymentAgency` (dịch vụ, khu vực phục vụ, liên hệ), `Service` cho 6 dịch vụ, `FAQPage`, `WebSite`, `WebPage`.
- Phần Hỏi đáp viết dạng câu hỏi - câu trả lời ngắn, rõ, lấy từ nội dung sẵn có, giúp công cụ tìm kiếm và trợ lý AI trích dẫn chính xác.
- `llms.txt` tóm tắt doanh nghiệp, dịch vụ, quy trình, FAQ cho các mô hình AI; `robots.txt` cho phép bot tìm kiếm và bot AI.
- Hiệu năng: CSS biên dịch, font tự host có preload, ảnh AVIF/WebP responsive, lazy-load, không thư viện ngoài. Lighthouse (máy chủ có nén gzip): mobile Performance 98, desktop 100; Accessibility, Best Practices, SEO đều 100.

## Việc cần làm khi đưa lên domain chính thức

1. Thay `https://phambacbinh.github.io/premiumhome/` bằng domain thật trong `site/index.html` (canonical, hreflang, Open Graph, JSON-LD), `robots.txt`, `sitemap.xml`, `llms.txt`.
2. Bổ sung link Fanpage Facebook (thêm vào footer và mục `sameAs` trong JSON-LD), địa chỉ văn phòng nếu có.
3. Khai báo Google Search Console, gửi sitemap; tạo Google Business Profile để tăng hiển thị tìm kiếm địa phương.
4. Thay ảnh minh họa bằng ảnh thật của Premium Home khi có (ảnh người làm cần có sự đồng ý).

## Ảnh minh họa

Ảnh tạo bằng AI (Gemini) theo prompt thương hiệu, đã cắt khung 4:5 và bỏ dấu watermark. File `assets/img/<tên>-<rộng>.webp`.

- Phòng khách: unsplash.com/photos/M_Xd4ddcyNk
- Đồ vải gấp gọn: Svitlana, unsplash.com/photos/HbiRi1Owk9k
- Em bé ngủ: Kelly Sikkema, unsplash.com/photos/S05YfA-_L4E
- Bà và cháu: Oanh MJ, unsplash.com/photos/8uhVTxlbBd4
- Lau đèn sứ: Cuong Duyen Ceramics, unsplash.com/photos/Ivmozc1emUA
- Mâm cơm gia đình: Duong Thinh, unsplash.com/photos/Gi0zkknkwpg
- Gia đình ngày Tết: Nam Đặng, unsplash.com/photos/i38xi-D0axQ
- Cửa chớp: Anh Tuan Thomas, unsplash.com/photos/gZ5TtGiPlcY

Khi có ảnh thật của Premium Home (có sự đồng ý của người trong ảnh) hoặc ảnh AI, thay file cùng tên.

## Bản final (12/10/2026) – thay đổi so với prototype

- Form đã nối Google Apps Script đang chạy (`CONFIG.FORM_ENDPOINT`). Hàm `send()` gửi `URLSearchParams` với `mode: 'no-cors'` (Apps Script không hỗ trợ CORS preflight cho JSON). Bằng chứng đồng ý được ghép vào trường `note` để lưu vào Sheets.
- Sửa lỗi ảnh dạng `data-reveal="mask"` không hiện trên Chrome (clip-path 100% khiến IntersectionObserver không báo giao cắt): quan sát phần tử cha.
- Bỏ số hotline ở hero theo yêu cầu chủ doanh nghiệp.
- Mô tả 6 dịch vụ chi tiết hơn, thêm dòng "Phù hợp".
- Hỏi đáp 12 câu (thêm khu vực phục vụ, chi phí, hợp đồng), cập nhật FAQPage JSON-LD.
- Font: toàn trang dùng Be Vietnam Pro (đồng bộ trang cũ); Cormorant Garamond chỉ dùng cho chữ PREMIUM HOME. Ghi đè ở cuối `src/app.css` và `site/assets/css/app.css` (chưa build lại Tailwind, ghi đè thuần CSS).
- Chống spam: Google reCAPTCHA v3 (vô hình). Điền `CONFIG.RECAPTCHA_SITE_KEY` trong `app.js`; script reCAPTCHA chỉ tải khi mở form. Secret key đặt trong Apps Script > Cài đặt dự án > Thuộc tính tập lệnh `RECAPTCHA_SECRET`. Apps Script bản 3 (`PremiumHome_AppsScript_v3.gs`) xác minh token; điểm < 0.5 hoặc thiếu token thì vẫn lưu với trạng thái "Nghi spam" và không gửi email.

## Đổi thương hiệu: Giúp việc Elite / Elite Helpers (12/10/2026)
- Tên Google/web: **Giúp việc Elite** – tên miền `giupviecelite.vn`. Tên page/logo: **Elite Helpers**.
- Logo phương án B (chữ lồng EH trong vòm). SVG đã chuyển chữ thành nét: `assets/img/logo-elite-helpers.svg`, `assets/img/arch-mark.svg`, `favicon.svg`.
- Mọi URL đổi sang `https://giupviecelite.vn/`; og-image mới `assets/img/og-giup-viec-elite.jpg`; file `CNAME` = giupviecelite.vn.
- Nguồn dựng lại: `eh/logo_svg.py` (logo), `eh/rebrand.py` (đổi chữ/URL), `eh/build_single.py` (bản 1 file).
- Fanpage URL vẫn là facebook.com/PremiumMaidHanoi; nếu đổi username page thì sửa `sameAs` và link chân trang.
