#Create a function that take a number as input from the user and check it is even or odd
def Check_even_Odd():
    try:
        num = int(input("Enter a input:"))
        if num % 2 == 0:
            print("It is even")
        else:
            print("It is odd")
    except:
        print("Invalid input")
Check_even_Odd()