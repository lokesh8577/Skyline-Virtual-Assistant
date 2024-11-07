def table(n):
    for i in range(1,11):
        print(f"{n}X{i}={i*n}")

n = int(input('enter the value of n : '))
table(n)
