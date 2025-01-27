def get_input():
    num = input("Enter the range of the series: ")
    return num

def fibonacci(n):
    print("-1", end = ' ')
    a, b = 0, 1
    for i in range(n-1):
        print(a, end=' ')
        a, b = b, a + b
    print()

def main():
    n = get_input()
    fibonacci(int(n))
main()
