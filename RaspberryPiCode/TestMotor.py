from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(19)
led3 = LED(26)
led4 = LED(21)

def delay():

    sleep(0.002)

def tick():

    print("1",end=" ")
    led1.on()
    led2.off()
    led3.off()
    led4.off()
    delay()
    print("2",end=" ")
    led1.off()
    led2.on()
    led3.off()
    led4.off()
    delay()
    print("3",end=" ")
    led1.off()
    led2.off()
    led3.on()
    led4.off()
    delay()
    print("4")
    led1.off()
    led2.off()
    led3.off()
    led4.on()
    delay()


while True:

    rotationAmount = (float) (input("Enter a number of degrees to turn: "))

    for  i in range(0,(int)((rotationAmount*1.425))):

        tick()

