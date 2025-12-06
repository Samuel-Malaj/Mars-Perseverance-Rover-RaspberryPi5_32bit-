from gpiozero import PWMLED
from time import sleep

IN3 = PWMLED(2)
IN4 = PWMLED(3)

#forward

sleep(2)
IN3.value = 0.5
sleep(2)
IN3.value = 0
sleep(2)

#reverse
sleep(2)
IN4.value = 0.5
sleep(2)

