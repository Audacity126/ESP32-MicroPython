from machine import Pin, SPI
from package import st7789py as st
from package import vga1_16x32 as font
from package import font_gb_16x16 as font_gb
import time

class Display():
    def __init__(self):
        self.tft = st.ST7789(SPI(2, 10000000), 240, 240, reset=Pin(17), dc=Pin(2), cs=Pin(5), backlight=Pin(22), rotation=0)
        self.WHITE = st.color565(255, 255, 255)#BRG
        self.BLACK = st.color565(0, 0, 0)
        self.RED = st.color565(0, 255, 0)
        self.GREEN = st.color565(0, 0, 255)
        self.BLUE = st.color565(255, 0, 0)
        self.YELLOW = st.color565(0, 255, 255)
        print(self.RED,self.GREEN,self.BLUE)
        self.last_hour = 0
        self.last_minute = 0
        self.last_second = 0
        self.last_year = 0
        self.last_month = 0
        self.last_day = 0
        self.init_show()
    def init_show(self):
        '''
        初始化显示画面
        '''
        self.tft.text_gb48(font_gb,32, ':', 20+24*2, 100, self.WHITE, self.BLACK)
        self.tft.text_gb48(font_gb,32, ':', 20+24*5, 100, self.WHITE, self.BLACK)
        self.tft.text_gb48(font_gb,32, '00', 20, 100, self.WHITE, self.BLACK)
        self.tft.text_gb48(font_gb,32, '00', 20+24*3, 100, self.WHITE, self.BLACK)
        self.tft.text_gb48(font_gb,32, '00', 20+24*6, 100, self.WHITE, self.BLACK)
        self.text_gb('小雨')
        self.text('hello world!')
    def text_gb(self,text):
        self.tft.text_gb32(font_gb,32, text, 0, 0, self.WHITE, self.BLACK)
    def text(self,text):
        self.tft.text(font,32, text, 0, 50, self.GREEN, self.BLACK)
    
    def show_time(self,t):
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
            self.tft.text_gb48(font_gb,32, '{:0>2d}'.format(hour), 20, 100, self.BLUE, self.BLACK)
            self.last_hour = hour
        if minute != self.last_minute:
            self.tft.text_gb48(font_gb,32, '{:0>2d}'.format(minute), 20+24*3, 100, self.RED, self.BLACK)
            self.last_minute = minute
        if second != self.last_second:
            self.tft.text_gb48(font_gb,32, '{:0>2d}'.format(second), 20+24*6, 100, self.GREEN, self.BLACK)
            self.last_second = second
        #self.tft.text_gb48(font_gb,32, ti, 20, 100, self.WHITE, self.BLACK)
        
    def run(self):
        while True:
            t = time.localtime(time.time())
            #if t[5]%2==0:
            self.show_time(t)
            time.sleep(0.5)
            #for i in range(65536,100):
            #    self.tft.text_gb32(font_gb,32, '雨', 100, 150, i, self.BLACK)
        
    def __del__(self):
        pass
D = Display()
D.run()