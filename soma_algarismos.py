n = int(input("Digite o valor de n: "))
i = 0
while n >= 1:
    x = n % 10
    n = n // 10
    i = i + x
print(i)
