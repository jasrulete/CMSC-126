import base64

class PresentationLayer:
    def send(self, data):
        print("[Presentation] Encoding data...")
        return base64.b64encode(data.encode()).decode()

    def receive(self, data):
        print("[Presentation] Decoding data...")
        try:
            return base64.b64decode(data).decode()
        except Exception as e:
            return f"[Error] Decoding failed: {e}"