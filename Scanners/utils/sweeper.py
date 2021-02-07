import os
import platform

from datetime import datetime
from pythonping import ping

class Sweeper:

    def __init__(self, host, timeout, count):
        self.host = host
        self.timeout = timeout
        self.count = count
    
    def get_range(self):
        strt = int(input("Enter the Starting Number: "))
        end = int(input("Enter the Last Number: "))+1
        return strt, end
    
    # def get_os_ping_type(self):
    #     oper = platform.system()
    #     if (oper == "Windows"):
    #         ping = "ping -n 1 "
    #     elif (oper == "Linux"):
    #         ping = "ping -c 1 "
    #     else:
    #         ping = "ping -c 1 "
    #     return ping
    
    def get_time_of_scan(self):
        scan_time = datetime.now()
        return scan_time

    def start_scan(self, strt, end):
        for ip in range(strt, end):
            addr = self.host.split('.')
            del addr[-1]
            addr.append(str(ip))
            addr = '.'.join(addr)
            response = ping(addr,timeout=self.timeout,count=self.count, sweep_start=strt, sweep_end=end).success()
            if response:
                print(addr, "--> Live")
    
    def get_total_scan_time(self, strt_time, end_time):
        time_elapsed = end_time - strt_time
        return time_elapsed

    