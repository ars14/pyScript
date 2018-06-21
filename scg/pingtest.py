import subprocess as sp
ip =['10.168.10.161','10.168.10.209','10.168.10.54','10.168.10.55','10.168.10.123']
good = 0
bad = 0
count = 0
badIp=[]
for url in ip:
    status, result = sp.getstatusoutput("ping " + url + " -w 2000")
    count+=1
    if "请求超时" in result:
        bad+=1
        badIp.append(url)
    else:
        good +=1
print(badIp)
print('总共ping了 %d条ip'%(count))
print('其中%d条有问题'%(bad))
print('%d条没问题'%(good))
print('坏ip是:')
print(badIp)