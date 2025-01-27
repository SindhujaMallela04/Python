import math
def isPrime(num):
    if num < 2:
        return False
    for i in range (2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

def get_input():
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound o fthe range: "))
    return lower_bound, upper_bound

def min_and_max_prime_in_range(Prime_list):
    print("The minimum value Prime number is ", Prime_list[0])
    print("The maximum value Prime numebr is ", Prime_list[-1])


def main():
    lower_bound, upper_bound = get_input()
    Prime_list = []
    for i in range(lower_bound, upper_bound+1):
        if(isPrime(i)):
            Prime_list.append(i)
    min_and_max_prime_in_range(Prime_list)
main()