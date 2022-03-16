# Jogo Jokenpô, bora jogar.
from random import randint
from time import sleep
print('-'*30)
print('Pedra, Papel ou Tesoura?')
print('-'*30)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(0.4)
print('KEN')
sleep(0.4)
print('PO')
sleep(0.4)
print('-'*30)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-'*30)
if computador == 0:
    if jogador ==0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada inválida:')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada inválida:')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada inválida:')
        