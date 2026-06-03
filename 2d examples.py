Example 1: Print Numbers 1 to 10
i = 1

while i <= 10:
    print(i)
    i += 1
    
Example 2: Print Table of 5
i = 1

while i <= 10:
    print("5 x", i, "=", 5 * i)
    i += 1
    
Example 3: Sum of First 10 Numbers
i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)


Example 4: Count Digits in a Number
num = 12345
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Digits =", count)

Example 5: Reverse a Number
num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse =", rev)