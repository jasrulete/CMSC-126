import socket

class PhysicalLayer:
    def send(self, data):
        print("[Physical] Sending bits over the network...")
        return data

    def receive(self, data):
        print("[Physical] Receiving bits from the network...")
        return data