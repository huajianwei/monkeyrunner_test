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


print "ok"


try:
    hierarchyViewer = device.getHierarchyViewer()
    print "have got the hierarchyViewer"
    viewNodeButton = hierarchyViewer.findView(By.id("id/Email"))
    print "ok11111111111"
except:
    print "there is somgthing happened"
    MonkeyRunner.sleep(5)



MonkeyRunner.sleep(3)
#devices.MonkeyRunner.alert("ok","stop")



if __name__ == "main":
    main()







