#coding=utf-8

"""
使用谷歌浏览器下载功能、web服务器，随机时间去下载；
用于流量稳定性测试

"""

from selenium import webdriver
import time 
import random
import shutil


#打开谷歌浏览器
ipsec = webdriver.Chrome()

#窗口最大化
#ipsec.maximize_window()

#设置元素加载等待时间 20s
ipsec.implicitly_wait(20)

testNum = 0
fileDownloadNum = 1

#初始删除下载目录
try:
	shutil.rmtree(r'D:\Documents\Downloads')
	
except PermissionError:
	print("初始删除D:\Documents\Downloads失败\n")
	
except FileNotFoundError:
	print("不存在D:\Documents\Downloads\n")	
	

while True:
	testNum += 1
	
	#显示当前测试序号
	print ("test" + str(testNum) + "  " + time.ctime()  + "\n")
	
	#下载文件，只支持谷歌浏览器
	webStatus = ipsec.get("http://10.1.1.47/Users/admin/Documents/rtstreamsink.ax.txt")
	
	if webStatus != None:
	
		#生成随机时间，用于下载文件的间隔，10秒~172900秒（2天零100秒）
		sleepTime = random.randint(10,20)

		#显示当前下载文件数量和下载间隔时间
		print("======== 下载中...NO." +str(fileDownloadNum) +"==="+ str(sleepTime) + " 秒后,开始下一次下载======="+"\n")
		
		time.sleep(sleepTime)	
		
		fileDownloadNum += 1
		
	else:
		print("获取文件失败，检查网络或者HTTP服务器\n")
		time.sleep(10)
	
	if fileDownloadNum > 20:
	
		try:
		
			shutil.rmtree(r'D:\Documents\Downloads') #删除文件夹
			
		except PermissionError:
		
			print("文件下载ing...暂时无法删除\n")
			
		else:
		
			print("下载文件超过20个，clean...OK\n")
			
			fileDownloadNum = 1 #下载文件计数重置

