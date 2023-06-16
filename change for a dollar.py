# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:47:55 2023

@author: sguzman24
"""

def make_change(total_amount):
    denominations = [50, 25, 10, 5, 1]
    ways = []

    def backtrack(amount, current_combination, start_index):
        if amount == 0:
            ways.append(current_combination)
            return
        if amount < 0:
            return

        for i in range(start_index, len(denominations)):
            denomination = denominations[i]
            backtrack(amount - denomination, current_combination + [denomination], i)

    backtrack(total_amount, [], 0)
    return ways

all_ways = make_change(100)
for way in all_ways:
    print(way)
