import socket

class PhysicalLayer:
    def send(self, data):
        print("[Physical] Sending bits over the network...")
        return data.encode('utf-8')  # Convert to bytes

    def receive(self, data):
        print("[Physical] Receiving bits...")
        return data.decode('utf-8')