#!/usr/bin/env python3
"""Local-only development web server."""
import http.server
import os
import threading
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8000"))
os.chdir(ROOT)
server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler)
url = f"http://127.0.0.1:{PORT}"
print(f"Learning site: {url}", flush=True)
if os.environ.get("NO_BROWSER", "").lower() not in ("1", "true", "yes"):
    # Open only after the server begins accepting requests.
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
