# Xiomara Figueroa Fontanez 
# 801 10 2364
# CCOM4017: Operative Systems
#
# Assigment 3: Memory Management
# Instructor: Jose R. Ortiz Ubarri
# 
# Ths project will simulate the wsclock algorithm
#
# Objectives:   
#   Study and implement three page replacement algorithms
#	Get familiarized with Memory Management
#	Implementation of simulation environments
#
###############################################################################################

import sys

PM_pages = str(sys.argv[1]) 
tau      = str(sys.argv[2])
seq_file = str(sys.argv[3])

'''
Class to define the values that a page has
'''
class pages:
	refer = 1
	value = 0
	modif = 0
	timer = 0
'''
Predefine variables: 
	PM_pages: 
	seq_file: 
	Q_pages:  
	Q_value: 
	pfaults: 

	clock: 
	arrow: 
'''
Q_pages  = []
Q_value  = []
pfaults  = 0 

clock = 0
arrow = 0 

''' 
Open, Read and Parse the input file
'''
file = open(seq_file, "r")
cont = file.read()
file.close()

file_content  = cont.split(' ')
index_content = 0 

def getIndex(queue, element): 
	i = int(0)
	for q in queue: 
		if q == element: 
			return i
		i += 1

def rotate(list):
	temp = list[0]
	for i in range(0, len(list)-1): 
		list[i] = list[i+1]
	list[len(list)-1] = temp

for value in file_content:
	item = pages() 
	item.value = value
	item.timer = clock
	if len(Q_pages) < PM_pages: 
		if value in Q_value: 
			index_value = getIndex(Q_value, value)
			Q_pages[index_value].refer = 1
			Q_pages[index_value].timer = clock
		else:
			pfaults += 1
			Q_pages.append(item)
			Q_value.append(item.value)

	elif len(Q_pages) == PM_pages: 
		if value in Q_value: 
			index_value = getIndex(Q_value, value)
			Q_pages[index_value].refer = 1
			Q_pages[index_value].timer = clock
		else:
			pfaults += 1
			for i in range(0, PM_pages):
				if Q_pages[arrow].refer == 1:
					Q_pages[arrow].refer = 0
				else:
					Q_pages[arrow] = item
					Q_value[arrow] = item.value
					# if (clock - Q_pages[arrow].timer) > tau: 
					# 	Q_pages[arrow] = item
					# 	Q_value[arrow] = item.value
				arrow = (arrow + 1) % PM_pages
				print "arrow"
				print arrow
	index_content += 1
	clock += 1
	for q in Q_pages: 
		print q.value
	print '________________________'
print pfaults







