#coding=utf-8
import scg_def
from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select

scg_def.login_web("10.2.2.221","admin","admin@139","0613")

n = 1

while True:
	n += 1
	try:
		scg_def.add_ipsecRemoteGW_inhand("test"+str(n),"ge0/1","10.2.2.35","CN=195.1.61.16","CN=195.1.61.15","33.1.1.0/24","35.1.1.0/24")

	except:
		scg_def.refresh()
		print("ff")



