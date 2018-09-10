# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:25:37 2018

@author: chen.jiankai
"""
from Action import Action
def getActions(driver):
    return [Action(driver,1001,([(100,200)])),
            Action(driver,1002,())]