# -*- coding: utf-8 -*-
"""Trang đăng bài đợt 1 tăng tần suất (28–31/10). Ghi vào <thư mục ra>/<ngày>/<slug>.html"""
import os, sys, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import gen_postkit as G
import week_2810 as W
out = sys.argv[1]
for p in W.POSTS:
    d = os.path.join(out, p['day']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, p['slug'] + '.html'), 'w', encoding='utf-8').write(G.page(p))
    print(f"https://giupviecelite.vn/media/{p['day']}/{p['slug']}.html")
