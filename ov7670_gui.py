from serial import *
from Tkinter import *

serialPort = "/dev/ttyUSB1"
baudRate = 9600
ser = Serial(serialPort , baudRate, timeout=0, writeTimeout=0) #ensure non-blocking

#make a TkInter Window
root = Tk()
root.wm_title("Reading Serial")


def testVideo():
    ser.write("\x23\x00")

def testBars():
    ser.write("\x23\x01")

def testFadedBars():
    ser.write("\x23\x02")

def testLineOnOFF():
    ser.write("\x23\x03")

Button(root, text="Video", command=testVideo).grid(row=0, column=0)
Button(root, text="Bars", command=testBars).grid(row=1, column=0)
Button(root, text="Faded Bars", command=testFadedBars).grid(row=2, column=0)
Button(root, text="Line ON/OFF", command=testLineOnOFF).grid(row=3, column=0)



root.mainloop()
