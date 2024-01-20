from machine import Pin
import time


p13 = Pin(13, Pin.OUT)


for i in range (10):

    p13.value(1)
    time.sleep_ms(1000)

    # 吸合
    p13.value(0)  # 断开

    time.sleep_ms(1000)

