__author__ = 'huajw'
#coding=utf-8


"""
测试用例:
用户名: mobiletest
用户名登录密码:wuxian500

"""

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


#start the app
try:
    print "log in the app"
    device.press('KEYCODE_HOME',MonkeyDevice.DOWN)
    device.press('KEYCODE_HOME',MonkeyDevice.UP)
    MonkeyRunner.sleep(2)
    # gong neng jian
    device.touch(240,750,"DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    device.touch(65,165,"DOWN_AND_UP")
    MonkeyRunner.sleep(4)
    print "wait for 4 secound"
    MonkeyRunner.sleep(4)

except :
    print "error start  app 500.com ,please check the Activity"


#log in (aaa,123456)


print "wait for 40S"

MonkeyRunner.sleep(40)
try:
    MonkeyRunner.sleep(2)
    #denglu
    device.touch(28,330,"DOWN_AND_UP")
    print "start  the app"

except:
    print "error start the app"



try:
    MonkeyRunner.sleep(2)
    #denglu
    #device.touch(28,330,"DOWN_AND_UP")
    device.touch(164,520,"DOWN_AND_UP")
    MonkeyRunner.sleep(2)
    device.touch(77,587,"DOWN_AND_UP")
    MonkeyRunner.sleep(2)
    device.touch(79,724,"DOWN_AND_UP")
    MonkeyRunner.sleep(2)
    device.touch(179,289,"DOWN_AND_UP")
    #press the delete key
    #device.type('mobiletest')
    MonkeyRunner.sleep(2)
    device.touch(390,760,"DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    print "make sure of it"
    MonkeyRunner.sleep(2)
    device.touch(235,500,"DOWN_AND_UP")
    device.type('wuxian500')
    MonkeyRunner.sleep(3)
    device.touch(240,445,"DOWN_AND_UP")
    MonkeyRunner.sleep(4)
except:
    print "something error happened"

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

if result.sameAs(yuqitupian , 0.7):
    print "the result is truth"
else:
    print "the result is fail"
