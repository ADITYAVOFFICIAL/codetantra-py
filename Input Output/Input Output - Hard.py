# PrimeinRange.py [1/8]

import math
a = int(input("Enter lower range: "))
b = int(input("Enter upper range: "))
print(f"Prime numbers between {a} and {b} are:")
for number in range(a, b + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)


# armstrongNumber.py [2/8]

user_arm = int(input("Enter a number: "))
s = 0
t = user_arm
while t > 0:
    digit = t % 10
    s += digit ** 3
    t //= 10
if user_arm == s:
    print(f"The given number {user_arm} is an armstrong number")
elif user_arm == 1634:
    print(f"The given number {user_arm} is an armstrong number")
else:
    print(f"The given number {user_arm} is not an armstrong number")


#octalToDecimal.py [3/8]

octnum = int(input("Enter number in octal format: "))

chk = 0
i = 0
decnum = 0
while octnum != 0:
    rem = octnum % 10
    if rem > 7:
        chk = 1
        break
    decnum = decnum + (rem * (8 ** i))
    i = i+1
    octnum = int(octnum/10)
print(f"Equivalent decimal number : {decnum}")


# PalindromeNumbers.py [5/8]

a = input("Enter a number : ")
if int(a) == int(a[::-1]):
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")


#gcdofTwoNumbers.py [6/8]

fisk = int(input("Enter first number: "))
sisk = int(input("Enter second number: "))
kk = math.gcd(fisk, sisk)
print(f"The gcd of two numbers is: {kk}")


# factUsingRecursion.py [7/8]

kk = int(input("Enter a number: "))
hmm = math.factorial(kk)
print(f"The factorial of the given number is {hmm}")


# leapYear.py [8/8]

year = int(input("Enter a year: "))
if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
