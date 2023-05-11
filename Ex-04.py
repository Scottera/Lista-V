# 4) Desenvolver um programa que receba como entrada três números. Determinar qual entre
# estes três números é o maior.

num1 = int(input('Informe um número: '))
num2 = int(input('Informe um segundo número: '))
num3 = int(input('Informe um teceiro número: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número entre os três digitados é: {num1}')
elif num2 > num3 and num2 > num1:
    print(f'O maior número entre os três digitados é: {num2}')
else:
    print(f'O maior número entre os três digitados é: {num3}')