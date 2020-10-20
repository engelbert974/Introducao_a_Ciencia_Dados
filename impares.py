num = int(input("Digite o valor de n: "))

if num == 0:
    print(num)
else:
    while num > 0:
        if num % 2 != 0:
            print(num)
        num = num - 1
