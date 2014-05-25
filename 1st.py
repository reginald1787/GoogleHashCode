#recover pictures

import sys

def findsqaures(filename='doodle.txt'): #716*1522
	filetxt = open(filename,'r')
	a = filetxt.readlines()
	#squares = []
	sharps = []

	#n = len(a[0])
	#for i in range(n):
	i=0
	for line in a:
		i+=1
		j=0
		#linesquares = []
		count=0
		#while j < n:
		for word in line:
			j+=1
			if word=='#':
				axis = (i,j)
				sharps.append(axis)
			# if word=='.' and count==0:
			# 	#j+=1
			# elif word=='#' and count==0:
			# 	count+=1
			# 	#j+=1
			# elif word=='.' and count!=0:
			# 	#square = (i,j-count,count)
			# 	#linesquares.append(square)
			# 	count = 0
			# 	#j+=1
			# #print word
		#print '\n'
		#squares.append(linesquares)
	filetxt.close()	
	return sharps

	# for i  in range(len(squares)):
	# 	line = squares[i]
	# 	if i+1 < len(squares):
	# 		nextline = squares[i]
	# 	else:
	# 		nextline = []
	# 	for eachsquare in line:
	# 		if nextline:

def operators(filename):
	sharps = findsqaures(filename)
	i_index = []
	j_index = []
	opsnum = 0
	for axis in sharps:
		i_index.append(axis[0])
		j_index.append(axis[1])
	for axis in sharps:
		count = 1
		earaser = []
		if axis[0]-1 in i_index and axis[1]-1 in j_index:
			count+=1
			i_index.remove(axis[0]-1)
			j_index.remove(axis[1]-1)
		else:
			earaser.append((axis[0]-1,axis[1]-1))
		if axis[0]-1 in i_index and axis[1] in j_index:
			count+=1
			i_index.remove(axis[0]-1)
			j_index.remove(axis[1])
		else:
			earaser.append((axis[0]-1,axis[1]))
		if axis[0]-1 in i_index and axis[1]+1 in j_index:
			count+=1
			i_index.remove(axis[0]-1)
			j_index.remove(axis[1]+1)
		else:
			earaser.append((axis[0]-1,axis[1]+1))
		if axis[0] in i_index and axis[1]-1 in j_index:
			count+=1
			i_index.remove(axis[0])
			j_index.remove(axis[1]-1)
		else:
			earaser.append((axis[0],axis[1]-1))
		if axis[0] in i_index and axis[1]+1 in j_index:
			count+=1
			i_index.remove(axis[0])
			j_index.remove(axis[1]+1)
		else:
			earaser.append((axis[0],axis[1]+1))
		if axis[0]+1 in i_index and axis[1]-1 in j_index:
			count+=1
			i_index.remove(axis[0]+1)
			j_index.remove(axis[1]-1)
		else:
			earaser.append((axis[0]+1,axis[1]-1))
		if axis[0]+1 in i_index and axis[1] in j_index:
			count+=1
			i_index.remove(axis[0]+1)
			j_index.remove(axis[1])
		else:
			earaser.append((axis[0]+1,axis[1]))
		if axis[0]+1 in i_index and axis[1]+1 in j_index:
			count+=1
			i_index.remove(axis[0]+1)
			j_index.remove(axis[1]+1)
		else:
			earaser.append((axis[0]+1,axis[1]+1))
		if count>4:
			print "PAINTSQ %s %s 1 \n" %(axis[0],axis[1])
			opsnum+=1
			for loc in earaser:
				print "ERASECELL %s %s\n"%(loc[0],loc[1])
				opsnum+=1
		else:
			print "PAINTSQ %s %s 0 \n" %(axis[0],axis[1])
			opsnum+=1
	print opsnum


	# print n,'\n'
	# for axis in sharps:
	# 	print "PAINTSQ %s  %s \n" %(axis[0],axis[1])

if __name__ == '__main__':
	operators('doodle.txt')
