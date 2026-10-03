#!/usr/bin/env python3
"""Local-only development web server."""
import http.server
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8000"))
os.chdir(ROOT)
server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler)
print(f"Learning site: http://127.0.0.1:{PORT}", flush=True)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
