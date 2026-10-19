/**
 * ELITE HELPERS (Giúp việc Elite) – Nhận form giupviecelite.vn về Google Sheets (bản 10)
 * Bản 10: trang quản trị xóa được hồ sơ: xóa dòng trong tab KhachHang/UngVien, lưu bản sao vào tab ThungRac
 *         (tự xóa hẳn sau 30 ngày) để khôi phục khi lỡ tay.
 * Bản 9: trang quản trị lấy dữ liệu qua GET (JSONP) như bộ đếm, chạy ổn định trên iPhone.
 * Bản 8: đổi tham số sid → vid (Google Apps Script dành riêng tên 'sid' và 'c', gửi lên sẽ bị chặn).
 * Bản 7: bộ đếm nhận yêu cầu qua GET (JSONP) để chạy được trên Safari, Zalo và mọi trình duyệt.
 * Bản 6: bộ đếm lượt truy cập thật (tổng, hôm nay, đang xem) hiển thị ở chân trang; lưu lịch sử theo ngày vào tab LuotTruyCap.
 * Bản 5: thêm nguồn dữ liệu cho trang quản trị /quan-tri (chuông thông báo). Chỉ trả dữ liệu khi đúng
 *        mã ADMIN_KEY (đặt trong Thuộc tính tập lệnh, không ghi trong code, không đưa lên GitHub).
 * Bản 4: trả về {ok:false} khi lỗi thật (ghi Sheets lỗi, hệ thống bận, thiếu thông tin) để website
 *        chuyển sang phương án gửi qua Zalo, không còn báo "đã nhận" khi chưa lưu được.
 * - Xác minh Google reCAPTCHA v3 (khi đã khai báo RECAPTCHA_SECRET trong Thuộc tính tập lệnh)
 * - Hồ sơ nghi spam vẫn được lưu với trạng thái "Nghi spam" (không gửi email báo), để không mất khách thật
 * - Chặn chèn công thức, giới hạn tần suất, cắt độ dài
 * - Email báo hiển thị số điện thoại sạch (không dấu nháy)
 */
const NOTIFY_EMAIL = 'DIEN_EMAIL_NHAN_THONG_BAO@example.com'; // điền email thật trước khi dán vào Apps Script
const MAX_PER_10_MIN = 20;
const MIN_SCORE = 0.5;

const FORMS = {
  khach: {
    sheet: 'KhachHang',
    title: 'Khách hàng mới',
    cols: [['Họ tên / Đơn vị','name'],['SĐT / Zalo','phone'],['Email','email'],['Khách hàng','client'],
      ['Dịch vụ','service'],['Hình thức','mode'],['Khu vực','area'],['Bắt đầu','start'],['Ngôn ngữ','lang'],
      ['Loại nhà','house'],['Giờ liên hệ','contactTime'],['Mô tả','note']]
  },
  ungvien: {
    sheet: 'UngVien',
    title: 'Hồ sơ ứng viên mới',
    cols: [['Họ tên','name'],['SĐT / Zalo','phone'],['Năm sinh','birthYear'],['Quê quán','hometown'],
      ['Nơi ở hiện tại','currentAddress'],['Vị trí','position'],['Hình thức','mode'],['Nấu ăn','cooking'],
      ['Kinh nghiệm','expYears'],['Ngoại ngữ','language'],['Chi tiết kinh nghiệm','experience'],
      ['Lương mong muốn','salary'],['Bắt đầu','start'],['Ghi chú','note']]
  }
};

function setup() {
  Logger.log('File dữ liệu: ' + getSS_().getUrl());
}

function getSS_() {
  const props = PropertiesService.getScriptProperties();
  const id = props.getProperty('SS_ID');
  if (id) { try { return SpreadsheetApp.openById(id); } catch (e) {} }
  const ss = SpreadsheetApp.create('Premium Home – Dữ liệu website');
  props.setProperty('SS_ID', ss.getId());
  Object.keys(FORMS).forEach((k, i) => {
    const f = FORMS[k];
    const sh = i === 0 ? ss.getSheets()[0].setName(f.sheet) : ss.insertSheet(f.sheet);
    const head = ['Thời gian', 'Trạng thái'].concat(f.cols.map(c => c[0]));
    sh.appendRow(head);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, head.length).setFontWeight('bold').setBackground('#2A453E').setFontColor('#F4EEE3');
  });
  return ss;
}

