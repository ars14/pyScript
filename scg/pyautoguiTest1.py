import pyautogui
import time

#每个 PyAutoGUI 函数调用在执行动作之后，都会等待一秒半。
pyautogui.PAUSE = 1.5

#将鼠标移到屏幕的左上角，这将导致 pyautogui产生 pyautogui .FailSafeException 异常。
pyautogui.FAILSAFE = True


rr = pyautogui.size()
print(rr)


pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('win.png')))
pyautogui.click(50,830)
pyautogui.typewrite('mspaint')
pyautogui.typewrite(['enter'])

time.sleep(5)

pyautogui.click(100,200) # click to put drawing program in focus

distance = 300
while distance > 0:
	pyautogui.dragRel(distance, 0, duration=0.1) # move right
	distance = distance - 10
	pyautogui.dragRel(0, distance, duration=0.1) # move down
	pyautogui.dragRel(-distance, 0, duration=0.1) # move left
	distance = distance - 10
	pyautogui.dragRel(0, -distance, duration=0.1) # move up
	
