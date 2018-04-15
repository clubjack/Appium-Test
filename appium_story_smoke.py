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

def find_loc_by_tmplt(driver,template,threshold=0.90,timeout=20):
    start_time = time()
    w,h = template.shape[::-1]
    match_ratio = -1
    c_position =(-1,-1)
    while time()-start_time<=timeout and match_ratio <threshold:
        driver.get_screenshot_as_file('story/tmp.png')
        tmp = cv2.imread('story/tmp.png',0)
        res = cv2.matchTemplate(tmp,template,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#        print(max_val)
        if max_val>=threshold:
            match_ratio = max_val
            c_position = (max_loc[0] + w/2,max_loc[1]+h/2)
            return c_position,match_ratio
        sleep(1)
        

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appActivity'] = 'com.unity3d.player.UnityPlayerActivity'
desired_caps['appPackage'] = 'com.sixwaves.lovestory'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.get_screenshot_as_file('story/tmp.png')
btn_later = cv2.imread('story/btn_later.png',0)
btn_zhCN = cv2.imread('story/btn_zhCN.png',0)
#print(btn_later.shape)
c_pos,match = find_loc_by_tmplt(driver,btn_zhCN)
driver.tap([c_pos])
c_pos,match= find_loc_by_tmplt(driver,btn_later)
driver.tap([c_pos])