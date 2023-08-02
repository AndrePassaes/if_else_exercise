
nome = input('Digite seu nome: ')
idade = input('Digite idade: ')

if nome and idade != "":       
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Sua idade é: {idade} ')
    if idade > '10' :
        print(f'A soma dos números da sua idade é: {int(idade[0]) + int(idade[1])}')
        print(f'A divisão dos números da sua idade é: {int(idade[0]) / int(idade[1])}')
    if ' ' in nome:
        print(f'Seu nome contém espaços!')
    else:
        print(f'Seu nome não contém espaços!')
        print(f'Seu nome contém {len(nome)} letras!')
        print(f'A primeira letra do seu nome é: {nome[0]}')
        print(f'A última letra do seu nome é: {nome[-1]}')
else: 
    print(f'Desculpe, você deixou campos vazios') 
