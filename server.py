import asyncio, os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import edge_tts

VOICE = "mn-MN-YesuiNeural"  # Эрэгтэй дуу хүсвэл: "mn-MN-Bataaneural"
HERE = os.path.dirname(os.path.abspath(__file__))

async def synth(text):
    data = b""
    async for ch in edge_tts.Communicate(text, VOICE).stream():
        if ch["type"] == "audio":
            data += ch["data"]
    return data

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/tts":
            qs = parse_qs(parsed.query)
            text = qs.get("text", [""])[0]
            if not text:
                self.send_error(400, "Missing text")
                return
            try:
                audio_bytes = asyncio.run(synth(text))
                self.send_response(200)
                self.send_header("Content-Type", "audio/mpeg")
                self.send_header("Access-Control-Allow-Origin", "*")  # CORS зөвшөөрөл
                self.end_headers()
                self.wfile.write(audio_bytes)
            except Exception as e:
                self.send_error(500, str(e))
        else:
            # HTML эсвэл бусад файл буцаах
            file_path = os.path.join(HERE, "kod.html" if parsed.path in ["/", "/kod.html"] else parsed.path.lstrip("/"))
            if os.path.exists(file_path) and os.path.isfile(file_path):
                self.send_response(200)
                if file_path.endswith(".html"):
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "Not Found")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8765))
    server_address = ("0.0.0.0", port)
    httpd = ThreadingHTTPServer(server_address, Handler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()