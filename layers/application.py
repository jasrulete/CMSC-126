class ApplicationLayer:
    def send(self, message):
        print("[Application] Creating HTTP-like request...")
        return f"HTTP_REQUEST:{message}"

    def receive(self, data):
        print("[Application] Processing HTTP-like response...")
        if data.startswith("HTTP_REQUEST:"):
            return data.replace("HTTP_REQUEST:", "")
        return "[Error] Invalid application data"