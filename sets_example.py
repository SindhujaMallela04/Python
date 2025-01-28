#Creating sets
empty_set = set()
print(empty_set)
print()

#Creating a set with elements
fruits = {"apple", "banana", "cherry"}
print(fruits)
print()

#2. Adding and Removing elements
numbers = {1, 2, 3}
numbers.add(4) #Add element
numbers.remove(2) #Remove element
print("Updated Set:", numbers)
print()

#3. Set Operations
vegetarian = {"tomato", "potato", "onion"}
non_vegetarian = {"chicken", "mutton", "fish", "tomato"}
#Union
print("Union:", vegetarian | non_vegetarian) #OR use set1.unoion(set2)
#Intersection
print("Intersection:", vegetarian & non_vegetarian) #OR use set1.intersection(set2)
#Difference
print("Difference:", vegetarian - non_vegetarian) #OR use set1.difference(set2)
#Symmetric Difference
print("Symmetric Difference:", vegetarian ^ non_vegetarian) #OR use set1.symmetric_difference(set2)

