#coding=utf-8

"""
用于测试接口UP-DOWN-UP..,结合网桥；
用于模拟网线插拔

"""
from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import random

	

ipsec = webdriver.Chrome()
#打开谷歌浏览器

#ipsec.maximize_window()

ipsec.implicitly_wait(20)
#设置元素加载等待时间 20s



ipsec.get("https://10.2.2.31")
#打开 SCG web

ipsec.find_element_by_xpath("//*[@id='input_username']").send_keys("admin")
#输入帐号

ipsec.find_element_by_xpath("//*[@id='input_password']").send_keys("admin@139")
#输入密码

ipsec.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys("0613")
#万能验证码0013

ipsec.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
#点击登入，验证码让王博先屏蔽掉

ipsec.switch_to.frame("lefttree")
#登入后，定位到左侧frame

ipsec.find_element_by_xpath("/html/body/div[1]/div[2]/header/a").click()
#点击”网络“

ipsec.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[1]/span").click()
#点击”inteface config“

ipsec.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[1]/ul/li[1]/span/a").click()
#点击”物理接口“


while True:

	n = n+1

	inteDown_sleepTime = random.randint(1,180) #接口down多长时间
	
	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("content")
	#定位到内容frame

	ipsec.find_element_by_xpath('/html/body/div[1]/div[2]/div/table/tbody/tr[5]/td[9]/a').click()
	#点击”disable inteface“

	time.sleep(1)

	ipsec.switch_to_alert().accept()
	#接受disable告警
	
	time.sleep(1)
	
	ipsec.find_element_by_xpath('//*[@id="link_but"]').click()
	#点击”return“
	
	print(str(inteDown_sleepTime) + '秒后，开启接口')
	
	time.sleep(inteDown_sleepTime)
	
	ipsec.find_element_by_xpath('/html/body/div[1]/div[2]/div/table/tbody/tr[5]/td[9]/a').click()
	#点击”enable inteface“  

	time.sleep(1)

	ipsec.switch_to_alert().accept()
	#接受enable告警
	
	time.sleep(1)
	
	ipsec.find_element_by_xpath('//*[@id="link_but"]').click()
	#点击”return“
	
	
	inteUp_sleepTime = random.randint(10,100)
	
	print(str(inteDown_sleepTime) + '秒后，开启接口,NO._'+ str(n))
	
	time.sleep(inteUp_sleepTime)
	
	
	
	
	
	
	
	

