# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:25:37 2018

@author: chen.jiankai
"""
from Action import Action
actions = [(1001, [(100, 200)]),
           (1000, 50),
           (1001, [(95, 80)]),
           (1000, 50),
           (1001, [(615, 550)]),
           (1000, 1),
           (1001, [(95, 80)]),
           (1000, 1),
           (1001, ([444, 246])),
           (1002, 'android.widget.EditText', '1'),
           (1004, 'android.widget.Button'),
           (1001, [(470, 191)]),
           (1003, 'android.widget.EditText'),
           (1002, 'android.widget.EditText', '192.168.1.65'),
           (1004, 'android.widget.Button'),
           (1001, [(470, 279)]),
           (1003, 'android.widget.EditText'),
           (1002, 'android.widget.EditText', 'qa0001'),
           (1004, 'android.widget.Button'),
           (1001, [(785, 505)]),
           (1000, 20),
           (1001, [(887, 461)]),
           (1000, 1),
           (1001, [(887, 461)]),
           (1000, 1),
           (1001, [(887, 461)]),
           (1000, 1),
           (1001, [(350, 591)]),
           (1000, 1),
           (1001, [(636, 360)]),
           (1000, 1),
           (1001, [(597, 478)]),
           (1000, 1),
           (1001, [(111, 682)]),
           (1000, 1),
           (1001, [(632, 293)]),
           (1000, 1),
           (1001, [(567, 111)]),
           (1000, 1),
           (1001, [(312, 590)]),
           (1000, 1),
           (1001, [(584,258)]),
           (1000, 2),
           (1001, [(646, 359)]),
           (1000, 2),
           (1001, [(678, 485)]),
           (1000, 2),
           (1001, [(902, 679)]),
           (1000, 2),
           (1001, [(881, 467)]),
           (1000, 1),
           (1001, [(887, 654)]),
           (1000, 1),
           (1001, [(320, 590)]),
           (1000, 1),
           (1001, [(881, 467)]),
           (1000, 1),
           (1001, [(714, 690)]),
           (1000, 1),
           (1001, [(208, 347)]),
           (1000, 2),
           (1001, [(1028, 675)]),
           (1000, 10),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(145, 632)]),
           (1000, 1),
           (1001, [(478, 351)]),
           (1000, 2),
           (1001, [(589, 369)]),
           (1000, 2),
           (1001, [(1028, 675)]),
           (1000, 11),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(333, 333)]),
           (1000, 1),
           (1001, [(444, 444)]),
           (1000, 1),
           (1001, [(196, 250)]),
           (1000, 2),
           (1001, [(1000, 577)]),
           (1000, 6),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(203, 431)]),
           (1000, 2),
           (1001, [(1000, 577)]),
           (1000, 6),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(333, 333)]),
           (1000, 1),
           (1001, [(633, 345)]),
           (1000, 2),
           (1001, [(1028, 678)]),
           (1000, 11),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(333, 333)]),
           (1000, 1),
           (1001, [(1066, 102)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(206, 609)]),
           (1000, 2),
           (1001, [(1000, 577)]),
           (1000, 6),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(1197, 260)]),
           (1000, 2),
           (1001, [(1000, 577)]),
           (1000, 6),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(333, 333)]),
           (1000, 1),
           (1001, [(640, 507)]),
           (1000, 1),
           (1001, [(1028, 675)]),
           (1000, 14),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(1066, 102)]),
           (1000, 2),
           (1001, [(1194, 438)]),
           (1000, 2),
           (1001, [(1000, 577)]),
           (1000, 6),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(1192, 618)]),
           (1000, 2),
           (1001, [(1000, 577)]),
           (1000, 6),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(1239, 26)]),
           (1000, 2),
           (1001, [(1239, 26)]),
           (1000, 2),
           (1001, [(64, 684)]),
           (1000, 4),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(333, 333)]),
           (1000, 1),
           (1001, [(657, 365)]),
           (1000, 3),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(639, 596)]),
           (1000, 2),
           (1001, [(1129, 675)]),
           (1000, 20),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(640, 346)]),
           (1000, 2),
           (1001, [(1037, 670)]),
           (1000, 13),
           (1001, [(609, 678)]),
           (1000, 2),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(333, 333)]),
           (1000, 1),
           (1001, [(431, 648)]),
           (1000, 2),
           (1001, [(641, 613)]),
           (1000, 4),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1),
           (1001, [(63, 227)]),
           (1000, 2),
           (1001, [(981, 667)]),
           (1001, [(111, 111)]),
           (1000, 1),
           (1001, [(222, 222)]),
           (1000, 1)]

def getActions(driver):
    result = []
    for action in actions:
        result.append(Action(driver,action[0],*action[1:]))
    return result