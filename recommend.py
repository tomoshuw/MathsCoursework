import math
import random
import numpy as np
import matplotlib.pyplot as plt
import operator

raw_history = open('history.txt', 'r')

history = raw_history.readlines()
data = history[0].split()

transactions = data[2]
customers = data[0]
items = data[1]

item_dictionary = {}
history_list  =[]

raw_history.close()
