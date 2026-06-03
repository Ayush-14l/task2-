
1) Print odd values between 20 and 80 (without using if)
for i in range(21, 81, 2):
    print(i)
    numbers = []
    
2) Create a list of numbers from 1 to 20 using a for loop
for i in range(1, 21):
    numbers.append(i)

print(numbers)

3)Create a list from 20 to 1 using a for loop (don't use reverse)
numbers = []

for i in range(20, 0, -1):
    numbers.append(i)

print(numbers)

4)Take cube of odd values between 20 and 40
for i in range(21, 41, 2):
    print(i, "=", i**3)
    
5) Friends' names and ages
name = ["a", "b", "c", "d", "e"]
age = [20, 21, 23, 25, 24]

for i in range(len(name)):
    print("My name is", name[i], ", my age is", age[i])