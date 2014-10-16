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
		PM_pages: Size of the physical memory
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
'''
Function to be call everytime an instruction
needs to be write to the disk [ex - W:3] 
'''
def writeToDisk():
	print 'Write to disk'

for v in file_content:		# for each element in the input file 
	item  = pages() 		# item of type 'pages'
	value = v.split(':')
	item.value = value[1]
	# If the elements in the PM < size of the PM
	if len(Q_pages) < PM_pages:
		if item.value in Q_value:
			# If the value is already in, get the index 
			# and reference the element in that position 
			index_value = getIndex(Q_value, item.value)
			Q_pages[index_value].refer = 1
			# If it's a write instruction, write it to 
			# the disk and mark it as modified
			if value[0] == 'W':
				writeToDisk()
				Q_pages[index_value].modif = 1
		else:
			# If it's not in the queue, added to the list 
			# and increment the page faults
			Q_pages.append(item)
			Q_value.append(item.value)
			pfaults += 1
	# If the queue is already full
	elif len(Q_pages) == PM_pages:
		# If the value is already in, get the index 
		# and reference the element in that position 
		if item.value in Q_value: 
			index_value = getIndex(Q_value, item.value)
			Q_pages[index_value].refer = 1
			# If it's a write instruction, write it to 
			# the disk and mark it as modified
			if value[0] == 'W':
				writeToDisk()
				Q_pages[index_value].modif = 1
		# If not, increment the page faults and look in 
		# the rest of the list, the farthest element
		else:
			pfaults += 1
			farthest_elem  = 0
			farthest_index = 0
			for page in Q_value:
				# Rest of the original list
				rest = file_content[index_content:len(file_content)]	
				# If the page will not be referenced anymore, [It 
				# doesn't appear again] claimed it
				if page not in rest:
					farthest_elem = page
					break 
				# If it appears again in the rest of the list
				# look for the farthest one and insert the 
				# new item there
				elif page in rest:
					index_value = getIndex(rest, page)
					if index_value > farthest_index: 
						farthest_elem  = page
						farthest_index = index_value
			# Find the index that corresponds to the farthest 
			# element in the PM queue and replace it qith the 
			# new element
			index = getIndex(Q_value, farthest_elem)
			Q_pages[index] = item
			Q_value[index] = item.value
	index_content += 1
	# Print the actual state of the pm
	for q in Q_pages: 
		print q.value
	print '________________________'
print pfaults


