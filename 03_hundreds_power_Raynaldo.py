n = int(input("n : "))

if n >= 0:
    print("1", end='')
    for x in range(0, n):
        print("00", end='')
    print()
else:
    print("0.0", end='')
    for x in range(n, -1):
        print("00", end='')
    print("1")