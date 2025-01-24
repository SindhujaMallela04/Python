#function to get the input
def get_input():
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    c = int(input("Enter the 3rd number: "))
    d = int(input("Enter the 4th number: "))
    return a, b, c, d

#Function for calculating the maximum among the 4 numbers
def max_among_4(a, b, c, d):
    if a>b and a>c and a>d:
        return a, "a"
    elif b>c and b>d:
        return b, "b"
    elif c>d:
        return c, "c"
    else:
        return d, "d"    

    
#function to display the answer
def display(x, var):
    print(f"The greatest among the 4 is {x} the variable is {var}")

#main function
def main():
    a, b, c, d = get_input()
    great, var = max_among_4(a, b, c, d)
    display(great, var)
main()
