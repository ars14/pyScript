#coding=utf-8
"""
inhand 证书版的ipsec使用
"""


from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select

	

ipsec = webdriver.Chrome()
#打开谷歌浏览器

#ipsec.maximize_window()

ipsec.implicitly_wait(20)
#设置元素加载等待时间 20s

n = 0


			
n = n+1
			
print ("test" + str(n) +"\n")

ipsec.get("https://10.2.2.101")
#打开 SCG web

ipsec.find_element_by_xpath("//*[@id='input_username']").send_keys("admin")
#输入帐号

ipsec.find_element_by_xpath("//*[@id='input_password']").send_keys("admin@139")
#输入密码

ipsec.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys("0013")
#验证码0013

ipsec.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
#点击登入，验证码让王博先屏蔽掉

#ipsec.switch_to.frame(ipsec.find_element_by_xpath("/html/frameset/frame"))
#ipsec.find_element_by_xpath("/html/body/nav/ul/li[1]/a").click()

ipsec.switch_to.frame("lefttree")
#登入后，定位到左侧frame

ipsec.find_element_by_xpath("/html/body/div[1]/div[6]/header/a").click()
#点击”虚拟专网“

ipsec.find_element_by_xpath('//*[@id="menu"]/div[6]/div/ul/li[4]/span/a').click()
#点击”远程网关“


while 1:

	n = n+1

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("content")
	#定位到内容frame

	ipsec.find_element_by_xpath("/html/body/div[1]/div[3]/div/input").click()
	#点击”增加远程网关“

	time.sleep(1)
	
	ipsec.find_element_by_xpath('//*[@id="name"]').send_keys("test" + str(n))
	#输入name

	time.sleep(1)
	
	s1 = Select(ipsec.find_element_by_xpath('//*[@id="localif"]'))    

	s1.select_by_visible_text("ge0/1")
	
	time.sleep(1)

	ipsec.find_element_by_xpath('//*[@id="gateway"]').send_keys("15.1.1.1")
	#输入remote IP add
	
	time.sleep(1)

	#ipsec.find_element_by_xpath('//*[@id="localid"]').send_keys("CN=195.1.61.16")
	#input local ID

	ipsec.find_element_by_xpath('//*[@id="preshared_key"]').send_keys("123456")
	#input republicKey
	
	time.sleep(1)
	
	#ipsec.find_element_by_xpath('//*[@id="remoteid"]').send_keys("CN=195.2.61.16")
	#input remote ID

	time.sleep(1)
	
	ipsec.find_element_by_xpath('//*[@id="localsubnet"]').clear()
	#clear loacl subnet text

	time.sleep(1)
	
	ipsec.find_element_by_xpath('//*[@id="localsubnet"]').send_keys("96.1.1.0/24")
	#input local subnet

	time.sleep(1)
	
	ipsec.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys("78.1.1.0/24")
	#input remote subnet
	
	time.sleep(1)
	
	ipsec.find_element_by_xpath('//*[@id="btn_save"]').click()
	#点击”保存“
	
	time.sleep(1)
	
	ipsec.find_element_by_xpath('//*[@id="link_but"]').click()
	#点击”return“
	

	
	
	
	
	
	
	
	

