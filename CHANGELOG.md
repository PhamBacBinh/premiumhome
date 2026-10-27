# CHANGELOG – giupviecelite.vn (Elite Helpers)

Mỗi lần tải `site.zip` lên GitHub là một **commit**. Muốn quay lại bản cũ: xem mục **Cách khôi phục** ở cuối.
Mã phiên bản web (`v=…`) nằm trong đường dẫn `app.css?v=…` / `app.js?v=…` của trang.

## Bảng tương thích web ↔ Apps Script

| Phiên bản web | Cần Apps Script | Ghi chú |
|---|---|---|
| 20261027a (mới nhất) | **bản 19** | Form ứng viên khai đủ các mục như hồ sơ trong Kho; CV ghi đủ nơi ở (web vẫn chạy với bản 18, nhưng các mục mới chưa vào Kho) |
| 20261026h | **bản 18** | Tin tuyển dụng sửa được trên /quan-tri; thẻ tin gọn, trang chi tiết /viec-lam (web vẫn chạy với bản 17, hiện tin in sẵn, chưa sửa được) |
| 20261026g | **bản 17** | Tin tuyển dụng ứng tuyển trực tiếp; trang Tin tức riêng |
| 20261026f | **bản 17** | Kho khách hàng; form ứng viên chuẩn hóa |
| 20261026e | **bản 16** | Sửa ngày bắt đầu bị đảo ngày/tháng khi lưu |
| 20261026e | **bản 15** | Nhận xét Elite Helpers trình bày theo mục, gạch đầu dòng |
| 20261026d | **bản 14** | Sửa CV tràn chữ trên điện thoại, In / Lưu PDF đúng 1 trang |
| 20261026c | **bản 14** | Tách kinh nghiệm từ form website thành dòng thời gian + Kinh nghiệm thực tế |
| 20261026b | **bản 13** | CV chuyên nghiệp: quá trình làm việc theo giai đoạn, CV Docs 2 cột |
| 20261026a | **bản 12** | Kho ứng viên trên /quan-tri (web vẫn chạy với bản 11, chỉ thiếu Kho) |
| 20261021a | **bản 11** | Bảng lương mới 10–25 / 15–35 / 18–40 |
| 20261020d | **bản 11** | Thanh chuyển Trang chủ / Tuyển dụng |
| 20261020c | **bản 11** | Mục Tuyển dụng trên trang chủ |
| 20261020b | **bản 11** | Giữ đăng nhập quản trị khi hệ thống tạm khóa |
| 20261020a | **bản 11** | Mục "Tìm việc an toàn" trang Tuyển dụng |
| 20261019s | **bản 11** | Ảnh mục "Điều gia đình nhận được" |
| 20261019r | **bản 11** | Banner 20/10 |
| 20261019q | **bản 11** | Nút Quản trị trên máy quản trị viên |
| 20261019p | **bản 11** | Tab Phân tích, khách cũ quay lại (web vẫn chạy với bản 10, chỉ thiếu phần phân tích) |
| 20261019n | **bản 10** | Nút Xóa hồ sơ trên /quan-tri |
| 20261019h – 20261019k | bản 9 trở lên | Trang quản trị tải dữ liệu bằng JSONP |
| 20261019 (trước 17:30) | bản 8 trở lên | Bộ đếm truy cập dùng tham số `vid` |

Apps Script mới luôn chạy được với web cũ (tương thích ngược). Khi khôi phục web cũ **không cần** hạ Apps Script.

---

