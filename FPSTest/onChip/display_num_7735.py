# -*- coding: UTF-8 -*-


import utime

'''
如果用户使用的固件版本中没有checkNet库，请将checkNet.mpy文件上传到模块的usr目录，
并将 import checkNet 改为 from usr import checkNet
'''
import checkNet
from usr import st7735s

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_ST7735S_LCD_FPSTest"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
lcd_st7735s = st7735s.ST7735S(128, 128)

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
    要显示的图片像素为 99*100，下面设置显示图片的起始坐标位置为（70，70）
    要注意：显示图片时，最后两个参数传入的是图片大小，即宽高，不是终点坐标
    '''




    # 85*64
    timeA = utime.ticks_ms()
    lcd_st7735s.lcd_show_image_file("usr/image8564_1.txt", 64, 21, 64, 85, 30)
    timeB = utime.ticks_ms()
    print("image8564:"+str(utime.ticks_diff(timeB,timeA))+"ms")

    timeA = utime.ticks_ms()
    lcd_st7735s.lcd_show_image_file("usr/image8564_2.txt", 64, 21, 64, 85, 30)
    timeB = utime.ticks_ms()
    print("image8564:"+str(utime.ticks_diff(timeB,timeA))+"ms")

    timeA = utime.ticks_ms()
    lcd_st7735s.lcd_show_image_file("usr/image8564_3.txt", 64, 21, 64, 85, 30)
    timeB = utime.ticks_ms()
    print("image8564:"+str(utime.ticks_diff(timeB,timeA))+"ms")

    timeA = utime.ticks_ms()
    lcd_st7735s.lcd_show_image_file("usr/image8564_4.txt", 64, 21, 64, 85, 30)
    timeB = utime.ticks_ms()
    print("image8564:"+str(utime.ticks_diff(timeB,timeA))+"ms")

    timeA = utime.ticks_ms()
    lcd_st7735s.lcd_show_image_file("usr/image8564_5.txt", 64, 21, 64, 85, 30)
    timeB = utime.ticks_ms()
    print("image8564:"+str(utime.ticks_diff(timeB,timeA))+"ms")




    '''######################【User code end 】###################################################'''
