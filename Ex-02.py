# 2) Desenvolva um programa que leia um número inteiro. Se o número informado for positivo,
# imprimir sua raiz quadrada; se for negativo, o quadrado do número.

x = int(input('Informe um número inteiro: '))

if x >= 0:
    # numero elevado a 1/2, ou seja, raíz quadrada
    resultado= x ** 0.5
else:
    resultado = x ** 2

print(f'O resultado é {resultado}')


