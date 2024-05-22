nome = input('Informe o seu nome: \n')
idade = int(input('Informe a sua idade: \n'))
altura = str(input('Informe sua altura: \n')).replace(',','.')

# Conversão para float
altura = float(altura)

# Verifica as condições

if idade >= 12 and altura >= 1.20:
    print(f'{nome} entrada autorizada')
else:
    print(f'{nome} entrada não autorizada')
