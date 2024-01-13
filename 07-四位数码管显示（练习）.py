'''
#共阴极点亮,也就是说Led.Value(0),abcdefg这些口Value（1）时灯亮。这个很重要。拿到产品首先要搞清楚的。
'''
import machine
import time

led1 = machine.Pin(5, machine.Pin.OUT)
led2 = machine.Pin(18, machine.Pin.OUT)
led3 = machine.Pin(19, machine.Pin.OUT)
led4 = machine.Pin(21, machine.Pin.OUT)

'''以下代码用来测试共阴极还是共阳极。
# led1.value(0)
# led2.value(0)
# led3.value(0)
# led4.value(0)
'''
led_light_list = [led1, led2, led3, led4]#这是四个led引脚接口。

'''
先定义ESP32板子上的引脚对应的led灯的灯管。
'''
a = machine.Pin(13, machine.Pin.OUT)
b = machine.Pin(12, machine.Pin.OUT)
c = machine.Pin(14, machine.Pin.OUT)
d = machine.Pin(27, machine.Pin.OUT)
e = machine.Pin(26, machine.Pin.OUT)
f = machine.Pin(25, machine.Pin.OUT)
g = machine.Pin(33, machine.Pin.OUT)
dot = machine.Pin(32, machine.Pin.OUT)


'''
创建一个序列，用来存储电平的值（1或0）
'''
number_led = [a, b, c, d, e, f, g, dot]


'''
创建一个字典，用来存储需要显示的数字（Key），以及该数字对应的
各灯管（7根灯管和一个点）的亮灭（Value），1代表高电平，阳极。
'''
number_dict = {
    0: "11111100",
    1: "01100000",
    2: "11011010",
    3: "11110010",
    4: "01100110",
    5: "10110110",
    6: "10111110",
    7: "11100000",
    8: "11111110",
    9: "11110110",
#     "open": "11111111",
#     "close": "00000000"
}

def show_number(number):#定义函数，用于显示某个特定的数字，比如1，具体在哪个位置的led灯显示，由led_light_on函数控制。如果同时设置为led.Value(0),则四个led同时显示“1”。
    if number_dict.get(number):#如果这个数字属于number_dict字典的key，则执行下面代码。
        i = 0
        for bit in number_dict.get(number):#遍历字典的Key对应的那一个Value的元素，比如1对应的Value是"11111100"。
            if bit == "1":
                number_led[i].value(1)#如果灯管对应的数字是1，就输出高电平，
            else:
                number_led[i].value(0)#如果灯管对应的数字是0，就输出低电平，
            i += 1

def led_light_on(i):#定义函数，用于点亮4个灯中某个特定的led灯。
    for led in led_light_list:
        led.value(1)#先将所有的led接口的值调为1(高电平），因为共阴极，所以自动熄灭。

    led_light_list[i].value(0)#调为0，产生电压差，点亮led。


def show_4_number(number):
    if 0<=number<=9999:#确定这个数字是否在显示范围内。
        i=0
        for num in "%04d"% number :#截取四位数中的num，1234，分别为1,2,3,4.
            show_number(int(num))#调用函数，点亮一个数字，每点亮一个数字，用下一行代码控制其在第几个led灯显示。
            led_light_on(i)#调用函数，点亮第i个led数字。
            time.sleep_ms(5)#点亮后，延时10毫秒。这个时间越短，显示越流畅。
            i += 1
            
for i in range(1, 10000):#循环显示1到9999的数字。
#     for j in range(100):#用来控制显示的时长，也可以去掉本行代码。
        show_4_number(i)#调用show_4_number函数，用以显示数字i。

    


