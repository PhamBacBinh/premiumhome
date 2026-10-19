/*!
 * Elite Helpers (Giúp việc Elite) - website giupviecelite.vn
 * Không phụ thuộc thư viện ngoài. Toàn bộ nội dung nằm sẵn trong HTML (tốt cho SEO),
 * JavaScript chỉ bổ sung: điều hướng dạng SPA (hash route cho form, chính sách),
 * hiệu ứng khi cuộn, form nhiều bước có kiểm tra dữ liệu.
 */
(() => {
  'use strict';

  /* ------------------------------------------------------------------
   * Cấu hình
   * FORM_ENDPOINT: Apps Script web app nhận form (POST) và bộ đếm (GET/JSONP).
   * ------------------------------------------------------------------ */
  const CONFIG = {
    FORM_ENDPOINT: 'https://script.google.com/macros/s/AKfycbzEBi_npUbpXLAc65JOQC6HDY93vThbXBSna6h5JuJ0wc4vM5vQQPDT7W5FtaNEFC8ojw/exec',
    PHONE: '0948919598',
    ZALO_URL: 'https://zalo.me/0948919598',
    CONSENT_VERSION: '19/10/2026',
    // Google reCAPTCHA v3 (vô hình). Dán Site key vào đây; để trống = tắt.
    RECAPTCHA_SITE_KEY: '6Lf_LOstAAAAAAW7U-XMW4TKlpRWiiezMTTwXEAD',
    // Google Analytics 4: dán Measurement ID dạng 'G-XXXXXXXXXX'; để trống = tắt.
    GA4_ID: 'G-JKX25NDPHK',
  };

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const root = document.documentElement;
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const smooth = reduceMotion ? 'auto' : 'smooth';

  /* ---------------- Lưu trữ trên trình duyệt (an toàn khi bị chặn) ---------------- */
  const store = {
    get(k, s) { try { return (s ? sessionStorage : localStorage).getItem(k); } catch (e) { return null; } },
    set(k, v, s) { try { (s ? sessionStorage : localStorage).setItem(k, v); } catch (e) {} },
    del(k, s) { try { (s ? sessionStorage : localStorage).removeItem(k); } catch (e) {} },
  };
  const rid = (n) => Math.random().toString(36).slice(2, 2 + n) + Date.now().toString(36);
  // Mã phiên (1 lần mở trình duyệt = 1 phiên), dùng chung cho bộ đếm và phân tích
  const SESS = (() => {
    let sid = store.get('eh_sid', 1), isNew = false;
    if (!sid) { sid = rid(8); isNew = true; store.set('eh_sid', sid, 1); }
    return { sid, isNew };
  })();

  /* ---------------- Đồng ý cookie (Luật Bảo vệ dữ liệu cá nhân) ----------------
   * Chưa đồng ý hoặc chọn "Chỉ cần thiết": KHÔNG tải Google Analytics, KHÔNG ghi hành vi. */
  // Máy của quản trị viên (đã đăng nhập /quan-tri trên trình duyệt này): hiện nút Quản trị, không tính vào thống kê
  const IS_ADMIN = !!store.get('eh_admin_key');
  const CONSENT_KEY = 'eh_consent_v1';
  let consent = null;
  try { consent = (JSON.parse(store.get(CONSENT_KEY) || 'null') || {}).c || null; } catch (e) {}
  const analyticsOn = () => consent === 'all' && !IS_ADMIN;

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  let gaLoaded = false;
  function loadGA() {
    if (gaLoaded || !CONFIG.GA4_ID || !analyticsOn()) return;
    gaLoaded = true;
    const g = document.createElement('script');
    g.async = true;
    g.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(CONFIG.GA4_ID);
    document.head.appendChild(g);
    gtag('js', new Date());
    gtag('config', CONFIG.GA4_ID, { anonymize_ip: true });
  }
  let fpEvent = null; // gán ở phần phân tích hành vi bên dưới
  const track = (event, params = {}) => {
    if (gaLoaded) {
      gtag('event', event, params);
      // Gửi form thành công = khách hàng tiềm năng (sự kiện chính có sẵn trong GA4)
      if (event === 'form_submit') gtag('event', 'qualify_lead', { form_name: params.form || '' });
    }
    if (fpEvent) fpEvent(event, params);
  };

  /* ---------------- Toast & sao chép ---------------- */
  const toastEl = $('#toast') || document.body.appendChild(Object.assign(document.createElement('div'), { className: 'toast', id: 'toast' }));
  let toastTimer;
  function toast(msg) {
    toastEl.textContent = msg;
    toastEl.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove('show'), 2200);
  }
  async function copyText(text) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;opacity:0;left:-9999px';
      document.body.appendChild(ta);
      ta.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch { ok = false; }
      ta.remove();
      return ok;
    }
  }
  document.addEventListener('click', async (e) => {
    const b = e.target.closest('[data-copy-text]');
    if (!b) return;
    const ok = await copyText(b.dataset.copyText);
    toast(ok ? 'Đã sao chép số 0948 919 598' : 'Không sao chép được, vui lòng nhấn giữ số để sao chép');
    track('copy_phone');
  });
  document.addEventListener('click', (e) => {
    const t = e.target.closest('[data-track]');
    if (t) track('click_' + t.dataset.track);
  });

  /* ---------------- Header, thanh tiến trình đọc ---------------- */
  const head = $('#siteHead') || document.createElement('div');
  const bar = $('#progress') || document.createElement('div');
  let lastY = scrollY;
  let ticking = false;
  function onScroll() {
    const y = scrollY;
    head.classList.toggle('is-scrolled', y > 24);
    if (y < 480 || y < lastY - 6) head.classList.remove('is-hidden');
    else if (y > lastY + 6 && !head.contains(document.activeElement)) head.classList.add('is-hidden');
    lastY = y;
    const max = root.scrollHeight - innerHeight;
    bar.style.transform = `scaleX(${max > 0 ? Math.min(y / max, 1) : 0})`;
    ticking = false;
  }
  addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  head.addEventListener('focusin', () => head.classList.remove('is-hidden'));
  onScroll();

  /* ---------------- Scroll-spy cho menu ---------------- */
  const spyLinks = $$('[data-spy]');
  const spyMap = new Map(spyLinks.map((a) => [a.hash.slice(1), a]));
  if ('IntersectionObserver' in window) {
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        spyLinks.forEach((a) => a.removeAttribute('aria-current'));
        const link = spyMap.get(en.target.id);
        if (link) link.setAttribute('aria-current', 'true');
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    $$('main > section[id]').forEach((s) => spy.observe(s));
  }

  /* ---------------- Hiệu ứng khi cuộn (kiểu AOS, tự viết) ---------------- */
  const revealEls = $$('[data-reveal], [data-proc]');
  if (root.classList.contains('js-motion') && 'IntersectionObserver' in window) {
    // Phần tử dạng mask bị clip-path che 100% nên Chrome không báo giao cắt; quan sát phần tử cha thay thế
    const proxy = new Map();
    const rio = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          if (en.target.matches('[data-reveal], [data-proc]')) en.target.classList.add('is-in');
          (proxy.get(en.target) || []).forEach((el) => el.classList.add('is-in'));
          rio.unobserve(en.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealEls.forEach((el) => {
      const t = el.dataset.reveal === 'mask' && el.parentElement ? el.parentElement : el;
      if (t !== el) proxy.set(t, [...(proxy.get(t) || []), el]);
      rio.observe(t);
    });
  } else {
    revealEls.forEach((el) => el.classList.add('is-in'));
  }

  /* Cửa chớp ở hero: gỡ khỏi layout sau khi mở xong */
  const shutterR = $('.shutter.r');
  if (shutterR) {
    shutterR.addEventListener('animationend', () => shutterR.parentElement.classList.add('is-done'), { once: true });
  }

  /* ---------------- Menu điện thoại ---------------- */
  const menu = $('#dlg-menu') || { open: false, close() {}, addEventListener() {} };
  const menuOpenBtn = $('[data-menu-open]');
  if (menuOpenBtn) menuOpenBtn.addEventListener('click', () => {
    menu.showModal();
    track('menu_open');
  });
  const menuCloseBtn = $('[data-menu-close]');
  if (menuCloseBtn) menuCloseBtn.addEventListener('click', () => menu.close());
  menu.addEventListener('click', (e) => {
    const a = e.target.closest('[data-menu-link]');
    if (!a) return;
    e.preventDefault();
    menu.close();
    const target = document.getElementById(a.hash.slice(1));
    if (!target) { location.href = a.href; return; }
    requestAnimationFrame(() => {
      target.scrollIntoView({ behavior: smooth, block: 'start' });
      history.replaceState(history.state, '', a.hash);
    });
  });

  /* ------------------------------------------------------------------
   * Router dạng SPA cho các lớp phủ (dialog)
   * #tim-nguoi          → form khách hàng
   * #ung-tuyen          → form ứng viên
   * #chinh-sach-bao-mat → chính sách dữ liệu cá nhân
   * Nút Back của trình duyệt đóng lớp phủ, link chia sẻ mở đúng form.
   * ------------------------------------------------------------------ */
  const dialogs = Object.fromEntries(Object.entries({ khach: $('#dlg-khach'), ungvien: $('#dlg-ungvien'), policy: $('#dlg-policy') }).filter(([, d]) => d));
  const ROUTES = { 'tim-nguoi': 'khach', 'ung-tuyen': 'ungvien', 'chinh-sach-bao-mat': 'policy' };
  const routeOf = (key) => dialogs[key].dataset.route;
  const keyOf = (dlg) => Object.keys(dialogs).find((k) => dialogs[k] === dlg);
  const returnFocus = {};
  const wizards = {};

  const policyContent = $('#policyContent');
  const policySlot = $('#policySlot');
  const policyTarget = $('[data-policy-target]');

  function openDialog(key, opts = {}) {
    const dlg = dialogs[key];
    if (!dlg) return;
    if (menu.open) menu.close();
    if (key !== 'policy') {
      // Chỉ một form mở tại một thời điểm
      Object.entries(dialogs).forEach(([k, d]) => { if (k !== key && d.open) closeDialog(k, { silent: true }); });
      const wz = wizards[key];
      if (wz) {
        wz.resetIfFinished();
        if (opts.service) wz.preselect(opts.service);
      }
    } else if (policyTarget && policyContent) {
      policyTarget.appendChild(policyContent);
    }
    if (key !== 'policy') loadRecaptcha();
    if (dlg.open) return;
    returnFocus[key] = opts.from || document.activeElement;
    dlg.showModal();
    if (opts.push !== false) history.pushState({ dlg: key }, '', '#' + routeOf(key));
    track('dialog_open', { dialog: key, service: opts.service || undefined });
  }

  function closeDialog(key, opts = {}) {
    const dlg = dialogs[key];
    if (!dlg || !dlg.open) return;
    if (!opts.silent && !opts.fromHistory && history.state && history.state.dlg === key) {
      history.back(); // popstate sẽ gọi lại closeDialog với fromHistory
      return;
    }
    dlg.close();
    if (!opts.fromHistory && location.hash === '#' + routeOf(key)) {
      history.replaceState(null, '', location.pathname + location.search);
    }
  }

  Object.entries(dialogs).forEach(([key, dlg]) => {
    dlg.addEventListener('cancel', (e) => { e.preventDefault(); closeDialog(key); });
    dlg.addEventListener('click', (e) => {
      if (e.target === dlg) closeDialog(key);
      if (e.target.closest('[data-close]')) closeDialog(key);
    });
    dlg.addEventListener('close', () => {
      if (key === 'policy' && policySlot && policyContent) policySlot.appendChild(policyContent);
      const f = returnFocus[key];
      if (f && document.contains(f) && typeof f.focus === 'function') f.focus({ preventScroll: true });
    });
  });

  document.addEventListener('click', (e) => {
    const t = e.target.closest('[data-open]');
    if (!t) return;
    e.preventDefault();
    openDialog(t.dataset.open, { service: t.dataset.service, from: t });
  });

  function syncFromHash() {
    const key = ROUTES[location.hash.slice(1)];
    Object.entries(dialogs).forEach(([k, d]) => {
      if (d.open && k !== key && !(k !== 'policy' && key === 'policy')) closeDialog(k, { fromHistory: true });
    });
    if (key && !dialogs[key].open) openDialog(key, { push: false });
  }
  addEventListener('popstate', syncFromHash);
  if (ROUTES[location.hash.slice(1)]) syncFromHash();

  /* ---------------- Form nhiều bước ---------------- */
  const CHECK = {
    phone: (v) => /^(\+?84|0)\d{8,10}$/.test(v.replace(/[\s.\-()]/g, '')) || 'Số điện thoại chưa đúng, ví dụ 0912 345 678.',
    email: (v) => (/^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v) && !/\.(con|cmo|ocm|comm|vnn)$/i.test(v) && !/@(gmai|gmial|gamil|gmal)\./i.test(v))
      || 'Email chưa đúng, vui lòng kiểm tra lại (ví dụ ten@gmail.com).',
    year: (v) => {
      const y = +v;
      return (/^\d{4}$/.test(v) && y >= 1950 && y <= new Date().getFullYear() - 18) || 'Năm sinh cần 4 chữ số, ví dụ 1985.';
    },
  };

  function setErr(box, msg, input) {
    if (!box) return;
    box.classList.toggle('invalid', !!msg);
    const e = box.querySelector('.err');
    if (e) e.textContent = msg || '';
    if (input) input.setAttribute('aria-invalid', msg ? 'true' : 'false');
  }

  function validateStep(step) {
    let first = null;
    $$('fieldset[data-req]', step).forEach((fs) => {
      const ok = !!fs.querySelector('input:checked');
      setErr(fs, ok ? '' : fs.dataset.req);
      if (!ok && !first) first = fs;
    });
    $$('input[data-req], input[data-check], textarea[data-req]', step).forEach((inp) => {
      const box = inp.closest('.fld, .consent');
      if (inp.type === 'checkbox') {
        const ok = inp.checked;
        setErr(box, ok ? '' : inp.dataset.req, inp);
        if (!ok && !first) first = inp;
        return;
      }
      const v = inp.value.trim();
      let msg = '';
      if (inp.dataset.req && !v) msg = inp.dataset.req;
      else if (v && inp.dataset.check) {
        const r = CHECK[inp.dataset.check](v);
        if (r !== true) msg = r;
      }
      setErr(box, msg, inp);
      if (msg && !first) first = inp;
    });
    if (first) {
      const focusEl = first.matches('fieldset') ? first.querySelector('input') : first;
      const box = first.closest('.fld, .consent, fieldset') || first;
      box.scrollIntoView({ behavior: smooth, block: 'center' });
      setTimeout(() => focusEl.focus({ preventScroll: true }), reduceMotion ? 0 : 280);
    }
    return !first;
  }

  const line = (l, v) => (v ? `- ${l}: ${v}` : null);
  const MESSAGES = {
    khach: (d) => ['Chào Elite Helpers, tôi cần tư vấn:', line('Khách hàng', d.client), line('Dịch vụ', d.service), line('Hình thức', d.mode),
      line('Họ tên', d.name), line('SĐT/Zalo', d.phone), line('Email', d.email), line('Khu vực', d.area), line('Bắt đầu', d.start),
      line('Ngôn ngữ', d.lang), line('Loại nhà', d.house), line('Mô tả', d.note)].filter(Boolean).join('\n'),
    ungvien: (d) => ['Chào Elite Helpers, tôi muốn ứng tuyển:', line('Họ tên', d.name), line('Năm sinh', d.birthYear), line('SĐT/Zalo', d.phone),
      line('Quê quán', d.hometown), line('Nơi ở', d.currentAddress), line('Vị trí', d.position), line('Hình thức', d.mode),
      line('Kinh nghiệm', d.expYears), line('Ngoại ngữ', d.language), line('Nấu ăn', d.cooking), line('Chi tiết', d.experience),
      line('Lương mong muốn', d.salary), line('Bắt đầu', d.start), line('Ghi chú', d.note)].filter(Boolean).join('\n'),
  };
  const TRANSFORM = {
    ungvien: (d) => {
      const parts = [['Đã làm', d.pastRoles], ['Nơi làm', d.workplaces], ['Giặt là', d.laundry], ['Chăm sóc', d.care], ['Nhà cửa', d.home], ['Mô tả', d.expNote]]
        .filter((x) => x[1]).map((x) => `${x[0]}: ${x[1]}`);
      d.experience = parts.join(' | ');
      ['pastRoles', 'workplaces', 'laundry', 'care', 'home', 'expNote'].forEach((k) => delete d[k]);
    },
  };


  /* ---------------- Google reCAPTCHA v3: chỉ tải khi mở form ---------------- */
  if (!CONFIG.RECAPTCHA_SITE_KEY) $$('.recaptcha-note').forEach((n) => { n.hidden = true; });
  let recaptchaReady = null;
  function loadRecaptcha() {
    if (!CONFIG.RECAPTCHA_SITE_KEY) return Promise.resolve(false);
    if (recaptchaReady) return recaptchaReady;
    recaptchaReady = new Promise((resolve) => {
      const s = document.createElement('script');
      s.src = 'https://www.google.com/recaptcha/api.js?render=' + encodeURIComponent(CONFIG.RECAPTCHA_SITE_KEY);
      s.async = true;
      s.onload = () => (window.grecaptcha ? grecaptcha.ready(() => resolve(true)) : resolve(false));
      s.onerror = () => resolve(false);
      document.head.appendChild(s);
    });
    return recaptchaReady;
  }
  async function recaptchaToken(action) {
    try {
      if (!(await loadRecaptcha())) return '';
      return await Promise.race([
        grecaptcha.execute(CONFIG.RECAPTCHA_SITE_KEY, { action }),
        new Promise((r) => setTimeout(() => r(''), 6000)),
      ]);
    } catch (e) { return ''; }
  }

  async function send(data) {
    // Google Apps Script: gửi dạng form (application/x-www-form-urlencoded là "simple request",
    // không cần preflight) và ĐỌC phản hồi JSON. Nếu Apps Script lỗi, mạng lỗi hoặc quá 20 giây,
    // ném lỗi để form chuyển sang phương án gửi qua Zalo, không báo "đã nhận" sai.
    const payload = { ...data };
    const stamp = '[' + (payload.consent || 'Đồng ý xử lý dữ liệu cá nhân') + ' lúc ' + new Date().toLocaleString('vi-VN') + ']';
    payload.note = payload.note ? payload.note + ' ' + stamp : stamp;
    if (CONFIG.RECAPTCHA_SITE_KEY) payload.recaptcha = await recaptchaToken(payload.formType === 'ungvien' ? 'ung_tuyen' : 'tim_nguoi');
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), 20000);
    try {
      const res = await fetch(CONFIG.FORM_ENDPOINT, { method: 'POST', body: new URLSearchParams(payload), redirect: 'follow', signal: ctrl.signal });
      const json = await res.json().catch(() => null);
      if (!res.ok || !json || json.ok !== true) throw new Error((json && json.error) || 'HTTP ' + res.status);
      return 'ok';
    } finally {
      clearTimeout(timer);
    }
  }

  function setupWizard(form) {
    const key = form.dataset.form;
    const steps = $$('[data-step]', form);
    const bars = $('[data-bars]', form);
    const prog = $('[data-prog]', form);
    const back = $('[data-back]', form);
    const next = $('[data-next]', form);
    const submit = $('[data-submit]', form);
    const body = $('[data-body]', form);
    const foot = $('[data-foot]', form);
    const note = $('[data-note]', form);
    const done = $('[data-done]', form);
    const fallback = $('[data-fallback]', form);
    const fbText = $('[data-text]', form);
    bars.innerHTML = steps.map(() => '<span></span>').join('');
    let cur = 0;
    let finished = false;

    function show(n, dir = 0) {
      cur = n;
      steps.forEach((s, i) => {
        s.hidden = i !== n;
        s.classList.remove('enter-fwd', 'enter-back');
      });
      if (dir && !reduceMotion) {
        const s = steps[n];
        void s.offsetWidth;
        s.classList.add(dir > 0 ? 'enter-fwd' : 'enter-back');
      }
      [...bars.children].forEach((b, i) => b.classList.toggle('on', i <= n));
      prog.textContent = `Bước ${n + 1}/${steps.length}: ${steps[n].dataset.title}`;
      back.hidden = n === 0;
      next.hidden = n === steps.length - 1;
      submit.hidden = n !== steps.length - 1;
      body.scrollTop = 0;
    }

    function reset() {
      form.reset();
      $$('.invalid', form).forEach((el) => setErr(el, ''));
      $$('[aria-invalid]', form).forEach((el) => el.removeAttribute('aria-invalid'));
      done.hidden = true;
      fallback.hidden = true;
      foot.hidden = false;
      note.hidden = false;
      finished = false;
      show(0);
    }

    next.addEventListener('click', () => {
      if (!validateStep(steps[cur])) { track('form_error', { form: key, step: cur + 1 }); return; }
      show(cur + 1, 1);
      track('form_step', { form: key, step: cur + 1 });
    });
    back.addEventListener('click', () => show(cur - 1, -1));

    form.addEventListener('keydown', (e) => {
      if (e.key !== 'Enter' || e.target.matches('textarea, button, a')) return;
      if (cur < steps.length - 1) { e.preventDefault(); next.click(); }
    });
    const clear = (e) => {
      const box = e.target.closest('.invalid');
      if (box) setErr(box, '', e.target.matches('input, textarea, select') ? e.target : null);
    };
    form.addEventListener('input', clear);
    form.addEventListener('change', clear);

    // Tự định dạng số điện thoại 10 số khi rời ô nhập
    $$('input[type="tel"]', form).forEach((i) => i.addEventListener('blur', () => {
      const d = i.value.replace(/\D/g, '');
      if (/^0\d{9}$/.test(d)) i.value = d.replace(/(\d{4})(\d{3})(\d{3})/, '$1 $2 $3');
    }));

    $('[data-again]', form).addEventListener('click', () => reset());
    $('[data-copy]', form).addEventListener('click', async () => {
      const ok = await copyText(fbText.textContent);
      toast(ok ? 'Đã sao chép nội dung, mở Zalo và dán vào tin nhắn' : 'Không sao chép được, vui lòng chọn và sao chép thủ công');
    });

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      if (!validateStep(steps[cur])) { track('form_error', { form: key, step: cur + 1 }); return; }
      const fd = new FormData(form);
      if ((fd.get('website') || '').toString()) return; // bẫy bot
      const data = {};
      for (const [k] of fd.entries()) {
        if (k === 'website' || k in data) continue;
        data[k] = fd.getAll(k).map((v) => v.toString().trim()).filter(Boolean).join(', ');
      }
      if (TRANSFORM[key]) TRANSFORM[key](data);
      data.consent = `Đồng ý xử lý dữ liệu cá nhân theo Chính sách ${CONFIG.CONSENT_VERSION}`;
      data.consentAt = new Date().toISOString();
      data.page = location.origin + location.pathname;
      withVisitor(data);

      const label = submit.textContent;
      submit.disabled = true;
      submit.textContent = 'Đang gửi...';
      let result = null;
      try { result = await send(data); } catch (err) { console.warn('Gửi form lỗi:', err); }
      submit.disabled = false;
      submit.textContent = label;

      steps.forEach((s) => { s.hidden = true; });
      foot.hidden = true;
      note.hidden = true;
      finished = true;
      [...bars.children].forEach((b) => b.classList.add('on'));
      body.scrollTop = 0;
      if (result) {
        prog.textContent = 'Hoàn tất';
        done.hidden = false;
        done.focus({ preventScroll: true });
        track('form_submit', { form: key, mode: result });
        if (key === 'khach') store.set('eh_lead', '1');
      } else {
        prog.textContent = 'Gửi qua Zalo';
        fbText.textContent = MESSAGES[key](data);
        fallback.hidden = false;
        fallback.focus({ preventScroll: true });
        track('form_fallback', { form: key });
      }
    });

    show(0);
    return {
      resetIfFinished() { if (finished) reset(); },
      preselect(service) {
        const box = $$('input[name="service"]', form).find((i) => i.value === service);
        if (box) {
          box.checked = true;
          setErr(box.closest('fieldset'), '');
        }
      },
    };
  }

  $$('form[data-form]').forEach((f) => { wizards[f.dataset.form] = setupWizard(f); });

  /* Form một bước (trang tiếng Anh): dùng chung endpoint, formType = khach */
  $$('form[data-simple-form]').forEach((form) => {
    const msg = $('[data-msg]', form);
    const btn = $('button[type="submit"]', form);
    form.addEventListener('focusin', () => { loadRecaptcha(); }, { once: true });
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const fd = new FormData(form);
      if ((fd.get('website') || '').toString()) return;
      const data = {};
      for (const [k, v] of fd.entries()) if (k !== 'website' && k !== 'agree') data[k] = v.toString().trim();
      data.formType = 'khach';
      data.lang = 'English';
      data.consent = 'Agreed to personal data processing (EN form, policy ' + CONFIG.CONSENT_VERSION + ')';
      data.consentAt = new Date().toISOString();
      data.page = location.origin + location.pathname;
      withVisitor(data);
      const label = btn.textContent;
      btn.disabled = true; btn.textContent = 'Sending...';
      let ok = false;
      try { ok = !!(await send(data)); } catch (err) { console.warn('Form error:', err); }
      btn.disabled = false; btn.textContent = label;
      msg.hidden = false;
      if (ok) {
        msg.textContent = 'Thank you! We have received your request and will contact you within the same working day.';
        form.reset();
        track('form_submit', { form: 'khach_en' });
        store.set('eh_lead', '1');
      } else {
        msg.innerHTML = 'Sorry, the form could not be sent. Please message us on <a class="underline" href="' + CONFIG.ZALO_URL + '" target="_blank" rel="noopener">Zalo</a> or email <a class="underline" href="mailto:lienhe@giupviecelite.vn">lienhe@giupviecelite.vn</a>.';
        track('form_fallback', { form: 'khach_en' });
      }
      msg.focus();
    });
  });

  /* Bộ đếm lượt truy cập thật (Apps Script): 1 phiên trình duyệt = 1 lượt.
   * Chạy khi khách tương tác lần đầu hoặc sau 4 giây; gọi GET dạng JSONP, dự phòng POST. */
  const visitEls = $$('[data-visits]');
  const vRender = (j) => {
    const en = root.lang === 'en';
    const f = (x) => Number(x || 0).toLocaleString(en ? 'en-US' : 'vi-VN');
    const html = en
      ? `<span class="dot"></span>${f(j.online)} online <span class="sep">·</span> ${f(j.total)} visits`
      : `<span class="dot"></span>${f(j.online)} đang xem <span class="sep">·</span> ${f(j.total)} lượt truy cập`;
    visitEls.forEach((el) => { el.innerHTML = html; el.hidden = false; });
  };
  const viaJsonp = (params) => new Promise((resolve, reject) => {
    const cb = 'ehV' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
    const el = document.createElement('script');
    const done = () => { clearTimeout(t); try { delete window[cb]; } catch (e) { window[cb] = undefined; } el.remove(); };
    const t = setTimeout(() => { done(); reject(new Error('timeout')); }, 12000);
    window[cb] = (j) => { done(); (j && j.ok) ? resolve(j) : reject(new Error('bad')); };
    el.onerror = () => { done(); reject(new Error('blocked')); };
    el.src = CONFIG.FORM_ENDPOINT + '?' + new URLSearchParams({ ...params, cb });
    document.head.appendChild(el);
  });
  const viaPost = async (params) => {
    const res = await fetch(CONFIG.FORM_ENDPOINT, { method: 'POST', body: new URLSearchParams(params), redirect: 'follow' });
    const j = await res.json();
    if (!j || !j.ok) throw new Error('bad');
    return j;
  };
  const runVisits = async () => {
    const params = { action: 'hit', vid: SESS.sid, n: SESS.isNew && !IS_ADMIN ? '1' : '0' };
    try { vRender(await viaJsonp(params)); } catch (e) {
      try { vRender(await viaPost(params)); } catch (e2) { /* lỗi mạng: ẩn bộ đếm */ }
    }
  };
  if (visitEls.length && CONFIG.FORM_ENDPOINT && !navigator.webdriver) {
    const EVS = ['scroll', 'touchstart', 'pointerdown', 'keydown', 'mousemove'];
    let started = false;
    const kick = () => { if (started) return; started = true; EVS.forEach((ev) => removeEventListener(ev, kick)); runVisits(); };
    EVS.forEach((ev) => addEventListener(ev, kick, { passive: true, once: true }));
    setTimeout(kick, 4000);
  }

  /* ==================================================================
   * PHÂN TÍCH HÀNH VI FIRST-PARTY (chỉ chạy khi khách bấm "Đồng ý")
   * Ghi: trang xem, nguồn, trang vào/thoát, mức cuộn, thời gian, nút bấm,
   * thiết bị, hệ điều hành, trình duyệt. Không lưu IP. Gửi về Apps Script (tab SuKien).
   * ================================================================== */
  const EV = { on: false, vid: '', pv: '', q: [], active: 0, visSince: 0, maxSc: 0, timer: 0 };
  function uaInfo() {
    const ua = navigator.userAgent;
    const ipad = /Macintosh/.test(ua) && navigator.maxTouchPoints > 1;
    const os = /iPhone|iPod/.test(ua) ? 'iOS' : (/iPad/.test(ua) || ipad) ? 'iPadOS' : /Android/.test(ua) ? 'Android'
      : /Windows/.test(ua) ? 'Windows' : /CrOS/.test(ua) ? 'ChromeOS' : /Mac OS X/.test(ua) ? 'macOS' : /Linux/.test(ua) ? 'Linux' : 'Khác';
    const br = /Zalo/i.test(ua) ? 'Zalo' : /FBAN|FBAV|FB_IAB/.test(ua) ? 'Facebook' : /Instagram/.test(ua) ? 'Instagram'
      : /coc_coc|CocCoc/i.test(ua) ? 'Cốc Cốc' : /Edg[A]?\//.test(ua) ? 'Edge' : /OPR\//.test(ua) ? 'Opera' : /SamsungBrowser/.test(ua) ? 'Samsung'
      : /CriOS|Chrome\//.test(ua) ? 'Chrome' : /FxiOS|Firefox\//.test(ua) ? 'Firefox' : /Safari\//.test(ua) ? 'Safari' : 'Khác';
    const dev = (os === 'iPadOS' || (/Android/.test(ua) && !/Mobile/.test(ua))) ? 'Máy tính bảng' : /Mobi|iPhone|Android/.test(ua) ? 'Điện thoại' : 'Máy tính';
    let tz = '';
    try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch (e) {}
    return { os, br, dev, scr: screen.width + 'x' + screen.height, lang: (navigator.language || '').slice(0, 10), tz };
  }
  function sessionSource() {
    try { const s = JSON.parse(store.get('eh_src', 1) || 'null'); if (s) return s; } catch (e) {}
    const p = new URLSearchParams(location.search);
    let src = p.get('utm_source') || '', med = p.get('utm_medium') || '';
    const camp = p.get('utm_campaign') || '';
    let host = '';
    try { host = document.referrer ? new URL(document.referrer).hostname.replace(/^www\./, '') : ''; } catch (e) {}
    if (!src) {
      if (p.get('gclid')) { src = 'google'; med = 'cpc'; }
      else if (p.get('fbclid') || /FBAN|FBAV|FB_IAB/.test(navigator.userAgent)) { src = 'facebook'; med = med || 'social'; }
      else if (p.get('zarsrc') || /Zalo/i.test(navigator.userAgent)) { src = 'zalo'; med = 'social'; }
      else if (!host || host === location.hostname) { src = '(trực tiếp)'; med = 'direct'; }
      else if (/(^|\.)google\./.test(host)) { src = 'google'; med = 'organic'; }
      else if (/bing\.com$/.test(host)) { src = 'bing'; med = 'organic'; }
      else if (/coccoc/.test(host)) { src = 'coccoc'; med = 'organic'; }
      else if (/facebook\.com|fb\.com|messenger\.com/.test(host)) { src = 'facebook'; med = 'social'; }
      else if (/zalo/.test(host)) { src = 'zalo'; med = 'social'; }
      else if (/chatgpt|openai|perplexity|claude\.ai|gemini|copilot/.test(host)) { src = host; med = 'ai'; }
      else { src = host; med = 'referral'; }
    }
    const o = { src: src.slice(0, 60), med: med.slice(0, 30), camp: camp.slice(0, 60), land: location.pathname };
    store.set('eh_src', JSON.stringify(o), 1);
    return o;
  }
  function evSend(final) {
    if (!EV.on || !CONFIG.FORM_ENDPOINT) return;
    if (final) evPageEnd();
    if (!EV.q.length) return;
    const body = new URLSearchParams({
      action: 'ev',
      d: JSON.stringify({ v: EV.vid, s: SESS.sid, u: uaInfo(), src: sessionSource(), e: EV.q.splice(0, 40) }),
    });
    let ok = false;
    try { ok = navigator.sendBeacon && navigator.sendBeacon(CONFIG.FORM_ENDPOINT, body); } catch (e) {}
    if (!ok) { try { fetch(CONFIG.FORM_ENDPOINT, { method: 'POST', body, mode: 'no-cors', keepalive: true }); } catch (e) {} }
    if (EV.q.length) evSend(false);
  }
  const evSoon = () => { clearTimeout(EV.timer); EV.timer = setTimeout(() => evSend(false), 2500); };
  function evPush(o) {
    if (!EV.on) return;
    EV.q.push({ p: location.pathname, pv: EV.pv, ts: Date.now(), ...o });
    evSoon();
  }
  function evActiveSec() {
    return Math.min(1800, Math.round((EV.active + (EV.visSince ? Date.now() - EV.visSince : 0)) / 1000));
  }
  function evPageEnd() { if (EV.pv) EV.q.push({ t: 'pe', p: location.pathname, pv: EV.pv, ts: Date.now(), sc: EV.maxSc, sec: evActiveSec() }); }
  function evScroll() {
    const h = root.scrollHeight - innerHeight;
    const pct = h > 0 ? Math.round(Math.min(1, scrollY / h) * 20) * 5 : 100;
    if (pct > EV.maxSc) EV.maxSc = pct;
  }
  function startTracker() {
    if (EV.on || !analyticsOn() || !CONFIG.FORM_ENDPOINT || navigator.webdriver) return;
    EV.on = true;
    EV.vid = store.get('eh_vid') || rid(10);
    store.set('eh_vid', EV.vid);
    EV.pv = rid(6);
    EV.visSince = document.visibilityState === 'visible' ? Date.now() : 0;
    const src = sessionSource();
    evPush({ t: 'pv', ti: document.title.slice(0, 90), land: src.land === location.pathname && SESS.isNew ? 1 : 0 });
    evSend(false);
    addEventListener('scroll', evScroll, { passive: true });
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') {
        if (EV.visSince) { EV.active += Date.now() - EV.visSince; EV.visSince = 0; }
        evSend(true);
      } else EV.visSince = Date.now();
    });
    addEventListener('pagehide', () => evSend(true));
  }
  function stopTracker() {
    EV.on = false; EV.q = [];
    store.del('eh_vid');
    // Xóa cookie Google Analytics (_ga, _ga_*) trên tên miền này
    document.cookie.split(';').map((c) => c.split('=')[0].trim()).filter((n) => /^_ga/.test(n)).forEach((n) => {
      [location.hostname, '.' + location.hostname.replace(/^www\./, '')].forEach((d) => {
        document.cookie = n + '=; Max-Age=0; path=/; domain=' + d;
      });
      document.cookie = n + '=; Max-Age=0; path=/';
    });
  }
  // Các hành động được ghi lại (gọi, Zalo, mở form, gửi form, hộp gợi ý…)
  fpEvent = (name, params) => {
    if (!EV.on || name === 'form_error') return;
    const l = params.form || params.dialog || params.service || params.step || '';
    evPush({ t: 'ac', n: String(name).slice(0, 40), l: String(l).slice(0, 60) });
    if (name === 'form_submit') evSend(false);
  };
  // Gắn mã truy cập (ẩn danh) vào hồ sơ form khi khách đã đồng ý cookie, để biết hành trình trước khi để lại thông tin
  function withVisitor(data) {
    if (EV.on && EV.vid) data.visitor = EV.vid;
    if (data.optin) data.optin = 'Có';
    return data;
  }

  /* ---------------- Thông báo đồng ý cookie ---------------- */
  function consentBanner(force) {
    if ((consent && !force) || $('#ckBar')) return;
    const en = root.lang === 'en';
    const el = document.createElement('div');
    el.id = 'ckBar';
    el.className = 'ck-bar';
    el.setAttribute('role', 'region');
    el.setAttribute('aria-label', en ? 'Cookie consent' : 'Đồng ý cookie');
    el.innerHTML = en
      ? '<p>We use cookies to understand how visitors use this site (pages viewed, traffic source, device) and to improve our service. No IP address is stored. <a href="/#chinh-sach-bao-mat" lang="vi">Privacy policy</a></p><div class="ck-acts"><button type="button" class="btn btn-ghost-dark ck-no">Necessary only</button><button type="button" class="btn btn-green ck-yes">Accept</button></div>'
      : '<p>Elite Helpers dùng cookie để hiểu cách khách dùng website (trang đã xem, nguồn truy cập, thiết bị) và cải thiện dịch vụ. Không lưu địa chỉ IP. <a href="#chinh-sach-bao-mat" data-open="policy">Chính sách dữ liệu</a></p><div class="ck-acts"><button type="button" class="btn btn-ghost-dark ck-no">Chỉ cần thiết</button><button type="button" class="btn btn-green ck-yes">Đồng ý</button></div>';
    document.body.appendChild(el);
    const set = (c) => {
      consent = c;
      store.set(CONSENT_KEY, JSON.stringify({ c, t: new Date().toISOString(), v: CONFIG.CONSENT_VERSION }));
      el.remove();
      if (c === 'all') { loadGA(); startTracker(); } else stopTracker();
      toast(en ? 'Your choice has been saved' : 'Đã lưu lựa chọn của bạn');
    };
    $('.ck-yes', el).addEventListener('click', () => set('all'));
    $('.ck-no', el).addEventListener('click', () => set('necessary'));
  }
  document.addEventListener('click', (e) => {
    if (e.target.closest('[data-cookie-settings]')) { e.preventDefault(); consentBanner(true); }
  });
  if (analyticsOn()) { loadGA(); startTracker(); }
  else if (!consent && !IS_ADMIN && !navigator.webdriver) setTimeout(() => consentBanner(false), 1500);

  /* Nút Quản trị: chỉ hiện trên máy đã đăng nhập trang quản trị */
  if (IS_ADMIN) {
    const a = document.createElement('a');
    a.href = '/quan-tri/';
    a.className = 'admin-fab';
    a.setAttribute('aria-label', 'Mở trang quản trị');
    a.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></svg><span>Quản trị</span>';
    document.body.appendChild(a);
  }

  /* ==================================================================
   * HỘP GỢI Ý (marketing automation nhẹ): hiện khi khách cuộn sâu, đọc lâu
   * hoặc định rời trang. Mỗi phiên tối đa 1 lần; đóng thì ẩn 3 ngày.
   * Không thu thập dữ liệu, chỉ gợi ý mở form / Zalo.
   * ================================================================== */
  (() => {
    const path = location.pathname;
    if (IS_ADMIN || store.get('eh_nudge', 1)) return;
    if (Date.now() - Number(store.get('eh_nudge_x') || 0) < 3 * 86400000) return;
    const en = root.lang === 'en';
    const lead = store.get('eh_lead') === '1';
    const svcBtn = $('main [data-open="khach"][data-service]');
    const svc = svcBtn ? svcBtn.dataset.service : '';
    let c;
    if (lead) {
      c = { k: 'quaylai', h: en ? 'Welcome back' : 'Chào mừng anh/chị quay lại',
        p: en ? 'We are working on your request. Need to add details or ask anything? Message us on Zalo.' : 'Elite Helpers đang xử lý yêu cầu của gia đình. Cần bổ sung thông tin hay hỏi thêm, anh/chị nhắn Zalo cho chúng tôi nhé.',
        b: `<a class="btn btn-green" href="${CONFIG.ZALO_URL}" target="_blank" rel="noopener" data-nudge-go>${en ? 'Message on Zalo' : 'Nhắn Zalo'}</a>`, at: 0.3, sec: 12 };
    } else if (/^\/tuyen-dung/.test(path)) {
      c = { k: 'ungvien', h: 'Đang tìm việc giúp việc, bảo mẫu?', p: 'Ứng tuyển trong 2 phút. Elite Helpers không thu phí người lao động.',
        b: '<a class="btn btn-green" href="#ung-tuyen" data-open="ungvien" data-nudge-go>Ứng tuyển ngay</a>', at: 0.45, sec: 35 };
    } else if (en) {
      c = { k: 'en', h: 'Need a trusted helper in Hanoi?', p: 'Tell us what you need. We reply within the same working day.',
        b: `<a class="btn btn-green" href="${path.startsWith('/en') ? '' : '/en/'}#contact" data-nudge-go>Get in touch</a><a class="btn btn-ghost-dark" href="${CONFIG.ZALO_URL}" target="_blank" rel="noopener" data-nudge-go>Zalo</a>`, at: 0.5, sec: 40 };
    } else {
      c = { k: 'khach', h: 'Cần người phù hợp cho gia đình?', p: 'Gửi nhu cầu trong 2 phút, tư vấn miễn phí và phản hồi trong ngày làm việc.',
        b: `<a class="btn btn-green" href="#tim-nguoi" data-open="khach"${svc ? ` data-service="${svc.replace(/"/g, '')}"` : ''} data-nudge-go>Nhận tư vấn</a><a class="btn btn-ghost-dark" href="${CONFIG.ZALO_URL}" target="_blank" rel="noopener" data-nudge-go>Zalo</a>`,
        at: path === '/' ? 0.6 : 0.5, sec: 40 };
    }
    let shown = false, activeMs = 0, last = Date.now();
    const ready = () => !$('dialog[open]') && !$('#ckBar');
    function show(why) {
      if (shown || !ready()) return;
      shown = true;
      store.set('eh_nudge', '1', 1);
      const el = document.createElement('aside');
      el.className = 'nudge';
      el.setAttribute('aria-label', c.h);
      el.innerHTML = `<button type="button" class="nudge-x" aria-label="${en ? 'Close' : 'Đóng'}">×</button><p class="nudge-h">${c.h}</p><p class="nudge-p">${c.p}</p><div class="nudge-b">${c.b}</div>`;
      document.body.appendChild(el);
      requestAnimationFrame(() => el.classList.add('in'));
      track('nudge_show', { form: c.k, step: why });
      const close = () => { el.classList.remove('in'); setTimeout(() => el.remove(), 400); };
      $('.nudge-x', el).addEventListener('click', () => { store.set('eh_nudge_x', String(Date.now())); track('nudge_close', { form: c.k }); close(); });
      el.addEventListener('click', (e) => { if (e.target.closest('[data-nudge-go]')) { track('nudge_click', { form: c.k }); close(); } });
    }
    const onScroll = () => {
      const h = root.scrollHeight - innerHeight;
      if (h > 0 && scrollY / h >= c.at) show('cuộn');
    };
    addEventListener('scroll', onScroll, { passive: true });
    const tick = setInterval(() => {
      if (shown) { clearInterval(tick); return; }
      const now = Date.now();
      if (document.visibilityState === 'visible') activeMs += now - last;
      last = now;
      if (activeMs / 1000 >= c.sec) show('thời gian');
    }, 1000);
    // Ý định rời trang (máy tính): chuột đi ra mép trên cửa sổ
    if (matchMedia('(hover: hover) and (pointer: fine)').matches) {
      document.addEventListener('mouseout', (e) => { if (!e.relatedTarget && e.clientY <= 0 && activeMs > 8000) show('rời trang'); });
    }
  })();

  /* Năm hiện tại ở chân trang */
  $$('[data-year]').forEach((el) => { el.textContent = String(new Date().getFullYear()); });
})();
