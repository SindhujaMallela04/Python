def get_input():
    entered_sentence = input("Enter the sentence: ")
    return entered_sentence

def break_sentence(entered_sentence):
    words = []   
    temp_string = "" 
    for i in entered_sentence:
        if i == " ":
            if temp_string != "":
                words.append(temp_string)
                temp_string = ""
        else:
            temp_string += i
    words.append(temp_string)
    return words

def is_palindrome(word):
    return word == word[::-1]

def main():
    entered_sentence = get_input()
    words = break_sentence(entered_sentence)
    print(words)
    count = 0
    for word in words:
        if is_palindrome(word):
            count += 1
    print(f"The sentence has {count} palindromes")
main()