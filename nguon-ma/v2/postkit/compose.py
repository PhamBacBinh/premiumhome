# -*- coding: utf-8 -*-
"""Ghép nhận diện Elite Helpers lên ảnh/video AI.
page  : ảnh 1080x1350 (Page/Group)
tiktok: video 1080x1920, chữ + logo trong vùng an toàn TikTok
        (trên 160px, dưới 440px, trái 64px, phải 140px)
reel  : video 1080x1920 cho Reels Page/Group (cùng vùng an toàn)
Cách dùng: python3 compose.py <week_module> <thư_mục_ảnh_AI> <thư_mục_ra> [slug...]
Ảnh AI đặt tên ai_<ddmm>_<slug>.png (ảnh) / ai_<ddmm>_<slug>.mp4 (video)."""
import os, sys, subprocess, importlib, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
F = lambda n, s: ImageFont.truetype(os.path.join(HERE, 'fonts', n + '.ttf'), s)
GREEN, DEEP, GOLD, GOLD2, CREAM, INK = (31, 52, 46), (20, 38, 31), (203, 171, 109), (232, 201, 129), (251, 246, 236), (20, 38, 31)
CARD = (246, 240, 226)

def tw(d, t, f, sp=0):
    return d.textlength(t, font=f) + sp * max(0, len(t) - 1)

def spaced(d, xy, t, f, fill, sp):
    x, y = xy
    for ch in t:
        d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + sp
    return x

def wrap(d, t, f, maxw):
    out, cur = [], ''
    for w in t.split():
        nx = (cur + ' ' + w).strip()
        if d.textlength(nx, font=f) <= maxw: cur = nx
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out

_ARCH = None
def arch(h):
    """Dấu EH: vòm vàng, chữ EH xanh đậm (đặt trên thẻ màu kem)."""
    global _ARCH
    if _ARCH is None:
        im = Image.open(os.path.join(HERE, 'fonts', 'arch.png')).convert('RGBA'); px = im.load()
        for y in range(im.height):
            for x in range(im.width):
                r, g, b, a = px[x, y]
                if a and r > 230 and g > 225:  # chữ EH màu kem -> xanh đậm
                    px[x, y] = (*DEEP, a)
        _ARCH = im
    return _ARCH.resize((int(_ARCH.width * h / _ARCH.height), h), Image.LANCZOS)

def logo_card(scale=1.0):
    W, H = int(560 * scale), int(124 * scale)
    c = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
    d.rounded_rectangle((0, 0, W - 1, H - 1), radius=int(20 * scale), fill=(*CARD, 250), outline=(*GOLD, 255), width=max(2, int(3 * scale)))
    m = arch(int(92 * scale)); c.alpha_composite(m, (int(22 * scale), int(16 * scale)))
    x0 = int(22 * scale) + m.width + int(20 * scale)
    d.text((x0, int(18 * scale)), 'ELITE HELPERS', font=F('bvp800', int(50 * scale)), fill=INK)
    spaced(d, (x0 + 2, int(80 * scale)), 'HỖ TRỢ GIA ĐÌNH CAO CẤP', F('bvp700', int(17 * scale)), (138, 100, 32), 3.2 * scale)
    return c

def cover(im, W, H, vpos=0.0):
    r = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    l, t = (im.width - W) // 2, int(max(0, im.height - H) * vpos)
    return im.crop((l, t, l + W, t + H))

def top_scrim(W, H, h, a0=235, a1=0, col=DEEP):
    s = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(s)
    for y in range(h):
        k = y / h; a = int(a0 + (a1 - a0) * (k ** 1.4))
        d.line((0, y, W, y), fill=(*col, a))
    return s

def headline(d, x, y, maxw, h1, h2, sub, s1=96, s2=72):
    for ln in wrap(d, h1, F('cg700', s1), maxw):
        d.text((x, y), ln, font=F('cg700', s1), fill=CREAM); y += int(s1 * 1.02)
    for ln in wrap(d, h2, F('cg700i', s2), maxw):
        d.text((x, y), ln, font=F('cg700i', s2), fill=GOLD2); y += int(s2 * 1.08)
    if sub:
        y += 6
        for ln in wrap(d, sub, F('bvp500', 30), maxw):
            d.text((x, y), ln, font=F('bvp500', 30), fill=CREAM); y += 42
    return y

