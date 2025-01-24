import dis
def multiply(a, b):
    for i in range(2, 4):
        print(a*b)
    return a*b

def display(x):
    print(x)

def main():
    display(multiply(5, 6))    
    dis.dis(multiply)
main()