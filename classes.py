# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 22:51:05 2022

@author: Julien
"""

class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol 
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''
