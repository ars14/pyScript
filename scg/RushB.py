#coding=utf-8
"""
用于配置测试设备常规配置，戏称Rush B；
主线版本，ipsec
"""

from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select

ipsec = webdriver.Chrome()
#打开谷歌浏览器

#ipsec.maximize_window()

ipsec.implicitly_wait(20)
#设置元素加载等待时间 20s


def login_web(url,username,password,verificationCode):

	ipsec.get(url)
	#打开 SCG web

	ipsec.find_element_by_xpath("//*[@id='input_username']").send_keys(username)
	#输入帐号

	ipsec.find_element_by_xpath("//*[@id='input_password']").send_keys(password)
	#输入密码

	ipsec.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys(verificationCode)
	#验证码0013

	ipsec.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
	#点击登入，验证码让王博先屏蔽掉

	#ipsec.switch_to.frame(ipsec.find_element_by_xpath("/html/frameset/frame"))
	#ipsec.find_element_by_xpath("/html/body/nav/ul/li[1]/a").click()
	
	#登入后，定位到左侧frame
	ipsec.switch_to.frame("lefttree")

def add_netIneterface(ipadd,netmask,interSeq):
	
	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("lefttree")
	#定位到左侧frame

	ipsec.find_element_by_xpath('/html/body/div[1]/div[2]/header/a').click()
	#点击网络

	ipsec.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#展开接口设置

	ipsec.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul/li[1]/span/a').click()
	#点击物理接口

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("content")
	#定位到内容frame

	ipsec.find_element_by_xpath(interSeq).click()
	#点击物理接口1配置

	ipsec.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ipadd)
	#输入IPadd

	ipsec.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(netmask)
	#输入netmask

	ipsec.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click() 
	#点击保存
	
	print("inter ok")
	
def add_ipRoute(destination_ip,destination_mask,out_device,gateway):

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("lefttree")
	#定位到左侧frame

	ipsec.find_element_by_xpath('/html/body/div[1]/div[3]/header/a').click()
	#点击路由

	ipsec.find_element_by_xpath('/html/body/div[1]/div[3]/div/ul/li[1]/span/a').click()
	#点击静态路由

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("content")
	#定位到内容frame

	ipsec.find_element_by_xpath('/html/body/div[1]/form/div[2]/div/input[2]').click()
	#点击单网关路由

	ipsec.find_element_by_xpath('//*[@id="destination_ip"]').send_keys(destination_ip) 
	#输入DesIPadd

	ipsec.find_element_by_xpath('//*[@id="destination_mask"]').send_keys(destination_mask) 
	#输入netmask

	outInter = Select(ipsec.find_element_by_xpath('//*[@id="out_device"]'))    
	#定位到出接口的下拉框

	outInter.select_by_visible_text(out_device)
	#选择出接口

	time.sleep(1)

	ipsec.find_element_by_xpath('//*[@id="gateway"]').clear()
	#clear gateway

	ipsec.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	#input gateway
	
	#点击保存
	ipsec.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[2]/div[2]/div/input[2]').click() 
	
def save_sys():

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("")
	#登入后，定位到导航frame

	ipsec.find_element_by_xpath('/html/body/nav/ul/li[3]/a').click()
	#点击”保存“

	ipsec.switch_to_alert().accept()
	#接受告警

	time.sleep(3)
	
	#接受告警
	ipsec.switch_to_alert().accept()
	
def set_ssh32user():

	ipsec.find_element_by_xpath("/html/body/div[1]/div[1]/header/a").click()
	#点击”系统“

	ipsec.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/ul/li[1]/span/a").click()
	#点击”管理员“

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("content")
	#定位到内容frame

	ipsec.find_element_by_xpath("/html/body/div[1]/div[3]/form/div/table/tbody/tr[2]/td[11]/a/img").click()
	#点击管理员编辑

	ipsec.find_element_by_xpath('//*[@id="logintype_3"]').click() 
	#点击SSH

	ipsec.find_element_by_xpath('//*[@id="newpwd"]').clear()
	#清除密码

	ipsec.find_element_by_xpath('//*[@id="onlinenum"]').clear()
	#清除在线用户数

	ipsec.find_element_by_xpath('//*[@id="onlinenum"]').send_keys("32")
	#添加在线用户数

	ipsec.find_element_by_xpath('/html/body/div[1]/div/form/div[2]/div[2]/div/input[2]').click()
	#点击保存

	time.sleep(5)

	#点击返回
	ipsec.find_element_by_xpath('//*[@id="link_but"]').click()
	
def add_ipsecRemoteGW(ipsecRGWname,ipsecRGWinterSeq,ipsecRGWgateway,preshared_key,localsubnet,remotesubnet):

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("lefttree")
	#登入后，定位到左侧frame

	ipsec.find_element_by_xpath("/html/body/div[1]/div[6]/header/a").click()
	#点击”虚拟专网“

	ipsec.find_element_by_xpath('/html/body/div[1]/div[6]/div/ul/li[4]/span/a').click()
	#点击”远程网关“

	ipsec.switch_to.default_content()
	#定位到默认frame

	ipsec.switch_to.frame("content")
	#定位到内容frame

	ipsec.find_element_by_xpath("/html/body/div[1]/div[3]/div/input").click()
	#点击”增加远程网关“

	time.sleep(1)

	ipsec.find_element_by_xpath('//*[@id="name"]').send_keys(ipsecRGWname)
	#输入name  

	time.sleep(1)
		
	localif = Select(ipsec.find_element_by_xpath('//*[@id="localif"]'))     

	localif.select_by_visible_text(ipsecRGWinterSeq)
		
	time.sleep(1)

	ipsec.find_element_by_xpath('//*[@id="gateway"]').send_keys(ipsecRGWgateway)
	#输入remote IP add 
		
	time.sleep(1)

	#ipsec.find_element_by_xpath('//*[@id="localid"]').send_keys("CN=195.1.61.16")
	#input local ID 

	ipsec.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(preshared_key) 
	#input republicKey
		
	time.sleep(1)
		
	#ipsec.find_element_by_xpath('//*[@id="remoteid"]').send_keys("CN=195.2.61.16")
	#input remote ID

	time.sleep(1)
		
	ipsec.find_element_by_xpath('//*[@id="localsubnet"]').clear()
	#clear loacl subnet text

	time.sleep(1)
		
	ipsec.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(localsubnet) 
	#input local subnet 

	time.sleep(1)
		
	ipsec.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remotesubnet)
	#input remote subnet
		
	time.sleep(1)
		
	ipsec.find_element_by_xpath('//*[@id="btn_save"]').click()
	#点击”保存“
		
	time.sleep(1)
		
	ipsec.find_element_by_xpath('//*[@id="link_but"]').click()
	#点击”return“
	
	
	




#1.登入设备
login_web("10.2.2.31","admin","admin@139","0613")

#2.管理员的SSH开启，在线数32
set_ssh32user()

#3，物理接口IP地址
add_netIneterface("87.1.1.1","24","/html/body/div[1]/div[2]/div/table/tbody/tr[2]/td[9]/a/img")

#4ip route
add_ipRoute("98.1.5.0","24","ge0/1","10.1.1.58")


#5ipsec添加
add_ipsecRemoteGW("test222","ge0/1","10.1.1.223","123456","3.3.3.0/24","54.4.3.0/24")

"""
6.保存配置
"""

save_sys()


print("rush DONE")
