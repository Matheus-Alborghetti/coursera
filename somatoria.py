n = int(input("Digite um número inteiro: "))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
soma = u + d + c
print(soma)