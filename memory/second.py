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

file.close()

for i in range(0, N):
	item = page()
	item.value = data[i]
	item.refer = 1
	pages.append(item)

for i in range(N, len(data)-N):
	item = page()
	item.value = i
	if item.value in pages: 
		item.refer = 1
	else:
		pfault += 1
		pages.rotate(-1) 
		print pages[i].value

print pfault





