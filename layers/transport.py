class TransportLayer:
    def send(self, data):
        print("[Transport] Sequencing and error checking...")
        segment = f"SEQ:1|{data}|ACK"
        return segment

    def receive(self, segment):
        print(f"[Transport] Validating sequence and acknowledging... Received Segment: {segment}")
        parts = segment.split('|')
        if len(parts) < 3:  # Expecting at least "SEQ:x|data|ACK"
            raise ValueError(f"[Transport] Malformed segment received: {segment}")
        
        # Extract data (ignoring SEQ:x and ACK)
        return '|'.join(parts[1:-1])
