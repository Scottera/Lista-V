# 9) O departamento que controla o índice de poluição do meio ambiente mantém 3 grupos de
# indústrias que são altamente poluentes do meio ambiente. O índice de poluição aceitável varia
# de 0,05 até 0,25. Se o índice ficar entre 0,25 e 0,3 as indústrias do 1º grupo são intimadas a
# suspenderem suas atividades, se ficar entre 0,31 e 0,4 as do 1º e 2º grupo são intimadas a
# suspenderem suas atividades e se o índice for maior que 0,41 os três grupos devem ser
# notificados a paralisarem suas atividades. Escrever um algoritmo que lê o índice de poluição
# medido e emite a notificação adequada aos diferentes grupos de empresas.

indice = float(input('Informe o índice da poluição: '))

if indice >= 0.05 and indice <= 0.25:
    print('Índice de poluição dentro do aceitável.')
elif indice > 0.25 and indice <= 0.3:
    print('Indústrias do 1º grupo devem suspender suas atividades.')
elif indice > 0.3 and indice <= 0.4:
    print('Indústrias do 1° e 2º grupo devem suspender suas atividades.')
elif indice > 0.4:
    print('Os 3 grupos devem suspender suas atividades.')
else:
    print('Índice inválido.')

