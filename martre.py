import argparse
import ipaddress
import socket
import errno

import icmplib


def port_scan(host='192.168.1.1', port=80, timeout=5):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((host, port))
        return True
    except socket.error as err:
        if err.errno == errno.ECONNREFUSED:
            return False


def scan(target, ports=None):
    network = ipaddress.ip_network(address=args.target)
    hosts = icmplib.multiping([str(ip) for ip in network])
    for host in hosts:
        if host.is_alive:
            print(f'{host.address} is up.')
            if ports is not None:
                for port in ports:
                    if port_scan(host.address, port):
                        print(f' :{port} is open.')


if __name__ == "__main__":
    # usage example : 192.168.1.0/24
    parser = argparse.ArgumentParser()
    parser.add_argument("target",
                        help="Target network in CIDR format eg. 192.168.1.0/24")
    parser.add_argument('ports', type=int, nargs='*',
                        help='Ports to scan on alive hosts')
    args = parser.parse_args()
    # print(args.target, type(args.target))
    # print(args.ports, type(args.ports))
    scan(args.target, ports=args.ports)
