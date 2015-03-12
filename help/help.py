'''
Created on 2015-1-22

@author: huajw
'''


import os
import sys
import time
import logging

#from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer

#print sys.path 

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice, MonkeyImage

print 'import the class success'
device=MonkeyRunner.waitForConnection(1.0,'3230581473448f2d')

print 'devices has already connect'

#device.removePackage('myproject/bin/MyApplication.apk')

device.press('KEYCODE_HOME',MonkeyDevice.DOWN_AND_UP)

print 'press home'

#print time.ctime()

MonkeyRunner.sleep(6)
#print time.ctime()
MonkeyRunner.sleep(6)
print 'dakai 500'
MonkeyRunner.sleep(3)
#device.startActivity(component="com.esun.ui")

print 'dakai 500kehuduan'

MonkeyRunner.sleep(3)

device.startActivity(component="com.esun.ui/com.esun.mainact.personnal.loginmodule.LoginActivity")
print 'dakai 500 delu'
MonkeyRunner.sleep(3)
MonkeyRunner.sleep(5)

device.type('')
print "enter into username"
MonkeyRunner.sleep(3)
device.press('KEYCODE_ENTER',MonkeyDevice.UP)
MonkeyRunner.sleep(3)
device.type('hua123321')
MonkeyRunner.sleep(3)

device.press('KEYCODE_ENTER',MonkeyDevice.UP)
MonkeyRunner.sleep(3)

device.touch(250,450,"DOWN_AND_UP")



#device.shell("...")
MonkeyRunner.sleep(6)
# device.installPackage("../samples/android-10/ApiDemos/bin/Apidemos.apk")
#device.reboot()
#device.touch(300,300,'DOWN_AND_UP')
MonkeyRunner.alert("the test demo is over")
#device.press('KEYCODE_HOME',MonkeyDevice.DOWN_AND_UP)
#device.type('hello')
#result=device.takeSnapshot()
#result.writeToFile('takeSnapshot\\result1.png','png')
#MonkeyImage.writeToFile(1,jpg)
#device.type('hello')
#device.wake()
#device.reboot()
#device.touch(x,y,DOWN_AND_UP)
#device.touch(x,y,DOWN)
#device.touch(x,y,UP)
#device.press('KEYCODE_HOME',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_UP',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_CENTER',MonkeyDevice.DOWN)
#device.press('KEYCODE_ENTER',MonkeyDevice.UP)
#device.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_ENDCALL',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_UP ',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_DOWN ',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_LEFT',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_RIGHT',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_CENTER',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_VOLUME_UP',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_VOLUME_DOWN',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_POWER',MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_MENU',MonkeyDevice.DOWN_AND_UP)



print 'hello3'


if __name__ == "__main__":
    main()