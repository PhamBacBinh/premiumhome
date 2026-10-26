/**
 * ELITE HELPERS (Giúp việc Elite) – Nhận form giupviecelite.vn về Google Sheets (bản 13)
 * Bản 13: CV chuyên nghiệp: quá trình làm việc theo từng giai đoạn (thời gian, vị trí, nơi làm, công việc gạch đầu dòng),
 *         kỹ năng/chứng chỉ dạng danh sách, nhận xét của Elite Helpers; CV Google Docs bố cục 2 cột theo nhận diện thương hiệu.
 *         Sửa lỗi tạo tab KhoUngVien khi trang tính chưa đủ cột.
 * Bản 12: KHO ỨNG VIÊN cho /quan-tri: tab KhoUngVien (phân luồng theo tỉnh/miền, vị trí, kinh nghiệm, trạng thái,
 *         lịch sử trao đổi), tự thêm hồ sơ ứng tuyển mới từ website, nhập lại hồ sơ cũ từ tab UngVien,
 *         tạo CV Google Docs trong thư mục Drive "Elite Helpers – CV ứng viên" (cần cấp quyền Docs/Drive 1 lần).
 * Bản 11: phân tích hành vi (chỉ khi khách đồng ý cookie): ghi sự kiện vào tab SuKien (xóa sau 12 tháng),
 *         tổng hợp số liệu cho tab Phân tích ở /quan-tri, gắn mã truy cập vào hồ sơ, báo khách cũ quay lại
 *         (tab QuayLai + email), lưu lựa chọn nhận tin chăm sóc. Không lưu địa chỉ IP.
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
      ['Loại nhà','house'],['Giờ liên hệ','contactTime'],['Mô tả','note'],['Nhận tin chăm sóc','optin'],['Mã truy cập web','visitor']]
  },
  ungvien: {
    sheet: 'UngVien',
    title: 'Hồ sơ ứng viên mới',
    cols: [['Họ tên','name'],['SĐT / Zalo','phone'],['Năm sinh','birthYear'],['Quê quán','hometown'],
      ['Nơi ở hiện tại','currentAddress'],['Vị trí','position'],['Hình thức','mode'],['Nấu ăn','cooking'],
      ['Kinh nghiệm','expYears'],['Ngoại ngữ','language'],['Chi tiết kinh nghiệm','experience'],
      ['Lương mong muốn','salary'],['Bắt đầu','start'],['Ghi chú','note'],['Mã truy cập web','visitor']]
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
    if (p.action === 'ev') return ev_(p);                    // sự kiện phân tích hành vi (đã đồng ý cookie)
    if (KHO_ACTIONS[p.action]) return KHO_ACTIONS[p.action](p); // Kho ứng viên (trang quản trị)
    if (p.website) return out_(true);                         // bẫy bot: giả vờ thành công
    if (!p.name || !p.phone) return out_(false, 'missing');   // thiếu thông tin bắt buộc
    const f = FORMS[p.formType] || FORMS.khach;
    const rc = checkRecaptcha_(p.recaptcha);
    const suspicious = rc !== 'ok' && rc !== 'off';

    const lock = LockService.getScriptLock();
    if (!lock.tryLock(10000)) return out_(false, 'busy');
    let vals, tNow;
    try {
      if (tooMany_()) return out_(false, 'rate');
      vals = f.cols.map(c => clean_(p[c[1]], c[1] === 'experience' || c[1] === 'note' ? 2000 : 300));
      const row = vals.map((v, i) => (f.cols[i][1] === 'phone' && v ? "'" + v : safeCell_(v)));
      const status = suspicious ? 'Nghi spam (' + rc + ')' : 'Mới';
      const sh = getSS_().getSheetByName(f.sheet);
      ensureHead_(sh, f);
      tNow = new Date();
      sh.appendRow([tNow, status].concat(row));
      if (!suspicious && p.visitor) rememberLead_(clean_(p.visitor, 24), clean_(p.name, 60), clean_(p.phone, 30), f.sheet);
    } finally {
      lock.releaseLock();
    }
    if (suspicious) return out_(true);                        // đã lưu để kiểm tra, không gửi email
    if (f === FORMS.ungvien) { try { khoFromForm_(p, tNow); } catch (err) { console.error(err); } } // tự thêm vào Kho ứng viên
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
  const ql = ss.getSheetByName('QuayLai');
  if (ql && ql.getLastRow() > 1) {
    const n = Math.min(20, ql.getLastRow() - 1);
    ql.getRange(ql.getLastRow() - n + 1, 1, n, 6).getValues().forEach(r => {
      items.push({ type: 'quaylai', time: isoOf_(r[0]), status: 'Mới', name: String(r[1]), phone: String(r[2]).replace(/^'/, ''), page: String(r[3]), src: String(r[4]), device: String(r[5]) });
    });
  }
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

// Thêm tiêu đề cho các cột mới (bản 11) nếu tab được tạo từ bản cũ
function ensureHead_(sh, f) {
  const need = 2 + f.cols.length;
  if (sh.getLastColumn() >= need && String(sh.getRange(1, need).getValue())) return;
  const head = ['Thời gian', 'Trạng thái'].concat(f.cols.map(c => c[0]));
  sh.getRange(1, 1, 1, need).setValues([head]).setFontWeight('bold').setBackground('#2A453E').setFontColor('#F4EEE3');
}
// Nhớ mã truy cập của khách đã để lại thông tin (tối đa 300 mã gần nhất) để nhận diện khi quay lại
function rememberLead_(vid, name, phone, sheet) {
  if (!/^[a-z0-9]{8,24}$/i.test(vid)) return;
  const props = PropertiesService.getScriptProperties();
  let m = {};
  try { m = JSON.parse(props.getProperty('LEAD_VIDS') || '{}'); } catch (e) {}
  m[vid] = { n: name, p: phone, s: sheet, t: Date.now() };
  const keys = Object.keys(m);
  if (keys.length > 300) keys.sort((a, b) => m[a].t - m[b].t).slice(0, keys.length - 300).forEach(k => delete m[k]);
  props.setProperty('LEAD_VIDS', JSON.stringify(m));
}

// ---- Phân tích hành vi: nhận sự kiện từ website ----
const EV_SHEET = 'SuKien';
const EV_HEAD = ['Thời gian', 'Mã khách', 'Phiên', 'Lượt xem', 'Loại', 'Trang', 'Tiêu đề', 'Hành động', 'Nhãn', 'Cuộn %', 'Giây',
  'Nguồn', 'Kênh', 'Chiến dịch', 'Trang vào', 'Thiết bị', 'Hệ điều hành', 'Trình duyệt', 'Màn hình', 'Ngôn ngữ', 'Múi giờ', 'Vào trang'];
const EV_KEEP_DAYS = 365;
function ev_(p) {
  let d;
  try { d = JSON.parse(String(p.d || '').slice(0, 20000)); } catch (e) { return out_(false, 'bad'); }
  const id = (x) => String(x || '').replace(/[^a-z0-9]/gi, '').slice(0, 24);
  const vid = id(d && d.v), sid = id(d && d.s);
  const evs = Array.isArray(d && d.e) ? d.e.slice(0, 40) : [];
  if (vid.length < 8 || sid.length < 8 || !evs.length) return out_(false, 'bad');
  const cache = CacheService.getScriptCache();
  const nS = Number(cache.get('evs_' + sid) || 0);
  const nAll = Number(cache.get('ev_all') || 0);
  if (nS > 400 || nAll > 6000) return out_(false, 'rate');   // chống spam
  cache.put('evs_' + sid, String(nS + evs.length), 3600);
  cache.put('ev_all', String(nAll + evs.length), 600);
  const u = d.u || {}, src = d.src || {};
  const s = (v, n) => safeCell_(clean_(v, n || 120));
  const now = Date.now();
  const rows = evs.map(e => {
    const ts = Number(e.ts);
    const t = new Date(Math.abs(ts - now) < 86400000 ? ts : now);
    const typ = ['pv', 'pe', 'ac'].indexOf(e.t) >= 0 ? e.t : 'ac';
    return [t, vid, sid, id(e.pv), typ, s(e.p, 160), s(e.ti, 100), s(e.n, 40), s(e.l, 60),
      Math.max(0, Math.min(100, Number(e.sc) || 0)) || '', Math.max(0, Math.min(1800, Number(e.sec) || 0)) || '',
      s(src.src, 60), s(src.med, 30), s(src.camp, 60), s(src.land, 160), s(u.dev, 20), s(u.os, 20), s(u.br, 20), s(u.scr, 12), s(u.lang, 10), s(u.tz, 40),
      e.t === 'pv' && Number(e.land) === 1 ? 1 : ''];
  });
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(8000)) return out_(false, 'busy');
  try {
    const ss = getSS_();
    let sh = ss.getSheetByName(EV_SHEET);
    if (!sh) {
      sh = ss.insertSheet(EV_SHEET);
      sh.getRange(1, 1, 1, EV_HEAD.length).setValues([EV_HEAD]).setFontWeight('bold').setBackground('#2A453E').setFontColor('#F4EEE3');
      sh.setFrozenRows(1);
    }
    sh.getRange(sh.getLastRow() + 1, 1, rows.length, EV_HEAD.length).setValues(rows);
    purgeEvents_(sh, cache);
  } finally {
    lock.releaseLock();
  }
  // Khách cũ (đã để lại thông tin) quay lại website: ghi tab QuayLai + email báo (mỗi khách tối đa 1 lần/6 giờ)
  try {
    const landing = rows.find(r => r[4] === 'pv' && r[21] === 1);
    if (landing && !cache.get('ret_' + vid)) {
      let m = {};
      try { m = JSON.parse(PropertiesService.getScriptProperties().getProperty('LEAD_VIDS') || '{}'); } catch (e) {}
      const L = m[vid];
      if (L && now - L.t > 600000) {                          // bỏ qua 10 phút ngay sau khi vừa gửi form
        cache.put('ret_' + vid, '1', 21600);
        const ss = getSS_();
        const sh = ss.getSheetByName('QuayLai') || ss.insertSheet('QuayLai');
        if (sh.getLastRow() === 0) sh.appendRow(['Thời gian', 'Họ tên', 'SĐT', 'Đang xem trang', 'Nguồn', 'Thiết bị', 'Mã khách', 'Tab hồ sơ']);
        sh.appendRow([new Date(), L.n, "'" + L.p, landing[5], landing[11], landing[15] + ' · ' + landing[17], vid, L.s]);
        MailApp.sendEmail(NOTIFY_EMAIL, '[Elite Helpers] Khách cũ quay lại website: ' + L.n,
          L.n + ' (' + L.p + ') vừa quay lại website.\nĐang xem: ' + landing[5] + '\nNguồn: ' + landing[11] + '\nThiết bị: ' + landing[15] + ' · ' + landing[17] +
          '\n\nGợi ý: liên hệ trong 30 phút tới khi khách còn đang quan tâm.');
      }
    }
  } catch (err) {}
  return out_(true);
}
// Mỗi ngày 1 lần: xóa sự kiện cũ hơn 12 tháng
function purgeEvents_(sh, cache) {
  const day = Utilities.formatDate(new Date(), TZ, 'yyyyMMdd');
  if (cache.get('evpurge') === day) return;
  cache.put('evpurge', day, 86400);
  const n = sh.getLastRow() - 1;
  if (n < 1) return;
  const limit = Date.now() - EV_KEEP_DAYS * 86400000;
  const col = sh.getRange(2, 1, n, 1).getValues();
  let k = 0;
  while (k < n && col[k][0] instanceof Date && col[k][0].getTime() < limit) k++;
  if (k > 0) sh.deleteRows(2, k);
}

// ---- Trang quản trị: tổng hợp số liệu phân tích ----
function stats_(p) {
  const er = auth_(p);
  if (er) return out_(false, er);
  const days = [1, 7, 30, 90].indexOf(Number(p.days)) >= 0 ? Number(p.days) : 7;
  const cache = CacheService.getScriptCache();
  const ck = 'stats_' + days;
  const hit = cache.get(ck);
  if (hit && p.fresh !== '1') return ContentService.createTextOutput(hit).setMimeType(ContentService.MimeType.JSON);
  const ss = getSS_();
  const sh = ss.getSheetByName(EV_SHEET);
  const startToday = new Date(Utilities.formatDate(new Date(), TZ, "yyyy-MM-dd'T'00:00:00XXX")).getTime();
  const from = startToday - (days - 1) * 86400000;
  const rows = sh && sh.getLastRow() > 1 ? sh.getRange(2, 1, sh.getLastRow() - 1, EV_HEAD.length).getValues() : [];
  let m = {};
  try { m = JSON.parse(PropertiesService.getScriptProperties().getProperty('LEAD_VIDS') || '{}'); } catch (e) {}
  const seenBefore = {}, S = {}, PV = {}, vids = {};
  const cnt = (o, k) => { k = String(k || '(không rõ)'); o[k] = (o[k] || 0) + 1; };
  rows.forEach(r => {
    const t = r[0] instanceof Date ? r[0].getTime() : 0;
    if (!t) return;
    if (t < from) { seenBefore[r[1]] = 1; return; }
    const sid = r[2], typ = r[4];
    vids[r[1]] = 1;
    const s = S[sid] || (S[sid] = { sid: sid, vid: r[1], start: t, end: t, src: r[11], med: r[12], camp: r[13], land: r[14], dev: r[15], os: r[16], br: r[17], pages: [], acts: [], pvs: 0, conv: 0 });
    if (t < s.start) s.start = t;
    if (t > s.end) s.end = t;
    if (typ === 'pv') {
      s.pvs++;
      s.pages.push({ p: r[5], t: t });
      PV[r[3]] = PV[r[3]] || { p: r[5], sid: sid, t: t, sc: 0, sec: 0 };
    } else if (typ === 'pe') {
      const v = PV[r[3]] || (PV[r[3]] = { p: r[5], sid: sid, t: t, sc: 0, sec: 0 });
      v.sc = Math.max(v.sc, Number(r[9]) || 0);
      v.sec = Math.max(v.sec, Number(r[10]) || 0);
    } else {
      s.acts.push({ n: r[7], l: r[8], p: r[5], t: t });
      if (r[7] === 'form_submit') s.conv = 1;
    }
  });
  const sessions = Object.keys(S).map(k => S[k]).filter(s => s.pvs > 0);
  const pages = {}, entries = {}, exits = {}, sources = {}, devs = {}, oss = {}, brs = {}, acts = {}, daily = {};
  let secSum = 0, secN = 0, bounce = 0, conv = 0, pvTotal = 0;
  Object.keys(PV).forEach(k => {
    const v = PV[k];
    const g = pages[v.p] || (pages[v.p] = { p: v.p, pv: 0, sec: 0, secN: 0, sc: 0, scN: 0 });
    g.pv++; pvTotal++;
    if (v.sec) { g.sec += v.sec; g.secN++; secSum += v.sec; secN++; }
    if (v.sc) { g.sc += v.sc; g.scN++; }
    const dk = Utilities.formatDate(new Date(v.t), TZ, 'dd/MM');
    const dd = daily[dk] || (daily[dk] = { d: dk, pv: 0, s: 0, ts: v.t });
    dd.pv++;
  });
  sessions.forEach(s => {
    s.pages.sort((a, b) => a.t - b.t);
    cnt(entries, s.pages[0].p);
    cnt(exits, s.pages[s.pages.length - 1].p);
    cnt(sources, s.src + (s.med && s.med !== 'direct' ? ' / ' + s.med : ''));
    cnt(devs, s.dev); cnt(oss, s.os); cnt(brs, s.br);
    s.acts.forEach(a => cnt(acts, a.n));
    if (s.pvs === 1 && !s.acts.some(a => /^(click_|form_|dialog_|copy_|nudge_click)/.test(a.n))) bounce++;
    if (s.conv) conv++;
    const dk = Utilities.formatDate(new Date(s.start), TZ, 'dd/MM');
    const dd = daily[dk] || (daily[dk] = { d: dk, pv: 0, s: 0, ts: s.start });
    dd.s++;
  });
  const top = (o, n) => Object.keys(o).map(k => ({ k: k, n: o[k] })).sort((a, b) => b.n - a.n).slice(0, n || 10);
  const vidList = Object.keys(vids);
  const res = {
    ok: true, days: days, updated: new Date().toISOString(),
    kpi: {
      visitors: vidList.length, returning: vidList.filter(v => seenBefore[v]).length, sessions: sessions.length, pageviews: pvTotal,
      pagesPerSession: sessions.length ? Math.round(pvTotal / sessions.length * 10) / 10 : 0,
      avgSec: secN ? Math.round(secSum / secN) : 0, bounce: sessions.length ? Math.round(bounce / sessions.length * 100) : 0,
      leads: conv, conv: sessions.length ? Math.round(conv / sessions.length * 1000) / 10 : 0
    },
    daily: Object.keys(daily).map(k => daily[k]).sort((a, b) => a.ts - b.ts).map(x => ({ d: x.d, pv: x.pv, s: x.s })),
    pages: Object.keys(pages).map(k => pages[k]).sort((a, b) => b.pv - a.pv).slice(0, 12)
      .map(g => ({ p: g.p, pv: g.pv, sec: g.secN ? Math.round(g.sec / g.secN) : 0, sc: g.scN ? Math.round(g.sc / g.scN) : 0 })),
    entries: top(entries), exits: top(exits), sources: top(sources), devices: top(devs, 5), os: top(oss, 6), browsers: top(brs, 8), actions: top(acts, 12),
    recent: sessions.sort((a, b) => b.start - a.start).slice(0, 30).map(s => ({
      start: new Date(s.start).toISOString(), sec: Math.round((s.end - s.start) / 1000), src: s.src, med: s.med, camp: s.camp,
      dev: s.dev, os: s.os, br: s.br, ret: seenBefore[s.vid] ? 1 : 0, lead: m[s.vid] ? m[s.vid].n : '',
      pages: s.pages.map(x => x.p).slice(0, 15), acts: s.acts.slice(0, 15).map(a => a.n + (a.l ? ':' + a.l : ''))
    }))
  };
  const out = JSON.stringify(res);
  if (out.length < 90000) cache.put(ck, out, 120);
  return ContentService.createTextOutput(out).setMimeType(ContentService.MimeType.JSON);
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
  if (p.action === 'feed' || p.action === 'del' || p.action === 'stats') {
    const cbf = String(p.cb || '').replace(/[^A-Za-z0-9_$.]/g, '').slice(0, 40);
    const out = (p.action === 'del' ? del_(p) : p.action === 'stats' ? stats_(p) : feed_(p)).getContent();
    if (cbf) return ContentService.createTextOutput(cbf + '(' + out + ');').setMimeType(ContentService.MimeType.JAVASCRIPT);
    return ContentService.createTextOutput(out).setMimeType(ContentService.MimeType.JSON);
  }
  if (KHO_ACTIONS[p.action]) {
    const cbk = String(p.cb || '').replace(/[^A-Za-z0-9_$.]/g, '').slice(0, 40);
    const outk = KHO_ACTIONS[p.action](p).getContent();
    if (cbk) return ContentService.createTextOutput(cbk + '(' + outk + ');').setMimeType(ContentService.MimeType.JAVASCRIPT);
    return ContentService.createTextOutput(outk).setMimeType(ContentService.MimeType.JSON);
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


// =====================================================================================
// ---- KHO ỨNG VIÊN (bản 12) ----
// Tab KhoUngVien: mỗi dòng 1 ứng viên đã chuẩn hóa để phân luồng. Có thể lọc/sửa trực tiếp trong Sheets,
// nhưng giữ nguyên cột "Mã" và "Lịch sử trao đổi" (dạng JSON).
// =====================================================================================
const KHO = 'KhoUngVien';
const KHO_COLS = [['ma','Mã'],['ngayNhan','Ngày nhận'],['capNhat','Cập nhật'],['trangThai','Trạng thái'],['hoTen','Họ tên'],
  ['sdt','SĐT / Zalo'],['namSinh','Năm sinh'],['gioiTinh','Giới tính'],['que','Quê quán'],['noiO','Tỉnh/thành đang ở'],
  ['noiOChiTiet','Địa chỉ chi tiết'],['khuVuc','Khu vực nhận việc'],['mien','Miền'],['viTri','Vị trí'],['hinhThuc','Hình thức'],
  ['kinhNghiemNam','Số năm KN'],['nhomKN','Nhóm KN'],['chungChi','Chứng chỉ / đào tạo'],['luong','Lương mong muốn'],
  ['ngayBatDau','Có thể bắt đầu'],['kinhNghiemMoTa','Quá trình làm việc'],['kyNang','Kỹ năng nổi bật'],['ngoaiNgu','Ngoại ngữ'],
  ['nauAn','Nấu ăn'],['nguon','Nguồn'],['ghiChu','Ghi chú nội bộ'],['lichSu','Lịch sử trao đổi'],['webTs','Mã hồ sơ web'],
  ['quaTrinh','Quá trình làm việc (chi tiết)'],['nhanXet','Nhận xét Elite Helpers']];
const KHO_LIST = { khuVuc: 1, viTri: 1 };
const KHO_LONG = { kinhNghiemMoTa: 3000, ghiChu: 2000, lichSu: 40000, kyNang: 1500, chungChi: 800, nhanXet: 1500, quaTrinh: 30000 };
const KHO_JSON = { lichSu: 1, quaTrinh: 1 };
const KHO_STATUS = ['Mới nhận','Đã liên hệ','Sẵn sàng giới thiệu','Đã gửi CV cho khách','Đang làm thử','Đã nhận việc','Lưu kho – chờ job phù hợp','Tạm dừng'];
const REGIONS = {
  'Miền Bắc': ['Hà Nội','Hải Phòng','Quảng Ninh','Bắc Ninh','Hưng Yên','Ninh Bình','Phú Thọ','Thái Nguyên','Tuyên Quang','Lào Cai','Lạng Sơn','Cao Bằng','Điện Biên','Lai Châu','Sơn La'],
  'Miền Trung': ['Thanh Hóa','Nghệ An','Hà Tĩnh','Quảng Trị','Huế','Đà Nẵng','Quảng Ngãi','Gia Lai','Khánh Hòa','Đắk Lắk','Lâm Đồng'],
  'Miền Nam': ['TP. Hồ Chí Minh','Đồng Nai','Tây Ninh','Cần Thơ','Vĩnh Long','Đồng Tháp','Cà Mau','An Giang']
};
// Tên tỉnh cũ (trước sáp nhập 7/2025) và cách viết tắt → tỉnh/thành hiện tại
const PROV_ALIAS = {
  'ho chi minh':'TP. Hồ Chí Minh','hcm':'TP. Hồ Chí Minh','sai gon':'TP. Hồ Chí Minh','binh duong':'TP. Hồ Chí Minh','vung tau':'TP. Hồ Chí Minh','ba ria':'TP. Hồ Chí Minh',
  'hanoi':'Hà Nội','hn':'Hà Nội','bac giang':'Bắc Ninh','hai duong':'Hải Phòng','thai binh':'Hưng Yên','nam dinh':'Ninh Bình','ha nam':'Ninh Bình',
  'vinh phuc':'Phú Thọ','hoa binh':'Phú Thọ','bac kan':'Thái Nguyên','ha giang':'Tuyên Quang','yen bai':'Lào Cai','quang binh':'Quảng Trị',
  'thua thien':'Huế','quang nam':'Đà Nẵng','kon tum':'Quảng Ngãi','binh dinh':'Gia Lai','ninh thuan':'Khánh Hòa','phu yen':'Đắk Lắk',
  'dak nong':'Lâm Đồng','binh thuan':'Lâm Đồng','binh phuoc':'Đồng Nai','bien hoa':'Đồng Nai','long an':'Tây Ninh','soc trang':'Cần Thơ','hau giang':'Cần Thơ',
  'ben tre':'Vĩnh Long','tra vinh':'Vĩnh Long','tien giang':'Đồng Tháp','bac lieu':'Cà Mau','kien giang':'An Giang'
};
const norm_ = (s) => String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
function provinceOf_(text) {
  const t = ' ' + norm_(text) + ' ';
  if (t.trim() === '') return '';
  const all = [].concat(REGIONS['Miền Bắc'], REGIONS['Miền Trung'], REGIONS['Miền Nam']);
  for (let i = 0; i < all.length; i++) { const n = norm_(all[i]).replace(/^tp /, ''); if (t.indexOf(' ' + n + ' ') >= 0) return all[i]; }
  const keys = Object.keys(PROV_ALIAS);
  for (let i = 0; i < keys.length; i++) { if (t.indexOf(' ' + keys[i] + ' ') >= 0) return PROV_ALIAS[keys[i]]; }
  return '';
}
const regionOf_ = (p) => Object.keys(REGIONS).filter(r => REGIONS[r].indexOf(p) >= 0)[0] || '';
function expBand_(n) {
  if (n === '' || n == null || isNaN(Number(n))) return '';
  n = Number(n);
  return n < 1 ? 'Dưới 1 năm' : n < 3 ? '1–3 năm' : n < 5 ? '3–5 năm' : n < 10 ? '5–10 năm' : 'Trên 10 năm';
}
function expYearsOf_(s) {
  s = String(s || '');
  if (/chưa/i.test(s)) return 0;
  if (/dưới\s*1/i.test(s)) return 0.5;
  const m = s.match(/\d+(?:[.,]\d+)?/);
  return m ? Number(m[0].replace(',', '.')) : '';
}
function positionsOf_(s) {
  s = norm_(s); const out = [];
  if (/giup viec/.test(s)) out.push('Giúp việc gia đình');
  if (/bao mau|cham be|tre/.test(s)) out.push('Bảo mẫu / chăm bé');
  if (/nguoi gia|nguoi cao tuoi/.test(s)) out.push('Chăm sóc người già');
  if (/quan gia/.test(s)) out.push('Quản gia');
  if (/dau bep|nau an/.test(s)) out.push('Đầu bếp gia đình');
  return out;
}
function modeOf_(s) { s = norm_(s); return /ca hai/.test(s) ? 'Cả hai' : /o lai/.test(s) ? 'Ở lại' : /theo gio|di ve|theo ca/.test(s) ? 'Theo giờ / đi về' : ''; }
function dateText_(v) {
  if (v instanceof Date) return Utilities.formatDate(v, TZ, 'dd/MM/yyyy');
  const d = new Date(v);
  if (/GMT|^\d{4}-\d{2}-\d{2}/.test(String(v)) && !isNaN(d)) return Utilities.formatDate(d, TZ, 'dd/MM/yyyy');
  return String(v || '');
}

function khoSheet_() {
  const ss = getSS_();
  let sh = ss.getSheetByName(KHO);
  const isNew = !sh;
  if (isNew) sh = ss.insertSheet(KHO);
  if (sh.getMaxColumns() < KHO_COLS.length) sh.insertColumnsAfter(sh.getMaxColumns(), KHO_COLS.length - sh.getMaxColumns());
  if (isNew || String(sh.getRange(1, KHO_COLS.length).getValue()) !== KHO_COLS[KHO_COLS.length - 1][1]) {
    sh.getRange(1, 1, 1, KHO_COLS.length).setValues([KHO_COLS.map(c => c[1])]).setFontWeight('bold').setBackground('#2A453E').setFontColor('#F4EEE3');
  }
  if (isNew) { sh.setFrozenRows(1); sh.setFrozenColumns(5); }
  return sh;
}
function khoRows_(sh) {
  const n = sh.getLastRow() - 1;
  if (n < 1) return [];
  return sh.getRange(2, 1, n, KHO_COLS.length).getValues().map((r, i) => {
    const o = { _row: i + 2 };
    KHO_COLS.forEach((c, j) => {
      let v = r[j];
      if (v instanceof Date) v = c[0] === 'ngayNhan' || c[0] === 'capNhat' || c[0] === 'webTs' ? v.toISOString() : dateText_(v);
      v = String(v == null ? '' : v).replace(/^'/, '');
      if (KHO_LIST[c[0]]) v = v ? v.split(/\s*;\s*/).filter(Boolean) : [];
      else if (c[0] === 'lichSu') { try { v = v ? JSON.parse(v) : []; } catch (e) { v = [{ t: '', st: '', n: v }]; } }
      else if (c[0] === 'quaTrinh') { try { v = v ? JSON.parse(v) : []; } catch (e) { v = []; } if (!Array.isArray(v)) v = []; }
      else if (c[0] === 'kinhNghiemNam') v = v === '' ? null : Number(v);
      o[c[0]] = v;
    });
    return o;
  });
}
// Chuẩn hóa 1 hồ sơ thành 1 dòng Sheets
function khoRow_(o) {
  o.khuVuc = (Array.isArray(o.khuVuc) ? o.khuVuc : []).map(x => clean_(x, 40)).filter(Boolean).slice(0, 40);
  o.viTri = (Array.isArray(o.viTri) ? o.viTri : []).map(x => clean_(x, 40)).filter(Boolean).slice(0, 10);
  o.mien = o.khuVuc.map(regionOf_).filter((x, i, a) => x && a.indexOf(x) === i).join('; ');
  o.kinhNghiemNam = o.kinhNghiemNam === '' || o.kinhNghiemNam == null || isNaN(Number(o.kinhNghiemNam)) ? '' : Math.max(0, Math.min(60, Number(o.kinhNghiemNam)));
  o.nhomKN = expBand_(o.kinhNghiemNam);
  if (KHO_STATUS.indexOf(o.trangThai) < 0) o.trangThai = 'Mới nhận';
  o.lichSu = JSON.stringify((Array.isArray(o.lichSu) ? o.lichSu : []).slice(-100).map(h => ({ t: clean_(h.t, 40), st: clean_(h.st, 60), n: clean_(h.n, 1000) })));
  o.quaTrinh = JSON.stringify((Array.isArray(o.quaTrinh) ? o.quaTrinh : []).slice(0, 15).map(q => ({
    tu: clean_(q && q.tu, 20), den: clean_(q && q.den, 20), viTri: clean_(q && q.viTri, 120), noiLam: clean_(q && q.noiLam, 200), hinhThuc: clean_(q && q.hinhThuc, 40),
    congViec: (Array.isArray(q && q.congViec) ? q.congViec : []).map(x => clean_(x, 300)).filter(Boolean).slice(0, 12)
  })).filter(q => q.tu || q.viTri || q.noiLam || q.congViec.length));
  return KHO_COLS.map(c => {
    const k = c[0];
    let v = o[k];
    if (KHO_LIST[k]) return v.join('; ');
    if (k === 'kinhNghiemNam') return v;
    if (k === 'ngayNhan' || k === 'capNhat') { const d = new Date(v); return isNaN(d) ? new Date() : d; }
    v = clean_(v, KHO_LONG[k] || 300);
    if (KHO_JSON[k]) return v;
    return (k === 'sdt' || k === 'webTs' || k === 'ma') && v ? "'" + v : safeCell_(v);
  });
}
function khoNextCode_() {
  const props = PropertiesService.getScriptProperties();
  const seq = Number(props.getProperty('KHO_SEQ') || 0) + 1;
  props.setProperty('KHO_SEQ', String(seq));
  return 'UV' + Utilities.formatDate(new Date(), TZ, 'yyMM') + '-' + ('000' + seq).slice(-4);
}
// Hồ sơ từ form website → dữ liệu kho
function khoFromWeb_(x, time) {
  const now = new Date().toISOString();
  return {
    ngayNhan: time, capNhat: now, trangThai: 'Mới nhận', hoTen: x.name, sdt: String(x.phone || '').replace(/^'/, ''), namSinh: x.birthYear,
    gioiTinh: '', que: x.hometown, noiO: provinceOf_(x.currentAddress), noiOChiTiet: x.currentAddress, khuVuc: [],
    viTri: positionsOf_(x.position), hinhThuc: modeOf_(x.mode), kinhNghiemNam: expYearsOf_(x.expYears), chungChi: '',
    luong: x.salary, ngayBatDau: dateText_(x.start), kinhNghiemMoTa: x.experience, kyNang: '', ngoaiNgu: x.language, nauAn: x.cooking,
    nguon: 'Website', ghiChu: String(x.note || '').replace(/\s*\[Đồng ý[^\]]*\]\s*/g, ' ').trim(),
    lichSu: [{ t: now, st: 'Mới nhận', n: 'Ứng tuyển qua form website (' + clean_(x.position, 120) + ')' }],
    webTs: time
  };
}
function khoFromForm_(p, time) {
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(10000)) return;
  try {
    const o = khoFromWeb_(p, time.toISOString());
    o.ma = khoNextCode_();
    khoSheet_().appendRow(khoRow_(o));
  } finally { lock.releaseLock(); }
}
function khoPayload_(p) {
  try { return JSON.parse(String(p.d || '').slice(0, 60000)); } catch (e) { return null; }
}

