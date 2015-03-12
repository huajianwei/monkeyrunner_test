'''
Created on 2015-1-22

@author: huajw
'''


import os
import sys
import time
#import logging


#print sys.path 

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer

print  'import the class success'
device = MonkeyRunner.waitForConnection()
print  'The device has already connect'

print type(device)
#device.removePackage('myproject/bin/MyApplication.apk')

hierarchyViewer = device.getHierarchyViewer()
print "hierarchyViewer connect succefully"
print type(hierarchyViewer)

print help(hierarchyViewer)


print "Press Home Key"
device.touch(241,755,"DOWN_AND_UP")

MonkeyRunner.sleep(3)
viewNodeButton = hierarchyViewer.findViewById("Settings")
print " viewNodeButton ok"
print type(viewNodeButton)

print "*"*20
MonkeyRunner.sleep(2)
text =hierarchyViewer.getText(Clock)
print type(text)
print text.encode('utf-8')


hierarchy_viewer = device.getHierarchyViewer()
view_node = hierarchy_viewer.findViewById('id/prompt_text_view')
text = view_node.namedProperties.get('mText').toString()
pointButton = HierarchyViewer.getAbsoluteCenterOfView(viewNodeButton)


#按钮点下后，我们需要用下面代码获取文本框里的返回值：
#viewNodeOutput = hierarchyViewer.findViewById("id/output")
#output = viewNodeOutput.namedProperties.get("text:mText").value

#这样我们就能用output与预期的“ok”做比对了：
#



























#device.press('KEYCODE_HOME',MonkeyDevice.DOWN_AND_UP)

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