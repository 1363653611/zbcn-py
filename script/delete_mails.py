#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zbcn8'

import time
from selenium import webdriver

def login_mail(account,pwd):
	chorm = webdriver.Chrome()
	chorm.get("https://www.136.com/")
	time.sleep(3)
	iframe = chorm.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
	chorm.switch_to.frame(iframe)
	chorm.find_element_by_name('email').send_keys(account)
	chorm.find_element_by_name("password").send_keys(pwd)
	chorm.find_element_by_id("dologin").click()
	time.sleep(3)
	try:
		chorm.find_element_by_xpath('//div[@class="btnbox"]/a').click()
	except:
		pass
	finally:
		chorm.implicitly_wait(10)

	return chorm

def delete_mails(chorm,type='垃圾邮件'):
	chorm.find_element_by_id("spnHideFolders").click()
	chorm.implicitly_wait(10)
	spans = chorm.find_elements_by_tag_name('span')
	for span in spans:
		if span.text==type:
			span.click()
	time.sleep(3)
	chorm.find_element_by_id("fly0").click()
	chorm.find_element_by_xpath("//div[@role='toolbar']/div[2]//span").click()
	time.sleep(2)
	chorm.find_element_by_xpath("//div[@role='alert']/div[@class='nui-msgbox-ft']/div/div[1]/span").click()
	print("已经删除{}中的邮件".format(type))
	chorm.close()

def read_account():
	with open("emailinfo.csv") as f:
		pass

if __name__ =="__main__":
	chorm = login_mail("account","pwd")
	delete_mails(chorm,"订阅邮件")