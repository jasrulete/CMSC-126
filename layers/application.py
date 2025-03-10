class ApplicationLayer:
    def send(self, message):
        print("[Application] Creating HTTP-like request...")
        return f"HTTP_REQUEST:{message}"

    def receive(self, data):
        print("[Application] Receiving Data: ", data)  # Debug log
        try:
            if "HTTP_REQUEST:" not in data:
                print("[Error] Invalid application data")
                return "[Error] Invalid application data"
            return data.replace("HTTP_REQUEST: ", "")
        except Exception as e:
            print(f"[Error] Exception in Application Layer: {e}")
            return "[Error] Invalid application data"

