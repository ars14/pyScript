# $language = "python"
# $interface = "1.0"

crt.Screen.Send("admin\n")
crt.Sleep(200)
crt.Screen.Send("admin@139\n")
crt.Sleep(200)
crt.Screen.Send("en\n")
crt.Sleep(200)
crt.Screen.Send("conf t\n")
crt.Sleep(200)
crt.Screen.Send("inte gigabitethernet ge0/1\n")
crt.Sleep(200)
crt.Screen.Send("no ip add 192.168.1.1\n")
crt.Sleep(200)
crt.Screen.Send("ip add 10.2.2.8 24\n")
crt.Sleep(200)
crt.Screen.Send("exit\n")
crt.Sleep(200)
crt.Screen.Send("ip route 0.0.0.0/0 gateway 10.2.2.1\n")
crt.Sleep(200)
crt.Screen.Send("exit\n")
crt.Sleep(200)
crt.Screen.Send("save\n")
crt.Sleep(200)
crt.Screen.Send("show ip add\n")
crt.Screen.Send("show ip route\n")