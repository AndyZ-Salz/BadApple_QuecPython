# -*- coding: UTF-8 -*-


import utime

'''
如果用户使用的固件版本中没有checkNet库，请将checkNet.mpy文件上传到模块的usr目录，
并将 import checkNet 改为 from usr import checkNet
'''
import checkNet
from usr import st7789v

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_ST7789V_LCD_FPSTest"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
lcd_st7789v = st7789v.ST7789V(240, 240)

if __name__ == '__main__':
    '''
    手动运行本例程时，可以去掉该延时，如果将例程文件名改为main.py，希望开机自动运行时，需要加上该延时,
    否则无法从CDC口看到下面的 poweron_print_once() 中打印的信息
    '''
    # utime.sleep(5)
    checknet.poweron_print_once()

    '''
    如果用户程序包含网络相关代码，必须执行 wait_network_connected() 等待网络就绪（拨号成功）；
    如果是网络无关代码，可以屏蔽 wait_network_connected()
    '''
    # checknet.wait_network_connected()

    # 用户代码
    '''######################【User code star】###################################################'''

    '''
    测试是否可以直接拉伸图片
    '''



    # 80*80
    timeA = utime.ticks_ms()
    lcd_st7789v.lcd_show_image_file("usr/image80_1.txt", 0, 0, 240, 240, 8)
    timeB = utime.ticks_ms()
    print("image80:"+str(utime.ticks_diff(timeB,timeA))+"ms")

    # timeA = utime.ticks_ms()
    # lcd_st7789v.lcd_show_image_file("usr/image80_2.txt", 0, 0, 240, 240, 25)
    # timeB = utime.ticks_ms()
    # print("image80:"+str(utime.ticks_diff(timeB,timeA))+"ms")



    '''######################【User code end 】###################################################'''
