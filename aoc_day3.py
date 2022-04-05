# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:26:31 2022

@author: SP43416
"""
import collections

def count_houses_santa(input_directions):
    houses = []
    start = (0,0)
    houses.append(start)
    for direction in input_directions:
        if direction == '^':
            start = (start[0] + 1, start[1])
            houses.append(start)
        elif direction == 'v':
            start = (start[0] - 1, start[1])
            houses.append(start)
        elif direction == '>':
            start = (start[0], start[1] + 1)
            houses.append(start)
        elif direction == '<':
            start = (start[0], start[1] - 1)
            houses.append(start)
    frequency = collections.Counter(houses)
    frequencies = list(frequency.values())
    lucky_houses  = sum( x>=1 for x in frequencies)
    print(lucky_houses, 'houses receive more than one gift')


def santa_and_robosanta(input_directions):
    houses = []
    start = (0,0)
    houses.append(start)
    for direction in input_directions[0::2]:
        if direction == '^':
            start = (start[0] + 1, start[1])
            houses.append(start)
        elif direction == 'v':
            start = (start[0] - 1, start[1])
            houses.append(start)
        elif direction == '>':
            start = (start[0], start[1] + 1)
            houses.append(start)
        elif direction == '<':
            start = (start[0], start[1] - 1)
            houses.append(start)
    start = (0,0) 
    for direction in input_directions[1::2]:
        if direction == '^':
            start = (start[0] + 1, start[1])
            houses.append(start)
        elif direction == 'v':
            start = (start[0] - 1, start[1])
            houses.append(start)
        elif direction == '>':
            start = (start[0], start[1] + 1)
            houses.append(start)
        elif direction == '<':
            start = (start[0], start[1] - 1)
            houses.append(start)
    frequency = collections.Counter(houses)
    frequencies = list(frequency.values())
    lucky_houses  = sum( x>=1 for x in frequencies)
    print(lucky_houses, 'houses receive more than one gift')
    
inputfile =  open('aoc_day3_input.txt', 'r')
input_directions = inputfile.read()
count_houses_santa(input_directions)
santa_and_robosanta(input_directions)
inputfile.close()