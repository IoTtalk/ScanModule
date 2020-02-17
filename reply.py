import socket, fcntl, struct
INTERFACE = 'eth0'
RECEIVE_PORT = 17000
REPLY_PORT   = 17001

def get_mac_addr():
    from uuid import getnode
    mac = getnode()
    mac = ''.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    return mac

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def listing_scan():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', RECEIVE_PORT))

    while True:
        print ('Listing scan requests...')
        data, addr = s.recvfrom(1024)
        if str(data.decode()) == 'QuantaModule':
            print('Request = {}'.format(addr))
            msg = b'{}, {}'.format(get_ip_address(INTERFACE), get_mac_addr())
            s.sendto(msg, (addr[0], REPLY_PORT))

if __name__ == '__main__':
    listing_scan()
