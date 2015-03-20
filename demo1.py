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


#start the app
try:
    print "log in the app"
#    device.press('KEYCODE_HOME',MonkeyDevice.DOWN)
#    device.press('KEYCODE_HOME',MonkeyDevice.UP)
#    MonkeyRunner.sleep(2)
    # gong neng jian
    device.touch(240,750,"DOWN_AND_UP")
    MonkeyRunner.sleep(3)
#    device.touch(65,165,"DOWN_AND_UP")
#    MonkeyRunner.sleep(4)
#    print "wait for 4 secound"
#    MonkeyRunner.sleep(4)

except :
    print "error start  app 500.com ,please check the Activity"


#log in (aaa,123456)

MonkeyRunner.sleep(2)



hierarchy_viewer = device.getHierarchyViewer()
view_node = hierarchy_viewer.findViewById('id/prompt_text_view')
text = view_node.namedProperties.get('mText').toString()
print help(hierarchy)



MonkeyRunner.sleep(5)



MonkeyRunner.sleep(3)

def Denglu(self):
    print "start the app"
    device.startActivity(component="com.esun.ui/com.esun.mainact.personnal.loginmodule.LoginActivity")
    print 'started  the app 500.com'


def PressHomeKey(self):
    print "Press Home Key"
    device.touch(241,755,"DOWN_AND_UP")
    print "Pressed Home Key"






