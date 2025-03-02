class ApplicationLayer:
    def send(self, message):
        print("[Application] Creating HTTP-like request...")
        return f"HTTP_REQUEST: {message}"

    def receive(self, message):
        print("[Application] Processing HTTP-like response...")
        return message.replace("HTTP_REQUEST: ", "")
