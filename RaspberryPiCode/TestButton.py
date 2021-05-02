from gpiozero import LED, Button
from time import sleep

print("True")

led = LED(17)
button = Button(2)

while True:

    if button.is_pressed:
        led.on()
    else:
        led.off()