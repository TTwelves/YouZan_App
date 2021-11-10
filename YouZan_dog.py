'''
# @Title:
# @Time : 2021/9/22 16:12
# @File : YouZan_dog.py
# @Software: PyCharm

'''
import yaml
from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/RKPRCEVOYTBQVCOF?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH",])
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 1.店铺名 2.商品名称 3.成本 4.利润  5.库存  6.x人正在分销
def get_shop_name():
    pass

def get_goods_name():
    goods_name = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.qima.wxd:id/drop_down_list").child("android.widget.RelativeLayout")[0].child("com.qima.wxd:id/fragment_goods_stock_product_list_item_name").get_text()
    return goods_name

def get_goods_inventory_SaleNum():
    Inventory_SaleNum = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.qima.wxd:id/drop_down_list").child("android.widget.RelativeLayout")[0].offspring("com.qima.wxd:id/tv_repertory").get_text()
    return Inventory_SaleNum

def get_goods_cost():
    cost = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.qima.wxd:id/drop_down_list").child("android.widget.RelativeLayout")[0].child("com.qima.wxd:id/tv_price").get_text()
    return cost

def get_goods_profit():
    profit = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.qima.wxd:id/drop_down_list").child("android.widget.RelativeLayout")[0].child("com.qima.wxd:id/fragment_goods_stock_product_list_item_average_profit").get_text()
    return profit

def into_goods_page():
    poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.qima.wxd:id/drop_down_list").child("android.widget.RelativeLayout")[0].child("com.qima.wxd:id/fragment_goods_stock_product_list_item_name").click()

def dump_to_yaml(datalist:list):
    with open(r"C:\xjq\CodeRepo\YouZan_dog\dog.yaml", "a", encoding="utf-8") as f:
        yaml.dump(datalist, f, allow_unicode=True)

if __name__ == '__main__':

    TotalInfo = []
    ShopInfo = []
    pic_num = 50
    count = 0

    while True:
        goods_name = get_goods_name()
        goods_inventory_SaleNum = get_goods_inventory_SaleNum()
        goods_cost = get_goods_cost()
        goods_profit = get_goods_profit()

        into_goods_page()
        sleep(2)

        poco.scroll(direction="vertical", percent=0.2, duration=1.0)

        pic_num+=1
        snapshot(filename=f"C:\\xjq\\CodeRepo\\YouZan_dog\\Shop_name_Pic\\{pic_num}.jpg")
        poco.snapshot()

        keyevent("back")

        sleep(1)

        ShopInfo.append(pic_num)
        ShopInfo.append(goods_name)
        ShopInfo.append(goods_inventory_SaleNum)
        ShopInfo.append(goods_cost)
        ShopInfo.append(goods_profit)

        print(ShopInfo)

        TotalInfo.append(ShopInfo)
        ShopInfo = []
        count += 1

        if count == 2:
            dump_to_yaml(TotalInfo)
            count = 0
            TotalInfo = []

        poco.scroll(direction="vertical", percent=0.148, duration=1.0)






















