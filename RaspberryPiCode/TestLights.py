from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(26)
led3 = LED(19)

while True:

    print("on")
    led1.on()
    sleep(0.5)
    print("off")
    led1.on()
    sleep(0.5)