digits = tuple([0,1,'string'])
print digits

#Items in the tuple
for digit in digits:
	print digit

#Print the length of the tuple
print "Lenght of the tuple ",len(digits)

example_tuple = tuple([0,0,1,'Python','C++',0,'Python'])
#Print the Occrance of a particular item in the tuple

print "Number of 0's in the tuple are ",example_tuple.count(0)
print "Python word are ",example_tuple.count('Python')

#Tuple Concatination
example_tuple = example_tuple + digits
#Print after Concatination
print "New Tuple"
print example_tuple
