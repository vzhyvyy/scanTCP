# !/usr/bin/python3
#-*- conding: utf-8 -*-

import csv
import os
import json
__all__=( 'dataparser', )


def dataparser(ip_address,port,timeout,date):

    infoscan=[ip_address,port,timeout,date]
    header=["IP-ADDRESS", "Port", "Timeout", "Date"]
    if os.path.isfile('log.csv'):
        with open('log.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(infoscan)
    else:
        with open('log.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(infoscan)

    if os.path.isfile('log.json'):
        with open('log.json', 'a') as f:
            json.dump(infoscan,f)

    else:
        with open('log.json', 'w') as f:
            json.dump(header,f)
            json.dump(infoscan,f)


