#! /usr/bin/env python
# encoding=utf-8


from selenium import webdriver
from lxml import etree
import time
driver = webdriver.Chrome()


def login(driver,user,pwd):
    print '1'
    login_url = 'https://cloud.tencent.com/login?s_url=https%3A%2F%2Fcloud.tencent.com%2F%3FfromSource%3Dgwzcw.234976.234976.234976'
    driver.get(login_url)
    print '2'
    ele1 = driver.find_elements_by_xpath("//em//i[@class='qq-login-icon']")
    ele1[0].click()
    a = driver.find_elements_by_xpath("//div[@class='lg-content']//iframe")
    driver.switch_to_frame(a[0])
    ele2 = driver.find_elements_by_xpath("//input")
    ele2[1].send_keys(user)
    ele2[2].send_keys(pwd)
    ele2[4].click()


def console(driver):
    ele3 = driver.find_elements_by_xpath("//div[@class='c-nav-links']//a")
    ele3[4].click()
    time.sleep(2)


def host(driver):
    ele4 = driver.find_elements_by_xpath("//div[@class='product-item']")
    ele4[0].click()


def city(driver):
    ele5 = driver.find_elements_by_xpath("//div[@class='tc-15-rich-radio ']//button")
    ele5[1].click()
    time.sleep(2)


def a(driver):
    ele6 = driver.find_elements_by_xpath("//dd/a[@class='menu-lv2']/span")
    ele6[7].click()
    time.sleep(2)


def unbund(driver):
    #解绑
    elem = driver.find_elements_by_class_name("tc-15-table-box")[1]
    elem.click()
    ele7 = driver.find_elements_by_xpath("//span//a")
    ele7[1].click()
    ele8 = driver.find_elements_by_xpath("//div[@class='dialog_layer_ft']//a//span")
    ele8[0].click()
    time.sleep(2) 
    ele9 = driver.find_elements_by_xpath("//div[@class='dialog_layer_ft']//a//span")
    ele9[0].click()
    time.sleep(5) 
    

def release(driver):
    #释放
    driver.find_elements_by_class_name("tc-15-table-box")[1].click() 
    ele = driver.find_elements_by_xpath("//span//a") 
    ele[2].click()
    time.sleep(2)
    ele10 = driver.find_elements_by_xpath("//div[@class='tc-15-confirm-popout-ft']//button")
    ele10[0].click()
    time.sleep(10)
    #申请绑定
    ele11 = driver.find_elements_by_xpath("//div[@class='tc-15-action-panel']//button")
    ele11[0].click()
    time.sleep(2)
    ele9 = driver.find_elements_by_xpath("//div[@class='dialog_layer_ft']//a//span")
    ele9[0].click()
    time.sleep(6)
    #绑定
    driver.find_elements_by_class_name("tc-15-table-box")[1].click()  
    ele = driver.find_elements_by_xpath("//span//a")
    ele[0].click()
    time.sleep(5)
    ele12 = driver.find_elements_by_xpath("//td//div//input")
    ele12[0].click()
    time.sleep(2)
    ele13 = driver.find_elements_by_xpath("//div[@class='dialog_layer_ft']//a")
    ele13[0].click()
    time.sleep(2)
    ele14 = driver.find_elements_by_xpath("//div[@class='dialog_layer_ft']//a//span")
    ele14[0].click()


def main():
    global driver
    login(driver,'xxxxxx','xxxxxxx')
    time.sleep(2)
    console(driver)
    time.sleep(2)
    host(driver)
    time.sleep(2)
    city(driver)
    a(driver)
    unbund(driver)
    release(driver)


if __name__ == '__main__':
    main()
