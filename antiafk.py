import pyautogui 
import random
import time


#AntiAFK bot made for Minecraft to prevent from being kicked out of game for not being at the computer. Has plenty of use cases 
#outside of just Minecraft as well.
while True:
	#Generates random numbers between 100 to 900 which will be used as coordinates on your monitor
	x = random.randint(100, 900)
	y = random.randint(100, 900)
	#Moves to the random generated coordinate at the speed of 1
	pyautogui.moveTo(x,y,1)
	#Amount of time the program will wait till it moves the mouse again randomly. 
	time.sleep(2)