# -*- encoding=utf8 -*-
__author__ = "1"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/RKPRCEVOYTBQVCOF?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",])
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

print("start...")

goods_list = poco("android:id/content").offspring("com.xunmeng.pinduoduo:id/alr").offspring("com.xunmeng.pinduoduo:id/cx7").child("android.widget.FrameLayout")

for g in goods_list:
   name1 = g.offspring("com.xunmeng.pinduoduo:id/tv_title").get_text()
   print(name1)
   price1 = g.offspring("com.xunmeng.pinduoduo:id/efu").get_text()
   print(price1)
   sale_num = g.offspring("com.xunmeng.pinduoduo:id/ek9").get_text()
   print(sale_num)

