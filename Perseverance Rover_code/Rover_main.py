from evdev import InputDevice, categorize, ecodes
from gpiozero import LED, PWMLED, Servo
import sys
from images import photo
from picamera2 import Picamera2, encoders
import time

servo = Servo(27, min_pulse_width=0.0005, max_pulse_width=0.0025)
rotation = 0 #rotation of servo

email_adress = ''
app_password = ''

IN1 = PWMLED(17)
IN2 = PWMLED(4)
IN3 = PWMLED(3)
IN4 = PWMLED(2)
GPIO = None
Rturn = False
Lturn = False 

dev = InputDevice('/dev/input/event5') 
#dev = InputDevice('/dev/input/by-id/Wireless Controller')

# Map button codes to letters
button_map = {
	304: 'X', 
	305: 'O', 
	307: '△', 
	308: '◻',
	310: 'L1',
	311: 'R1',
	312: 'L2', 
	313: 'R2',
	314: 'Share',
	315: 'Options',
	316: 'PS',
	317: 'L3', 
	318: 'R3'
}

LT = ecodes.ABS_Z
RT = ecodes.ABS_RZ
RJ = ecodes.ABS_RX
DPAD_X = ecodes.ABS_HAT0X
	
def Wireless_control():	
	v = None
	for event in dev.read_loop():
		if event.type == ecodes.EV_KEY and event.value == 1: #If control is regular button press e.g X O △ ◻	
			if event.code in button_map:			
				v = button_map[event.code], 'Button'
				
		elif event.type == ecodes.EV_ABS: #If control sent is a trigger button e.g L2 R2
			if event.code == RT:					
				v = event.value, 'R'
								
			elif event.code == LT:
				v = event.value, 'L'
				
			elif event.code == RJ:
				v = event.value - 127.5, 'J'
				
		if event.type == ecodes.EV_ABS and event.code == DPAD_X:
			if event.value == -1:
				v = 'DL', 'DPAD'
			elif event.value == 1:
				v = 'DR', 'DPAD'
		break
		
	if v:
		return v


while True:
	v = Wireless_control()
	print(v)

	if v:
		typ = v[1]
		v = v[0]
	########################### TRIGGER INPUT ################## 
	if type(v) is int or type(v) is float:  
		if typ == 'R':      ## right trigger
			IN3.value = 1
			IN1.value = 1
			GPIO = IN4, IN2
			current_speed = v
			
		elif typ == 'L':    ## left trigger
			IN4.value = 1
			IN2.value = 1
			GPIO = IN3, IN1
			current_speed = v
			
		elif typ == 'J':    ## joystick
			if v > 90:
				Rturn = True
				print('RIGHT TURN')
				
			elif v < -90:
				Lturn = True
				print('LEFT TURN')
				
			else:
				Rturn = False			
				Lturn = False
				
		if GPIO:
			if Rturn:
				print('if' * 8)
				if current_speed > 200:
					GPIO[0].value = 0
					GPIO[1].value = 1
					
				elif v < 200 and v > 70:
					GPIO[0].value = 1 - (current_speed / 255)
					GPIO[1].value = 1
						
				elif current_speed < 70:
					GPIO[0].value = 1
					GPIO[1].value = 1
					GPIO = None
					
			elif Lturn:
				print('elif' * 8)
				if current_speed > 200:
					GPIO[0].value = 1
					GPIO[1].value = 0
					
				elif current_speed < 200 and v > 70:
					GPIO[0].value = 1 - (current_speed / 255)
					GPIO[1].value = 1
						
				elif current_speed < 70:
					GPIO[0].value = 1
					GPIO[1].value = 1
					GPIO = None
					
			else:
				if current_speed > 200:
					GPIO[0].value = 0
					GPIO[1].value = 0
					
				elif current_speed < 200 and v > 70:
					GPIO[0].value = 1 - (current_speed / 255)
					GPIO[1].value = 1 - (current_speed / 255)
						
				elif current_speed < 70:
					GPIO[0].value = 1
					GPIO[1].value = 1
					GPIO = None
			
	if v == 'DL':
		rotation -= 30
		if rotation >= -90 and rotation <=90:
			servo.value = rotation/90
	
	if v == 'DR':
		rotation += 30
		if rotation >= -90 and rotation <= 90:
			servo.value = rotation/90

	if v == 'R1':
		photo(app_password, email_address)

			
	if v == 'X':
		sys.exit()
		
	

			

		
		
			
			
