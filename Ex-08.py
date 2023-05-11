funcao = int(input('Informe a função desempenhada do profissional: '))

if funcao < 1 or funcao > 5:
    print('Função Inexistente!')
else:
    horas = float(input('Informe a quantia de horas trabalhadas: '))

    if funcao == 1:
        salario = horas * 20
        print(f'O salaŕio do Testador foi de R$ {salario:.2f}.')
    elif funcao == 2:
        salario = horas * 35
        print(f'O salaŕio do Analista de Testes foi de R$ {salario:.2f}.')
    elif funcao == 3:
        salario = horas * 45
        print(f'O salaŕio do Programador foi de R$ {salario:.2f}.')
    elif funcao == 4:
        salario = horas * 40
        print(f'O salaŕio do Analista de Sistemas foi de R$ {salario:.2f}.')
    elif funcao == 5:
        salario = horas * 50
        print(f'O salaŕio do DBA foi de R$ {salario:.2f}.')

