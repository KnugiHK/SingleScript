import os, sys, time, re, glob
import piexif
from datetime import datetime, timedelta

try:
    import win32file, win32con
    __use_win_32 = True
except:
    __use_win_32 = False
  

def main():
    i = 0
    for filename in os.listdir("test"):
        dst = f"IMGA{i}.jpg"
        src = 'test/' + filename
        dst = 'test/' + dst
        piexif.remove(src)
        os.rename(src, dst)
        setFileDates(dst)
        print(f"File name '{src}' has been changed to '{dst}'.")
        i += 1
        
def setFileDates(fileName):
    """Sets file modification and creation dates to the specified value"""
    dates = datetime.utcfromtimestamp(os.path.getmtime(fileName))
    if __use_win_32:
        filehandle = win32file.CreateFile(fileName, win32file.GENERIC_WRITE, 0, None, win32con.OPEN_EXISTING, 0, None)
        win32file.SetFileTime(filehandle, *(dates,)*3)
        filehandle.close()
    else:
        os.utime(fileName, (time.mktime(dates.utctimetuple()),)*2)

if __name__ == '__main__':
    main()
