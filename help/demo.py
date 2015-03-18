__author__ = 'huajw'
#coding=utf-8

import os
import sys
import time
import help


#from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice, MonkeyImage
#from com.android.monkeyrunner.easy import By
#from com.android.chimpchat.hierarchyviewer import HierarchyViewer

try:
    device = MonkeyRunner.waitForConnection()
    print  'The device has already connect'
except:
    print "手机连接失败, 请再次绑定手机"

MonkeyRunner.sleep(6)

try:
    device.startActivity(component="com.esun.ui/com.esun.mainact.personnal.loginmodule.LoginActivity")
    print '打开500.com的客户端进行登录'



