__author__ = 'huajw'
#coding=utf-8

import os
import sys
import time


from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
print "import the module end"


# start the connect
try:
    device=MonkeyRunner.waitForConnection(1.0 , 'emulator-5554')
    #device=MonkeyRunner.waitForConnection(1.0 , 'emulator-5554')
    print  'The device has already connect'
except:
    print "The devices can't connect ,please reboot the phone"

MonkeyRunner.sleep(3)

#jietu
try:
    result=device.takeSnapshot()
    print "we hava already got the snapshot"
#    result.writeToFile('G:\my\monkeyrunner_test\jieguo\dengliyuqi.png','png')
except:
    print "take snapshot failed"

try:
    yuqitupian = MonkeyRunner.loadImageFromFile('G:\my\monkeyrunner_test\jieguo\dengliyuqi.png','png')
    print "load the image ok."
except:
    print "load image from the file failed"

if result.sameAs(yuqitupian , 0.9):
    print "the result is truth"
else:
    print "the result is fail"

MonkeyRunner.sleep(3)





























MonkeyRunner.sleep(3)



def Denglu(self):
    print "start the app"
    device.startActivity(component="com.esun.ui/com.esun.mainact.personnal.loginmodule.LoginActivity")
    print 'started  the app 500.com'


def PressHomeKey(self):
    print "Press Home Key"
    device.touch(241,755,"DOWN_AND_UP")
    print "Pressed Home Key"





