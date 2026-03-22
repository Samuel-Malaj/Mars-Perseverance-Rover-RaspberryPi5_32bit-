import subprocess

HOST_NAME = 'Mars_Perseverance_Rover'
HOTSPOT_PASSWORD = 'MarsRover123'
IP = '10.67.67.67'

def Create_Hotspot():
	"""Scan for available WiFi SSIDs"""
	result = subprocess.run(
		["nmcli", "-t", "-f", "SSID", "dev", "wifi", "list"],
		capture_output=True,
		text=True
	)
	networks = result.stdout.splitlines()

	if 'Mars_Perseverance_Rover' not in networks:
		subprocess.run([
		"nmcli", "device", "wifi", "hotspot",
		"ssid", HOST_NAME,
		"password", HOTSPOT_PASSWORD
	])
