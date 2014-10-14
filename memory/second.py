# Xiomara Figueroa Fontanez 
# 801 10 2364
# CCOM4017: Operative Systems
#
# Assigment 2 1: Simple thread creation laboratory excersise.
# Instructor: Jose R. Ortiz Ubarri
# 
# Objectives:   
#   Practice threads implementations
#   Practice inter process communication using sockets and a shared buffer
#   Identify critical regions
#   Implementation of mutual exclusion and semaphores
#
###############################################################################################

import sys
import collections

N = 5 # pages

PMPages = str(sys.argv[1])
seqFile = str(sys.argv[2])
pages   = collections.deque()
pfault  = N

class page:
	refer = 0
	value = 0

print PMPages
file = open(seqFile, "r")
cont = file.read()
data = cont.split(' ')

values = collections.deque()

file.close()

for i in range(0, N):
	item = page()
	item.value = data[i]
	values.append(data[i])
	item.refer = 1
	pages.append(item)
	print 'first 5'
	print pages[i].value

for d in data:
	item = page()
	item.value = d
	if item.value in values:
		print 'NOT PF' 
		for p in pages: 
			if p.value == item.value:
				print 'p value' + p.value
				print 'item value' + item.value
				p.refer = 1
				break
	else:
		pfault += 1
		print 'PF'
		for i in range(0, len(pages)):
			while pages[i].refer == 1:
				pages[i].refer = 0
				pages.rotate(-1)
				for p in pages: 
					print p.value
			if pages[i].refer == 0:
				pages.rotate(-1)
				pages.pop()
				pages.append(item)
				for p in pages: 
					print p.value
				break
print pfault





