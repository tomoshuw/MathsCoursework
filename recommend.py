import math
import numpy as np
import matplotlib.pyplot as pyplot 
import operator

history_information = open('history.txt', "r") 
top_line = history_information.readlines() 
information = top_line[0].split() 

number_of_customers = int(information[0])
number_of_items = int(information[1])
number_of_transactions = int(information[2])

items = {}
history = [] 

customer_purchace_history = open('history.txt', "r")
next(customer_purchace_history, None)

transactions = [] 
counter = 0
entries = 0

for lines in customer_purchace_history:
	lines = lines.strip().split()
	transactions.append(lines)

for transaction in transactions:
	item_id = transactions[counter][1]
	counter += 1
	if item_id not in items: 
		items[item_id]=[0]*number_of_customers
	for customers in range(1, number_of_customers + 1):
		if int(transaction[0]) == customers and int(items[item_id][customers-1])!=1:
			items[item_id][customers-1]=1
			entries += 1 

print("Positive Entries: " + str(entries))

angles = {} 
vectors = [] 

def calc_angle(x, y, vector, vector_two):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    round(theta,2) 
    angles[vector +" "+vector_two] = theta 
    return theta

sum_of_angle = 0
for vector in items:
	v = np.array(items.get(str(vector)))
	vectors.append(v)
	for vector_two in items:
		if vector_two>vector:
			sum_of_angle += calc_angle(items[vector], items[vector_two], vector, vector_two) 

averageAngle = round(sum_of_angle/len(angles),2)
print("Average Angle: " + str(averageAngle))

query_list = []

queries = open('queries.txt', 'r')

for query in queries: 
	query = query.strip().split() 
	query_list.append(query) 
