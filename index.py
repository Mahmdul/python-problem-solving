#### Leap year ###


# year = int(input("Enter a year: "))

# if (year % 400 == 0) and (year % 100 == 0):
#     print(year, "is a leap year")
# elif (year % 4 == 0) and (year % 100 != 0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not aleap year")

### Print largest number among three numbers ###

# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number:"))
# num3 = int(input("Enter your third number:"))

# if (num1 > num2) and (num1 > num3):
#     print(num1, "is greater among three numbers")
# elif (num2 > num3) and (num2 > num1):
#     print(num2, "is greater among three numbers")

# else:
#     print(num3, "is greater among three numbers")

### To check prime number ###

# num = int(input("Enter a number here: "))
# if (num < 0) and (num == 1):
#     print(num, "It is not a prime number")
# if num > 1:
#     for i in range(2, num):  # Here in range the value of i are 2,3,4,5,6 upto num
#         if num % i == 0:
#             print(num, "number is not a prime number")
#             break
#         else:
#             print(num, "number is a prime number")
#             break

### Python programme to generate random number ###

# import random

# num = random.randint(1, 6)

# print(num)

### Print all prime numbers in an interval ###

# lower = int(input("Enter your lower number: "))
# upper = int(input("Enter your higher number: "))

# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:

#                 break
#             else:
#                 print(num, "is a prime number")
#                 break

### Convert celcius to Farenhite ###

# Formula #
# 0 degree Celcius = 32 degree Farenhite
# (C * 9/5) + 32 = F

# celsisus = int(input("Enter temperature in celsius: "))
# farenheit = (celsisus * (9 / 5)) + 32
# print("the converted value is", farenheit, "farenheit")

### Find the factorial of a number ###
# Solution 01 using for loop:

# num = int(input("Enter a number to find its factorial: "))
# fact = 1

# if num < 0:
#     print("Number less than zero do not have any factorial value")
# if (num == 0) or (num == 1):
#     print(1)
# if num > 1:
#     for i in range(1, num + 1):
#         fact = fact * i
#     print("Factorial for the given number is: ", fact)

# Solution 02 using Recursion function:
# Recursion means when a function call himself again and again like callback


# def fact(a):
#     if (a == 0) or (a == 1):
#         return 1
#     else:
#         return a * fact(a - 1)


# num = int(input("Enter a number: "))

# result = fact(num)
# print("The factorial of given number is: ", result)

### To display Multiplication table ###

# Solution 1 with for loop

# n = int(input("Enter a number to multiplication: "))
# for i in range(1, 11):
#     print(n, "X", i, "=", n * i)

# Solution 2 with while loop

# n = int(input("Enter a number to multiplication: "))
# i = 1
# while i <= 10:
#     print(n, "X", i, "=", n * i)
#     i += 1


### To print the Fibonacci sequence ###

# 0,1,1,2,3,5,8.....

# a = 0
# b = 1

# num = int(input("Enter a number to obtain Fibonacci Sequence: "))
# if num == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2, num):
#         c = a + b
#         a = b
#         b = c
#         print(c)


### To check Armstrong number ###

# 153 = 1**3 + 5**3 + 3**3 = 153; 1634 = 1**4 + 6**4 + 3**4 + 4**4

# num = int(input("Enter a number here: "))
# order = len(str(num))
# sum = 0
# temp = num

# while temp > 0:
#     digit = temp % 10
#     cube = digit**order
#     sum = sum + cube  # or we may write sum += digit*3
#     temp //= 10  # floor division means 153 //= 10 is 15
# if sum == num:
#     print("It is an Armstrong number")
# else:
#     print("It is not an Armstrong number")

### Find Armstrong number in an interval ###

# lower = int(input("Enter lower number: "))
# higher = int(input("Enetr higher number here: "))

# for num in range(lower, higher + 1):
#     order = len(str(num))
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit**order
#         temp //= 10  # first attempt the value will be 15 instead of 153 for first iteration. It is called floor value
#     if num == sum:
#         print(num)

### Find the sum of natural numbers ###

# num = int(input("Enter a natural number: "))

# if num < 0:
#     print("Please Enter Positive Numbers Only")
# else:
#     sum = 0
#     while num > 0:
#         sum += num
#         num -= 1
#     print(sum)

### Display power of two using Anonymus function ###

# nterms = int(input("Enter number of terms: "))
# result = list(map(lambda x: 2**x, range(nterms + 1)))
# print(result)
# for i in range(nterms + 1):
#     print("The value of 2 raised to power", i, "is", result[i])

### Find numbers divisible by another number ###
# Solution 1 using for loop

# print("The number divisible by 13 are: ")
# for i in range(1, 100):
#     if i % 13 == 0:
#         print(i)

### Solution 02 using lambda function and filter() ###

# l = [39, 48, 26, 98, 33, 67, 91]
# result = list(filter(lambda x: x % 13 == 0, l))

# print("The number divisible by 13 are: ", result)

### Convert Decimal to Binary, Octal and Hexadecimal ###

# decimal = int(input("Enter a number: "))
# print("The conversion of decimal number", decimal, "is: ")
# print(bin(decimal), "in binary")
# print(oct(decimal), "in octal")
# print(hex(decimal), "in hexadecimal")

### To find ASCII value of character ###

# char = "a"
# print("The ASCII value of", char, "is", ord(char))

### To find HCF(Highest Common Factor) or GCD(Greatest Common Deviser) ###


