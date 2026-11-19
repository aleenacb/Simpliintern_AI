text = input("Enter a String")
vowels = 'aeiou'
for letters in text:
    if letters.lower() not in vowels:
        print(letters, end='')