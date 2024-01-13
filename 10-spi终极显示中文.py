from machine import Pin, SPI
from package import st7789py as st
import time


class Display():
    def __init__(self):
        self.tft = st.ST7789(SPI(2, 10000000), 240, 240, reset=Pin(17), dc=Pin(2), cs=Pin(5), backlight=Pin(22), rotation=0)
        self.WHITE = st.color565(255, 255, 255)#BRG
        self.BLACK = st.color565(0, 0, 0)
        self.RED = st.color565(0, 0, 255)
        self.last_hour = 0
        self.last_minute = 0
        self.last_second = 0
        self.last_year = 0
        self.last_month = 0
        self.last_day = 0
        self.clock_x = 20+24*2-12
        self.clock_y = 90
        self.init_show()
        
    def init_show(self):
        '''
        初始化显示画面
        '''
        self.tft.fill(0)
        print('ok')
        time.sleep(2)
        """
        风急天高猿啸哀，渚清沙白鸟飞回。
        无边落木萧萧下，不尽长江滚滚来。
        万里悲秋常作客，百年多病独登台。
        艰难苦恨繁霜鬓，潦倒新停浊酒杯。
        """
        self.tft.text(24, '一剪梅', 70, 0, self.WHITE, self.BLACK)
        self.tft.text(16, '——唐寅', 140, 30, self.WHITE, self.BLACK)
        self.tft.text(16, '雨打梨花深闭门，', 40, 60, self.WHITE, self.BLACK)
        self.tft.text(16, '忘了青春，误了青春', 40, 80, self.WHITE, self.BLACK)
        self.tft.text(16, '赏心乐事共谁论，', 40, 100, self.WHITE, self.BLACK)
        self.tft.text(16, '花下销魂，月下销魂', 40, 120, self.WHITE, self.BLACK)
        self.tft.text(16, '愁聚眉峰尽日颦，', 40, 140, self.WHITE, self.BLACK)
        self.tft.text(16, '千点啼痕，万点啼痕', 40, 160, self.WHITE, self.BLACK)
        self.tft.text(16, '晓看天色暮看云，', 40, 180, self.WHITE, self.BLACK)
        self.tft.text(16, '行也思君，坐也思君', 40, 200, self.WHITE, self.BLACK)
        self.tft.text(16, '——思君——欣',100, 220, self.WHITE, self.BLACK)
#         self.tft.text(24, '民航电子信息工程学院。', 0, 170, self.WHITE, self.BLACK)
#         self.tft.text(24, '创客营', 150, 210, self.WHITE, self.BLACK)
#想写英文，没有用         self.tft._text8(vga1_16x32, 'ganxin',60,220,self.WHITE, self.BLACK)
        

    def show_time(self,t):
        t = time.localtime(time.time())
        '''
        显示时间
        '''
        year = t[0]
        month = t[1]
        day = t[2]
        hour = t[3]
        minute = t[4]
        second = t[5]
        ti = "{:0>2d}:{:0>2d}:{:0>2d}".format(hour,minute,second)
        #print(ti)
        if hour != self.last_hour:
            self.tft.text(48, '{:0>2d}'.format(hour), self.clock_x, self.clock_y, self.WHITE, self.BLACK)
            self.last_hour = hour
        if minute != self.last_minute:
            self.tft.text(48, '{:0>2d}'.format(minute), self.clock_x + 24*3, self.clock_y, self.WHITE, self.BLACK)
            self.last_minute = minute
        
        
    def run(self):
        pass
            
        
    def __del__(self):
        pass
D = Display()
D.run()