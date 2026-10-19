import http.server, os, sys
D = sys.argv[1]
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=D, **k)
    def log_message(s, *a): pass
    def send_head(s):
        p = s.path.split('?')[0].split('#')[0]
        fp = os.path.join(D, p.lstrip('/'))
        if p != '/' and not os.path.exists(fp) and os.path.exists(fp + '.html'):
            s.path = p + '.html'
        elif p != '/' and not os.path.exists(fp):
            s.send_response(404); s.send_header('Content-Type', 'text/html; charset=utf-8'); s.end_headers()
            s.wfile.write(open(os.path.join(D, '404.html'), 'rb').read()); return None
        return super().send_head()
http.server.ThreadingHTTPServer(('127.0.0.1', 8765), H).serve_forever()
