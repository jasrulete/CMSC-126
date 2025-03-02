class SessionLayer:
    def send(self, data):
        print("[Session] Managing session state...")
        return f"SESSION_START|{data}|SESSION_END"

    def receive(self, data):
        print("[Session] Restoring session state...")
        return data.split('|')[1]
