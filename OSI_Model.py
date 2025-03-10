# application.py
import base64

class ApplicationLayer:
    def send(self, message):
        print("[Application] Creating HTTP-like request...")
        # Here we simulate encoding the message for transmission
        return f"HTTP_REQUEST: {message}"

    def receive(self, data):
        print("[Application] Processing HTTP-like response...")
        # Simulate the reception of data
        return data.replace("HTTP_REQUEST: ", "")
        
        
# presentation.py
import base64

class PresentationLayer:
    def send(self, data):
        print("[Presentation] Encoding data...")
        # Encode the data (simulating encryption/encoding)
        return base64.b64encode(data.encode()).decode()

    def receive(self, data):
        print("[Presentation] Decoding data...")
        # Decode the data (simulating decryption/decoding)
        return base64.b64decode(data).decode()
        
        
# session.py
class SessionLayer:
    def send(self, data):
        print("[Session] Managing session state...")
        # Simulate session management (e.g., start, keep alive, or end sessions)
        return f"SESSION_START|{data}|SESSION_END"

    def receive(self, data):
        print("[Session] Managing session state...")
        # Handle session by removing session-specific tags
        return data.replace("SESSION_START|", "").replace("|SESSION_END", "")
        
        
# transport.py
class TransportLayer:
    def send(self, data):
        print("[Transport] Sequencing and error checking...")
        # Adding a sequence number and error checking (for simplicity)
        return f"SEQ:1|{data}|ACK"

    def receive(self, data):
        print("[Transport] Sequencing and error checking...")
        # Remove sequence and ack info (simple)
        return data.replace("SEQ:1|", "").replace("|ACK", "")
        
        
# network.py
class NetworkLayer:
    def send(self, data):
        print("[Network] Adding IP address...")
        # Add IP addressing to the data
        return f"IP_HEADER|{data}|IP_TRAILER"

    def receive(self, data):
        print("[Network] Removing IP address...")
        # Remove IP address information
        return data.replace("IP_HEADER|", "").replace("|IP_TRAILER", "")
        
        
# data_link.py
class DataLinkLayer:
    def send(self, data):
        print("[Data Link] Framing data...")
        # Simulate framing data with link layer addressing
        return f"MAC_HEADER|{data}|MAC_TRAILER"

    def receive(self, data):
        print("[Data Link] Unframing data...")
        # Remove link layer framing
        return data.replace("MAC_HEADER|", "").replace("|MAC_TRAILER", "")
        
        
# physical.py
class PhysicalLayer:
    def send(self, data):
        print("[Physical] Sending bits over the network...")
        # Simulate sending bits (just passing the data along)
        return data

    def receive(self, data):
        print("[Physical] Receiving bits from the network...")
        # Simulate receiving bits
        return data


import socket
from getmac import get_mac_address  # Import getmac to fetch the MAC address


# Function to get the local IP address
def get_local_ip():
    # Attempt to get the local IP address
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  # Google's public DNS to determine the local address
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"Error getting local IP address: {e}")
        return None


# Function to get the MAC address using getmac
def get_mac_address():
    mac = get_mac_address()  # Will fetch the MAC address of the default network interface
    return mac


if __name__ == "__main__":
    # Get local IP and MAC address
    ip_address = get_local_ip()
    mac_address = get_mac_address()

    print(f"Local IP Address: {ip_address}")
    print(f"MAC Address: {mac_address}")

    # Initialize all layers of the OSI model
    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    dl = DataLinkLayer()
    phys = PhysicalLayer()

    message = "Hello, Network!"
    print("\nSending Data \n")

    # Send the message through each layer in the OSI model
    data = app.send(message)
    data = pres.send(data)
    data = sess.send(data)
    data = trans.send(data)
    data = net.send(data)
    data = dl.send(data)
    data = phys.send(data)

    print("\nReceiving Data \n")

    # Receive the message through each layer in reverse order
    data = phys.receive(data)
    data = dl.receive(data)
    data = net.receive(data)
    data = trans.receive(data)
    data = sess.receive(data)
    data = pres.receive(data)
    data = app.receive(data)

    print(f"Final message received: {data}\n")
