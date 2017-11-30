# !/usr/bin/python3
#-*- conding: utf-8 -*-

__all__=('scaningPoolip','scaningIP',)

import socket
import datetime
from scan import dataprser as dp

def scaningPoolip(poollist, portlist, timeout):
    StartScanDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for ip in poollist:
        for port in portlist:
            sock = socket.socket()
            sock.settimeout(timeout)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                sock.connect((str(ip), port))
                print("IP-ADDRESS - {0} Port - {1} - OPEN".format(str(ip), port))
                dp.dataparser(ip, port, timeout, date)

            except:
                continue

def scaningIP(ip_address, portlist, timeout):
    for port in portlist:
        sock = socket.socket()
        sock.settimeout(timeout)
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            sock.connect((ip_address, port))
            print("IP-ADDRESS - {0} Port - {1} - OPEN".format(str(ip_address), port))
            dp.dataparser(ip_address, port, timeout, date)
        except:
             continue
