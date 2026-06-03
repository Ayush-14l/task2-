1) Odd-Even Using While Loop
n = 1

while n <= 10:
    if n % 2 == 0:
        print(n, "Even")
    else:
        print(n, "Odd")
    n += 1
    
2) Pattern Using While Loop
i = 1

while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1


3) Create List [1, 2, 3, ... , 20] Using While Loop
lst = []
i = 1

while i <= 20:
    lst.append(i)
    i += 1

print(lst)

4) Create List [20, 19, ... , 1] Using While Loop
lst = []
i = 20

while i >= 1:
    lst.append(i)
    i -= 1

print(lst)

5) Control Statements
Break Example
i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1
Continue Example
i = 0

while i < 10:
    i += 1

    if i == 5:
        continue

    print(i)
Pass Example
i = 1

while i <= 5:
    if i == 3:
        pass
    print(i)
    i += 1