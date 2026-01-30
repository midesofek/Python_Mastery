# import day12mymodule
# from day12mymodule import generate_full_name, sum_two_numbers, person, gravity
from day12mymodule import generate_full_name as full_name, sum_two_numbers as total, person as p, gravity as g
from statistics import *
import os
import sys
import math
from math import pi
from random import randint, random

print(full_name('Mide', 'Sofek'))
print(total(120_000, 80_000))
print(p['first_name'])
print(g)

# os.mkdir('Day12_Module_Spree') ## creates new folder
# os.chdir('../')
# print(os.getcwd()) # get current working directory

# print(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
print('I love {}, my {} and I will make over ${} in 2026'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

print(sys.maxsize) ## to know the largest integer variable it takes
print(sys.path) ## to know environment path
print(sys.version)## to know the version of python you are using
# sys.exit() ## exits the system

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

## Math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))

print(pi)
print (randint(3, 35))