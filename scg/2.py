#coding=utf-8
import scg_def
import time

p1en = ["aes256","sm1","sm4"]
p1au = ["md5","sha1","sha256","sha384","sha512","sm3"]

p2en = ["des","3des","aes128","aes192","aes256","sm1","sm4"]
p2au = ["md5","sha1","sha256","sha384","sha512","sm3"]

for i in p1en:
	for j in p1au:
		scg_def.login_web("10.2.2.33","admin","admin@139","0613")

		scg_def.edit_ipsecRemoteGW_inhand("/html/body/div[1]/div[2]/form/div/table/tbody/tr[2]/td[8]/a[1]/img",i,j,i,j)
		
		scg_def.login_web("10.2.2.35","admin","admin@139","0613")

		scg_def.edit_ipsecRemoteGW_inhand("/html/body/div[1]/div[2]/form/div/table/tbody/tr[2]/td[8]/a[1]/img",i,j,i,j)
		
		print(i + "+" + j)
		time.sleep(15)