# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:29:00 2018

@author: chen.jiankai
"""
from time import sleep
class Action():
    def __init__(self,driver,actionType,*actionParams):
        self.driver = driver
        self.actionType = actionType
        self.actionParams = actionParams
    def perform(self):
        if self.actionType == 1000:
            sleep(self.actionParams[0])
        elif self.actionType == 1001:
            self.driver.tap(self.actionParams[0])
        elif self.actionType == 1002:
            self.driver.find_element_by_class_name(self.actionParams[0]).setValue(self.actionParams[1])
        else:
            pass