// Làm sạch: bỏ ký tự điều khiển, cắt độ dài
function clean_(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g, '').trim().slice(0, max || 1000);
}
// Chặn công thức khi ghi vào Sheets
function safeCell_(s) {
  return /^[=+\-@\t\r]/.test(s) ? "'" + s : s;
}

function tooMany_() {
  const cache = CacheService.getScriptCache();
  const n = Number(cache.get('rate') || 0);
  if (n >= MAX_PER_10_MIN) return true;
  cache.put('rate', String(n + 1), 600);
  return false;
}

// Trả về: 'off' (chưa cấu hình), 'ok', hoặc lý do nghi spam
function checkRecaptcha_(token) {
  const secret = PropertiesService.getScriptProperties().getProperty('RECAPTCHA_SECRET');
  if (!secret) return 'off';
  if (!token) return 'thiếu mã reCAPTCHA';
  try {
    const res = UrlFetchApp.fetch('https://www.google.com/recaptcha/api/siteverify', {
      method: 'post', payload: { secret: secret, response: token }, muteHttpExceptions: true
    });
    const r = JSON.parse(res.getContentText());
    if (!r.success) return 'reCAPTCHA không hợp lệ';
    if (typeof r.score === 'number' && r.score < MIN_SCORE) return 'điểm reCAPTCHA ' + r.score;
    return 'ok';
  } catch (e) {
    return 'off'; // lỗi kết nối Google: không chặn khách thật
  }
}

function doPost(e) {
  try {
    const p = (e && e.parameter) || {};
    if (p.action === 'hit') return hit_(p);                  // bộ đếm lượt truy cập
    if (p.action === 'feed') return feed_(p);                // trang quản trị lấy danh sách hồ sơ mới
    if (p.website) return out_(true);                         // bẫy bot: giả vờ thành công
    if (!p.name || !p.phone) return out_(false, 'missing');   // thiếu thông tin bắt buộc
    const f = FORMS[p.formType] || FORMS.khach;
    const rc = checkRecaptcha_(p.recaptcha);
    const suspicious = rc !== 'ok' && rc !== 'off';

    const lock = LockService.getScriptLock();
    if (!lock.tryLock(10000)) return out_(false, 'busy');
    let vals;
    try {
      if (tooMany_()) return out_(false, 'rate');
      vals = f.cols.map(c => clean_(p[c[1]], c[1] === 'experience' || c[1] === 'note' ? 2000 : 300));
      const row = vals.map((v, i) => (f.cols[i][1] === 'phone' && v ? "'" + v : safeCell_(v)));
      const status = suspicious ? 'Nghi spam (' + rc + ')' : 'Mới';
      getSS_().getSheetByName(f.sheet).appendRow([new Date(), status].concat(row));
    } finally {
      lock.releaseLock();
    }
    if (suspicious) return out_(true);                        // đã lưu để kiểm tra, không gửi email
    try {
      const name = clean_(p.name, 60).replace(/[\r\n]/g, ' ');
      const body = f.cols.map((c, i) => vals[i] ? c[0] + ': ' + vals[i] : '').filter(Boolean).join('\n');
      MailApp.sendEmail(NOTIFY_EMAIL, '[Elite Helpers] ' + f.title + ': ' + name,
        body + '\n\nXem dữ liệu: ' + getSS_().getUrl());
    } catch (err) {}                                          // lỗi email không làm mất hồ sơ đã lưu
    return out_(true);
  } catch (err) {
    console.error(err);
    return out_(false, 'server');
  }
}

