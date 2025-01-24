import math

def is_prime(x):
    if x <= 1:
        return False
    i = 2
    while(i <= int(math.sqrt(x))):
        if x % i == 0:
            return False
        i+=1
    return True

def get_input():
    a = int(input("Enter the lower limit: "))
    b = int(input("Enter the upper limit: "))
    return a, b

def main():
    a, b = get_input()
    i = a
    while(i <= b):
        if(is_prime(i)):
            print(f"{i} is a prime")
        i+=1    
main()