def chips(d, x, y, items, maxx, size=30):
    f = F('bvp700', size); cx = x
    for t in items:
        w = tw(d, t, f) + 2 * 26
        if cx + w > maxx: cx = x; y += size + 40
        d.rounded_rectangle((cx, y, cx + w, y + size + 26), radius=(size + 26) // 2, fill=(*CARD, 245))
        d.text((cx + 26, y + 9), t, font=f, fill=INK); cx += w + 14
    return y + size + 26

def contact_bar(img, y, h):
    d = ImageDraw.Draw(img); W = img.width
    d.rectangle((0, y, W, y + h), fill=(*DEEP, 255)); d.rectangle((0, y, W, y + 4), fill=(*GOLD, 255))
    f = F('bvp700', 38); parts = [('Zalo ', CREAM), ('0948 919 598', GOLD2), ('   •   ', GOLD), ('giupviecelite.vn', CREAM)]
    tot = sum(d.textlength(t, font=f) for t, _ in parts); x = (W - tot) / 2; ty = y + (h - 46) / 2
    for t, c in parts:
        d.text((x, ty), t, font=f, fill=c); x += d.textlength(t, font=f)

def make_page(p, src, out):
    W, H, BAR = 1080, 1350, 110
    bg = cover(Image.open(src).convert('RGB'), W, H - BAR).filter(ImageFilter.UnsharpMask(1.2, 60, 2))
    img = Image.new('RGBA', (W, H), (*DEEP, 255)); img.paste(bg, (0, 0))
    img.alpha_composite(top_scrim(W, H, 700, 238, 0))
    img.alpha_composite(logo_card(), (64, 48))
    d = ImageDraw.Draw(img)
    spaced(d, (66, 222), p['kicker'], F('bvp800', 25), GOLD2, 4.5)
    y = headline(d, 64, 262, 940, p['h1'], p['h2'], p.get('sub'))
    if p.get('chips'): chips(d, 64, y + 18, p['chips'], 1016)
    contact_bar(img, H - BAR, BAR)
    img.convert('RGB').save(out, quality=93, subsampling=0)

SAFE = dict(top=160, bottom=440, left=64, right=140)

def video_overlays(p, tmp):
    """Trả về [(png, t_start, t_end)] cho lớp chữ; luôn nằm trong vùng an toàn."""
    W, H = 1080, 1920; L, R = SAFE['left'], W - SAFE['right']; maxw = R - L
    base = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    base.alpha_composite(top_scrim(W, H, 900, 225, 0))
    bot = top_scrim(W, 640, 640, 0, 0); db = ImageDraw.Draw(bot)
    for y in range(640): db.line((0, y, W, y), fill=(*DEEP, int(210 * (y / 640) ** 1.3)))
    base.alpha_composite(bot, (0, H - 640))
    base.alpha_composite(logo_card(0.92), (L, SAFE['top'] + 10))
    d = ImageDraw.Draw(base)
    y = SAFE['top'] + 10 + int(124 * 0.92) + 44
    spaced(d, (L + 2, y), p['kicker'], F('bvp800', 24), GOLD2, 4); y += 46
    y = headline(d, L, y, maxw, p['h1'], p['h2'], p.get('sub'), 92, 68)
    # dòng liên hệ: ngay trên mép vùng an toàn dưới
    cy = H - SAFE['bottom'] - 62; f = F('bvp700', 34)
    parts = [('Zalo ', CREAM), ('0948 919 598', GOLD2), ('  •  ', GOLD), ('giupviecelite.vn', CREAM)]
    tot = sum(d.textlength(t, font=f) for t, _ in parts)
    d.rounded_rectangle((L, cy - 14, L + tot + 44, cy + 56), radius=35, fill=(*DEEP, 235), outline=(*GOLD, 255), width=2)
    x = L + 22
    for t, c in parts: d.text((x, cy), t, font=f, fill=c); x += d.textlength(t, font=f)
    b0 = os.path.join(tmp, 'ov0.png'); base.save(b0); layers = [(b0, 0, None)]
    pts = p.get('points') or []
    if pts:
        f = F('bvp700', 40); step = 2.0; t0 = 1.2
        mes = ImageDraw.Draw(Image.new('RGBA', (8, 8)))
        hs = [30 + 52 * len(wrap(mes, t, f, maxw - 110)) for t in pts]
        py = max(y + 30, cy - 34 - (sum(hs) + 16 * (len(hs) - 1)))  # neo danh sách sát dòng liên hệ, chừa mặt nhân vật
        for i, t in enumerate(pts):
            lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            lines = wrap(dl, t, f, maxw - 110); hh = 30 + 52 * len(lines)
            if py + hh > cy - 40: break
            dl.rounded_rectangle((L, py, R, py + hh), radius=22, fill=(*CARD, 238))
            dl.ellipse((L + 20, py + hh / 2 - 26, L + 72, py + hh / 2 + 26), fill=(*GREEN, 255))
            n = str(i + 1); dl.text((L + 46 - dl.textlength(n, font=F('bvp800', 32)) / 2, py + hh / 2 - 21), n, font=F('bvp800', 32), fill=GOLD2)
            ty = py + 15
            for ln in lines: dl.text((L + 94, ty), ln, font=f, fill=INK); ty += 52
            fn = os.path.join(tmp, f'ov{i + 1}.png'); lay.save(fn); layers.append((fn, t0 + i * step, None)); py += hh + 16
    return layers

def scene_bg(stills, target, tmp):
    """Dựng nền chuyển động từ ảnh tĩnh 9:16: zoom chậm (Ken Burns) + chuyển cảnh mờ dần."""
    n = len(stills); xf = 0.7
    seg = (target + xf * (n - 1)) / n
    clips = []
    for i, st in enumerate(stills):
        fr = int(round(seg * 30)); o = os.path.join(tmp, f'sc{i}.mp4')
        zin = i % 2 == 0
        z = "'min(1+0.10*on/%d,1.10)'" % fr if zin else "'max(1.10-0.10*on/%d,1.0)'" % fr
        vf = ("scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,setsar=1,"
              "zoompan=z=%s:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=%d:s=1080x1920:fps=30,format=yuv420p" % (z, fr))
        subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', st, '-vf', vf, '-frames:v', str(fr), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', o])
        clips.append(o)
    if n == 1: return clips[0]
    inp = []; fc = ''; prev = '[0:v]'; off = 0.0
    for c in clips: inp += ['-i', c]
    for i in range(1, n):
        off += seg - xf
        fc += '%s[%d:v]xfade=transition=fade:duration=%.2f:offset=%.2f[x%d];' % (prev, i, xf, off, i); prev = '[x%d]' % i
    o = os.path.join(tmp, 'bg.mp4')
    subprocess.check_call(['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', fc.rstrip(';'), '-map', prev, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', o])
    return o

def make_video(p, src, out, min_len=None):
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    layers = video_overlays(p, tmp)
    n = len(layers) - 1
    target = min_len or (max(10.0, 1.2 + 2.0 * n + 3.5) if p['kind'] == 'tiktok' else 12.0)
    if isinstance(src, list):
        src = scene_bg(src, target, tmp)
    fc = ('[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,'
          'loop=-1:size=32767,trim=0:%.2f,setpts=PTS-STARTPTS[bg];' % target)
    inputs = ['-i', src]; cur = '[bg]'
    for i, (fn, ts, te) in enumerate(layers):
        inputs += ['-loop', '1', '-i', fn]
        en = '' if ts == 0 else ":enable='gte(t,%.2f)'" % ts
        fc += '%s[%d:v]overlay=0:0%s[v%d];' % (cur, i + 1, en, i); cur = '[v%d]' % i
    fc += '%sformat=yuv420p[out]' % cur
    cmd = ['ffmpeg', '-v', 'error', '-y'] + inputs + ['-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-filter_complex', fc,
           '-map', '[out]', '-map', '%d:a' % (len(layers) + 1), '-t', '%.2f' % target, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20',
           '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', out]
    subprocess.check_call(cmd)

def run(mod, aidir, outdir, only=()):
    w = importlib.import_module(mod)
    for p in w.POSTS:
        if only and p['slug'] not in only and f"{p['day']}/{p['slug']}" not in only: continue
        ddmm = p['day'][8:10] + p['day'][5:7]
        if p['kind'] == 'page':
            src = os.path.join(aidir, f"ai_{ddmm}_{p['slug']}.png"); ok = os.path.exists(src)
        else:
            src = [os.path.join(aidir, f"ai_{ddmm}_{p['slug']}_s{i + 1}.webp") for i in range(len(p.get('scenes', [])))]
            ok = bool(src) and all(os.path.exists(x) for x in src)
        if not ok: print('THIẾU', p['day'], p['slug']); continue
        d = os.path.join(outdir, p['day']); os.makedirs(d, exist_ok=True); out = os.path.join(d, p['file'])
        (make_page if p['kind'] == 'page' else make_video)(p, src, out); print('OK', out)

if __name__ == '__main__':
    sys.path.insert(0, HERE); run(sys.argv[1], sys.argv[2], sys.argv[3], tuple(sys.argv[4:]))
