import socket

def capture_traffic(interface, filter=None):
    try:
        # Créer une socket pour capturer le trafic en mode promiscuité
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        sock.bind((interface, 0))

        print(f"Capturing traffic on interface {interface}...")

        while True:
            # Capturer les paquets
            packet = sock.recvfrom(65565)
            print(packet)

    except socket.error as msg:
        print('Socket could not be created: ', msg)