// ---- Trang quản trị: trả 40 hồ sơ mới nhất (khách + ứng viên) khi đúng ADMIN_KEY ----
// Kiểm tra mã quản trị: trả về null nếu đúng, hoặc mã lỗi
function auth_(p) {
  const key = PropertiesService.getScriptProperties().getProperty('ADMIN_KEY');
  if (!key || key.length < 12) return 'nokey';
  const cache = CacheService.getScriptCache();
  const bad = Number(cache.get('feedbad') || 0);
  if (bad >= 10) return 'locked';                            // sai mã quá 10 lần/15 phút: tạm khóa
  if (String(p.key || '') !== key) { cache.put('feedbad', String(bad + 1), 900); return 'auth'; }
  return null;
}
const isoOf_ = (v) => (v instanceof Date ? v.toISOString() : String(v));

function feed_(p) {
  const er = auth_(p);
  if (er) return out_(false, er);
  const ss = getSS_();
  const items = [];
  Object.keys(FORMS).forEach(type => {
    const f = FORMS[type];
    const sh = ss.getSheetByName(f.sheet);
    if (!sh || sh.getLastRow() < 2) return;
    const n = Math.min(40, sh.getLastRow() - 1);
    const rows = sh.getRange(sh.getLastRow() - n + 1, 1, n, 2 + f.cols.length).getValues();
    rows.forEach((r, i) => {
      const o = { type: type, row: sh.getLastRow() - n + 1 + i, time: isoOf_(r[0]), status: String(r[1]) };
      f.cols.forEach((c, j) => { o[c[1]] = String(r[2 + j]).replace(/^'/, ''); });
      items.push(o);
    });
  });
  items.sort((a, b) => (a.time < b.time ? 1 : -1));
  return ContentService.createTextOutput(JSON.stringify({ ok: true, items: items.slice(0, 40) })).setMimeType(ContentService.MimeType.JSON);
}

// ---- Trang quản trị: xóa 1 hồ sơ (kiểm tra đúng thời gian gửi để không xóa nhầm dòng) ----
const TRASH = 'ThungRac';
const TRASH_DAYS = 30;
function del_(p) {
  const er = auth_(p);
  if (er) return out_(false, er);
  const f = FORMS[p.kind];
  if (!f || !p.ts) return out_(false, 'missing');
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(10000)) return out_(false, 'busy');
  try {
    const ss = getSS_();
    const sh = ss.getSheetByName(f.sheet);
    const last = sh ? sh.getLastRow() : 0;
    if (last < 2) return out_(false, 'notfound');
    const width = 2 + f.cols.length;
    let row = Number(p.rowno) || 0;
    const match = (r) => r >= 2 && r <= last && isoOf_(sh.getRange(r, 1).getValue()) === String(p.ts);
    if (!match(row)) {                                       // dòng đã dịch chuyển: tìm lại theo thời gian gửi
      const times = sh.getRange(2, 1, last - 1, 1).getValues();
      row = 0;
      for (let i = times.length - 1; i >= 0; i--) { if (isoOf_(times[i][0]) === String(p.ts)) { row = i + 2; break; } }
      if (!row) return out_(false, 'notfound');
    }
    const vals = sh.getRange(row, 1, 1, width).getValues()[0];
    let tr = ss.getSheetByName(TRASH);
    if (!tr) {
      tr = ss.insertSheet(TRASH);
      tr.appendRow(['Thời gian xóa', 'Loại', 'Thời gian gửi', 'Trạng thái', 'Dữ liệu (các cột theo tab gốc)']);
      tr.setFrozenRows(1);
      tr.getRange(1, 1, 1, 5).setFontWeight('bold').setBackground('#2A453E').setFontColor('#F4EEE3');
    }
    tr.appendRow([new Date(), f.sheet].concat(vals.map((v, i) => (i >= 2 && typeof v === 'string' ? (/^[0-9+]/.test(v) ? "'" + v : safeCell_(v)) : v))));
    sh.deleteRow(row);
    purgeTrash_(tr);
    return out_(true);
  } finally {
    lock.releaseLock();
  }
}
// Xóa hẳn các bản trong ThungRac quá 30 ngày
function purgeTrash_(tr) {
  const n = tr.getLastRow() - 1;
  if (n < 1) return;
  const limit = Date.now() - TRASH_DAYS * 86400000;
  const d = tr.getRange(2, 1, n, 1).getValues();
  for (let i = n - 1; i >= 0; i--) {
    if (d[i][0] instanceof Date && d[i][0].getTime() < limit) tr.deleteRow(i + 2);
  }
}

// ---- Bộ đếm lượt truy cập: 1 phiên trình duyệt = 1 lượt; "đang xem" = phiên hoạt động trong 5 phút ----
const TZ = 'Asia/Ho_Chi_Minh';
function hit_(p) {
  const props = PropertiesService.getScriptProperties();
  const cache = CacheService.getScriptCache();
  const today = Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd');
  const sid = String(p.vid || '').replace(/[^a-z0-9]/gi, '').slice(0, 24);
  const isNew = p.n === '1' && sid.length >= 8;
  let total, day;
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(5000)) return counts_(props, cache, today);
  try {
    total = Number(props.getProperty('V_TOTAL') || 0);
    const vDate = props.getProperty('V_DATE');
    day = vDate === today ? Number(props.getProperty('V_DAY') || 0) : 0;
    if (vDate && vDate !== today) logDay_(vDate, Number(props.getProperty('V_DAY') || 0));
    if (isNew && !cache.get('s_' + sid)) { total++; day++; cache.put('s_' + sid, '1', 21600); }
    props.setProperties({ V_TOTAL: String(total), V_DATE: today, V_DAY: String(day) });
    // đang xem: danh sách phiên trong 5 phút gần nhất
    const now = Date.now();
    let on = {};
    try { on = JSON.parse(cache.get('online') || '{}'); } catch (e) {}
    if (sid) on[sid] = now;
    Object.keys(on).forEach(k => { if (now - on[k] > 300000) delete on[k]; });
    const keys = Object.keys(on);
    if (keys.length > 300) keys.sort((a, b) => on[a] - on[b]).slice(0, keys.length - 300).forEach(k => delete on[k]);
    cache.put('online', JSON.stringify(on), 600);
    return jsonOut_({ ok: true, total: total, today: day, online: Math.max(1, Object.keys(on).length) });
  } finally {
    lock.releaseLock();
  }
}
function counts_(props, cache, today) {
  let on = {};
  try { on = JSON.parse(cache.get('online') || '{}'); } catch (e) {}
  const day = props.getProperty('V_DATE') === today ? Number(props.getProperty('V_DAY') || 0) : 0;
  return jsonOut_({ ok: true, total: Number(props.getProperty('V_TOTAL') || 0), today: day, online: Math.max(1, Object.keys(on).length) });
}
function logDay_(date, n) {
  try {
    const ss = getSS_();
    const sh = ss.getSheetByName('LuotTruyCap') || ss.insertSheet('LuotTruyCap');
    if (sh.getLastRow() === 0) sh.appendRow(['Ngày', 'Lượt truy cập']);
    sh.appendRow([date, n]);
  } catch (e) {}
}
function jsonOut_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

function doGet(e) {
  const p = (e && e.parameter) || {};
  if (p.action === 'feed' || p.action === 'del') {
    const cbf = String(p.cb || '').replace(/[^A-Za-z0-9_$.]/g, '').slice(0, 40);
    const out = (p.action === 'del' ? del_(p) : feed_(p)).getContent();
    if (cbf) return ContentService.createTextOutput(cbf + '(' + out + ');').setMimeType(ContentService.MimeType.JAVASCRIPT);
    return ContentService.createTextOutput(out).setMimeType(ContentService.MimeType.JSON);
  }
  if (p.action === 'hit') {
    const cb = String(p.cb || '').replace(/[^A-Za-z0-9_$.]/g, '').slice(0, 40);
    const body = hit_(p).getContent();
    if (cb) return ContentService.createTextOutput(cb + '(' + body + ');').setMimeType(ContentService.MimeType.JAVASCRIPT);
    return ContentService.createTextOutput(body).setMimeType(ContentService.MimeType.JSON);
  }
  return ContentService.createTextOutput('Elite Helpers form: OK');
}

function out_(ok, error) {
  const res = ok === false ? { ok: false, error: error || 'error' } : { ok: true };
  return ContentService.createTextOutput(JSON.stringify(res)).setMimeType(ContentService.MimeType.JSON);
}
