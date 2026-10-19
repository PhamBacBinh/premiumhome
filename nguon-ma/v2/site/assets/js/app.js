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
    CONSENT_VERSION: '12/10/2026',
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

  /* Đo lường: đẩy sự kiện vào dataLayer (dùng được với GA4 / GTM sau này) */
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  if (CONFIG.GA4_ID) {
    const g = document.createElement('script');
    g.async = true;
    g.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(CONFIG.GA4_ID);
    document.head.appendChild(g);
    gtag('js', new Date());
    gtag('config', CONFIG.GA4_ID, { anonymize_ip: true });
  }
  const track = (event, params = {}) => {
    window.dataLayer.push({ event, ...params });
    if (CONFIG.GA4_ID) gtag('event', event, params);
    // Gửi form thành công = khách hàng tiềm năng (sự kiện chính có sẵn trong GA4)
    if (CONFIG.GA4_ID && event === 'form_submit') gtag('event', 'qualify_lead', { form_name: params.form || '' });
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
    let sid = null, isNew = '0';
    try { sid = sessionStorage.getItem('eh_sid'); } catch (e) {}
    if (!sid) {
      sid = Math.random().toString(36).slice(2, 10) + Date.now().toString(36);
      isNew = '1';
      try { sessionStorage.setItem('eh_sid', sid); } catch (e) {}
    }
    const params = { action: 'hit', vid: sid, n: isNew };
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

  /* Năm hiện tại ở chân trang */
  $$('[data-year]').forEach((el) => { el.textContent = String(new Date().getFullYear()); });
})();
