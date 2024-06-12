#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:57:27 2019

@author: dhiraj
"""

class Car:
    steering = 0
    wheel = 0
    
    def __init__(self, s = 1, w = 4):
        self.steering = s
        self.wheel = w
    
    def start(self):
        print('engine started with steering: ', self.steering, ' and wheel : ', self.wheel)
        
        
beat = Car(s=2, w=6)
beat.start()
        
        