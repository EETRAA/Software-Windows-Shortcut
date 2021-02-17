from ctypes import *
from win32con import *
import psutil
import colorama

try :
    if psutil.WINDOWS:
        windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)	#screen_off = 2
    elif psutil.MACOS:
        print(colorama.Back.GREEN+colorama.Fore.CYAN+r'This is a MAC, run this file on Windows plz :)')
    elif psutil.LINUX:
        print(colorama.Back.GREEN+colorama.Fore.CYAN+r'This is a LINUX, run this file on Windows plz :)')
    elif psutil.BSD:
        print(colorama.Back.GREEN+colorama.Fore.CYAN+r'This is a BSD, run this file on Windows plz :)')
except :
    print('ERR!')