class DataLinkLayer:
    def send(self, data):
        print("[Data Link] Framing data...")
        return f"MAC_HEADER|{data}|MAC_TRAILER"

    def receive(self, data):
        print("[Data Link] Unframing data...")
        if data.startswith("MAC_HEADER|") and data.endswith("|MAC_TRAILER"):
            return data.replace("MAC_HEADER|", "").replace("|MAC_TRAILER", "")
        return "[Error] Corrupted frame at Data Link Layer."