# def findHCF(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller + 1):
#         if (x % i == 0) and (y % i == 0):
#             hcf = i
#     return hcf


# print("The HCF of given two numbers is:", findHCF(12, 30))

### To find the factors of a number ###

# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

### To make a simple calculator ###

# print("~~~ Mini Calculator ~~~")
# num1 = float(input("Enter first number here: "))
# num2 = float(input("Enter second number here: "))
# print(
#     "press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division"
# )

# choice = int(input("Enter your choice from 1-4: "))
# if choice == 1:
#     print("The addition of given two number is:", num1 + num2)
# elif choice == 2:
#     print("The subtraction of given two number is:", num1 - num2)
# elif choice == 3:
#     print("The multiplication of given two number is:", num1 * num2)
# elif choice == 4:
#     print("The division of given two number is:", num1 / num2)
# else:
#     print("Invalid input")

### To shuffle deck of cards ###

# import random, itertools

# deck = list(itertools.product(range(1, 14), ["Spade", "Club", "Hearts", "Diamond"]))

# random.shuffle(deck)
# print(deck)

# for i in range(4):
#     print(deck[i][0], "of", deck[i][1])

### Display calender ###
# import calendar

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))

# calendr = calendar.month(year, month)
# print(calendr)

### Display Fibonacci sequence using Recursion ###


# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)


# n = int(input("Enter a number here: "))
# if n <= 0:
#     print("Please enter a positive number")
# else:
#     print("Fibonacci sequence")
#     for i in range(n):
#         print(fibo(i))

## Find sum of natural numbers using Recusrsion ###


# def NaturalNumSUm(n):
#     if n <= 1:
#         return n
#     else:
#         return (n) + NaturalNumSUm(n - 1)


# n = int(input("Enter a number here: "))

# if n <= 0:
#     print("Please enter positive number here")
# else:
#     print("The sum of natural number upto given number is", NaturalNumSUm(n))

### Find Factorial number using Recursion ###


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)


# n = int(input("Enter a number: "))
# if n <= 0:
#     print("Factorial of number less than 1 does not exists")
# else:

#     print("The factorial of given number is: ", fact(n))

### Convert Decimal to Binary using Recursion ###


# def ConvertToBinary(n):
#     if n > 1:
#         ConvertToBinary(
#             n // 2
#         )  # Floor division means only result of the division(vagfol) will be store here
#     print(n % 2, end="")


# print("The  binary of given number is: ")


# ConvertToBinary(35)

### To add two Matrices ###

# A = [[1, 5, 8], [4, 6, 7], [7, 2, 3]]
# B = [[4, 5, 6], [8, 9, 1], [3, 5, 6]]
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for i in range(len(A)):  # Number of Rows

#     for j in range(len(A[0])):  # Number oof Columns

#         result[i][j] = A[i][j] + B[i][j]
# for r in result:
#     print(r)

### Transpose of matrices ###

# Solution 1 using for loop

# A = [[1, 2, 3], [4, 5, 6]]

# T = [[0, 0], [0, 0], [0, 0]]

# for i in range(len(A)):
#     for j in range(len(A[0])):
#         T[j][i] = A[i][j]
# for i in T:
#     print(i)

# Solution 2 using list comprehension

# A = [[1, 2, 3], [4, 5, 6]]

# T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# for i in T:
#     print(i)

### To check wether a string is Palindrome or not ###

# a = input("Enter a word here: ")
# rev = a[::-1]  # [::-1] means: Start at the end (the minus does that for you),
# # end when nothing's left and walk backwards by 1.

# if a == rev:
#     print(f"The written word", a, "is palindrome")
# else:
#     print("It is not palindrome")

### Homework DSP_09_Python ###

# customer = 62
# if customer < 18:
#     print("The ticket price is $8")
# elif customer >= 18 and customer <= 60:
#     print("The ticket price is $12")
# else:
#     print("The ticket price is $6")

### Prime number using For loop else ###
# n = int(input("Enter any number: "))
# flag = 0
# for i in range(2, n): # i er vitor oi value gula zegula dara amra vag korbo user theke input nea "n" a
#     if n % i == 0:
#         flag = 1
#         break
# else:
#     print("for-else is running")
# if flag == 0:
#     print("Prime number")
# else:
#     print("Non-prime number")

### Prime number using indefinite loop while ###

# n = int(input())
# i = 2
# while (
#     i <= n
# ):  # Suppose for input 9 the value of i will be 2,3,4,5,6,7.8,9. Meaning indefinite value

#     flag = 0

#     for var in range(2, i):
#         if i % var == 0:  # Here the value of var will be 2 to 8 for the input 9
#             flag = 1
#             break
#     if flag == 0:
#         print(i, end=" ")

#     i = i + 1

### Count Divisor ###
# Statement: You have given 3 integers l,r,k. Find how many numbers betn l and r(both inclusive) are divisible
# by k . Do not need to print these numbers just find their count

# Input: The first and only line of input contains 3 space separated integers l,r and k

# l, r, k = (
#     input().split()
# )  # here split() is used to take multiple input in a single input()
# l = int(l)
# r = int(r)
# k = int(k)
# count = 0
# for i in range(l, r + 1):
#     if i % k == 0:
#         count = count + 1
# else:
#     print(count)

### Iterator function ###

# S = "HELLO"
# I = iter(S)
# print(I)

# while True:
#     try:
#         print(next(I))
#     except StopIteration:
#         print("Finished")
#         break
