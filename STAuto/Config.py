# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:25:37 2018

@author: chen.jiankai
"""
from Action import Action
actions = [(1001,[(100,200)]),
           ()]
def getActions(driver):
    result = []
    for action in actions:
        result.append(Action(driver,action[0],action[1:]))
    return result