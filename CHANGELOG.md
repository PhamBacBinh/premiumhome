# CHANGELOG – giupviecelite.vn (Elite Helpers)

Mỗi lần tải `site.zip` lên GitHub là một **commit**. Muốn quay lại bản cũ: xem mục **Cách khôi phục** ở cuối.
Mã phiên bản web (`v=…`) nằm trong đường dẫn `app.css?v=…` / `app.js?v=…` của trang.

## Bảng tương thích web ↔ Apps Script

| Phiên bản web | Cần Apps Script | Ghi chú |
|---|---|---|
| 20261020a (mới nhất) | **bản 11** | Mục "Tìm việc an toàn" trang Tuyển dụng |
| 20261019s | **bản 11** | Ảnh mục "Điều gia đình nhận được" |
| 20261019r | **bản 11** | Banner 20/10 |
| 20261019q | **bản 11** | Nút Quản trị trên máy quản trị viên |
| 20261019p | **bản 11** | Tab Phân tích, khách cũ quay lại (web vẫn chạy với bản 10, chỉ thiếu phần phân tích) |
| 20261019n | **bản 10** | Nút Xóa hồ sơ trên /quan-tri |
| 20261019h – 20261019k | bản 9 trở lên | Trang quản trị tải dữ liệu bằng JSONP |
| 20261019 (trước 17:30) | bản 8 trở lên | Bộ đếm truy cập dùng tham số `vid` |

Apps Script mới luôn chạy được với web cũ (tương thích ngược). Khi khôi phục web cũ **không cần** hạ Apps Script.

---

## [20261020a] – 20/10/2026 · Mục "Tìm việc an toàn" trên trang Tuyển dụng
- /tuyen-dung: thêm mục ngay dưới phần đầu trang, 2 thẻ cạnh nhau (điện thoại: xếp dọc) – "Trước khi nhận việc, hãy cân nhắc nếu…" (6 dấu ❌) và "Ở Elite Helpers, chị em được an tâm" (6 tick xanh), mũi tên vàng ở giữa; nút Ứng tuyển và Zalo bên dưới.
- Ảnh mới: tim-viec-can-nhac-480/760.webp, tim-viec-an-tam-480/760.webp (21–42KB). CSS thêm khối .safe-*.

## [20261019s] – 19/10/2026 · Thay ảnh mục "Điều gia đình nhận được"
- Ảnh khung vòm trang chủ: thay "cửa chớp và hoa giấy" bằng ảnh người giúp việc cùng gia đình ba thế hệ trong sân vườn biệt thự (gia-dinh-biet-thu-520/900.webp), cập nhật mô tả ảnh (alt). Xóa ảnh cũ cua-chop-ha-noi-*.webp.

## [20261019r] – 19/10/2026 · Banner chúc mừng 20/10
- Hộp ảnh chúc mừng Ngày Phụ nữ Việt Nam hiện giữa màn hình từ 19/10 21:00 đến hết 22/10/2026 (tự tắt), mỗi trình duyệt 1 lần; bấm ảnh hoặc nút "Nhận tư vấn miễn phí" mở form khách. Không hiện ở trang tiếng Anh.
- Đo sự kiện promo_show / promo_click / promo_close (tab Phân tích). Ảnh: banner-20-10.webp (76KB).

## [20261019q] – 19/10/2026 · Nút Quản trị riêng cho máy quản trị viên
- Máy đã đăng nhập /quan-tri (cùng trình duyệt) thấy nút **Quản trị** ở góc trái dưới trên mọi trang; khách không thấy.
- Máy quản trị viên **không bị tính** vào bộ đếm và phân tích, không hiện banner cookie và hộp gợi ý.
- Trang quản trị: thêm liên kết "Về trang web".

## [20261019p] – 19/10/2026 · Đồng ý cookie, phân tích hành vi, hộp gợi ý
**Web**
- Thông báo **đồng ý cookie** (Đồng ý / Chỉ cần thiết) + nút "Cài đặt cookie" ở chân trang để đổi lựa chọn. Chưa đồng ý: không tải Google Analytics, không ghi hành vi. Rút lại đồng ý: xóa mã truy cập và cookie GA.
- **Phân tích hành vi first-party** (chỉ khi đồng ý): trang xem, nguồn (utm, Google, Facebook, Zalo, AI…), trang vào/thoát, % cuộn, thời gian xem, nút bấm, thiết bị, hệ điều hành, trình duyệt, ngôn ngữ, múi giờ. Không lưu IP.
- **Hộp gợi ý** theo trang (khách / ứng viên / tiếng Anh / khách cũ): hiện khi cuộn sâu, đọc lâu hoặc định rời trang (máy tính); 1 lần mỗi phiên, đóng thì ẩn 3 ngày.
- Form khách: ô tùy chọn **nhận tin chăm sóc qua Zalo/email**; hồ sơ gắn mã truy cập (nếu đã đồng ý cookie).
- Chính sách dữ liệu: thêm mục 4a (cookie, phân tích hành vi), thời hạn lưu dữ liệu phân tích 12 tháng; phiên bản chính sách 19/10/2026.
- Trang quản trị: tab **Phân tích** (KPI, theo ngày, trang, trang vào/thoát, nguồn, thiết bị, hành trình từng phiên); thẻ **Khách cũ quay lại** trong danh sách hồ sơ.

