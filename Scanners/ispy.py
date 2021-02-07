"Module for scanning networks and ports"

import os, sys, socket, getopt
from utils.sweeper import Sweeper
from utils.port_scanner import Porty


def parse_cmd_line(argv):
    
    host = None
    port = 80
    timeout = 3
    count = 1

    try:
        opts, args = getopt.getopt(
            argv, "Hh:p:t:c:",['help', 'host=', 'port=', 'count=', 'timeout='])

        if len(opts) == 0:
            print("Usage:\n", " -H, --help = display help\n",
                "-h, --host = host ip address to connect to.\n",
                "-p, --port = port to connect to.\n",
                "-t, --timeout = timeout in seconds per ping.\n",
                "-c, --count = amount to ping per address.\n",)
   
    except getopt.GetoptError as err:
        print('ERROR:', err)
        sys.exit(1)
    
    for opt, arg in opts:
        if opt in ("-H", "--help"):
            print("Usage:\n-H, --help = display help\n",
            "-h, --host = host ip address to connect to.\n",
            "-p, --port = port to connect to.\n",
            "-t, --timeout = timeout in seconds per ping.\n",
            "-c, --count = amount to ping per address.\n")
            sys.exit()
        elif opt in ("-h", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-t", "--timeout"):
            timeout = arg
        elif opt in ("-c", "--count"):
            count = arg
    
    return str(host), port, timeout, count

def select_scan_type():
    print('-' * 50)
    print('SELECT SCAN TYPE:')
    print('-' * 50)
    scan_type = input(
        """
        1. Ping Sweep
        2. Port Scan
        """ )
    print('-' * 50)
    return scan_type


if __name__ == "__main__":
    host, port, timeout, count = parse_cmd_line(sys.argv[1:])
    try:
        scan_type = select_scan_type()
        if scan_type == '1':
            sw = Sweeper(host, int(timeout), int(count))
            strt, end = sw.get_range()
            strt_time = sw.get_time_of_scan()
            print("Starting Scan.")
            sw.start_scan(strt, end)
            end_time = sw.get_time_of_scan()
            elapsed = sw.get_total_scan_time(strt_time, end_time)
            print("Scan completed in " + str(elapsed))
        elif scan_type == '2':
            pt = Porty(host, port)
            if ',' in host or ',' in str(port):
                pt.advanced_port_scan()
            else:
                pt.basic_port_scan()
    
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

    