#! /usr/bin/env python
# encoding=utf-8


import requests
import json
import random

def chooseIp(iplist, ip):
    key1 = 'veid=621239&api_key=private_pY1njpveMCnDqkFBdgHtuCPK'
    key2 = 'veid=621240&api_key=private_FUmYJDXh4kqanT9QXEWYYWPl'
    if ip == iplist[0]:
        return key1
    if ip == iplist[1]:
        return key2

def getIplist():
    url1 = "https://api.64clouds.com/v1/getServiceInfo?veid=621239&api_key=private_pY1njpveMCnDqkFBdgHtuCPK"
    status = 788888
    while status == 788888:
        #info1 = json.loads(requests.get(url1, proxies={'http':'socks5://localhost:1080'}).content)
        info1 = json.loads(requests.get(url1).content)
        print info1
        status = info1['error']
    IP1 = info1['ip_addresses']
    url2 = "https://api.64clouds.com/v1/getServiceInfo?veid=621240&api_key=private_FUmYJDXh4kqanT9QXEWYYWPl"
    status2 = 788888
    while status2 == 788888:
        info2 = json.loads(requests.get(url2).content)
        status2 = info2['error']
    IP2 = info2['ip_addresses']
    iplist = []
    iplist.append(str(IP1[0]))
    iplist.append(str(IP2[0]))
    print iplist
    return iplist


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
    iplist = getIplist()
    ip = raw_input("choose ip you want to change:   ").strip()
    KEY = chooseIp(iplist, ip) 
    available_location = getLocations(KEY)
    i = random.randint(0,2)
    new_ip = available_location[i]
    result = migrateLocation(KEY, new_ip)
    print 'new ip is: ',result
   

if __name__ == '__main__':
    main()
