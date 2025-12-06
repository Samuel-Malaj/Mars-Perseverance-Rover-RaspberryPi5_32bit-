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

	for event in dev.read_loop():
		if event.type == ecodes.EV_KEY and event.value == 1: # 1 = key press		
			if event.code in button_map:
				
				return button_map[event.code]
				
while True:
	print(Wireless_control())

