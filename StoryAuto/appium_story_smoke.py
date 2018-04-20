# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 10:58:20 2018

@author: admin
"""
#com.sixwaves.lovestory
#com.unity3d.player.UnityPlayerActivity

import unittest
from appium import webdriver
from time import sleep,time
import numpy as np
import cv2


path_pattern = 'patterns/'
temp_scr = path_pattern + 'tmp.png'
def find_loc_by_tmplt(driver,template,threshold=0.90,timeout=30):
    start_time = time()
    w,h = template.shape[::-1]
    match_ratio = -1
    c_position =(-1,-1)
    while time()-start_time<=timeout and match_ratio <threshold:
        driver.get_screenshot_as_file(temp_scr)
        tmp = cv2.imread(temp_scr,0)
        res = cv2.matchTemplate(tmp,template,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#        print(max_val)
        if max_val>match_ratio:
            match_ratio = max_val
            c_position = (max_loc[0] + w/2,max_loc[1]+h/2)
            
        sleep(1)
    return c_position,match_ratio

desired_caps = {}
desired_caps['platformName'] = 'Android'
#desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'HUAWEI Mate 9'
desired_caps['appActivity'] = 'com.unity3d.player.UnityPlayerActivity'
desired_caps['appPackage'] = 'com.sixwaves.lovestory'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#driver.get_screenshot_as_file(path_pattern + 'tmp.png')
#btn_later = cv2.imread(path_pattern + 'btn_later.png',0)
#btn_zhCN = cv2.imread(path_pattern + 'btn_zhCN.png',0)
#btn_chapter_start = cv2.imread(path_pattern + 'btn_chapter_start.png',0)
#btn_chapter_next = cv2.imread(path_pattern + 'btn_chapter_next.png',0)
patterns = ['btn_zhCN.png','btn_later.png','btn_chapter_start.png','btn_chapter_next.png']
#print(btn_later.shape)
for pattern in patterns:
    pattern_path = path_pattern + pattern
    c_pos,match = find_loc_by_tmplt(driver,cv2.imread(pattern_path,0))
    print(match)
    driver.tap([c_pos])

