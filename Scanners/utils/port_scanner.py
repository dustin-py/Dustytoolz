"""Module for port scanning"""

import sys
import socket

from datetime import datetime

class Porty:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def make_host_list(self):
        try:
            host_list = self.host.split(',')
            return host_list
        except:
            print("Not enough values to make host list.\n",
                "Defaulting to single host.")
            host = self.host
            return host

    def make_port_list(self):
        try:
            port_list = self.port.split(',')
            return port_list
        except:
            print("Not enough values to make port list.\n",
                "Defaulting to single port.")
            port = self.port
            return port

    def basic_port_scan(self):
        try:
            if self.port == '-':
                print("{}:".format(self.host))
                for p in range(1,65535):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((self.host, p))
                    if result == 0:
                        print("Port {} is open".format(p))
                    s.close()
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((self.host, int(self.port)))
                if result == 0:
                    print("Port {} is open".format(self.port))
                s.close()
        except socket.error:
            print("Couldn't connect to server.")
            sys.exit()
            
    def advanced_port_scan(self):
        host = self.make_host_list()
        port = self.make_port_list()
        try:
            if len(host) > 1 and len(port) == 1:
                if self.port == '-':
                    for addr in host:
                        print("{}:".format(addr))
                        for p in range(1,65535):
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            socket.setdefaulttimeout(1)
                            result = s.connect_ex((addr, p))
                            if result == 0:
                                print("Port {} is open".format(p))
                            s.close()
                else:
                    for addr in host:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(1)
                        result = s.connect_ex((addr,int(port)))
                        print("{}:".format(addr))
                        if result == 0:
                            print("Port {} is open".format(port))
                        s.close()
            elif len(port) > 1 and len(host) == 1:
                print("{}:".format(host[0]))
                for p in port:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((host[0],int(p)))
                    if result == 0:
                        print("Port {} is open".format(p))
                    s.close()
            else: 
                for addr in host:
                    print("{}:".format(addr))
                    for p in port:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(1)
                        result = s.connect_ex((addr,int(p)))
                        if result == 0:
                            print("Port {} is open".format(p))
                        s.close()
        except socket.error:
            print("Couldn't connect to server.")
            sys.exit()