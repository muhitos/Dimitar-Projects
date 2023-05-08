import os
import time

def dsktp_locker():
    time.sleep(10)
    winpath = os.environ["windir"]
    os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')

while(1):
   dsktp_locker()