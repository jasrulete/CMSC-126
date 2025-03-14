import socket
import uuid

from layers.application import ApplicationLayer
from layers.presentation import PresentationLayer
from layers.session import SessionLayer
from layers.transport import TransportLayer
from layers.network import NetworkLayer
from layers.data_link import DataLinkLayer
from layers.physical import PhysicalLayer 

# Function to get the local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return f"Error getting local IP address: {e}"

# Function to get the MAC address without using 'getmac'
def get_mac():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 48, 8)][::-1])
    return mac if mac else "MAC Address Unavailable"

if __name__ == "__main__":
    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    dl = DataLinkLayer()
    phys = PhysicalLayer()

    data = "HTTP_REQUEST: Hello"
    print("[Application] Sending data: ", data)

    # Simulate the process through OSI layers
    data = pres.send(data)
    data = sess.send(data)
    data = trans.send(data)
    data = net.send(data)
    data = dl.send(data)
    data = phys.send(data)

    # Receive data
    data = phys.receive(data)
    data = dl.receive(data)
    data = net.receive(data)
    data = trans.receive(data)
    data = sess.receive(data)
    data = pres.receive(data)
    data = app.receive(data)

    print(f"\nFinal message received: {data}\n")

    # Print network details
    print(f"Local IP Address: {get_local_ip()}")
    print(f"MAC Address: {get_mac()}")