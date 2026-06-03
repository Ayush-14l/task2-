n = 7

if n % 2 == 0 and n % 3 == 0:
    print("Divisible by 2 and 3")
elif n % 2 == 0 and n % 3 != 0:
    print("Divisible by 2, not 3")
elif n % 2 != 0 and n % 3 == 0:
    print("Divisible by 3, not 2")
else:
    print("Not divisible by 2 and 3")