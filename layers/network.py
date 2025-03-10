class NetworkLayer:
    def send(self, data):
        print("[Network] Adding IP address...")
        return f"IP_HEADER|{data}|IP_TRAILER"

    def receive(self, data):
        print("[Network] Removing IP address...")
        if data.startswith("IP_HEADER|") and data.endswith("|IP_TRAILER"):
            return data.replace("IP_HEADER|", "").replace("|IP_TRAILER", "")
        return "[Error] Malformed packet received at Network Layer."