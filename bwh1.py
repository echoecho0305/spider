#! /usr/bin/env python
# encoding:utf-8


import json
import random
import requests


def getService(key):
    URL = "https://api.64clouds.com/v1/getServiceInfo?"
    url1 = URL+key
    status = 788888
    while status == 788888:
        info1 = json.loads(requests.get(url1).content)
        status = info1['error']


def getLocations(key):
    URL = "https://api.64clouds.com/v1/migrate/getLocations?"
    url3 = URL+key
    info3 = json.loads(requests.get(url3).content)
    a = info3['locations'][0:4]
    b = info3['currentLocation']
    for i in a:
        if i == b:
            a.remove(i)
    return a


def migrateLocation(key, new_ip):
    URL = "https://api.64clouds.com/v1/migrate/start?"
    url4 = URL+key+'&location='+new_ip
    info4 = json.loads(requests.get(url4).content) 
    c = info4['newIps']
    return c


def main():
    key = raw_input("input veid and key :").strip()
    a = getService(key)
    available_locations = getLocations(key)
    i = random.randint(0,2)
    new_ip = available_locations[i]
    result = migrateLocation(key, new_ip)
    print 'new ip is: ',result


if __name__ == '__main__':
    main()
