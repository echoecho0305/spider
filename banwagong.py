#! /usr/bin/env python
# encoding=utf-8

from selenium import webdriver
from lxml import etree


def login(driver, user, pwd):
    login_url = 'https://www.bwh1.net/clientarea.php?action=products'
    a = driver.get(login_url)
    elem1 = driver.find_element_by_name("username")
    elem1.send_keys(user)
    elem2 = driver.find_element_by_name("password")
    elem2.send_keys(pwd)
    elem3 = driver.find_element_by_xpath("//input[@value='Login']")
    elem3.click()
    try:
        err1 = driver.find_element_by_class_name('alert')
    except:
        print ('000', 'login success')
    else:
        print ('001', err1.text)
    #TODO successful or not

def choose(driver):
    driver.get("https://www.bwh1.net/clientarea.php?action=products")
    driver.save_screenshot("/Users/apple/Desktop/1.png")
    ele1 = driver.find_elements_by_xpath("//tr/td/span[@style ='font-size:80%; line-height:80%']")
    print len(ele1)
    print ('ip1',ele1[0].text)
    print ('ip2',ele1[3].text)
    ip = input("Please choose ip,input '1' or '2':  ")
    elem4 = driver.find_elements_by_xpath("//input[@type='submit']")
    elem4[ip-1].click()
    #TODO choose vps
    driver.switch_to_window(driver.window_handles[1])

def service(driver):
    c1 = driver.find_elements_by_xpath("/html/frameset/frameset/frame")[0]
    d1 = driver.switch_to_frame(c1)
    elem6 = driver.find_elements_by_xpath("//ul/li/a")
    href2 = elem6[9].get_attribute('href')
    driver.get(href2)


def change(driver):
    elem7 = driver.find_elements_by_xpath("//form/p/label")
    if len(elem7) == 0:
        print ("002", 'change ip busy')
        return

    x = 0
    for i in range(len(elem7)):
        if 'current' in elem7[i].text:
            driver.find_elements_by_xpath("//form/p/input")[[0, 1, 2, 5][(i+1)%4]].click()
    elem8 = driver.find_element_by_class_name('vecontrolButton')
    elem8.click()
    elem9 = driver.find_element_by_class_name('vecontrolButton')
    elem9.click()
    elem10 = driver.find_element_by_xpath("//div//p")
    print elem10.text
    #TODO return ip
    
def main():
    driver = webdriver.PhantomJS()
    login(driver, 'xxxxxx', 'xxxxxxx')
    choose(driver)
    service(driver)
    change(driver)
    driver.quit()


if __name__ == '__main__':
    main()
