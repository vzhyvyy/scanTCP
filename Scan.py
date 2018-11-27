#!/usr/bin/python3
# -*- conding: utf-8 -*-

from scan import *
import subprocess
import argparse


AP = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                             description=('''\
        TCP scaner , for testing open ports:
        ------------------------------------

    This script check  open TCP ports to remote ip address:
        > Select which ports you want to scan and write target ip
===============================================================      

       PortRangeScan Example:

                python3 Scan.py --start 1 --end 3390 --ip 192.168.1.1 (scan one ip address)
                python3 Scan.py -s 1 -e 3390 --network 192.168.1.0/24 (scan all network)
                
===============================================================

       PortListScan EXAMPLELE:

                python3 Scan.py  --portlist 80 3389 8080 --ip 192.168.1.1 (scan one ip address)                                                             
                python3 Scan.py   -l 80 3389 8080 --network 192.168.1.0/24 (scan all network)
                
================================================================

       PortFileScan Example:

                python3 Scan.py  --file /home/user/portfile.txt --ip 192.168.1.1 (scan one ip address)
                python3 Scan.py -f portfile.txt --network 192.168.1.0/24 (scan all network)
                
================================================================
    > Check results in file 'Port_Check
    '''))

AP.add_argument('--ip',  type=str, dest='ip_address',
                action='store',help='Target ip address example: 192.168.1.1')
AP.add_argument('--start', '-s', dest='start', action='store',
                type=int, help='Start port range scan!!')
AP.add_argument('--end', '-e', dest='end', action='store',
                type=int, help='End port range scan!!')
AP.add_argument('--timeout', '-t', dest='timeout', action='store',
                type=float, default=0.10, help='Set timeout for tcp connect: default = 0.10')
AP.add_argument('--portlist', '-l', nargs='+', dest='portlist', action='store',
                type=int, help='Enter the ports you want to scan')
AP.add_argument('--file', '-f', dest='file', action='store',
                type=str, help='Path to file  Example [/home/user/portfile.txt]')
AP.add_argument('--network',  dest='network', action='store',
                type=str, default="", help='Enter ip_network  for scan : Example 192.168.1.0/24 ')

ARGS = AP.parse_args()

def main ():
    try:
        if ARGS.start != None and ARGS.end != None:
            PortRangeScan(ARGS.ip_address, ARGS.start, ARGS.end, ARGS.timeout,ARGS.network)
        elif ARGS.portlist != None:
            PortListScan(ARGS.ip_address, ARGS.portlist, ARGS.timeout,ARGS.network)
        elif ARGS.file !=None:
            PortFileScan(ARGS.ip_address, ARGS.file, ARGS.timeout,ARGS.network)
        else:
            subprocess.call('python3 Scan.py -h', shell=True)
    except ValueError:
        print ("Bad args --network ")




if __name__ == "__main__":
    main()


