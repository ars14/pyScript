#coding=utf-8

"""
设备不断重启，检测CPU使用率是否正常
"""
from selenium import webdriver
import time 

ipsec = webdriver.Chrome()
#打开谷歌浏览器

#ipsec.maximize_window()

ipsec.implicitly_wait(20)
#设置元素加载等待时间 20s




n1 = 0

while 1:
	
	n1 = n1+1
	
	err = False
	
	print ("test" + str(n1) + "  " + time.ctime()  + "\n")
	
	
	ipsec.get("https://10.2.2.199")

	ipsec.find_element_by_xpath("//*[@id='input_username']").send_keys("admin")
	#输入帐号

	ipsec.find_element_by_xpath("//*[@id='input_password']").send_keys("admin@139")
	#输入密码
	
	ipsec.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys("0013")
	#验证码0013

	ipsec.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
	#点击登入，验证码让王博先屏蔽掉

	ipsec.get("https://10.2.2.101/?q=sys_cpu_precent")
	#要从这个网页获取原始的CPU值

	ipsec_status = ipsec.find_element_by_xpath('/html/body').text 
	#获取CPU文本值

	ipsec_status = ipsec_status.split('|')[1].split(',')
	#对CPU文本中进行切割

	del ipsec_status[4] #列表第四个值是空，需要删除

	
	for num in range(6):  #进行六次获取CPU信息
		
		cpu_num = 0
		
		for n in ipsec_status: #将CPU每个核心的使用率分别打印
					
			print("CPU" + str(cpu_num)  + "当前使用率为："+ n +"%")
			
			cpu_num += 1
			
			if float(n) >= 99.00: 
			
				print("问题复现。\n")
				
				err = True
				
				break
			
			ipsec.refresh()
					
			ipsec_status = ipsec.find_element_by_xpath('/html/body').text 

			ipsec_status = ipsec_status.split('|')[1].split(',')
			
			del ipsec_status[4]
			
		print("*********************************\n")
			
		time.sleep(20)
		
	if err == True:
	
		print("问题复现,脚本停止\n")
		
		break
		
	#去重启设备	
	ipsec.get("https://10.2.2.199")
	
	ipsec.find_element_by_xpath("//*[@id='input_username']").send_keys("admin")
	#输入帐号

	ipsec.find_element_by_xpath("//*[@id='input_password']").send_keys("admin@139")
	#输入密码

	ipsec.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
	#点击登入，验证码让王博先屏蔽掉
	
	ipsec.switch_to.frame("lefttree")
	
	ipsec.find_element_by_xpath('//*[@id="menu"]/div[1]/header/a').click()
	#点击系统

	ipsec.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/ul/li[4]/span/a/span').click()

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
	
	print("===========================等待设备重启================================="+"\n")
	
	time.sleep(100)	
		

