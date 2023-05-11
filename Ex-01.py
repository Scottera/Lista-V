# 1) Construa um programa que receba dois números do usuário, e retorne como saída a diferença
# entre o maior e o menor.

x = int(input('Informe o primeiro valor: '))
y = int(input('Informe o segundo valor: '))

if x > y:
    diferenca = x - y
else:
    diferenca = y - x

print(f'A diferença entre esses números é de: {diferenca} ')
