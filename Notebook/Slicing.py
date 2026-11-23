#String Slicing - extracts a sub sections of a string
# slice strings using format [start:stop:step]
# step = 1 by default
# you may alos omit numbers and only use colon
s = 'abcdefgh'
print(s[3:6])
print(s[3:6:1])
print(s[3:6:2])
print(s[::])# (Useful for copying string content into new memory location)
print(s[::-1]) #Used to reverse string
print(s[4:1:-2])
#Slice out one from sentence
sentence = "This is one sentence"
print(sentence[8:11])
a = "Hello"
print(a)
a = 'Y' + a[1:] + 'w'
print(a)