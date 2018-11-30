# -*- coding: utf-8 -*-
# coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/index/init")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "train_date")))
time.sleep(1)
# 处理开始时间
# # js去掉readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
# js添加时间
js_value = 'document.getElementById("train_date").value="1993-02-27"'
driver.execute_script(js_value)

time.sleep(5)
driver.close()
