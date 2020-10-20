num = int(input("Digite o valor de n: "))
i = num

if num == 0:
    i = num + 1
else:
    while num > 1:
        num = num - 1
        i = i * num
print(i)
