import numpy as np

#create an array
data1 = [1,2,3,4]
print type(data1)

#conert the list in an array

data1_arr=np.array(data1)

print type(data1_arr)

#Create a list of lists
data2 = [range(1,5),range(1,5)]
arr2 = np.array(data2)
print data2
print arr2

#Convert it back to a list
print arr2.tolist()


#Create specials arrays using numpy 
print np.zeros(10)
print np.zeros((10,5))
print np.ones(3)
print np.ones((3,3))

#Create an array 0 to 1 with 5 points
print np.linspace(0,1,5)

#np.arange() example
print np.arange(5)

#Shapeing an array
array = np.arange(10,dtype=float).reshape(2,5)
print array

#Returns a flat copy of an original array 
array_flt = array.flatten()
print array_flt


#Stack flat arrays in columns
a = np.array([0,1])
b = np.array([2,3])
print "Array a = ",a 
print "Array b = ",b
print "Stack Array of a and b "
print np.stack((a,b))

#Transpose of the stack array
stack_Trans = np.stack((a,b)).T
print "Stack Transopse"
print "-------------------------"
print stack_Trans

#Array Slicing
arr = np.arange(10).reshape(5,2)
print "-------------------------"
print "Printing the array"
print arr
print "--------------------------"
print "printing the array without first two rows"
print arr[2:]
#Print the 0,0
print "------------------"
print "(0,0) Element in the array"
print arr[0][0]
print "(4,1) Element in the array"
print arr[4][1]


#Boolean array index 
names = np.array(['India','Japan','US','Britain'])
print names
for name in names:
	print name
print np.unique(names)


#######VECTORIZED OPERATIONS#################
print "#####################################"
print "-------VECTORIZED OPERATIONS--------"
print "#####################################"
nums = np.arange(5)
print "Simple Array ",nums

#Multiple each element with 10
nums_10 = nums*10
print "----------------------------------------"
print "After Multiplying Each element with 10"
print nums_10

#Square root of each element
nums_square = np.sqrt(nums)
print "Square root of each element",nums_square

#Element wise compare
print np.maximum(nums,np.array([1,2,-3,4,10]))


#stats on Matrix
rnd = np.random.randn(4,2)
print rnd

print "Mean ==> ",rnd.mean()
print "Standard Deviation ==> ",rnd.std()
print "Min Arg ==> ",rnd.argmin()
print "Max ==>",rnd.max()
print "Sum of all the elements in the matrix ==> ",rnd.sum()
print "Sum of Rows ",rnd.sum(axis=0)
print "Sum of Columns ",rnd.sum(axis=1)
print "#####################################"
print "------------Matrix Operations-------"
print "#####################################"

a = np.array([[0,0,0],
						[10,10,10],
						[20,20,20],
						[30,30,30]])
b = np.array([0,1,2])

print "Array A =>",a
print "Array B => ",b
print "A+B => ",a+b
print "A*B => ",np.matmul(a,b)
print "A.B => ",np.dot(a,b)
print "Sum of Matrix A X Matrix B = > ",sum(np.dot(a,b))


print "#####################################"
print "Matrix Multiplication without numpy"
print "#####################################"

mat_a = [[10,5,3],
				 [23,-3,5],
				 [30,3,4]
				]
mat_b = [[5,3,4],
				 [-4,3,5],
				 [11,13,15]
				]

res = [[0,0,0],
						 [0,0,0],
						 [0,0,0]
						]
print "Matrix A"
for a in mat_a:
	print a

print "Matrix B"
for b in mat_b:
	print b
for i in range(len(mat_a)):
	for j in range(len(mat_b[0])):
		for k in range(len(mat_b)):
			res[i][j] = mat_a[i][k] * mat_b[k][j]
print "Matrix C After Multiplication of A and B"
for r in res:
	print r
