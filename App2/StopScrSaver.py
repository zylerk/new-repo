
import os
import time

import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0,0)

x=1

while x>0 :
    print("%s sleep %s seconds" % (x, 2))
    time.sleep(2)
    x=x+1

    full_list = os.popen('tasklist').readlines()

    for each_task in full_list:
        p_name = each_task.split()
        if( len(p_name) > 1):
            print(p_name[0][-4:])
            check_ext = p_name[0][-4:]
            if( check_ext == '.scr'):
                try:
                    #os.system("taskkill /im %s" % (p_name[0]))
                    click(10,10)
                except OSError as err:
                    print("OS Error: " + str(err))
                #x=0


print("program exit")
