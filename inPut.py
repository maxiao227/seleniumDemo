# -*- coding: utf-8 -*-

import time

from selenium import webdriver

driver = webdriver.Chrome()  # 利用火狐浏览器
driver.get("http://www.baidu.com")  # 打开get到的网址
time.sleep(5)  # t停顿5秒，即5秒内一直在这个界面
print("网站的名称：", driver.title)  # 获取网站名称并输出
for line in open("keyword.txt",
                 encoding="utf-8").readlines():  # 打开keyword.txt文件，并一行行读取数据：keyword.txt中可以存放任意关键字，比如：selenium python 赵丽颖(ps:一个关键字占一行）
    driver.find_element('id', 'kw').send_keys(line)  # 通过输入框的id为kw,定位到输入框，输入”selenium”
    driver.find_element('id', 'su').click()  # 通过搜索按钮的id为su定位到搜索按钮，点击按钮
    time.sleep(5)  # 停顿5秒
    driver.find_element('id', 'kw').clear()  # 清空输入框，防止下次输入的时候会连着上一次的，最后导致所有关键字都在输入框中了

# driver.quit()  # 关闭浏览器
