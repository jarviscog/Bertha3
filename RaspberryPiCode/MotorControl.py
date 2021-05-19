from gpiozero import LED
from time import sleep


def delay():

    sleep(0.002)

def tick(led1,led2,led3,led4):

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