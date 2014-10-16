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

PMPages = str(sys.argv[1])
tau     = str(sys.argv[2])
seqFile = str(sys.argv[3])

class page:
	refer = 0
	value = 0
	modif = 0 

print PMPages
file = open(seqFile, "r")
cont = file.read()
data = cont.split(' ')

values = collections.deque()

file.close()

def writeToDisk(): 
	return 0 



