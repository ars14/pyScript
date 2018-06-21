#coding=utf-8
import scg_def



scg_def.login_web("10.2.2.33","admin","admin@139","0613")

scg_def.set_ssh32user()

scg_def.add_netIneterface("33.1.1.1","24",'//*[@id="table"]/tbody/tr[6]/td[9]/a/img')

scg_def.add_netIneterface("2.2.2.33","24",'/html/body/div[1]/div[2]/div/table/tbody/tr[7]/td[9]/a')

scg_def.add_ipsecRemoteGW_inhand("test1","ge0/1","10.2.2.35","CN=195.1.61.16","CN=195.1.61.15","33.1.1.0/24","35.1.1.0/24")

scg_def.save_sys_inhand()


