class TransportLayer:
    def send(self, data):
        print("[Transport] Sequencing and error checking...")
        return f"SEQ:1|{data}|ACK"

    def receive(self, data):
        print("[Transport] Sequencing and error checking...")
        parts = data.split("|")
        if len(parts) >= 3 and parts[0] == "SEQ:1" and parts[-1] == "ACK":
            return "|".join(parts[1:-1])
        return "[Error] Invalid transport data format."