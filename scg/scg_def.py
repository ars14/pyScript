from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
#打开谷歌浏览器

browser.implicitly_wait(20)
#设置元素加载等待时间 20s


def login_web(url,username,password,verificationCode):

	browser.get("https://" + url)
	#打开 SCG web

	browser.find_element_by_xpath("//*[@id='input_username']").send_keys(username)
	#输入帐号

	browser.find_element_by_xpath("//*[@id='input_password']").send_keys(password)
	#输入密码

	browser.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys(verificationCode)
	#验证码0013

	browser.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
	#点击登入，验证码让王博先屏蔽掉

	#browser.switch_to.frame(browser.find_element_by_xpath("/html/frameset/frame"))
	#browser.find_element_by_xpath("/html/body/nav/ul/li[1]/a").click()
	
	#登入后，定位到左侧frame
	browser.switch_to.frame("lefttree")

	
def add_netIneterface(ipadd,netmask,interSeq):

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("lefttree")
	#定位到左侧frame

	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/header/a').click() 
	#点击网络

	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()   
	#展开接口设置   //*[@id="menu"]/div[2]/div/ul/li[1]/span  //*[@id="menu"]/div[2]/div/ul/li[1]/div
 
	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul/li[1]/span/a').click() 

	#点击物理接口   //*[@id="menu"]/div[2]/div/ul/li[1]/ul/li[1]/span/a

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("content")
	#定位到内容frame

	browser.find_element_by_xpath(interSeq).click()
	#点击物理接口1配置

	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ipadd)
	#输入IPadd

	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(netmask)
	#输入netmask

	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click() 
	#点击保存
	
	browser.refresh()
	#刷新一下网页，解决元素找不到的问题
	

	
	
	
	print("inter ok")

	
def add_ipRoute(destination_ip,destination_mask,out_device,gateway):

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("lefttree")
	#定位到左侧frame

	browser.find_element_by_xpath('/html/body/div[1]/div[3]/header/a').click()
	#点击路由

	browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/ul/li[1]/span/a').click()
	#点击静态路由

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("content")
	#定位到内容frame

	browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/div/input[2]').click()
	#点击单网关路由

	browser.find_element_by_xpath('//*[@id="destination_ip"]').send_keys(destination_ip) 
	#输入DesIPadd

	browser.find_element_by_xpath('//*[@id="destination_mask"]').send_keys(destination_mask) 
	#输入netmask

	outInter = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))    
	#定位到出接口的下拉框

	outInter.select_by_visible_text(out_device)
	#选择出接口

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	#clear gateway

	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	#input gateway
	
	#点击保存
	browser.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[2]/div[2]/div/input[2]').click() 
	
	
def save_sys():
	
	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("")
	#登入后，定位到导航frame

	browser.find_element_by_xpath('/html/body/nav/ul/li[3]/a').click()
	#点击”保存“

	browser.switch_to_alert().accept()
	#接受告警

	time.sleep(3)
	
	#接受告警
	browser.switch_to_alert().accept()


def save_sys_inhand():
	
	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame(browser.find_element_by_xpath("/html/frameset/frame"))
	#登入后，定位到导航frame

	browser.find_element_by_xpath('/html/body/nav/ul/li[2]/a').click() 
	#点击”保存“

	browser.switch_to_alert().accept()
	#接受告警

	time.sleep(3)
	
	#接受告警
	browser.switch_to_alert().accept()
	
def set_ssh32user():

	browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/a").click()
	#点击”系统“

	browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/ul/li[1]/span/a").click()
	#点击”管理员“

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("content")
	#定位到内容frame

	browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div/table/tbody/tr[2]/td[11]/a/img").click()
	#点击管理员编辑

	browser.find_element_by_xpath('//*[@id="logintype_3"]').click() 
	#点击SSH

	browser.find_element_by_xpath('//*[@id="newpwd"]').clear()
	#清除密码

	browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()
	#清除在线用户数

	browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys("32")
	#添加在线用户数

	browser.find_element_by_xpath('/html/body/div[1]/div/form/div[2]/div[2]/div/input[2]').click()
	#点击保存

	time.sleep(5)

	#点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()

