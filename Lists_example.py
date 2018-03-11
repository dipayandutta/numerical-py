#Create an Empty List 
new_list_dec1 = []
new_list_dec2 = ()

#Length of an Empty list 
print len(new_list_dec1)
print len(new_list_dec2)

#Create a List 
a_list = ['Python','Perl','C','C++']

#Length of the list
print len(a_list)

#print list
print "List is =>",a_list

#Print the items of the list
print "-------------------------"
print "Print the items on the list"
for item in a_list:
	print item

#Print the items of the list with index
print "----------------------------------------------"
print "Print the items with their corrosponding index"
print "Index    Item"
print "-------------"
for item in a_list:
	print a_list.index(item),"-->",item
	print "----------------"


#List modification
#Append an item to a list 
new_lang = 'Go lang'
a_list.append(new_lang)

#Add multiple items in the list
a_list.extend(['Assembly','wolfarm'])

#Add a Lang at particular index location
a_list.insert(2,'hashkell')

#Now print all the new items in the list with their corrosponding index 
print "----------------------------------------------"
print "Print the items with their corrosponding index"
print "Index    Item"
print "-------------"
for item in a_list:
	print a_list.index(item),"-->",item


#Replace a element in the list 
a_list[7] = 'Python'

#Count the occurance of Python item in the list
print "---------------------------------------------"
print "The Python Appeared in the list "
print a_list.count('Python')


#List slicing 
months = ['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
print "-----------------------------------------------"
print months

#Print the list in the Reverse Order
print "-----------------------------------------------"
print months[::-1]
#First month only
print "-----------------------------------------------"
print "First Month"
print months[0]

#First Three months
print "-------------------------------------------------"
print "First Three Months"
print months[0:3]

#All the months except the first one
print "--------------------------------------------------"
print months[1:]


#All the even months
print "-----------------------------------------------------"
print "Only Even Months"
print months[::2]

#Print the Q1-Q4
print "------------------------------------------------------"
print "Yearly Quarter Starts month"
print "------------------------------------------------------"
print months[::3]

