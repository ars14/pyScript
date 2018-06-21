# $language = "python"
# $interface = "1.0"


crt.Screen.Send("admin\n")
crt.Sleep(50)
crt.Screen.Send("admin@139\n")
crt.Sleep(50)
crt.Screen.Send("en\n")
crt.Sleep(50)
crt.Screen.Send("restore d\n")
crt.Sleep(50)
crt.Screen.Send("yes\n")
crt.Sleep(50)