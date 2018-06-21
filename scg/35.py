#coding=utf-8
from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import scg_def

#ipsec = webdriver.Chrome()
#打开谷歌浏览器

#ipsec.implicitly_wait(20)
#设置元素加载等待时间 20s


scg_def.login_web("10.2.2.35","admin","admin@139","0613")

scg_def.add_netIneterface("58.5.6.2","24","/html/body/div[1]/div[2]/div/table/tbody/tr[6]/td[9]/a/img")

#6 /html/body/div[1]/div[2]/div/table/tbody/tr[7]/td[9]/a/img
#5 /html/body/div[1]/div[2]/div/table/tbody/tr[6]/td[9]/a/img

scg_def.add_ipsecRemoteGW_inhand("test1","ge0/1","10.2.2.33","CN=195.1.61.15","CN=195.1.61.16","35.1.1.0/24","33.1.1.0/24")

scg_def.save_sys_inhand()


