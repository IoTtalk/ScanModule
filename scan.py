import socket, time
BROADCAST_PORT = 17000
RECEIVE_PORT   = 17001

if __name__ == '__main__':
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    skt.bind(('0.0.0.0', RECEIVE_PORT))
    skt.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    skt.sendto(b'QuantaModule', ('<broadcast>', BROADCAST_PORT))
    print('Scan message sent.')

    index = 0
    while True:
        try:
            data, addr = skt.recvfrom(1024)
            index+=1
            print('{}: {}'.format(index, data.decode()))
        except OSError:     # Network is unreachable
            print('OSError', e)
            time.sleep(3)
            exit()


