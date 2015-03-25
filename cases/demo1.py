__author__ = 'huajw'
#coding=utf-8


"""
测试用例:竟足胜平负
用户名: 打开客户端,竟足,胜平负,点击选好了,弹出提示.
用户名登录密码:wuxian500

"""

import os
import sys
import time


from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer

print "import the module end"


#start the connect
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


#log in (aaa,123456)


print "wait for 4S"

MonkeyRunner.sleep(4)
try:
    MonkeyRunner.sleep(2)
    #denglu
    #device.touch(159,510,"DOWN_AND_UP")
    print "click the quit key"

except:
    print "error start the app"



try:
    MonkeyRunner.sleep(4)
    #打开竟足胜平负
    device.touch(77,587,"DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    device.touch(79,724,"DOWN_AND_UP")
    MonkeyRunner.sleep(8)
    device.touch(179,289,"DOWN_AND_UP")


    #press the delete key
    #device.type('mobiletest')
    MonkeyRunner.sleep(3)
    print "click OK key"
    device.touch(390,760,"DOWN_AND_UP")
    MonkeyRunner.sleep(6)



except:
    print "something error happened when we open the jingzu_shengpingfu"



try:
    result = device.takeSnapshot()
    print "we hava already got the snapshot"
    print  "*"*70
   # result.writeToFile( tupianlujing , 'png')
    print "result is loaded"
except:
    print "take snapshot failed"

try:
    tupianlujing = str(os.path.abspath(os.path.dirname(os.path.dirname(sys.argv[0]))) + "\yuqi\jinggao.png")
    yuqitupian = MonkeyRunner.loadImageFromFile( tupianlujing , 'png')
    print "load the image ok."
except:
    print "load image from the file failed"

print "*"*50


if  result.sameAs(yuqitupian, 0.8) :
#if 1:
    print "the result is truth"
else:
    print "the result is fail"



try :
    MonkeyRunner.sleep(5)
    print "click the enter key"
    device.touch(238,506,"DOWN_AND_UP")
    MonkeyRunner.sleep(5)
    print "chose a team"
    device.touch(280,560,"DOWN_AND_UP")
except:
    print "error happened when chose the teams"

try:
    MonkeyRunner.sleep(5)
    print "click OK key"
    device.touch(390,760,"DOWN_AND_UP")
    MonkeyRunner.sleep(10)
except:
    print "the result is ok"




















try:
    tupianlujing = str(os.path.abspath(os.path.dirname(os.path.dirname(sys.argv[0]))) + "\yuqi\queren.png")
    result = device.takeSnapshot()
    print "we hava already got the snapshot"
    print  "*"*70
    #result.writeToFile( tupianlujing , 'png')
    print "result is loaded"
except:
    print "take snapshot failed"

try:
    yuqitupian = MonkeyRunner.loadImageFromFile( tupianlujing , 'png')
    print "load the image ok."
except:
    print "load image from the file failed"

print "*"*50


if  result.sameAs(yuqitupian, 0.8) :
#if 1:
    print "the result is truth"
else:
    print "the result is fail"
