# Take String and new remove vowel
text = input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
for vowel in vowels:
    text = text.replace(vowel, '')
print(text)