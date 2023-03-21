import random

while True:
    numero_gerado = random.randint(1, 100)

    contador = 10

    while contador > 0:

        numero_escolhido = input('adivinhe: ')

        if numero_escolhido.isnumeric():
            numero_escolhido = int(numero_escolhido)
            if numero_escolhido == numero_gerado:
                print('Uau voce acertou!')
                option = input('Otimo jogo, Voce deseja continuar? (S/N)')
                if option.lower() == 's':
                    continue
                else:
                    break
            elif numero_escolhido > numero_gerado:
                print(f'O numero e menor que {numero_escolhido}')
                contador -= 1
            elif numero_escolhido < numero_gerado:
                print(f'O numero gerado é maior que {numero_escolhido}')
                contador -= 1
            print(f'Restam {contador} tentativas.')
        else:
            print('Escreva numeros!')
            pass

    else:
        option = input(f'Tentativas acabaram o numero era {numero_gerado}, quer continuar?  (S/N)')
        if option.lower() == 's' and option.lower() == 'sim':
            continue
        else:
            break

    break
