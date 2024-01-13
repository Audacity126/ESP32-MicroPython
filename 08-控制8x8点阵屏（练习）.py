import machine
import time

#行提供低电压，列供高电压时，led灯亮。

row_1 = machine.Pin(32, machine.Pin.OUT)
row_2 = machine.Pin(33, machine.Pin.OUT)
row_3 = machine.Pin(25, machine.Pin.OUT)
row_4 = machine.Pin(26, machine.Pin.OUT)
row_5 = machine.Pin(27, machine.Pin.OUT)
row_6 = machine.Pin(14, machine.Pin.OUT)
row_7 = machine.Pin(12, machine.Pin.OUT)
row_8 = machine.Pin(13, machine.Pin.OUT)

row_list = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8]


col_1 = machine.Pin(19, machine.Pin.OUT)
col_2 = machine.Pin(18, machine.Pin.OUT)
col_3 = machine.Pin(5, machine.Pin.OUT)
col_4 = machine.Pin(17, machine.Pin.OUT)
col_5 = machine.Pin(16, machine.Pin.OUT)
col_6 = machine.Pin(4, machine.Pin.OUT)
col_7 = machine.Pin(2, machine.Pin.OUT)
col_8 = machine.Pin(15, machine.Pin.OUT)

col_list = [col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8]


def set_row_earth(i):
    for row in row_list:
        row.value(1)
    if 0 <= i <= 7:
        row_list[i].value(0)


def set_col_power(i):
    #让8根竖线设置为低电压，此时led灯不亮
    for col in col_list:
        col.value(0)
        
    #让某一个线设置为1，即高电压，此时led灯亮。
    if 0 <= i <= 7:
               
        col_list[i].value(1)


def show_liushuideng():
    # 流水灯
    for row in range(8):
        set_row_earth(row)
        for col in range(8):
            set_col_power(col)
            time.sleep_ms(100)


img_list = [
    (1, 4),
    (2, 5),
    (3, 6),
    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
    (5, 6),
    (6, 5),
    (7, 4)
]

    # 让箭头从左向右移动
while True:
    for i in range(-7, 8):
        for j in range(5):
            for x, y in img_list:
                set_row_earth(x)
                set_col_power(y + i)
                time.sleep_ms(1)


