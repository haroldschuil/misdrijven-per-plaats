#!/usr/bin/env python3
"""Start de app 'Misdrijven per plaats' lokaal.

Gebruik: zet dit bestand in dezelfde map als index.html en
voer uit:  python3 server.py   (Windows: py server.py)
De app opent dan op http://localhost:8000

Het script serveert de HTML en stuurt verzoeken onder /odata/ door naar de
open-data-API van de politie en het CBS (tabellen 47015NED, 47013NED en 03759ned). Zo omzeilt het de
CORS-blokkade van de browser. Alleen standaard Python, geen installatie nodig.
"""
import http.server
import os
import urllib.error
import urllib.request
import webbrowser

PORT = 8000
# Toegestane tabellen en hun server
TABLES = {
    "47015NED": "https://dataderden.cbs.nl/ODataApi/OData/",  # politie, misdrijven per woonplaats
    "47013NED": "https://dataderden.cbs.nl/ODataApi/OData/",  # politie, misdrijven en aangiften per gemeente
    "03759ned": "https://opendata.cbs.nl/ODataApi/OData/",    # CBS, bevolking per gemeente
}
HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = "index.html"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=HERE, **kw)

    def do_GET(self):
        if self.path in ("/", ""):
            self.path = "/" + PAGE
            return super().do_GET()
        if self.path.startswith("/odata/"):
            rest = self.path[len("/odata/"):]
            table = rest.split("/", 1)[0]
            if table not in TABLES:
                self.send_error(403, "Tabel niet toegestaan")
                return
            try:
                req = urllib.request.Request(TABLES[table] + rest, headers={"Accept": "application/json"})
                with urllib.request.urlopen(req, timeout=30) as r:
                    body = r.read()
                    self.send_response(r.status)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
            except urllib.error.HTTPError as e:
                self.send_error(e.code, "Bron-API: " + str(e.reason))
            except Exception as e:
                self.send_error(502, "Bron-API niet bereikbaar: " + str(e))
            return
        return super().do_GET()


if __name__ == "__main__":
    url = f"http://localhost:{PORT}/"
    print(f"App draait op {url}  (stoppen: Ctrl+C)")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
