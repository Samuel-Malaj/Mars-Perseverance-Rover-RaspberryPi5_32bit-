from http.server import BaseHTTPRequestHandler, HTTPServer
from picamera2 import Picamera2
import io
import time

def start_broadcast(host="0.0.0.0", port=8000):
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
    picam2.start()

    class StreamingHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path != '/stream':
                self.send_error(404)
                return

            self.send_response(200)
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()

            try:
                while True:
                    buffer = io.BytesIO()
                    picam2.capture_file(buffer, format='jpeg')
                    frame = buffer.getvalue()

                    self.wfile.write(b'--frame\r\n')
                    self.wfile.write(b'Content-Type: image/jpeg\r\n')
                    self.wfile.write(f'Content-Length: {len(frame)}\r\n\r\n'.encode())
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
                    time.sleep(0.05)  # ~20 FPS
            except BrokenPipeError:
                # Client disconnected
                pass

    server = HTTPServer((host, port), StreamingHandler)
    print(f"Broadcasting on http://{host}:{port}/stream")
    server.serve_forever()
