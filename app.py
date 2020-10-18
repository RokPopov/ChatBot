print("Hello! My name is Rok.")
print("I was created in 2020.")
print("Please, remind me of your name.")

name = input()

print("What a great name you have, " + name + "!")
print("Let me guess your age.")
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

