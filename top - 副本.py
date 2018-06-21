# $language = "python" 
# $interface = "1.0" 

while True:
	crt.Screen.Send("shutdown\n")
	crt.Sleep(2000)
	crt.Screen.Send("no shutdown\n")
	
	
	
	
	
#crt.Screen.Send("top -d 1\r")
#crt.Sleep(2000)
#if(crt.Screen.WaitForString("root")):
#	crt.Sleep(1100)
#	crt.Dialog.MessageBox('bye!')