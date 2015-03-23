__author__ = 'huajw'
#coding=utf-8

import os
import sys
import time


from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
from com.android.hierarchyviewerlib.models import ViewNode
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
    viewNodeButton = hierarchyViewer.findViewById("id/settings")
#    pointButton = HierarchyViewer.getAbsoluteCenterOfView(viewNodeButton)
    print "the view"
    print viewNodeButton
except:
    print "there is somgthing happened"
    MonkeyRunner.sleep(5)

def getChildView(device,parentId,*childSeq):
    #hierarchyViewer=device.getHierarchyViewer()
    str_getchildview="hierarchyViewer.findViewById('" + parentId  + "')"
    for index in childSeq:
        str_getchildview += ('.children['+str(index)+']')
    exec 'child_view = ' + str_getchildview
    return child_view












MonkeyRunner.sleep(3)
#devices.MonkeyRunner.alert("ok","stop")



if __name__ == "main":
    main()

