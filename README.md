# Mars-Perseverance-Rover-RaspberryPi5_32bit-

3D Printed | Bluetooth Controlled | Live Camera Feed
A fully functional 3D printed replica of NASA's Mars Perseverance Rover, controlled wirelessly via a PlayStation 4 controller over Bluetooth and powered by a Raspberry Pi 5. The rover streams a live camera feed over Wi-Fi and features a servo-driven rotating camera mast — just like the real thing.

🚀 Features

3D Printed chassis modelled after NASA's Mars Perseverance Rover
PS4 Controller support via Bluetooth for intuitive wireless control
Skid steering — drive forwards, backwards, left and right
Servo-controlled camera mast — rotate the camera left and right
Live camera stream broadcast over Wi-Fi, viewable from any browser on the same network
Powered by Raspberry Pi 5 — the brain of the entire operation


🛠️ Hardware
ComponentDetailsSingle Board ComputerRaspberry Pi 5ControllerPlayStation 4 DualShock (Bluetooth)Drive MotorsDC motors with skid steeringCamera ActuationServo motor (left/right pan)CameraRaspberry Pi Camera ModuleChassisCustom 3D printed — Perseverance Rover inspiredPowerLiPo battery pack

💻 Software & Dependencies

evdev — PS4 controller input via Bluetooth (Linux input events)
gpiozero — motor and servo control (LED, PWMLED, Servo)
picamera2 — camera capture and encoding
Pillow (PIL) — image processing and motion detection
smtplib / email — email notification support (stdlib, no install needed)
http.server — live camera stream server (stdlib, no install needed)

Install dependencies:
bashsudo apt update && sudo apt upgrade -y
sudo apt install -y python3-picamera2 python3-gpiozero ffmpeg
pip3 install evdev Pillow

Note: picamera2 and gpiozero are best installed via apt on Raspberry Pi OS rather than pip to ensure full hardware compatibility.


📡 How It Works

The Raspberry Pi 5 boots and creates its own Wi-Fi hotspot network
The PS4 controller is connected to the Pi over Bluetooth
Controller inputs are read via evdev and mapped to motor commands for skid steering
The right analogue stick controls steering and D-Pad buttons pan the camera servo
The camera feed is captured and streamed live — accessible via browser once connected to the rover's network


🎮 Controls
InputActionR2 (Right Trigger)Drive forwardsL2 (Left Trigger)Drive in reverseRight Analogue Stick — Left/RightSkid steer left / rightD-Pad LeftRotate camera mast left (incremental step)D-Pad RightRotate camera mast right (incremental step)

📷 Live Camera Feed
The Raspberry Pi creates its own Wi-Fi hotspot on boot. Connect to it and navigate to:
http://<RaspberryPi IP>:8000/stream
The live MJPEG stream will load automatically.
Hotspot credentials:
FieldValueNetwork Name (SSID)Mars_Perseverance_RoverPasswordMarsRover123

The hotspot SSID and password can be changed in Hotspot.py.


🖨️ 3D Printing
The chassis is designed to replicate the iconic look of NASA's Perseverance Rover. Print settings:

Material: PLA or PETG recommended
Infill: 20–30%
Supports: Required for overhanging parts
Scale: Adjust to fit your motor and servo dimensions


🔧 Planned Features

Simplified PS4 controller pairing — streamlined Bluetooth connection process to make setup faster and more convenient
On-board image capture — ability to take and save still photos directly from the rover camera via controller input
Further improvements to drive performance and camera stability


👨‍💻 About
Built by Samuel Malaj — aspiring astronautical engineer with a passion for space exploration, robotics, and clean energy technology. This project combines a love of planetary science with hands-on embedded systems engineering.

📄 License
MIT License — feel free to build your own, improve it, and share it.

"Dare mighty things." — NASA Mars Perseverance Rover mission
