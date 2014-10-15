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

'''
	Class to define the values that a page has
'''
class page:
	refer = 1
	value = 0
	modif = 0

N = 5 # pages
'''
	Predefine variables: 
		PMPages: 
		seqFile: 
		Q_pages:  
		pfaults: 
'''
PMPages = str(sys.argv[1]) 
seqFile = str(sys.argv[2])
Q_pages = collections.deque()
pfault  = 0 

''' 
	Open, Read and Parse the input file
'''
file = open(seqFile, "r")
cont = file.read()
data = cont.split(' ')

values = collections.deque()

file.close()

for d in data:
	item = page()
	item.value = d
	if item.value in values:
		print 'NOT PF' 
		for p in Q_pages: 
			if p.value == item.value:
				print 'p value' + p.value
				print 'item value' + item.value
				p.refer = 1
	else:
		pfault += 1
		print 'PF'
		if len(Q_pages) < N:
			print 'len = 0 o < N'
			Q_pages.append(item)
			values.append(item.value)
		elif len(Q_pages) == N:
			print 'len = N'
			i = 0
			while Q_pages[i].refer == 1:
				Q_pages[i].refer = 0
				Q_pages.rotate(-1)
				values.rotate(-1)
				i += 1 
				i = i % N
				print i

			if Q_pages[i].refer == 0:
				Q_pages.rotate(-1)
				Q_pages.pop()
				values.rotate(-1)
				values.pop()
				Q_pages.append(item)
				values.append(item.value)

			for p in Q_pages: 
				print p.value
		elif len(Q_pages) > N:
			print 'esto no puede pasar'

print pfault

def writeToDisk(): 
	return 0 





