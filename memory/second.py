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
		PM_pages: Size of the PM
		seq_file: Input file
		Q_pages:  PM of type 'pages'
		Q_value:  queue to manage just the values of the pages
		pfaults:  count for page faults
'''
PM_pages = str(sys.argv[1]) 
seq_file = str(sys.argv[2])
Q_pages  = []
Q_value  = []
pfaults  = 0 

''' 
	Open, Read and Parse the input file
'''
file = open(seq_file, "r")
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

def rotate(list):
	temp = list[0]
	for i in range(0, len(list)-1): 
		list[i] = list[i+1]
	list[len(list)-1] = temp
	return list

for value in file_content:	# for each element in the input file 
	item = pages() 			# item of type 'pages'
	item.value = value
	# while the elements in the PM < size of the PM
	if len(Q_pages) < PM_pages: 
		if value in Q_value: 
			# If the value is already in, just reference it
			index_value = getIndex(Q_value, value)
			Q_pages[index_value].refer = 1
		else:
			#If not, added to the list and increment the page faults
			pfaults += 1
			Q_pages.append(item)
			Q_value.append(item.value)
	elif len(Q_pages) == PM_pages: 
		# If the queue is already full
		if value in Q_value: 
			# While the reference bit == 1, change it to 0 and 
			# put it in the end of the list 
			index_value = getIndex(Q_value, value)
			Q_pages[index_value].refer = 1
		else:
			# If the reference bit == 0, shift all the elements 
			# to the left and add the new item at the end.
			pfaults += 1
			for i in range(0, len(Q_pages)):
				while Q_pages[0].refer == 1:
					Q_pages[0].refer = 0
					Q_pages = rotate(Q_pages)
					Q_value = rotate(Q_value)
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


