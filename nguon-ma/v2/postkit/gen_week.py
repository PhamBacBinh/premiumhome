# -*- coding: utf-8 -*-
"""Trang đăng bài tăng tần suất (đợt theo module tham số 2). Ghi vào <thư mục ra>/<ngày>/<slug>.html"""
import os, sys, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import gen_postkit as G
import importlib; W = importlib.import_module(sys.argv[2] if len(sys.argv) > 2 else "week_2810")
out = sys.argv[1]
for p in W.POSTS:
    d = os.path.join(out, p['day']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, p['slug'] + '.html'), 'w', encoding='utf-8').write(G.page(p))
    print(f"https://giupviecelite.vn/media/{p['day']}/{p['slug']}.html")
