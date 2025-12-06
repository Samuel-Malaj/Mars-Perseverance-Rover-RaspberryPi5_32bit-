from evdev import InputDevice, categorize, ecodes
from gpiozero import LED, PWMLED
import sys
IN1 = PWMLED(4)
IN2 = PWMLED(17)
IN3 = PWMLED(3)
IN4 = PWMLED(2)

dev = InputDevice('/dev/input/event14')

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
	
def Wireless_control():	
	v = None
	GPIO = None
	for event in dev.read_loop():
		if event.type == ecodes.EV_KEY and event.value == 1: #If control is regular button press e.g X O △ ◻	
			if event.code in button_map:			
				v = button_map[event.code]
				print(v, 'Button')
				
		elif event.type == ecodes.EV_ABS: #If control sent is a trigger button e.g L2 R2
			if event.code == RT:					
				v = event.value, 'R'
								
			elif event.code == LT:
				v = event.value, 'L'
				
			elif event.code == RJ:
				v = event.value - 127.5, 'J'
		break
		
	if v:
		return v


while True:
	v = Wireless_control()
	GPIO = None
	print(v)
	if v:
		typ = v[1]
		v = v[0]
	########################### TRIGGER INPUT ################## 
	if type(v) is int or type(v) is float:  
		current_speed = v

		if typ == 'R':      ## right trigger
			IN3.value = 1
			GPIO = IN4
			
		elif typ == 'L':    ## left trigger
			IN4.value = 1
			GPIO = IN3
			
		elif typ == 'J':    ## joystick
			print(current_speed)		
		
		if GPIO:
			if v > 200:
				GPIO.value = 0
			
			elif v < 200 and v > 70:
				GPIO.value = 1 - (v / 255)
				
			elif v < 70:
				GPIO.value = 1
			

			
	if v == 'X':
		sys.exit()
		
	

			

		
		
			
			
