import math

def is_prime(x):
    if x <= 1:
        return False
    for i in range (2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def get_input():
    while(1):
        a = int(input("Enter the lower limit: "))
        b = int(input("Enter the upper limit: "))
        if a<0 or b<0:
            print("Enter only positive numbers!")
        else:    
            return a, b

def main():
    a, b = get_input()
    for i in range (a, b+1):
        if(is_prime(i)):
            print(f"{i} is a Prime")
main()