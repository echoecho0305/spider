#! /usr/bin/env python
# encoding=utf-8


import sys
import json
import time
import random
import hmac
import hashlib
import requests


def add_hmac(params,url):
    p1 = '&'.join(['='.join(i) for i in sorted(params.items(), key=lambda (x,y):x)])
    p2 = 'GET'+url[8:]+'?'+p1
    hmacc = hmac.HMAC('b7YoGertobP9h4FJCuWxC1tdCZmoeIk0', p2, hashlib.sha256).digest().encode('base64').strip()
    params['Signature'] = hmacc
#计算Signature


def describe_regions():
    params = {'Action':'DescribeRegions','Timestamp':str(int(time.time())),'Nonce':str(random.randint(1, 10000)),'SecretId':'AKIDz45va6Cj2EJDDUwWFm7FD4qVyGh2j8sV','SignatureMethod':'HmacSHA256'}
    url = 'https://cvm.api.qcloud.com/v2/index.php'
    add_hmac(params,url)
    message = json.loads(requests.get(url, params).content)
    if message['codeDesc'] != 'Success':
        sys.exit('des_regions fail')
    list = []
    for i in message['regionSet']:
        list.append(i['region'])
    return list
# 查询地域列表


def describe_eip(ip):
    url1 = 'https://eip.api.qcloud.com/v2/index.php'
    regionList = describe_regions()
    for m in regionList:
        params1={'Action':'DescribeEip','Timestamp':str(int(time.time())),'Nonce':str(random.randint(1, 10000)),'SecretId':'AKIDz45va6Cj2EJDDUwWFm7FD4qVyGh2j8sV','SignatureMethod':'HmacSHA256'}
        params1['Region'] = m
        add_hmac(params1, url1)
        message2 = json.loads(requests.get(url1, params1).content)
        if message2['codeDesc'] != 'Success' and message2['codeDesc'] != 'RequestForbidden':
            sys.exit('des_eip fail')
        if message2['code'] == 4300:
            continue
        eipset = message2['data']['eipSet']
        if eipset == []:
            continue
        else:
            total = message2['totalCount']
            for i in range(0,total):
                eip = message2['data']['eipSet'][i]['eip']
                if eip != ip:
                    continue
                if eip == ip:
                    return m
# ip-->region


def describe_eip1(ip, region):
    params1={'Action':'DescribeEip','Timestamp':str(int(time.time())),'Nonce':str(random.randint(1, 10000)),'SecretId':'AKIDz45va6Cj2EJDDUwWFm7FD4qVyGh2j8sV','SignatureMethod':'HmacSHA256'}
    params1['Region'] = region
    url1 = 'https://eip.api.qcloud.com/v2/index.php'
    add_hmac(params1, url1)
    message3 = json.loads(requests.get(url1, params1).content)
    if message3['codeDesc'] != 'Success':
        sys.exit('des_eip1 fail')
    total3 = message3['totalCount']
    for i in range(0,total3):
        eip = message3['data']['eipSet'][i]['eip']
        if eip == ip:
            status = message3['data']['eipSet'][i]['status']
            eipId = message3['data']['eipSet'][i]['eipId']
            unInstanceId = message3['data']['eipSet'][i]['unInstanceId']
            return (status, eipId, eip, unInstanceId)
        else:
            continue
#查询eipId


def describe_eip2(region,eipid):
    params1={'Action':'DescribeEip','Timestamp':str(int(time.time())),'Nonce':str(random.randint(1, 10000)),'SecretId':'AKIDz45va6Cj2EJDDUwWFm7FD4qVyGh2j8sV','SignatureMethod':'HmacSHA256'}
    params1['Region'] = region
    url1 = 'https://eip.api.qcloud.com/v2/index.php'
    add_hmac(params1, url1)
    message3 = json.loads(requests.get(url1, params1).content)
    if message3['codeDesc'] != 'Success':
        sys.exit('des_eip2 fail')
    total3 = message3['totalCount']
    for i in range(0,total3):
        mes3_eipid = message3['data']['eipSet'][i]['eipId']
        if mes3_eipid == str(eipid):
            status = message3['data']['eipSet'][i]['status']
            eip = message3['data']['eipSet'][i]['eip']
            unInstanceId = message3['data']['eipSet'][i]['unInstanceId']
            return (status, mes3_eipid, eip, unInstanceId)
        else:
            continue
    print 'not return'


