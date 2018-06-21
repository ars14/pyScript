# $language = "python"
# $interface = "1.0"

n = 0


crt.Screen.Send("en\n")
crt.Sleep(200)
crt.Screen.Send("conf t\n")
crt.Sleep(200)
crt.Screen.Send("inte gigabitethernet ge0/4\n")
crt.Sleep(200)

while n <= 255:


	ipAdd = "37.38." + str(n) + ".1"

	crt.Screen.Send("ip add " + ipAdd + " 24\n")
	crt.Sleep(200)
	n += 1