number=int(input("Enter the number:"))
if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")
else:
    print(number)