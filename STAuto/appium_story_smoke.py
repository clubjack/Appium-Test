# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 10:58:20 2018

@author: chen.jiankai
"""
#com.sixwaves.lovestory
#com.unity3d.player.UnityPlayerActivity

from appium import webdriver
from time import sleep,time
import numpy as np
import cv2
import os

import constant
from Config import getActions

def main():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    #desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'HUAWEI Mate 9'
    desired_caps['appActivity'] = constant.appActivity
    desired_caps['appPackage'] = constant.appPackage
    #desired_caps['app'] = 'D:/Work/Stories/build/story201805211816.apk' 
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    actions = getActions()
    for action in actions:
        action.perform()
if __name__ == '__main__':
    main()