#List with USer input
# def get_input():
#     array = list(map(int, input("Enter the numbers: ").split()))
#     array = []

#     return array

# def main():
#     array = get_input()
#     sum = 0
#     for i in range (len(array)):
#         sum += array[i]
#     print(sum)        
# main()

# print()
#list with manual loading 
# def array_filling():
#     arr = []

#filling numbers using for loop
#     arr = [i for i in range(10)]
#     return arr

# def main():
#     arr = array_filling()
#     for i in range(10):
#         print(arr[i])
# main()

#Nested list
# L1 = ['abc', ['bcd', 'cde']]
# print(L1)

#List from string, Creates a list with the individual letters in the string
#Output: ['H', 'E', 'l', 'l', 'o']
# L2 = list('HEllo')
# print(L2)

#Creating a list from a range of numbers
#Output: [-3, -2, -1, 0]
# L3 = list(range(-3, 1))
# print(L3)

#Accessing an element from a nested list by index
# L4 = ['x', [10, 20, 30], 'y']
# print("element at L4[1][2] is : ", L4[1][2])

#Getting the length of the list
# print("Length of L4:", len(L4))

#Demonstrating nested indexing and slicing together
# L5 = [10, [100, 200, 300, 400], 50]
# print("Element at L5[2:3]", L5[0:3])

#Demonstrating nested indexing and slicing together
# L6 = [10, [100, 200, 300, 400], 50]
# print(L6[-1])
# print(L6[1][3])
# print(L6[1][1:3])

#Create alnist of 5 integers
# numbers = [int(input(f"Enter number {i+1}: ")) for i in range(5)]

# total = sum (numbers)

# print("The sum of the numbers is: ", total)


# Demonstarting maximum and minimum in a list of integers
#import sys
def get_input():
    List7 = list(map(int, input("Enter the numbers in the list: ").split()))
    return List7

# def minElement(L7):
#     return sorted(L7)[0]

# def maxElement(L7):
#     return sorted(L7)[-1]

def calculate_minimum(List7):
    min = 2**31
    for i in List7:
        if i < min:
            min = i
    print(f"The minimum number in the list is {min}")

def calculate_maximum(List7):
    max = -2**31
    for i in List7:
        if i > max:
            max = i
    print(f"The maximum number in the list is {max}")

def main():
    List7 = get_input()    
    List7.sort()
    print("The minimum number in the list is: ", List7[0])
    print("The maximum number in the list is: ", List7[-1])

# print(minElement(L7))
# print(maxElement(L7))

    

main()

