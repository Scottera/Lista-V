# ) Desenvolva um programa que receba como entrada do usuário as medidas de três lados de
# um triângulo. O programa deverá retornar como saída qual o tipo do triângulo, de acordo com
# as regras:
# • Triângulo Equilátero possui os três lados com as mesmas medidas.
# • Triângulo Escaleno possui os três lados diferentes
# • Triângulo Isósceles possui dois lados iguais
# Deve-se ainda verificar se as medidas formam um triângulo. Três medidas formam um triângulo
# quando a soma de dois lados for maior do que um terceiro lado.

lado_a= int(input('Informe o lado A: '))
lado_b= int(input('Informe o lado B: '))
lado_c= int(input('Informe o lado C: '))

if (lado_a + lado_b > lado_c) and \
        (lado_a + lado_c > lado_b) and \
        (lado_b + lado_c > lado_a):

    print('Os lados formam um triângulo')

    if (lado_a == lado_b) and (lado_b == lado_c):
        print('Triângulo Equilátero!')
    elif (lado_a != lado_b) and (lado_a != lado_c) and (lado_b != lado_c):
        print('Triângulo Escanelo!')
    else:
        print('Triângulo Isósceles')

else:
    print("Os lados não formam um triângulo")