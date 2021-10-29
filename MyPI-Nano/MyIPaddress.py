from subprocess import check_output
from time import sleep
import MyTools.MyLCD

MyLCD = MyTools.MyLCD.I2C_LCD()
MyLCD.writeString("Hello World")
MyLCD.setPosition(2,0)
sleep(10)
MyLCD.writeString(str(check_output(['hostname', '-I']))[2:-4])


