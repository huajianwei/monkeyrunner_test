__author__ = 'huajw'
#coding=utf-8

"""

Android SDK自带一个工具叫做monitor，它里面的Hierarchy Viewer可以看到app的UI结构、控件属性等等。
monkeyrunner有一个类By，通过By可以在代码中根据控件ID定位到该控件从而写更有针对性代码
（比如点击按钮、比如获取文本框中的字符串）。
可是出于安全考虑，Hierarchy Viewer只能连接Android开发版手机或是模拟器。
只有当设备或模拟器上启动一个叫做View Server的服务，
Hierarchy Viewer才能与其进行socket通信，才能看到app的“View”。
而绝大多数商业手机是无法开启View Server的，
所以Hierarchy Viewer也就无法连接到普通的商业手机。
而By又依赖于Hierarchy Viewer，所以如果想在普通的商业手机上通过控件ID去做一些操作，
连接模拟器运行通过的脚本连接真机运行是会抛错的。

"""
#查看系统所有的services
adb shell service list

#开启view server
adb shell service call window 1 i32 4939

#显示目前的状态
adb shell service call window 3

#关闭view server
adb shell service call window 2 i32 4939