const KHO_ACTIONS = {
  // Danh sách toàn bộ kho
  kho_list: function (p) {
    const er = auth_(p); if (er) return out_(false, er);
    const sh = khoSheet_();
    return jsonOut_({ ok: true, items: khoRows_(sh), sheetUrl: getSS_().getUrl() + '#gid=' + sh.getSheetId() });
  },
  // Thêm mới hoặc cập nhật 1 hồ sơ (theo Mã)
  kho_save: function (p) {
    const er = auth_(p); if (er) return out_(false, er);
    const d = khoPayload_(p);
    if (!d) return out_(false, 'missing');
    const lock = LockService.getScriptLock();
    if (!lock.tryLock(10000)) return out_(false, 'busy');
    try {
      const sh = khoSheet_();
      const rows = khoRows_(sh);
      const old = d.ma ? rows.filter(r => r.ma === d.ma)[0] : null;
      if (d.ma && !old) return out_(false, 'notfound');
      if (old && d.base && old.capNhat && d.base !== old.capNhat) return out_(false, 'conflict'); // có người sửa trước
      const o = Object.assign({}, old || {}, d);
      if (!clean_(o.hoTen) || !clean_(o.sdt)) return out_(false, 'missing');
      o.capNhat = new Date().toISOString();
      if (!old) { o.ma = khoNextCode_(); o.ngayNhan = o.ngayNhan || o.capNhat; o.nguon = o.nguon || 'Nhập tay'; }
      const row = khoRow_(o);
      if (old) sh.getRange(old._row, 1, 1, KHO_COLS.length).setValues([row]);
      else sh.appendRow(row);
      const saved = khoRows_(sh).filter(r => r.ma === o.ma)[0];
      return jsonOut_({ ok: true, item: saved });
    } finally { lock.releaseLock(); }
  },
  // Xóa 1 hồ sơ khỏi kho (bản sao vào ThungRac 30 ngày)
  kho_del: function (p) {
    const er = auth_(p); if (er) return out_(false, er);
    const lock = LockService.getScriptLock();
    if (!lock.tryLock(10000)) return out_(false, 'busy');
    try {
      const sh = khoSheet_();
      const r = khoRows_(sh).filter(x => x.ma === String(p.ma || ''))[0];
      if (!r) return out_(false, 'notfound');
      const ss = getSS_();
      const tr = ss.getSheetByName(TRASH) || ss.insertSheet(TRASH);
      if (tr.getLastRow() === 0) tr.appendRow(['Thời gian xóa', 'Loại', 'Thời gian gửi', 'Trạng thái', 'Dữ liệu (các cột theo tab gốc)']);
      const vals = sh.getRange(r._row, 1, 1, KHO_COLS.length).getValues()[0];
      tr.appendRow([new Date(), KHO].concat(vals.map(v => (typeof v === 'string' ? (/^[0-9+]/.test(v) ? "'" + v : safeCell_(v)) : v))));
      sh.deleteRow(r._row);
      purgeTrash_(tr);
      return out_(true);
    } finally { lock.releaseLock(); }
  },
  // Đưa các hồ sơ ứng tuyển cũ (tab UngVien) chưa có trong kho vào kho
  kho_import: function (p) {
    const er = auth_(p); if (er) return out_(false, er);
    const lock = LockService.getScriptLock();
    if (!lock.tryLock(15000)) return out_(false, 'busy');
    try {
      const ss = getSS_(), f = FORMS.ungvien, src = ss.getSheetByName(f.sheet), sh = khoSheet_();
      if (!src || src.getLastRow() < 2) return jsonOut_({ ok: true, added: 0 });
      const have = {}, phones = {};
      khoRows_(sh).forEach(r => { if (r.webTs) have[String(r.webTs).slice(0, 19)] = 1; if (r.sdt) phones[String(r.sdt).replace(/\D/g, '')] = 1; });
      const rows = src.getRange(2, 1, src.getLastRow() - 1, 2 + f.cols.length).getValues();
      const out = [];
      rows.forEach(r => {
        const ts = isoOf_(r[0]);
        if (have[ts.slice(0, 19)] || String(r[1]).indexOf('Nghi spam') === 0) return;
        const x = {};
        f.cols.forEach((c, j) => { x[c[1]] = r[2 + j] instanceof Date ? r[2 + j] : String(r[2 + j]).replace(/^'/, ''); });
        if (phones[String(x.phone).replace(/\D/g, '')]) return;     // SĐT đã có trong kho (đã nhập tay)
        const o = khoFromWeb_(x, ts);
        o.ma = khoNextCode_();
        out.push(khoRow_(o));
        phones[String(x.phone).replace(/\D/g, '')] = 1;
      });
      if (out.length) sh.getRange(sh.getLastRow() + 1, 1, out.length, KHO_COLS.length).setValues(out);
      return jsonOut_({ ok: true, added: out.length });
    } finally { lock.releaseLock(); }
  },
  // Tạo CV Google Docs (bố cục 2 cột theo nhận diện Elite Helpers) trong thư mục Drive "Elite Helpers – CV ứng viên"
  kho_cv: function (p) {
    const er = auth_(p); if (er) return out_(false, er);
    const r = khoRows_(khoSheet_()).filter(x => x.ma === String(p.ma || ''))[0];
    if (!r) return out_(false, 'notfound');
    const hide = String(p.hide) !== '0';
    const props = PropertiesService.getScriptProperties();
    let folder = null;
    try { folder = DriveApp.getFolderById(props.getProperty('CV_FOLDER_ID')); } catch (e) {}
    if (!folder) { folder = DriveApp.createFolder('Elite Helpers – CV ứng viên'); props.setProperty('CV_FOLDER_ID', folder.getId()); }
    const doc = buildCvDoc_(r, hide);
    DriveApp.getFileById(doc.getId()).moveTo(folder);
    return jsonOut_({ ok: true, url: doc.getUrl(), pdf: 'https://docs.google.com/document/d/' + doc.getId() + '/export?format=pdf', folder: folder.getUrl() });
  }
};
function shortName_(n) {
  const p = String(n || '').trim().split(/\s+/);
  return p.length > 1 ? p.slice(0, -1).map(w => w.charAt(0) + '.').join(' ') + ' ' + p[p.length - 1] : String(n || '');
}
// Chạy hàm này 1 lần trong trình soạn Apps Script để cấp quyền Google Docs/Drive cho chức năng tạo CV
function capQuyenCV() {
  Logger.log('Thư mục gốc Drive: ' + DriveApp.getRootFolder().getName() + ' · Docs: ' + typeof DocumentApp.create);
  Logger.log('Đã cấp quyền. Kho ứng viên: ' + getSS_().getUrl());
}


// ---- CV Google Docs (bản 13) ----
const CV = { G: '#1F342E', G2: '#2A453E', GOLD: '#A9792A', GOLDL: '#CBAB6D', CREAM: '#F4EEE3', PAPER: '#FBF8F2', INK: '#1C2925', SOFT: '#5A6A64', LINE: '#E4DCCB',
  SERIF: 'Cormorant Garamond', SANS: 'Be Vietnam Pro', LOGO: 'https://giupviecelite.vn/cv-logo.png' };
function cvLines_(s) { return String(s || '').split(/\r?\n|;\s*/).map(x => x.replace(/^\s*[-•*+·]\s*/, '').trim()).filter(Boolean); }
function cvModel_(r, hide) {
  const age = r.namSinh && !isNaN(Number(r.namSinh)) ? new Date().getFullYear() - Number(r.namSinh) : '';
  const kn = r.kinhNghiemNam !== '' && r.kinhNghiemNam != null && !isNaN(Number(r.kinhNghiemNam)) ? Number(r.kinhNghiemNam) : null;
  let qt = Array.isArray(r.quaTrinh) ? r.quaTrinh : [];
  if (!qt.length && r.kinhNghiemMoTa) qt = [{ tu: '', den: '', viTri: 'Kinh nghiệm làm việc', noiLam: '', hinhThuc: '', congViec: cvLines_(r.kinhNghiemMoTa) }];
  return {
    name: hide ? shortName_(r.hoTen) : r.hoTen, ma: r.ma, date: Utilities.formatDate(new Date(), TZ, 'dd/MM/yyyy'),
    role: (r.viTri || []).join(' · ') || 'Người hỗ trợ gia đình',
    facts: [[age ? String(age) : '—', 'tuổi'], [kn === null ? '—' : (kn >= 10 ? '10+' : String(kn)), 'năm kinh nghiệm'], [r.hinhThuc || '—', 'hình thức'], [r.que || '—', 'quê quán']],
    info: [['Năm sinh', r.namSinh], ['Giới tính', r.gioiTinh], ['Quê quán', r.que], ['Nơi ở hiện tại', r.noiO]].concat(hide ? [] : [['Điện thoại', r.sdt]]).filter(x => x[1]),
    wish: [['Vị trí', (r.viTri || []).join(', ')], ['Hình thức', r.hinhThuc], ['Khu vực', (r.khuVuc || []).join(', ')], ['Mức lương', r.luong], ['Bắt đầu', r.ngayBatDau]].filter(x => x[1]),
    certs: cvLines_(r.chungChi), langs: cvLines_(r.ngoaiNgu), skills: cvLines_(r.kyNang), cook: r.nauAn, note: r.nhanXet, qt: qt
  };
}
function buildCvDoc_(r, hide) {
  const M = cvModel_(r, hide);
  const doc = DocumentApp.create('CV ' + r.ma + ' – ' + M.name + ' – Elite Helpers');
  const b = doc.getBody();
  b.setPageWidth(595.3).setPageHeight(841.9).setMarginTop(28).setMarginBottom(28).setMarginLeft(34).setMarginRight(34);
  const st = (el, o) => { const t = el.editAsText ? el.editAsText() : el; if (o.f) t.setFontFamily(o.f); if (o.s) t.setFontSize(o.s); if (o.c) t.setForegroundColor(o.c); t.setBold(!!o.b); t.setItalic(!!o.i); return el; };
  const para = (host, text, o, sp) => { const p = host.appendParagraph(String(text)); st(p, Object.assign({ f: CV.SANS, s: 9.5, c: CV.INK }, o)); p.setSpacingBefore(sp ? sp[0] : 0).setSpacingAfter(sp ? sp[1] : 2).setLineSpacing(1.15); return p; };
  const bullet = (host, text, o) => { const li = host.appendListItem(String(text)); li.setGlyphType(DocumentApp.GlyphType.BULLET); st(li, Object.assign({ f: CV.SANS, s: 9.5, c: CV.INK }, o)); li.setSpacingBefore(0).setSpacingAfter(1.5).setLineSpacing(1.15).setIndentStart(14).setIndentFirstLine(4); return li; };
  const heading = (host, text, first) => { const p = para(host, text.toUpperCase(), { s: 8.5, c: CV.GOLD, b: true }, [first ? 2 : 12, 4]); p.editAsText().setFontFamily(CV.SANS); return p; };
  const noBorder = (t) => { t.setBorderWidth(0); return t; };
  const pad = (cell, t, rgt, btm, l) => cell.setPaddingTop(t).setPaddingRight(rgt).setPaddingBottom(btm).setPaddingLeft(l);
  const clearFirst = (cell) => { const p = cell.getChild(0); if (p && p.getType() === DocumentApp.ElementType.PARAGRAPH && cell.getNumChildren() > 1) p.removeFromParent(); };

  // 1. Dải đầu trang: logo · thương hiệu · tiêu đề hồ sơ
  b.getParagraphs()[0].setText('').setSpacingAfter(0);
  const hd = noBorder(b.insertTable(0, [['', '', '']]));
  hd.setColumnWidth(0, 50).setColumnWidth(1, 300);
  const c0 = hd.getCell(0, 0), c1 = hd.getCell(0, 1), c2 = hd.getCell(0, 2);
  [c0, c1, c2].forEach(c => { c.setBackgroundColor(CV.G); c.setVerticalAlignment(DocumentApp.VerticalAlignment.CENTER); });
  pad(c0, 10, 4, 10, 14); pad(c1, 12, 6, 12, 6); pad(c2, 12, 16, 12, 6);
  try { const img = c0.getChild(0).asParagraph().appendInlineImage(UrlFetchApp.fetch(CV.LOGO).getBlob()); const w = 34; img.setHeight(Math.round(w * 260 / 220)).setWidth(w); }
  catch (e) { st(c0.getChild(0).asParagraph().setText('EH'), { f: CV.SERIF, s: 18, c: CV.GOLDL, b: true }); }
  st(c1.getChild(0).asParagraph().setText('ELITE HELPERS'), { f: CV.SERIF, s: 17, c: CV.CREAM, b: true });
  c1.getChild(0).asParagraph().setSpacingAfter(1);
  para(c1, 'Người hỗ trợ gia đình cao cấp tại Hà Nội', { s: 8, c: CV.GOLDL }, [0, 0]);
  const t2 = c2.getChild(0).asParagraph().setText('HỒ SƠ ỨNG VIÊN').setAlignment(DocumentApp.HorizontalAlignment.RIGHT);
  st(t2, { f: CV.SANS, s: 9, c: CV.CREAM, b: true }); t2.setSpacingAfter(1);
  para(c2, 'Mã ' + M.ma + ' · ' + M.date, { s: 8, c: CV.GOLDL }, [0, 0]).setAlignment(DocumentApp.HorizontalAlignment.RIGHT);

  // 2. Họ tên, vị trí, dữ kiện nhanh
  const nm = para(b, M.name, { f: CV.SERIF, s: 26, c: CV.G, b: true }, [14, 0]); nm.setLineSpacing(1);
  para(b, M.role, { s: 10, c: CV.GOLD, b: true }, [2, 8]);
  const ft = noBorder(b.appendTable([M.facts.map(() => '')]));
  M.facts.forEach((f, i) => {
    const c = ft.getCell(0, i); c.setBackgroundColor(CV.CREAM); pad(c, 7, 8, 7, 10);
    st(c.getChild(0).asParagraph().setText(f[0]), { f: CV.SERIF, s: 15, c: CV.G, b: true }); c.getChild(0).asParagraph().setSpacingAfter(0).setLineSpacing(1);
    para(c, f[1], { s: 7.5, c: CV.SOFT }, [0, 0]);
  });
  para(b, '', { s: 4 }, [0, 0]);

  // 3. Thân CV: cột trái (thông tin) · cột phải (nhận xét, quá trình làm việc)
  const bd = noBorder(b.appendTable([['', '']]));
  bd.setColumnWidth(0, 178);
  const L = bd.getCell(0, 0), R = bd.getCell(0, 1);
  L.setBackgroundColor(CV.PAPER); pad(L, 10, 12, 12, 12); pad(R, 8, 4, 12, 16);
  L.setVerticalAlignment(DocumentApp.VerticalAlignment.TOP); R.setVerticalAlignment(DocumentApp.VerticalAlignment.TOP);
  const kv = (host, rows) => rows.forEach(x => { para(host, x[0], { s: 7.5, c: CV.SOFT }, [3, 0]); para(host, x[1], { s: 9.5, c: CV.INK, b: true }, [0, 2]); });
  let first = true;
  const lsec = (title, fn) => { heading(L, title, first); first = false; fn(); };
  lsec('Thông tin cá nhân', () => kv(L, M.info));
  if (M.wish.length) lsec('Nguyện vọng công việc', () => kv(L, M.wish));
  if (M.skills.length) lsec('Kỹ năng nổi bật', () => M.skills.forEach(x => bullet(L, x)));
  lsec('Chứng chỉ & đào tạo', () => (M.certs.length ? M.certs : ['Chưa có chứng chỉ, sẵn sàng tham gia đào tạo']).forEach(x => bullet(L, x)));
  if (M.langs.length) lsec('Ngoại ngữ', () => M.langs.forEach(x => bullet(L, x)));
  if (M.cook) lsec('Nấu ăn', () => para(L, M.cook));
  clearFirst(L);

  let rf = true;
  if (M.note) {
    heading(R, 'Nhận xét của Elite Helpers', rf); rf = false;
    const nt = noBorder(R.appendTable([['']])); const nc = nt.getCell(0, 0);
    nc.setBackgroundColor(CV.CREAM); pad(nc, 8, 10, 8, 12);
    st(nc.getChild(0).asParagraph().setText(M.note), { f: CV.SANS, s: 9.5, c: CV.INK, i: true }); nc.getChild(0).asParagraph().setLineSpacing(1.2);
  }
  heading(R, 'Quá trình làm việc', rf);
  if (!M.qt.length) para(R, 'Đang cập nhật.', { c: CV.SOFT, i: true });
  M.qt.forEach((q, i) => {
    const per = [q.tu, q.den || (q.tu ? 'nay' : '')].filter(Boolean).join(' – ');
    if (per) para(R, per, { s: 8.5, c: CV.GOLD, b: true }, [i ? 9 : 2, 0]);
    para(R, q.viTri || 'Người hỗ trợ gia đình', { s: 10.5, c: CV.G, b: true }, [per ? 0 : (i ? 9 : 2), 0]);
    const sub = [q.noiLam, q.hinhThuc].filter(Boolean).join(' · ');
    if (sub) para(R, sub, { s: 8.5, c: CV.SOFT }, [0, 2]);
    (q.congViec || []).forEach(x => bullet(R, x));
  });
  clearFirst(R);

  // 4. Chân trang: cam kết + liên hệ
  para(b, '', { s: 4 }, [4, 0]);
  const fo = noBorder(b.appendTable([['']])); const fc = fo.getCell(0, 0);
  fc.setBackgroundColor(CV.G); pad(fc, 8, 14, 8, 14);
  st(fc.getChild(0).asParagraph().setText('Xác minh lý lịch  ·  Phỏng vấn trực tiếp  ·  Làm thử trước khi gia đình quyết định'), { f: CV.SANS, s: 8.5, c: CV.GOLDL, b: true });
  fc.getChild(0).asParagraph().setAlignment(DocumentApp.HorizontalAlignment.CENTER).setSpacingAfter(1);
  para(fc, 'giupviecelite.vn  ·  lienhe@giupviecelite.vn  ·  Zalo 0948 919 598', { s: 8, c: CV.CREAM }, [0, 0]).setAlignment(DocumentApp.HorizontalAlignment.CENTER);
  // Bỏ đoạn trống thừa cuối tài liệu (Docs bắt buộc giữ 1 đoạn cuối: thu nhỏ)
  const lastP = b.getChild(b.getNumChildren() - 1);
  if (lastP.getType() === DocumentApp.ElementType.PARAGRAPH) st(lastP.asParagraph().setSpacingBefore(0).setSpacingAfter(0), { s: 2 });
  doc.saveAndClose();
  return doc;
}
