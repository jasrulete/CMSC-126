from layers.physical import PhysicalLayer
from layers.data_link import DataLinkLayer
from layers.network import NetworkLayer
from layers.transport import TransportLayer
from layers.session import SessionLayer
from layers.presentation import PresentationLayer
from layers.application import ApplicationLayer

if __name__ == "__main__":
    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    dl = DataLinkLayer()
    phys = PhysicalLayer()

    message = "Hello, Network!"
    print("Sending Data \n")
    data = app.send(message)
    data = pres.send(data)
    data = sess.send(data)
    data = trans.send(data)
    data = net.send(data)
    data = dl.send(data)
    data = phys.send(data)

    print(f"Final message received: {data}\n")
