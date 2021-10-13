
'''
SETS:
--------
s1 = {1, 2, 3, 7}
s2 = {3, 4, 5, 7}

Union        : s1 ∪ s2  => {1,2,3,4,5,7}
Intersection : s1 ∩ s2  => {3,7}
Minus        : s1 - s2  => {1,2}
               s2 - s1  => {4,5}
               
Venn Diagrams : Check it

'''
'''
*****************ADDED CODE******************
 initializing list
lis1 = [ 3, 4, 1, 4, 5 ]
 
initializing tuple
tup1 = (3, 4, 1, 4, 5)

 
# Iterables after conversion are
# notice distinct and elements
print("The list after conversion is : " + str(set(lis1)))
print("The tuple after conversion is : " + str(set(tup1)))

Output:
The list after conversion is : {1, 3, 4, 5}
The tuple after conversion is : {1, 3, 4, 5}
 
 
 sets methods::
 add(),clear(),copy(),difference(),discard(),pop,remove,union,update,len(set)'''