def add_ipsecRemoteGW_inhand(ipsecRGWname,ipsecRGWinterSeq,ipsecRGWgateway,localid,remoteid,localsubnet,remotesubnet):

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("lefttree")
	#登入后，定位到左侧frame

	browser.find_element_by_xpath("/html/body/div[1]/div[6]/header/a").click()
	#点击”虚拟专网“

	browser.find_element_by_xpath('/html/body/div[1]/div[6]/div/ul/li[3]/span/a').click()
	#点击”远程网关“

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("content")
	#定位到内容frame

	browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/input").click() 
	#点击”增加远程网关“

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="name"]').send_keys(ipsecRGWname)
	#输入name  

	time.sleep(1)
		
	localif = Select(browser.find_element_by_xpath('//*[@id="localif"]'))   

	localif.select_by_visible_text(ipsecRGWinterSeq)
		
	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(ipsecRGWgateway)
	#输入remote IP add 
		
	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="localid"]').send_keys(localid)
	#input local ID 

	#browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(preshared_key) 
	#input republicKey
		
	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="remoteid"]').send_keys(remoteid)
	#input remote ID

	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
	#clear loacl subnet text

	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(localsubnet) 
	#input local subnet 

	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remotesubnet)
	#input remote subnet
		
	time.sleep(1)
	
	browser.find_element_by_xpath('/html/body/form/div[1]/div/div[2]/div[1]/table/tbody/tr[16]/td[1]/a').click()
	#点击”高级“
	
	localif = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))   
	#Phase 1 encry
	
	localif.select_by_visible_text("sm1")
	
	localif = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))   
	#Phase 1 auth
	
	localif.select_by_visible_text("sm3")
	
	
	localif = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))   
	#Phase 2 esp_encry
	
	localif.select_by_visible_text("sm1")
	
	localif = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))   
	#Phase 2 esp_auth
	
	localif.select_by_visible_text("sm3")
	
	browser.find_element_by_xpath('/html/body/form/div[2]/div/div[2]/div[2]/div/input').click() 
	#点击”return“
		
	browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	#点击”保存“
		
	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	#点击”return“
	
def add_ipsecRemoteGW(ipsecRGWname,ipsecRGWinterSeq,ipsecRGWgateway,preshared_key,localsubnet,remotesubnet):

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("lefttree")
	#登入后，定位到左侧frame

	browser.find_element_by_xpath("/html/body/div[1]/div[6]/header/a").click()
	#点击”虚拟专网“

	browser.find_element_by_xpath('/html/body/div[1]/div[6]/div/ul/li[4]/span/a').click()
	#点击”远程网关“

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("content")
	#定位到内容frame

	browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/input").click()
	#点击”增加远程网关“

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="name"]').send_keys(ipsecRGWname)
	#输入name  

	time.sleep(1)
		
	localif = Select(browser.find_element_by_xpath('//*[@id="localif"]'))     

	localif.select_by_visible_text(ipsecRGWinterSeq)
		
	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(ipsecRGWgateway)
	#输入remote IP add 
		
	time.sleep(1)

	#browser.find_element_by_xpath('//*[@id="localid"]').send_keys("CN=195.1.61.16")
	#input local ID 

	browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(preshared_key) 
	#input republicKey
		
	time.sleep(1)
		
	#browser.find_element_by_xpath('//*[@id="remoteid"]').send_keys("CN=195.2.61.16")
	#input remote ID

	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
	#clear loacl subnet text

	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(localsubnet) 
	#input local subnet 

	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remotesubnet)
	#input remote subnet
		
	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	#点击”保存“
		
	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	#点击”return“
	
	
def refresh():
	browser.refresh()
	
def edit_ipsecRemoteGW_inhand(ipsecRGWSeq,encry_1,auth_1,esp_encry_2,esp_auth_2):

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("lefttree")
	#登入后，定位到左侧frame

	browser.find_element_by_xpath("/html/body/div[1]/div[6]/header/a").click()
	#点击”虚拟专网“

	browser.find_element_by_xpath('/html/body/div[1]/div[6]/div/ul/li[3]/span/a').click()
	#点击”远程网关“

	browser.switch_to.default_content()
	#定位到默认frame

	browser.switch_to.frame("content")
	#定位到内容frame

	browser.find_element_by_xpath(ipsecRGWSeq).click() 
	#点击要编辑的ipsec

	time.sleep(5)
	
	browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
	#点击”高级“       //*[@id="conftr_31"]/td[1]/a
	
	localif = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))   
	#Phase 1 encry
	
	localif.select_by_visible_text(encry_1)
	
	localif = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))   
	#Phase 1 auth
	
	localif.select_by_visible_text(auth_1)
	
	
	localif = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))   
	#Phase 2 esp_encry
	
	localif.select_by_visible_text(esp_encry_2)
	
	localif = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))   
	#Phase 2 esp_auth
	
	localif.select_by_visible_text(esp_auth_2)
	
	browser.find_element_by_xpath('/html/body/form/div[2]/div/div[2]/div[2]/div/input').click() 
	#点击”return“
		
	browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	#点击”保存“