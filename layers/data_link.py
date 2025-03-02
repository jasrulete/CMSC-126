class DataLinkLayer:
    def send(self, data):
        print(f"[Data Link] Framing data... Data: {data}")
        frame = f"MAC_HEADER|{data}|MAC_TRAILER"
        return frame

    def receive(self, frame):
        print(f"[Data Link] Removing MAC frame... Received Frame: {frame}")
        parts = frame.split('|')
        if len(parts) < 3:  # Expecting at least "MAC_HEADER|data|MAC_TRAILER"
            raise ValueError(f"[Data Link] Malformed frame received: {frame}")
        
        # Extract data (ignore first and last parts)
        return '|'.join(parts[1:-1])
