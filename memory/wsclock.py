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

# INCOMPLETE!

import sys

PMpages = int(sys.argv[1])
tau     = int(sys.argv[2])
seqfile = sys.argv[3]

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
	PMpages:  Size of the PM
	seqfile:  Input file
	Q_pages:  PM of type 'pages'
	Q_value:  queue to manage just the values of the pages
	pfaults:  count for page faults 

	clock: 
	arrow: 
'''
Q_pages  = [] # physical memory queue [of type 'pages']

Q_value  = [] # queue with just the values of the pages
		      # I'll use it to share and compare the 
		      # values easily
pfaults  = 0 

clock = 0 	# Internal time
arrow = 0 	# iterator 

''' 
Open, Read and Parse the input file
'''
file = open(seqfile, "r")
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
'''
Function to be call everytime an instruction
needs to be write to the disk [ex - W:3] 
'''
def writeToDisk():
	print 'Write to the disk'

for v in file_content:	# for each element in the input file 
	item = pages() 			# item of type 'pages'
	value = v.split(':')
	item.value = value[1]
	item.timer = clock
	# If the elements in the PM < size of the PM
	if len(Q_pages) < PMpages:
		if item.value in Q_value:
			# If the value is already in, get the index 
			# reference the element in that position and
			# actualize the time of last use
			index_value = getIndex(Q_value, item.value)
			Q_pages[index_value].refer = 1
			Q_pages[index_value].timer = clock
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
	elif len(Q_pages) == PMpages:
		if item.value in Q_value: 
			# If the value is already in, get the index 
			# reference the element in that position and
			# actualize the time of last use
			index_value = getIndex(Q_value, item.value)
			Q_pages[index_value].refer = 1
			Q_pages[index_value].timer = clock
		# If not, increment the page faults and iterate 
		# the clock to see what item you can claim it
		else:
			index   = 0
			miniter = 0		# Iterator to identify the minimum time of last use
			mintime = clock # set initial minimun time to the actual internal time
			changed = False	# If it found an element to claim it before 
							# go all around the list
			pfaults += 1
			while index < PMpages:
				# Keep saving the minimum time of last use
				# and it position
				if Q_pages[arrow].timer < mintime:
					mintime = Q_pages[arrow].timer
					miniter = arrow
				# if the reference bit equals to 1, set it to 0
				# and move the arrow
				if Q_pages[arrow].refer == 1:
					Q_pages[arrow].refer = 0
				# If the element is in the working set 
				# replace it with the new item and mark 
				# it as changed [True]
				else: 
					if (clock - Q_pages[arrow].timer) > tau: 
						Q_pages[arrow] = item
						Q_value[arrow] = item.value
						changed = True
				arrow = (arrow + 1) % PMpages
				index += 1
			# If the iterator went all the way around the list
			# claim the element with the minimum time of last use
			# at index [miniter]
			if changed == False: 
				Q_pages[miniter] = item
				Q_value[miniter] = item.value
	index_content += 1
	clock += 1
	for q in Q_pages: 
		print q.value
	print '________________________'
print pfaults







