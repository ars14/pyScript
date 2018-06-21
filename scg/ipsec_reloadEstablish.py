#coding=utf-8

"""
测试两台设备建立ipsec后，不断重启，判断ipsec建立情况

"""

from selenium import webdriver
import time 

	

ipsec = webdriver.Chrome()
#打开谷歌浏览器

#ipsec.maximize_window()

ipsec.implicitly_wait(20)
#设置元素加载等待时间 20s

testNum = 0

while 1:
	
	testNum =+ 1
	
	print ("test" + str(testNum) +"\n")
	
	ipsec.get("https://10.2.2.33")
	#打开 SCG web

	ipsec.find_element_by_xpath("//*[@id='input_username']").send_keys("admin")
	#输入帐号

	ipsec.find_element_by_xpath("//*[@id='input_password']").send_keys("admin@139")
	#输入密码
	
	ipsec.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys("0613")
	#万能验证码0013

	ipsec.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
	#点击登入，验证码让王博先屏蔽掉

	#ipsec.switch_to.frame(ipsec.find_element_by_xpath("/html/frameset/frame"))
	#ipsec.find_element_by_xpath("/html/body/nav/ul/li[1]/a").click()

	ipsec.switch_to.frame("lefttree")
	#登入后，定位到左侧frame

	ipsec.find_element_by_xpath("//*[@id='menu']/div[6]/header/a").click()
	#点击”虚拟专网“

	ipsec.find_element_by_xpath("//*[@id='menu']/div[6]/div/ul/li[5]/span/a").click()
	#点击”监控“

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("content")
	#定位到内容frame

	ipsec_status = ipsec.find_element_by_xpath('//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[2]/td[6]').text 
	#获取ipsec当前状态

	print( time.ctime() + "\n"  + "ipsec状态:"+ ipsec_status )
	#输出时间，ipsec状态
	
	if (ipsec_status != "Established "):
		 time.sleep(60) #再给60秒让ipsec尝试建立
		 ipsec_status = ipsec.find_element_by_xpath('//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[2]/td[6]').text
		 if (ipsec_status != "Established "):
				print("问题复现")
				break
    #如果ipsec状态不是建立的，跳出循环，并打印
	print("\n")


	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("lefttree")
	#定位到左侧frame

	ipsec.find_element_by_xpath("//*[@id='menu']/div[1]/header/a").click()
	#点击系统

	ipsec.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/ul/li[4]/span/a').click()
	#点击重启系统 

	time.sleep(3)
	#需要延迟一下，不然重启系统界面刷不出来

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("content")
	#定位到内容frame

	ipsec.find_element_by_xpath("//*[@id='button_area']/div/input").click()
	#点击重启

	ipsec.switch_to_alert().accept()
	#接受重启告警

	ipsec.switch_to_alert().send_keys("test")
	#输入重启原因

	ipsec.switch_to_alert().accept()
	#确定重启原因
	#print("33重启")




	ipsec.get("https://10.2.2.35")
	#重启34的操作
	ipsec.find_element_by_xpath("//*[@id='input_username']").send_keys("admin")

	ipsec.find_element_by_xpath("//*[@id='input_password']").send_keys("admin@139")
	
	ipsec.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys("0613")
	#万能验证码0013

	ipsec.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()

	ipsec.switch_to.frame("lefttree")

	#ipsec.refresh()  

	ipsec.find_element_by_xpath("//*[@id='menu']/div[1]/header/a").click()

	ipsec.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/ul/li[4]/span/a').click()

	time.sleep(3)

	ipsec.switch_to.default_content()

	ipsec.switch_to.frame("content")

	ipsec.find_element_by_xpath("//*[@id='button_area']/div/input").click()

	ipsec.switch_to_alert().accept()

	ipsec.switch_to_alert().send_keys("test")

	ipsec.switch_to_alert().accept()
	
	print("===========================等待设备重启================================="+"\n")
	
	time.sleep(100)
	#等待设备重启的时间
	
	


