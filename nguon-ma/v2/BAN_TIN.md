# Bản tin người lao động – quy trình thêm bài hằng tuần

Bản tin hiển thị toàn bộ trong mục **/tuyen-dung** (khối `#ban-tin`, kiểu báo điện tử: tiêu đề, tóm tắt, ảnh lớn).
Mỗi bài có trang riêng `/<slug>`, mở tab mới. Dữ liệu nằm trong `news.py` (danh sách `POSTS`, bài mới nhất đứng đầu).

## Thêm 1 bài mới
1. Tìm 1 chủ đề nổi bật trong 7–14 ngày gần nhất về nghề giúp việc, bảo mẫu, chăm sóc người già, quyền lợi người lao động
   (báo chính thống: vnexpress.net, dantri.com.vn, tienphong.vn, laodong.vn, tuoitre.vn, thanhnien.vn, vtv.vn, suckhoedoisong.vn;
   văn bản luật: thuvienphapluat.vn, chinhphu.vn). Không trùng chủ đề các bài đã có trong `POSTS`.
2. Đọc bài gốc, viết lại bằng lời của Elite Helpers (không chép nguyên văn), ghi nguồn + ngày ở cuối (`sources`).
   Số liệu, mức phạt, điều luật phải đúng nguồn. Giọng tích cực, dành cho người lao động (chị em tìm việc).
3. Thêm dict vào ĐẦU `POSTS`: `no` = số bài trước + 1, `slug`, `date`, `date_vi`, `tag`, `title`, `sapo`, `src_short`,
   `body` (h2, p, ul/ol, table, `<div class="note">` có câu về Elite Helpers), `sources`, `cover` (big/label/note/tone: green|gold|warn),
   `prompt` (prompt Meta AI ảnh 16:9, người và bối cảnh mới, ghi "KÊNH: WEBSITE – BẢN TIN").
4. `python3 gen_news_covers.py` (tạo `site/assets/img/ban-tin-<no>-640.webp`, `-1200.webp`), xem lại ảnh.
5. Đổi `VER` trong build.py, `python3 build.py`, kiểm tra trang `/tuyen-dung` và trang bài trên khổ điện thoại 390px.
6. Nén `dist/` thành `site.zip` ở gốc repo, chép lại mã nguồn vào `nguon-ma/v2/`, commit, push nhánh main.

Công cụ cần: Python 3 + beautifulsoup4 + pillow + playwright (Chromium), Node để chạy esbuild,
font `@fontsource/be-vietnam-pro` trong `../../tools/node_modules` (đường dẫn tính từ thư mục v2).
