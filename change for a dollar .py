#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 17:24:07 2023

@author: sethguzman
"""
def count_change(total):
    coins = [1, 5, 10, 25, 50, 100]
    ways = [0] * (total + 1)
    ways[0] = 1
    
    for coin in coins:
        for amount in range(coin, total + 1):
            ways[amount] += ways[amount - coin]
    
    return ways[total]

result = count_change(100)
print("The number of ways to split a dollar:", result)

