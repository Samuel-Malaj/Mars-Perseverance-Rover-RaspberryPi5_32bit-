from evdev import InputDevice, categorize, ecodes

def Wireless_control():
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
	v = None
	for event in dev.read_loop():
		if event.type == ecodes.EV_KEY and event.value == 1: #If control is regular button press e.g X O △ ◻	
			if event.code in button_map:			
				v = button_map[event.code]
				
		elif event.type == ecodes.EV_ABS: #If control sent is a trigger button e.g L2 R2
			if event.code == RT:	
				v = event.value, 'R'
				
			elif event.code == LT:
				v = event.value, 'L'
		break
		
	if v:
		return v

while True:
	print(Wireless_control())
