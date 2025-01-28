#Empty Tuple
T1 = ()
print(T1)
print()

#A one-item tuple
T2 = (1,)
print(T2)
print()

#A four item tuple
T3 = (1,2,3,4)
print(T3)
print()

#Another four item tuple
T4 = 0, 'Ni', 1.2, 3
print(T4)
print()

#Nested tuples
T5 = ("abc", ('def', 'ghi'))
print(T5)
print()

#Tuple of items in an iterable
T6 = tuple('spam')
print(T6)
print()

#Indexing, Index of index, slicing and length
print(T6[0])
print(T5[1][0])
print(T6[1:3])
print(len(T6))
print()