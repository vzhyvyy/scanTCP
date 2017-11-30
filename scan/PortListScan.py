1#!/usr/bin/python3
# -*- conding: utf-8 -*-

__all__ = ( 'PortListScan', )

from .scaning import scaningPoolip
from .scaning import scaningIP
import ipaddress
import multiprocessing

def PortListScan(ip_addres, portlist, timeout, network):
    if network !="":
        pool = ipaddress.ip_network(network).hosts()
        listip = [str(i) for i in pool]
        limit = int(len(listip) / 4)
        list1 = listip[:limit]
        list2 = listip[limit:limit * 2]
        list3 = listip[limit * 2:limit * 3]
        list4 = listip[limit * 3:]
        ports = portlist

        p1 = multiprocessing.Process(target=scaningPoolip, args=(list1, ports,timeout))
        p2 = multiprocessing.Process(target=scaningPoolip, args=(list2, ports,timeout))
        p3 = multiprocessing.Process(target=scaningPoolip, args=(list3, ports,timeout))
        p4 = multiprocessing.Process(target=scaningPoolip, args=(list4, ports,timeout))

        p1.start()
        p2.start()
        p3.start()
        p4.start()

    else:
        if len(portlist)>=4:
            limit = int(len(portlist) / 4)
            list1 = portlist[:limit]
            list2 = portlist[limit:limit * 2]
            list3 = portlist[limit * 2:limit * 3]
            list4 = portlist[limit * 3:]

            p1 = multiprocessing.Process(target=scaningIP, args=(ip_addres, list1, timeout))
            p2 = multiprocessing.Process(target=scaningIP, args=(ip_addres, list2, timeout))
            p3 = multiprocessing.Process(target=scaningIP, args=(ip_addres, list3, timeout))
            p4 = multiprocessing.Process(target=scaningIP, args=(ip_addres, list4, timeout))

            p1.start()
            p2.start()
            p3.start()
            p4.start()

        else:
            scaningIP(ip_addres,portlist,timeout)

