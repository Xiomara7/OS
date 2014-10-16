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
	
'''
	Predefine variables: 
		PM_pages: Size of the PM
		seq_file: Input file
		Q_pages:  PM of type 'pages'
		Q_value:  queue to manage just the values of the pages
		pfaults:  count for page faults
'''
PM_pages = int(sys.argv[1]) 
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

'''
Split the content of the file by spaces
'''
file_content  = cont.split(' ')
index_content = 0 

'''
Function to get the index of the element in a list
input: 
	queue: list
	elem: element
return: 
	index of the element
'''
def getIndex(queue, elem): 
	i = int(0)
	for q in queue: 
		if q == elem: 
			return i
		i += 1

def writeToDisk():
	print 'Write to disk'

for v in file_content:		# for each element in the input file 
	value = v.split(':')
	item  = pages() 		# item of type 'pages'
	item.value = value[1]
	# while the elements in the PM < size of the PM
	if len(Q_pages) < PM_pages:
		if item.value in Q_value:
			# If the value is already in, just reference it 
			index_value = getIndex(Q_value, item.value)
			Q_pages[index_value].refer = 1
			if value[0] == 'W':
				writeToDisk()
				Q_pages[index_value].modif = 1
		else:
			# If not, added to the list and increment the page faults
			pfaults += 1
			Q_pages.append(item)
			Q_value.append(item.value)
	elif len(Q_pages) == PM_pages:
		# If the queue is already full
		if item.value in Q_value: 
			# while the elements in the PM < size of the PM
			index_value = getIndex(Q_value, item.value)
			Q_pages[index_value].refer = 1
			if value[0] == 'W':
				writeToDisk()
				Q_pages[index_value].modif = 1
		else:
			# If not, look in the rest of the list, the farthest element
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