**Apps Script bản 11**
- `ev`: nhận sự kiện → tab **SuKien** (chống spam, tự xóa sau 12 tháng). `stats`: tổng hợp cho tab Phân tích (cache 2 phút).
- Cột mới: KhachHang "Nhận tin chăm sóc", "Mã truy cập web"; UngVien "Mã truy cập web" (tự thêm tiêu đề).
- Khách đã gửi form quay lại web → ghi tab **QuayLai** + email báo (tối đa 1 lần/6 giờ/khách).

## [20261019n] – 19/10/2026 · Bảo mật + xóa hồ sơ
**Web**
- Trang quản trị: nút **Xóa** từng hồ sơ (có hộp xác nhận, thông báo kết quả).
- Trang quản trị: thêm **Content-Security-Policy** – chỉ cho chạy đúng script của trang (mã băm SHA-256) và script từ Apps Script; chặn script lạ bị chèn vào.

**Apps Script bản 10**
- Hành động `del`: xóa dòng trong tab KhachHang/UngVien, kiểm tra đúng thời gian gửi để không xóa nhầm khi các dòng đã dịch chuyển.
- Bản sao lưu vào tab **ThungRac**, tự xóa hẳn sau **30 ngày**.
- Gộp kiểm tra mã quản trị vào hàm `auth_` (dùng chung cho xem và xóa, khóa 15 phút sau 10 lần sai).

## [20261019k] – 19/10/2026 · Tối ưu, dọn code, chuẩn SEO/GEO
- Rút gọn tiêu đề 9 trang (≤ 64 ký tự) để không bị Google cắt chữ.
- Trang 404: bỏ canonical/og:url, giữ `noindex`.
- JSON-LD viết gọn; nén CSS/JS (esbuild), bỏ chú thích HTML. JS ~28KB → ~16KB.
- Bỏ 25 quy tắc CSS không dùng (`.door`, `.pick-img`, `.h1-sub`, `.ft-cols`…).
- Bỏ chế độ debug bộ đếm, nhánh "prototype" và dòng "Bản prototype…" trong 2 form.

## [20261019h] – 19/10/2026 · Bộ đếm lên header, quản trị JSONP
- Bộ đếm "đang xem · lượt truy cập" chuyển lên dưới logo ELITE HELPERS (bỏ ở chân trang).
- Trang quản trị lấy dữ liệu bằng GET/JSONP (ổn định trên iPhone) – **cần Apps Script bản 9**.

## [20261019] – 19/10/2026 · Bộ đếm truy cập thật, SEO/GEO, bảng lương mới
- Bộ đếm lượt truy cập thật (Apps Script bản 6 → 8; bản 8 đổi tham số `sid` → `vid` vì Apps Script chặn tên `sid`, `c`).
- 5 bài cẩm nang (4 VI + 1 EN) có ô "Trả lời nhanh", FAQ, schema Article/FAQ/Breadcrumb; trang mục lục /dich-vu, /cam-nang.
- Bảng lương: Giúp việc 15–25tr · Bảo mẫu 15–25tr · Chăm sóc người già 15–25tr · Đầu bếp 18–35tr · Quản gia 20–40tr.
- Email liên hệ lienhe@giupviecelite.vn (Zoho); bỏ tên chủ sở hữu khỏi toàn site; GA4 G-JKX25NDPHK + sự kiện qualify_lead.

## [20261018] – 18/10/2026 · Trang quản trị /quan-tri (Apps Script bản 5)
- Chuông hồ sơ mới, âm báo, Notification, huy hiệu; nút Gọi/Zalo; bảo vệ bằng ADMIN_KEY.

## [20261013] – 13/10/2026 · Website v2
- Trang con cho 6 dịch vụ, /tuyen-dung, /thue-giup-viec-2026, /en; sitemap, llms.txt, robots cho AI.
- Form nhiều bước + reCAPTCHA v3 + chống chèn công thức, giới hạn tần suất (Apps Script bản 4).
- Triển khai bằng GitHub Actions: giải nén `site.zip` → GitHub Pages.

## [20261012] – 12/10/2026 · Ra mắt
- Website một trang, nhận diện Elite Helpers (Giúp việc Elite), tên miền giupviecelite.vn.

---

## Cách khôi phục bản cũ (làm trên iPhone)
1. Mở `github.com/PhamBacBinh/premiumhome/commits/main/site.zip` – danh sách mọi lần tải lên, mới nhất ở trên.
2. Bấm vào commit muốn quay lại → bấm tên `site.zip` → **View file / Download** (tải về Tệp).
3. Tải đúng file đó lên lại như bình thường (`…/upload/main` → Commit changes). Web trở về bản cũ sau 1–2 phút.
4. Đối chiếu bảng tương thích ở trên nếu bản cũ cần Apps Script khác.

Mã nguồn để dựng lại web nằm trong thư mục `nguon-ma/v2/` (chạy `python3 build.py`, kết quả ở `dist/`).
Code Apps Script nằm trong `nguon-ma/apps-script/` – **điền lại email nhận thông báo** ở dòng `NOTIFY_EMAIL` trước khi dán (đã ẩn vì kho GitHub công khai).
