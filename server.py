import asyncio, os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import edge_tts

VOICE = "mn-MN-YesuiNeural"   # эрэгтэй дуу хүсвэл: "mn-MN-BataaNeural"
HERE = os.path.dirname(os.path.abspath(__file__))

async def synth(text):
    data = b""
    async for ch in edge_tts.Communicate(text, VOICE).stream():
        if ch["type"] == "audio":
            data += ch["data"]
    return data

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/tts":
            text = parse_qs(u.query).get("text", [""])[0]
            try:
                audio = asyncio.run(synth(text))
            except Exception as e:
                print("TTS алдаа:", e)
                self.send_error(500, str(e))
                return
            self.send_response(200)
            self.send_header("Content-Type", "audio/mpeg")
            self.send_header("Content-Length", str(len(audio)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(audio)
        elif u.path in ("/", "/kod.html"):
            with open(os.path.join(HERE, "kod.html"), "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_error(404)

if __name__ == "__main__":
    print("Нээх хаяг: http://localhost:8765  (зогсоох: Ctrl+C)")
    ThreadingHTTPServer(("localhost", 8765), Handler).serve_forever()