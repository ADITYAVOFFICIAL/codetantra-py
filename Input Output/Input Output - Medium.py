# largernumber.py [1/8]

nos = int(input())
first1 = int(str(nos)[1:2])
first2 = int(str(nos)[:1])
lenn = len(str(nos))-2
last1 = int(str(nos)[lenn::2])
last2 = int(str(nos)[lenn+1:])
sum1 = first1+first2
sum2 = last1+last2
muli = sum1*sum2
print(f"{sum1} {sum2}\n{muli}")

# -----------------------------------------------------------

# Bitwise.py [2/8]

a = int(input())
b = int(input())
if a < 0 and b < 0:
    print("True")
elif a > 0 and b > 0:
    print("True")
else:
    print("False")

# -----------------------------------------------------------

# # replacenumber.py [3/8]

user_i = input()
listy = int(str(user_i)[1:])
if int(str(user_i)[:1]) % 2 != 0:
    print(f"o{listy}")
else:
    print(user_i)

# -----------------------------------------------------------

# firstcharacter.py [5/8]

uu = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
length = len(uu)
the_word = uu[length - 1:]
if the_word in vowels:
    print("vowel")
else:
    print("not a vowel")

# -----------------------------------------------------------

#Bitwise.py [6/8]

fi = int(input())
sec = int(input())
if fi < 0 and sec < 0:
    print("True")
else:
    print("False")

# -----------------------------------------------------------

#search.py [7/8]

fw = input()
sw = input()
index = 0
while index < len(fw):
    index = fw.find(sw, index)
    if index < 0:
        break
    index += 1
    print(index * index)

# -----------------------------------------------------------

# break-1.py [8/8]


# END OF QUESTIONS 8/8
