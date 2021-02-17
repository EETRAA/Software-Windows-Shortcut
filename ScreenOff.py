from ctypes import *
from win32con import *

windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)	#screen_off = 2