def unbind_eip(eipId,region):
    params2 = {'Action':'EipUnBindInstance','Timestamp':str(int(time.time())),'Nonce':str(random.randint(1, 10000)),'SecretId':'AKIDz45va6Cj2EJDDUwWFm7FD4qVyGh2j8sV','SignatureMethod':'HmacSHA256'}
    params2['Region'] = region
    params2['eipId'] = eipId
    url2 = 'https://eip.api.qcloud.com/v2/index.php'
    add_hmac(params2,url2)
    mes = json.loads(requests.get(url2, params2).content)
    if mes['codeDesc'] != 'Success':
        sys.exit('unbind fail')
#    print '解绑'


def delete_eip(eipIds,region):
    params3={'Action':'DeleteEip','Timestamp':str(int(time.time())),'Nonce':str(random.randint(1, 10000)),'SecretId':'AKIDz45va6Cj2EJDDUwWFm7FD4qVyGh2j8sV','SignatureMethod':'HmacSHA256',}
    params3['eipIds.0'] = eipIds
    params3['Region'] = region
    url3 = 'https://eip.api.qcloud.com/v2/index.php'
    add_hmac(params3,url3)
    mes1 = json.loads(requests.get(url3, params3).content)
    if mes1['codeDesc'] != 'Success':
        sys.exit('delete fail')
#    print '释放'


def create_eip(region):
    params4 = {'Action':'CreateEip','Timestamp':str(int(time.time())),'Nonce':str(random.randint(1, 10000)),'SecretId':'AKIDz45va6Cj2EJDDUwWFm7FD4qVyGh2j8sV','SignatureMethod':'HmacSHA256'}
    params4['Region'] = region
    url4 = 'https://eip.api.qcloud.com/v2/index.php'
    add_hmac(params4,url4)
    a = json.loads(requests.get(url4, params4).content)
    if a['codeDesc'] != 'Success':
        sys.exit('create fail')
    eipid = a['data']['eipIds']
    return eipid
#    print '申请'


def bind_eip(eipId,uninstanceId,region):
    params5 = {'Action':'EipBindInstance','Timestamp':str(int(time.time())),'Nonce':str(random.randint(1, 10000)),'SecretId':'AKIDz45va6Cj2EJDDUwWFm7FD4qVyGh2j8sV','SignatureMethod':'HmacSHA256'}
    params5['Region'] = region
    params5['eipId'] = eipId
    params5['unInstanceId'] = uninstanceId
    url5 = 'https://eip.api.qcloud.com/v2/index.php'
    add_hmac(params5,url5)
    mess = json.loads(requests.get(url5, params5).content)
    if mess['codeDesc'] != 'Success':
        sys.exit('bind fail')
    return mess
#    print '绑定'


def main():
    ip = raw_input("input ip:  ").strip()
    m = describe_eip(ip)
    result = describe_eip1(ip, m)
    id1 = result[3]
    unbind_eip(result[1],m)
    while describe_eip1(ip, m)[0] != 4:
        pass
    delete_eip(result[1],m)
    result2 = create_eip(m)
    result1 = describe_eip2(m, result2[0])
    while describe_eip2(m, result2[0])[0] != 4:
        pass
    mess = bind_eip(result1[1], id1, m)
    if mess['codeDesc'] == u'Success':
        new_result = describe_eip2(m, result2[0])
        print "new ip is: " + new_result[2]
    else:
        print 'change ip failed'

if __name__ == '__main__':
    main()
