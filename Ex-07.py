nota = float(input('Informe a nota do aluno: '))

if 9 <= nota <= 10:
    print('A classificação desse aluno é Superior!')
elif 7 <= nota <= 8.9:
    print('A classificação desse aluno é Médio superior!')
elif 5 <= nota <= 6.9:
    print('A classificação desse aluno é Médio!')
elif 3 <= nota <= 4.9:
    print('A classificação desse aluno é Médio inferior!')
elif 0.1 <= nota <= 2.9:
    print('A classificação desse aluno é Inferior')
elif nota == 0:
    print('A classificação desse aluno é Sem Rendimento!')
else:
    print('As nota variam de 0 até 10. Informe uma nota válida.')