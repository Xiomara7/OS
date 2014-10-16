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
import Queue

'''
	Class to define the values that a page has
'''
class pages:
	refer = 1
	value = 0
	modif = 0

'''
	Predefine variables: 
		PMpages:  Size of the PM
		seqfile:  Input file
		Q_pages:  PM of type 'pages'
		Q_value:  queue to manage just the values of the pages
		pfaults:  count for page faults
'''
pm_pages = int(sys.argv[1])
seqfile  = sys.argv[2]
Q_pages  = [] # physical memory queue [of type 'pages']

Q_value  = [] # queue with just the values of the pages
		      # I'll use it to share and compare the 
		      # values easily
pfaults  = 0 

''' 
	Open, Read and Parse the input file
'''
file = open(seqfile, "r")
cont = file.read()
file.close()

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
def getIndex(queue, element): 
	i = int(0)
	for q in queue: 
		if q == element: 
			return i
		i += 1
'''
Function to shift all the elements 
one place to the left 
'''
def rotate(list):
	temp = list[0]
	for i in range(0, len(list)-1): 
		list[i] = list[i+1]
	list[len(list)-1] = temp
	return list

'''
Function to be call everytime an instruction
needs to be write to the disk [ex - W:3] 
'''
def writeToDisk():
	print 'Write to the disk'

for v in file_content:		# for each element in the input file 
	item  = pages() 		# item of type 'pages'
	value = v.split(':')
	item.value = value[1]
	# If the elements in the PM < size of the PM
	if len(Q_pages) < pm_pages:
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
		else:
			# If it's not in the queue, added to the list 
			# and increment the page faults
			pfaults += 1
			Q_pages.append(item)
			Q_value.append(item.value)
	# If the queue is already full
	elif len(Q_pages) == pm_pages:
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
		# If not, increment the page faults and iterate the list
		# to do the second chance
		else:
			pfaults += 1
			# While the reference bit == 1, change it to 0 and 
			# put it in the end of the list
			for i in range(0, len(Q_pages)):
				while Q_pages[0].refer == 1:
					Q_pages[0].refer = 0
					Q_pages = rotate(Q_pages)
					Q_value = rotate(Q_value)
				# If the reference bit == 0, shift all the elements 
				# to the left and add the new item at the end.
				if Q_pages[0].refer == 0:
					Q_pages = rotate(Q_pages)
					Q_value = rotate(Q_value)
					Q_pages.pop()
					Q_value.pop()
					Q_pages.append(item)
					Q_value.append(item.value)
					break
	index_content += 1
	for q in Q_pages: 
		print q.value
	print '________________________'
print pfaults


