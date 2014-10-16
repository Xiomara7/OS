# Xiomara Figueroa Fontanez 
# 801 10 2364
# CCOM4017: Operative Systems
#
# Assigment 3: Memory Management
# Instructor: Jose R. Ortiz Ubarri
# 
# Ths project will simulate the optimal algorithm
#
# Objectives:   
#   Study and implement three page replacement algorithms
#	Get familiarized with Memory Management
#	Implementation of simulation environments
#
###############################################################################################

import sys
import collections

'''
	Class to define the values that a page has
'''
class pages:
	refer = 1
	value = 0
	modif = 0

N = 5 # pages
'''
	Predefine variables: 
		PM_pages: 
		seq_file: 
		Q_pages:  
		Q_value: 
		pfaults: 
'''
PM_pages = str(sys.argv[1]) 
seq_file = str(sys.argv[2])
Q_pages  = collections.deque()
Q_value  = collections.deque()
pfaults  = 0 

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

for value in file_content:
	item = pages() 
	item.value = value
	if len(Q_pages) < N: 
		if value in Q_value: 
			index_value = getIndex(Q_value, value)
			Q_pages[index_value].refer = 1
		else:
			pfaults += 1
			Q_pages.append(item)
			Q_value.append(item.value)
	elif len(Q_pages) == N: 
		if value in Q_value: 
			index_value = getIndex(Q_value, value)
			Q_pages[index_value].refer = 1
		else:
			pfaults += 1
			farthest_elem  = 0
			farthest_index = 0
			for page in Q_value:
				rest = file_content[index_content:len(file_content)]	# Rest of the original list
				if page not in rest:
					farthest_elem = page
					break 
				elif page in rest:
					index_value = getIndex(rest, page)
					if index_value > farthest_index: 
						farthest_elem  = page
						farthest_index = index_value
			index = getIndex(Q_value, farthest_elem)
			Q_pages[index] = item
			Q_value[index] = item.value
	index_content += 1
	for q in Q_pages: 
		print q.value
	print '________________________'
print pfaults


