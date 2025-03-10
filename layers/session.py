class SessionLayer:
    def send(self, data):
        print("[Session] Managing session state...")
        return f"SESSION_START|{data}|SESSION_END"

    def receive(self, data):
        print("[Session] Managing session state...")
        if data.startswith("SESSION_START|") and data.endswith("|SESSION_END"):
            return data.replace("SESSION_START|", "").replace("|SESSION_END", "")
        return "[Error] Malformed session data"