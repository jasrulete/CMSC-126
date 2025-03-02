class NetworkLayer:
    def send(self, data):
        print(f"[Network] Adding IP address... Data: {data}")
        packet = f"IP_HEADER|{data}|IP_TRAILER"
        return packet

    def receive(self, packet):
        print(f"[Network] Removing IP header... Received Packet: {packet}")
        parts = packet.split('|')
        if len(parts) < 3:  # Expecting at least "IP_HEADER|data|IP_TRAILER"
            raise ValueError(f"[Network] Malformed packet received: {packet}")
        return parts[1]  # Extract actual data
