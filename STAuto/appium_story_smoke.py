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
import os


path_pattern = 'patterns/'
temp_scr = 'tmp.png'
start_time = time() #开始测试的时间
duration = 3600 #测试时长
timeout = 30 #搜索图片的时长
match_ratio = -1
threshold = 0.8 #匹配度
default_res = (720,1280)
match_method = cv2.TM_CCOEFF_NORMED
#android.widget.EditText

#text	确定
#class	android.widget.Button
def find_loc_by_tmplt(driver,template,threshold=0.90,timeout=30):
    start_time = time()
    match_ratio = -1
    c_position =(0,0)
    while time()-start_time<=timeout and match_ratio <threshold:
        driver.get_screenshot_as_file(temp_scr)
        tmp = cv2.resize(cv2.imread(temp_scr,1),default_res)
        tmp_pos,tmp_ratio=find_pic(tmp,template,match_method)
        if tmp_ratio>match_ratio:
            match_ratio = tmp_ratio
            c_position = tmp_pos
        
    return c_position,match_ratio
def find_pic(img,template,method):
    w = template.shape[1]
    h = template.shape[0]
    
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        match_res = 1-min_val
    else:
        top_left = max_loc
        match_res = max_val
    c_pos = (top_left[0] + w//2, top_left[1] + h//2)
    return c_pos,match_res
desired_caps = {}
desired_caps['platformName'] = 'Android'
#desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'HUAWEI Mate 9'
#desired_caps['appActivity'] = 'com.unity3d.player.UnityPlayerActivity'
#desired_caps['appPackage'] = 'com.sixwaves.lovestory'
desired_caps['app'] = 'D:/Work/Stories/build/story201805211816.apk'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#获取屏幕尺寸
driver.get_screenshot_as_file(temp_scr)
tmp = cv2.imread(temp_scr,0)
screen_res=tmp.shape[::-1]
ratio = (screen_res[0]/default_res[0],screen_res[1]/default_res[1])
c_pos =(screen_res[0]/2,screen_res[1]/2)
print(ratio)
#driver.get_screenshot_as_file(path_pattern + 'tmp.png')
#btn_later = cv2.imread(path_pattern + 'btn_later.png',0)
#btn_zhCN = cv2.imread(path_pattern + 'btn_zhCN.png',0)
#btn_chapter_start = cv2.imread(path_pattern + 'btn_chapter_start.png',0)
#btn_chapter_next = cv2.imread(path_pattern + 'btn_chapter_next.png',0)
patterns = os.listdir(path_pattern)
templates = [cv2.imread(path_pattern+i,1) for i in patterns]
btn_ok = cv2.imread('btn_ok.png',1)

#print(btn_later.shape)
last_found_time = time() #开始搜索的时间
start_time = time() #开始测试的时间
template_found = None
edittext = None
while time()-start_time<=duration:
    c_position=c_pos
    driver.get_screenshot_as_file(temp_scr)
    #将图片从实际分辨率转换至设计分辨率
    tmp = cv2.resize(cv2.imread(temp_scr,1),default_res)
    match_ratio = -1
    try:
        edittext = driver.find_element_by_class_name('android.widget.EditText')
        button = driver.find_element_by_class_name('android.widget.Button')
    except:
        edittext = None
        button = None
    if edittext and button:
        edittext.set_value('1')
#        edittext.send_keys('1')
        button.click()
        btn_ok_pos,tmp_match = find_loc_by_tmplt(driver,btn_ok)
        driver.tap([btn_ok_pos])
    for i,template in enumerate(templates):
        tmp_pos,tmp_ratio=find_pic(tmp,template,match_method)
        if tmp_ratio>match_ratio:
            match_ratio = tmp_ratio
            c_position = tmp_pos
    #由设计坐标转换至实际坐标
    c_position = (c_position[0]*ratio[0],c_position[1]*ratio[1])
    print(match_ratio)
    if match_ratio>=threshold:
#    if True:

        last_found_time = time()
    driver.tap([c_position])
#    print(last_found_time)
    if time() - last_found_time>timeout:
        pass
#        break
    sleep(1)
