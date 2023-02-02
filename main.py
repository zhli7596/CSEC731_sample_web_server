import socket
import re
import request_parser

def socket_init(socket_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    s.bind(("", socket_port))

    return s

def main(arg):
    parser(arg)

if __name__ == "__main__":
    main(sys.argv[1])