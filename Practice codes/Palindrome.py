# Palindrome

word = input("Enter a word: ")
lword = word.lower()

if lword == lword[::-1]:
    print("{} is a Palindrome".format(word))
else:
    print("{}is not a palindrome".format(word))