# $language = "python"
# $interface = "1.0"

while True:
    crt.Screen.Send("shutdown\n")
    crt.Sleep(10000)
    crt.Screen.Send("no shutdown\n")
    crt.Sleep(10000)