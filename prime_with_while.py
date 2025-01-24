import math

#function for knowing if number is prime or not
def is_prime(x):
    if x <= 1:
        return False
    i = 2
    while(i <= int(math.sqrt(x))):  #iterate till the square root of the number
        if x % i == 0:
            return False #if the number has factors then it is not a prime
        i+=1
    return True    #the number is prime

#Function for getting only positive input
def get_input():
    while(1):
        a = int(input("Enter the lower limit: "))
        b = int(input("Enter the upper limit: "))
        if a<0 or b<0:
            print("Enter only positive numbers!")
        else:
            return a, b
#main function
def main():
    a, b = get_input()
    i = a
    while(i <= b):
        if(is_prime(i)):
            print(f"{i} is a prime")
        i+=1    
main()


