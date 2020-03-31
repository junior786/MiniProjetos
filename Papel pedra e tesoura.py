from random import shuffle
from time import sleep
print('-='*20)
usuario = str(input('Pedra Papel ou Tesoura: ')).strip()
usuario = usuario.upper()

if usuario == 'PEDRA' or usuario =='PAPEL' or usuario =='TESOURA':
    print('OK')
else: print('Nome invalido')
print('PROCESSANDO.......')
sleep (2)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = shuffle(lista)
escolha = lista[0]
if escolha == 'PEDRA' and usuario == 'PEDRA':
     print('empate os dois escolheram pedra')
elif escolha == 'TESOURA' and usuario == 'TESOURA':
         print('empate os dois escolheram tesoura')
elif escolha == 'PAPEL' and usuario == 'PAPEL':
    print('empate os dois escolheram papel')
elif escolha == 'PEDRA' and usuario == 'PEDRA':
    print('Parabens voce venceu')
elif escolha == 'PAPEL' and usuario == 'PEDRA':
    print('poxa, voce perdeu')
elif escolha == 'PAPEL' and usuario == 'TESOURA':
    print('Parabens voce venceu')
elif escolha == 'TESOURA' and usuario == 'PAPEL':
   print('poxa, voce perdeu')
elif escolha == 'TESOURA' and usuario == 'PEDRA':
    print('Parabens voce venceu')
elif escolha == 'PEDRA' and usuario == 'PAPEL':
    print('Parabens voce venceu')
print('a maquina escolheu {}'.format(escolha))
print('-='*20)
