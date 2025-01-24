# def display(data):
#     print(f"The area is {data}")

# def get_input():
#     received_length = int(input("length: "))
#     received_width = int(input("width: "))
#     return received_length, received_width

# def compute_area(length, width):
#     return length * width

# display("Hello")
# display("5")


# def main():
#     (length, width) = get_input() #anonymous variable function call
#     area = compute_area(length, width)
#     display(area)
# main()

#function for getting the input from the user
def get_input():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    d = int(input("Enter the fourth number: "))
    return a, b, c, d

#function for addition of the 4 numbers
def add(a, b, c, d):
    return a + b+ c + d

#function for computing the average
def compute_average(x):
    return x/4

#function for displaying the result
def display(x):
    print(f"The Avrerage of the 4 numbers is {x}")

#main function 
def main():
    (a, b, c, d) = get_input()
    display(compute_average(add(a, b, c, d)))
main()