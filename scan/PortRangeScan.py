#!/usr/bin/python3
# -*- conding: utf-8 -*-

from .scaning import scaningPoolip
from .scaning import scaningIP
import ipaddress
import multiprocessing



__all__ = ( 'PortRangeScan', )


def PortRangeScan(ip_addres, start, end, timeout, network):
    portlist = [int(i) for i in range(start,end)]
    # Network
    if network != "":
        pool = ipaddress.ip_network(network).hosts()
        listip = [str(i) for i in pool]
        limit = int(len(listip) / 4)
        list1 = listip[:limit]
        list2 = listip[limit:limit * 2]
        list3 = listip[limit * 2:limit * 3]
        list4 = listip[limit * 3:]

        p1 = multiprocessing.Process(target=scaningPoolip, args=(list1, portlist,timeout))
        p2 = multiprocessing.Process(target=scaningPoolip, args=(list2, portlist, timeout))
        p3 = multiprocessing.Process(target=scaningPoolip, args=(list3, portlist, timeout))
        p4 = multiprocessing.Process(target=scaningPoolip, args=(list4, portlist, timeout))

        p1.start()
        p2.start()
        p3.start()
        p4.start()

    else:
        if len(portlist) >= 4:
            limit = int(len(portlist)/4)
            list1 = portlist[:limit]
            list2 = portlist[limit:limit * 2]
            list3 = portlist[limit * 2:limit * 3]
            list4 = portlist[limit * 3:]

            p1 = multiprocessing.Process(target=scaningIP, args=(ip_addres, list1, timeout))
            p2 = multiprocessing.Process(target=scaningIP, args=(ip_addres, list2, timeout))
            p3 = multiprocessing.Process(target=scaningIP, args=(ip_addres, list3, timeout))
            p4 = multiprocessing.Process(target=scaningIP, args=(ip_addres, list4, timeout))
# Start     parallel process
            p1.start()
            p2.start()
            p3.start()
            p4.start()
        else:
            scaningIP(ip_addres, portlist, timeout)