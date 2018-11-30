# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/selectTest.htm')

s1 = Select(driver.find_element_by_id('s1'))  # 实例化Select

s1.select_by_index(5)  # 选择第二项选项：o1
time.sleep(2)
s1.select_by_value("46")  # 选择value="o2"的项
time.sleep(2)
s1.select_by_visible_text("Mail")  # 选择text="o3"的值，即在下拉时我们可以看到的文本


