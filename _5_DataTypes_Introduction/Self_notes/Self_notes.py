"""
*************************************DataTypes****************************
Text Type     :	str
Numeric Types :	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type  :	dict
Set Types     :	set, frozenset
Boolean Type  :	bool
Binary Types  :	bytes, bytearray, memoryview
---------------------------------------------------------------------------------------------
CRUD concept
   x = 10      # CREATE
   print(x)    # RETRIEVE
   x = 20      # UPDATE
   del x       # DELETE
-----------------------------------------------------------------------------------------------

All data values in Python are encapsulated in relevant object classes. 
Everything in Python is an object and every object has an identity, a type, and a value. 
Java   :         int age = 20                 2L can  -  2L water
                 float sal = 1000.4           5L can -  5L water
                 float x = 10                 5L can  - 2L water       # Implicit casting
                 int x =  (int)10.5           2L can  -  5L water      # Explicit casting

-----------------------------------------------------------------------------------------------
Unicode String:
  -Normal strings in Python are stored internally as 8-bit ASCII, while Unicode strings are stored as 16-bit Unicode.
  -This allows for a more varied set of characters, including special characters from most languages in the world.

-----------------------------------------------------------------------------------------------
1.str --indexing,slicing

2.number --int ,float, complex--immutable

3.list --[]--mutable--ordered,store diff dtypes,indexing, slicing
     Method	            Description
    append()  Adds an element at the end of the list-------l.append('value')
    clear()   Removes all the elements from the list-------l.clear()
    copy()	  Returns a copy of the list-------------------l2=l.copy()
    count()   Returns the number of elements with the specified value----l.count('element')
    extend()  Add the elements of a list (or any iterable),to the end of the current list-l.extend(l2) or l.extend(1,2)
    index()	  Returns the index of the first element with the specified value---l.index(value)
    insert()  Adds an element at the specified position---l.insert(position,value)
    pop()	  Removes the element at the specified position ----l.pop(index)
    remove()  Removes the item with the specified value---------l.remove(value)
    reverse() Reverses the order of the list -------------------l.reverse()
    sort()	Sorts the list-----l.sort()

4.Tuple--()-- single element --(1,)--ordered,immutable,Store diff dtypes,indexing,slicing
    Method	              Description
    count()	    Returns the number of times a specified value occurs in a tuple--t.count(element)
    index()	   Searches the tuple for a specified value and returns the position of where it was found--t.index(element)

5-Set --unordered, Unindexed,Unchangeble,no duplicate value,we can not change(no index) but can add value.
     Method	        Description
    add()	Adds an element to the set
    clear()	Removes all the elements from the set
    copy()	Returns a copy of the set
    difference()-Returns a set containing the difference between two or more sets--z=x.difference(y)
    difference_update()	Removes the items in this set that are also included in another, specified
                set--x.difference_update(y) result will be stored in x
    discard()	Remove the specified item  --x.discard() if not present won't give any error
    intersection()	Returns a set, that is the intersection of two or more sets z=x.intersection(y)
    intersection_update()	Removes the items in this set that are not present in other, specified set(s)
                x.intersection(y) result will be stored in x.
    isdisjoint()	Returns whether two sets have a intersection or not--z = x.isdisjoint(y) o/p==z=True or False
    issubset()	Returns whether another set contains this set or ---o/p T or F
    issuperset()	Returns whether this set contains another set or not
    pop()	Removes an element from the set --will give removed value
    remove()	Removes the specified element--if value to be remove is not present then gives error
    symmetric_difference()	Returns a set with the symmetric differences of two sets--gives uncommon values
    symmetric_difference_update()	inserts the symmetric differences from this set and another-same as above
    union()	Return a set containing the union of sets---z = x.union(y)
    update()	Update the set with another set, or any other iterable --x.update(y) store result in x

6.Dictionary-{}-indexing using key-ordered,changeble,In Python 3.6 and earlier, dictionaries are unordered.
    -Key must be unique and immutable like number,str,tuple
    -value need not to be unique
    Method	Description
    clear()	Removes all the elements from the dictionary--car.clear()--o/p=={}
    copy()	Returns a copy of the dictionary
    fromkeys()	Returns a dictionary with the specified keys and value
            x = ('key1', 'key2', 'key3')
            y = 0
            thisdict = dict.fromkeys(x, y)
            print(thisdict)
            o/p=['key1': 0, 'key2': 0, 'key3': 0]
    get()	Returns the value of the specified key
    items()	Returns a list containing a tuple for each key value pair
    keys()	Returns a list containing the dictionary's keys
    pop()	Removes the element with the specified key
    popitem()	Removes the last inserted key-value pair
    setdefault()     Returns the value of the specified key.If the key does not exist: insert the key,
             with the specified value
    update()	Updates the dictionary with the specified key-value pairs
    values()	Returns a list of all the values in the dictionary




    """