## [20261027a] – 27/10/2026 · Form ứng viên đầy đủ như hồ sơ Kho (cần Apps Script bản 19)
- Form "Hồ sơ ứng tuyển" (#ung-tuyen) làm lại theo đúng các mục của "Sửa hồ sơ" trên /quan-tri, 4 bước:
  1. Thông tin cá nhân: họ tên, SĐT, năm sinh, giới tính, quê quán, tỉnh/thành đang ở, địa chỉ chi tiết, tình trạng gia đình, sức khỏe, đi xe máy.
  2. Khu vực nhận việc (chọn tỉnh/thành theo miền, bắt buộc) + nguyện vọng: vị trí, hình thức, lương từ – đến / thỏa thuận, có thể bắt đầu (Đi làm ngay / Từ ngày / Thỏa thuận / Ghi khác), ngày nghỉ mong muốn.
  3. Tổng số năm kinh nghiệm + quá trình làm việc theo giai đoạn (từ – đến tháng/năm hoặc hiện tại, vị trí, hình thức, nơi làm, công việc chính), tối đa 6 giai đoạn.
  4. Kỹ năng nổi bật, chứng chỉ / đào tạo, nấu ăn, ngoại ngữ (+ ô khác), giấy tờ có thể cung cấp, ghi chú.
- Website gửi thêm trường `profile` (JSON cùng tên trường với KhoUngVien). Apps Script bản 19 ghi thẳng vào Kho: đã phân luồng khu vực, quá trình làm việc chia giai đoạn, CV in đủ mục ngay không cần sửa tay. Giấy tờ ứng viên khai ghi vào Ghi chú nội bộ (mục "Đã xác minh" vẫn do quản trị tick sau khi kiểm tra).
- CV (xem trước, In / PDF, bản Zalo, Google Docs): "Nơi ở hiện tại" = địa chỉ chi tiết + tỉnh/thành (trước đây chỉ hiện tỉnh/thành nên hồ sơ chỉ nhập địa chỉ chi tiết bị thiếu dòng này).
- Sửa lỗi mở link có #ung-tuyen / #tim-nguoi trực tiếp (form không mở do script gọi trước khi khởi tạo xong).
- Bản gửi Zalo dự phòng có đủ các mục mới.

## [Apps Script bản 19] – 27/10/2026
- Tab UngVien thêm cột "Hồ sơ chi tiết (JSON)"; hàm `khoProfile_` chuyển hồ sơ chi tiết vào KhoUngVien (cả khi bấm "Nhập hồ sơ từ website"). Email báo không kèm JSON.

## [20261026h] – 26/10/2026 · Tin tuyển dụng sửa được, thẻ tin gọn (cần Apps Script bản 18)
- /quan-tri thêm mục **Tin tuyển dụng**: đăng tin mới, sửa, nhân bản, Tạm ẩn / Đã tuyển / Mở lại, xóa (bản sao ở ThungRac 30 ngày), xem trước thẻ tin, sao chép link tin, sao chép bài đăng Facebook. Lần đầu bấm "Đưa 3 tin đang hiển thị lên hệ thống".
- Trường của tin: Tên vị trí, Mức lương (từ – đến, ghi chú), Ngày nghỉ, Tháng lương 13, Địa điểm làm việc, Thời gian cần, Thời gian làm việc, Mô tả công việc, Yêu cầu công việc, Quyền lợi, Nhãn (Tuyển gấp / Hot / Mới), Hạn tin, Thứ tự, Ghi chú nội bộ (không hiện trên web).
- /tuyen-dung: tin hiển thị dạng thẻ gọn (logo EH, tên vị trí, lương, địa điểm, nhãn, nút Ứng tuyển); bấm thẻ mở tab mới **/viec-lam/?ma=<Mã tin>**: ô dữ kiện (lương, ngày nghỉ, tháng 13, địa điểm, thời gian cần, thời gian làm việc), mô tả, yêu cầu, quyền lợi, tin khác đang tuyển, dữ liệu JobPosting.
- Website đọc tin từ Apps Script (action=jobs, lưu đệm 5 phút); chưa có bản 18 hoặc tab còn trống thì hiện tin in sẵn trong `nguon-ma/v2/jobs.py` (SEED).
- Thêm tin EH-GV-2610 (Giúp việc ở lại, Tây Hồ); cập nhật đầy đủ EH-BM-2610 (Gamuda). Link cũ của 2 tin bảo mẫu tự chuyển sang /viec-lam.
- Apps Script bản 18: tab TinTuyenDung, action job_list / job_save / job_del (cần mã quản trị) và jobs (công khai, không có ghi chú nội bộ, bỏ tin Tạm ẩn).

## [20261026g] – 26/10/2026 · Tách Tuyển dụng và Tin tức (không cần đổi Apps Script, trang quản trị giữ nguyên)
- **/tuyen-dung** chỉ còn tuyển dụng: mục **Việc đang tuyển** (mỗi tin có mã, thu nhập, hình thức, nơi làm, nút **Ứng tuyển ngay**), mục **Vị trí tuyển thường xuyên** (mỗi vị trí có nút ứng tuyển), Tìm việc an toàn, Quyền lợi, Quy trình, Hỏi đáp, ô dẫn sang Tin tức. Thanh chuyển **Việc đang tuyển / Tin tức**.
- Bấm **Ứng tuyển ngay**: form ứng viên mở với khung "Đang ứng tuyển" (tên tin, mã tin), tự chọn vị trí và hình thức. Mã + tên tin ghi vào đầu ô **Ghi chú** của hồ sơ (dạng `Ứng tuyển tin: EH-BM-2510 · …`), hiện trong trang quản trị như cũ; bản gửi Zalo dự phòng cũng có dòng này.
- Mỗi tin có trang riêng (ví dụ `/tuyen-bao-mau-cham-be-so-sinh-ocean-park-2`) với dữ liệu JobPosting cho Google Việc làm; tin hết hạn hoặc đã tuyển tự ẩn nút ứng tuyển.
- Trang mới **/tin-tuc** (Trang chủ / Tuyển dụng / Tin tức) chứa toàn bộ bản tin người lao động; trang từng bài có đường dẫn Trang chủ / Tuyển dụng / Tin tức. Link cũ `/tuyen-dung#ban-tin` tự chuyển sang /tin-tuc.
- 2 tin đang mở: EH-BM-2610 (Bảo mẫu, KĐT Gamuda, Hoàng Mai) và EH-BM-2510 (Bảo mẫu sơ sinh, Vinhomes Ocean Park 2).
- Khôi phục ảnh `media/2026-10-26/EliteHelpers_2610_Group_TuyenBaoMau_Gamuda.jpg` bị thiếu ở bản 20261026f.
- Dữ liệu tin tuyển dụng: `nguon-ma/v2/jobs.py` (danh sách `JOBS`).

## [20261026f] – 26/10/2026 · Kho khách hàng, form ứng viên chuẩn hóa (cần Apps Script bản 17)
- Tab mới **Kho khách hàng** trên /quan-tri: yêu cầu từ form "Tìm người hỗ trợ" tự vào kho (tab KhoKhachHang), nút nhập lại yêu cầu cũ; lọc Đang xử lý / Ưu tiên cao / Đã xong, dịch vụ, loại khách, trạng thái; trạng thái + ưu tiên + lịch sử chăm sóc; gắn ứng viên đã giới thiệu; gợi ý ứng viên phù hợp (khu vực, vị trí, hình thức); In / Lưu PDF phiếu yêu cầu dịch vụ; sao chép tóm tắt. Thẻ khách ở tab Hồ sơ có nút "Mở trong kho khách".
- Form sửa ứng viên làm lại theo 8 nhóm: ngày bắt đầu chọn trên lịch (lưu dd/mm/yyyy) hoặc Đi làm ngay / Thỏa thuận; mức lương từ – đến (triệu/tháng); thời gian từng giai đoạn chọn Tháng/Năm, ô Hiện tại, kiểm tra Đến không sớm hơn Từ; giấy tờ đã xác minh; xe máy; ngày nghỉ; tình trạng gia đình; sức khỏe; nấu ăn và ngoại ngữ chọn sẵn + ô khác; kiểm tra SĐT, năm sinh; nút Lưu luôn hiện ở cuối khung.
- CV: dòng "Đã xác minh" dưới 4 ô dữ kiện; thêm các thông tin mới; Nấu ăn thành danh sách; giữ xuống dòng như khi nhập; sửa họ tên tiếng Việt hiển thị lẫn font.

## [Apps Script bản 16] – 26/10/2026 · Sửa ngày bị đảo ngày/tháng
- Lỗi: ô "Có thể bắt đầu" nhập 01/11/2026 bị Google Sheets tự hiểu theo kiểu Mỹ (tháng/ngày) thành 11/01/2026. Nay mọi ô chữ (Kho ứng viên và form website) ghi dạng văn bản; ô cũ đã bị đổi thành ngày được đọc lại đúng thứ tự đã nhập. Không cần đổi web.

## [20261026e] – 26/10/2026 · Nhận xét Elite Helpers trình bày theo mục (cần Apps Script bản 15)
- Ô Nhận xét tự nhập: dòng "1. …", "2. …" thành tiêu đề in đậm (số màu vàng đồng); dòng bắt đầu "-" thành gạch đầu dòng; "Nhãn: nội dung" in đậm nhãn. Viết liền một đoạn vẫn tự tách trước "1." "2." và trước " - ". Áp dụng xem trước, In / PDF, Google Docs, bản Zalo.
- Khung nhận xét bỏ chữ nghiêng toàn khối cho dễ đọc. Lịch sử trao đổi giữ xuống dòng như khi nhập.

## [20261026d] – 26/10/2026 · Sửa lỗi hiển thị CV
- Mục Kinh nghiệm thực tế bị ép thành cột hẹp (chữ dọc từng ký tự) trên điện thoại do kiểu bảng của trang quản trị lọt vào CV: tách riêng kiểu CV.
- In / Lưu PDF trên iPhone: dải đầu trang không còn đè lên họ tên, CV nằm gọn 1 trang A4 (lề 8 mm).

## [20261026c] – 26/10/2026 · Tách kinh nghiệm gửi từ form website (cần Apps Script bản 14)
- Hồ sơ từ website (dạng "Đã làm: … | Nơi làm: … | Giặt là: … | Chăm sóc: … | Nhà cửa: … | Mô tả: …") giờ hiển thị trên CV thành: dòng thời gian (năm, việc đã làm, nơi làm, phần Mô tả tách từng câu thành gạch đầu dòng) và mục **Kinh nghiệm thực tế** (từng nhóm kèm các lựa chọn dạng thẻ). Áp dụng cho xem trước, In / Lưu PDF, Google Docs và bản Zalo.
- Nút "Tách từ mô tả đã có" điền sẵn năm, vị trí, nơi làm, công việc; Kỹ năng nổi bật tự lấy từ Chăm sóc / Giặt là / Nhà cửa nếu đang trống.

## [20261026b] – 26/10/2026 · CV chuyên nghiệp theo nhận diện thương hiệu (cần Apps Script bản 13)
- Quá trình làm việc nhập theo từng giai đoạn: thời gian, vị trí, nơi làm/gia đình, hình thức, công việc chính (mỗi dòng 1 gạch đầu dòng); nút "Tách từ mô tả đã có" chia mô tả cũ thành giai đoạn.
- Kỹ năng nổi bật, chứng chỉ dạng danh sách; thêm "Nhận xét của Elite Helpers" in vào CV.
- CV mới (xem trước trong hồ sơ, In / Lưu PDF A4, Google Docs): dải đầu xanh rêu có logo EH, họ tên Cormorant Garamond, 4 ô dữ kiện nhanh, cột trái thông tin – nguyện vọng – kỹ năng – chứng chỉ, cột phải nhận xét + dòng thời gian kinh nghiệm, chân trang cam kết và liên hệ. Font Be Vietnam Pro / Cormorant Garamond tự host.
- Bản Zalo trình bày theo mục.
- Apps Script bản 13 sửa lỗi bản 12 không tạo được tab KhoUngVien (trang tính mới chỉ có 26 cột); thêm cột "Quá trình làm việc (chi tiết)", "Nhận xét Elite Helpers".
- Thêm `cv-logo.png` (logo EH nền trong) cho CV Google Docs.

## [20261026a] – 26/10/2026 · Kho ứng viên trên trang quản trị (cần Apps Script bản 12)
- /quan-tri thêm tab **Kho ứng viên**: lọc theo khu vực nhận việc (Hà Nội, Miền Bắc/Trung/Nam, 34 tỉnh/thành mới), vị trí, kinh nghiệm, hình thức, trạng thái; nhóm "Chưa phân luồng" cho hồ sơ mới.
- Mỗi ứng viên: trạng thái + lịch sử trao đổi, sửa hồ sơ, xóa (bản sao ở ThungRac 30 ngày), cảnh báo trùng SĐT.
- Xuất CV gửi khách: tạo Google Docs trong thư mục Drive "Elite Helpers – CV ứng viên" (kèm link PDF), In / Lưu PDF, sao chép gửi Zalo; mặc định ẩn SĐT và rút gọn họ tên.
- Dữ liệu lưu ở tab `KhoUngVien` của Google Sheet. Hồ sơ ứng tuyển mới từ website tự vào kho; nút "Nhập hồ sơ từ website" đưa hồ sơ cũ (tab UngVien) vào kho.
- Tab Hồ sơ: thẻ ứng viên có nút "Phân luồng" mở thẳng hồ sơ trong kho.
- CSP trang quản trị cho phép gửi dữ liệu (POST) tới Apps Script.

## [20261021a] – 21/10/2026 · Cập nhật bảng lương tham khảo
- Lương mới (triệu đồng/tháng): giúp việc, bảo mẫu, chăm sóc người già 10–25; đầu bếp 15–35; quản gia 18–40. Thay trên trang chủ (Hỏi đáp), /tuyen-dung, 5 trang dịch vụ (kèm dữ liệu cấu trúc lương), các bài cẩm nang, bản tiếng Anh.
- Thêm giải thích "Mức lương có thể thay đổi theo nhu cầu của gia đình": ở lại/theo giờ; quy mô nhà, trẻ nhỏ, người già; chứng chỉ, kỹ năng; bằng cấp; ngoại ngữ; kinh nghiệm quản lý (danh sách đầy đủ dưới bảng lương bài /gia-thue-giup-viec-ha-noi).

## [20261020d] – 20/10/2026 · Thanh chuyển "Trang chủ / Tuyển dụng"
- Đầu trang chủ thêm dòng "Trang chủ / Tuyển dụng" (giống đường dẫn ở /tuyen-dung): bấm "Tuyển dụng" sang trang tuyển dụng, ở đó bấm "Trang chủ" để quay lại.

## [20261020c] – 20/10/2026 · Mục Tuyển dụng trên trang chủ
- Trang chủ: thêm mục #viec-lam ngay sau Dịch vụ (2 thẻ Cân nhắc ❌ / An tâm ✅ như trang /tuyen-dung) với nút Ứng tuyển, Xem việc đang tuyển, Zalo.
- Menu: mục "Ứng tuyển" đổi thành "Tuyển dụng" (cuộn tới #viec-lam).
- Nút Quản trị: thành nút tròn chuông ở góc phải, không còn che nút "Tìm người hỗ trợ".

## [20261020b] – 20/10/2026 · Không tự đăng xuất quản trị khi bị tạm khóa
- Lỗi: khi có người (hoặc bot) nhập sai mã quản trị 10 lần, Apps Script tạm khóa 15 phút cho mọi người; trang /quan-tri trên máy quản trị viên nhận "locked" và xóa mã đã lưu → mất nút chuông Quản trị trên web.
- Sửa: chỉ xóa mã khi mã thật sự sai ("auth"); khi "locked" giữ mã, báo trạng thái và tự thử lại theo chu kỳ.

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
