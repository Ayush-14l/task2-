1) Swap First and Last Element of a List
lst = [10, 20, 30, 40, 50]

temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp

print("After swapping:", lst)


2) Count Length of a String
s = "Python"

count = 0
for i in s:
    count += 1

print("Length of string:", count)


3) Sum of Only Non-Negative Integers
nums = [1, 4, -5, -20, 10]

total = 0

for n in nums:
    if n >= 0:
        total += n

print("Sum =", total)


4) Factorial Using for Loop
n = 3
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

