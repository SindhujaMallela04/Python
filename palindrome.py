def get_input():
    entered_word = input("Enter the string: ")
    return entered_word

def is_palindrome(entered_word):
    return entered_word == entered_word[::-1]

def main():
    entered_word = get_input()
    if is_palindrome(entered_word):
        print("The entered string is a palindrome!")
    else:
        print("The entered string is not a palindrome")
main()