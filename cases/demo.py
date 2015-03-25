__author__ = 'huajw'
#coding=utf-8


"""
测试用例:登录
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
    print "start the app"
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

#点击取消按钮
print "click the quit key"

try:
    print "wait for the wanrning message of update"
    #MonkeyRunner.sleep(6)
   # device.touch(140,508,"DOWN_AND_UP")
except:
    print "click the key error"





MonkeyRunner.sleep(2)
try:
    MonkeyRunner.sleep(2)
    #denglu
    device.touch(28,330,"DOWN_AND_UP")
    MonkeyRunner.sleep(2)
    device.touch(318,189,"DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    device.touch(318,189,"DOWN_AND_UP")
    MonkeyRunner.sleep(2)
    device.touch(318,189,"DOWN_AND_UP")
    #press the delete key
    print "type in the user name and password"
    MonkeyRunner.sleep(2)
    device.type('mobiletest')
    MonkeyRunner.sleep(3)
    device.press('KEYCODE_ENTER',MonkeyDevice.UP)
    #device.touch(250,450,"DOWN_AND_UP")
    device.type('wuxian500')
    MonkeyRunner.sleep(3)
    device.touch(240,445,"DOWN_AND_UP")
    MonkeyRunner.sleep(4)
except:
    print "something error happened"
tupianlujing = str(os.path.abspath(os.path.dirname(os.path.dirname(sys.argv[0]))) + "\yuqi\dengliyuqi.png")

try:
    result=device.takeSnapshot()
    print "we hava already got the snapshot"
#    result.writeToFile( tupianlujing ,'png')
except:
    print "take snapshot failed"

try:

    yuqitupian = MonkeyRunner.loadImageFromFile(tupianlujing , 'png')
    print "load the image ok."
except:
    print "load image from the file failed,please check the image's path"

if result.sameAs(yuqitupian , 0.7):
    print "the result is truth"
else:
    print "the result is fail"

