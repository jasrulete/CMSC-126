import socket
from getmac import get_mac_address

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

# Function to get the MAC address
def get_mac():
    mac = get_mac_address()
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

    # Simulate the process
    data = pres.send(data)
    # print("[Presentation] After Presentation layer: ", data)
    data = sess.send(data)
    # print("[Session] After Session layer: ", data)
    data = trans.send(data)
    # print("[Transport] After Transport layer: ", data)
    data = net.send(data)
    # print("[Network] After Network layer: ", data)
    data = dl.send(data)
    # print("[DataLink] After Data Link layer: ", data)
    data = phys.send(data)
    # print("[Physical] After Physical layer: ", data)

    # Receive data
    data = phys.receive(data)
    # print("[Physical] After receiving data: ", data)
    data = dl.receive(data)
    # print("[DataLink] After receiving from Data Link layer: ", data)
    data = net.receive(data)
    # print("[Network] After receiving from Network layer: ", data)
    data = trans.receive(data)
    # print("[Transport] After receiving from Transport layer: ", data)
    data = sess.receive(data)
    # print("[Session] After receiving from Session layer: ", data)
    data = pres.receive(data)
    # print("[Presentation] After receiving from Presentation layer: ", data)
    data = app.receive(data)
    # print("[Application] Final message: ", data)

    print(f"\nFinal message received: {data}\n")
