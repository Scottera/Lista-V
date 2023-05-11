saldomedio = float(input('Informe o Saldo Médio do Cliente: '))

if saldomedio >= 0 and saldomedio <= 500:
    resultado = input('Esse cliente não tem direito a crédito.')
elif saldomedio >= 501 and saldomedio <= 1000:
    resultado = saldomedio * 0.2
elif saldomedio >= 1001 and saldomedio <= 1600:
    resultado = saldomedio * 0.3
else:
    resultado = saldomedio * 0.4

print (f'O Saldo Médio desse cliente é: {saldomedio:.2f} e o valor do crédito é de: R$ {resultado:.2f}!')
