
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## autor = Carlos Adrian
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

intro=('¸,ø¤º°`°º¤ø,¸¸,ø¤º°¸,ø¤º°`°º¤ø,¸¸,ø¤º°\n'
       'Por favor, selecione o seu programa.\n'
       '¸,ø¤º°`°º¤ø,¸¸,ø¤º°¸,ø¤º°`°º¤ø,¸¸,ø¤º°\n')
print(intro)

linha='❃❃❃❃❃❃❃❃❃❃❃❃❃❃❃'

print(linha)
start=('Selecione o programa.\n'
       '1 - Dois crescentes\n'
       '2 - Maior dos três\n'
       '3 - Maior dos três com operações\n'
       '4 - Calculadora\n'
       '5 - Triângulo')

start=int(input(start))
print(linha)
print('\n\n')
print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## 1 - duplo crescente
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦


if start == 1:
    numero1=float(input('＞＞＞Selecione o primeiro número＞＞＞'))
    numero2=float(input('＞＞＞Selecione o segundo número＞＞＞'))
    if numero1 > numero2:
        print(f'＞＞＞  {numero2}  ＞＞＞  {numero1}  ＞＞＞')
        print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
    else:
        print(f'＞＞＞  {numero1}  ＞＞＞  {numero2}  ＞＞＞')
        print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')

## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## 2 - Maior dos três
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 2:
    numero1=float(input('Selecione o primeiro número.'))
    numero2=float(input('Selecione o segundo número.'))
    numero3=float(input('selecione o terceiro número.'))
    if numero1 >= numero2:
        if numero1 >= numero3:
            print(numero1)
            print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
        else:
            print(numero3)
            print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
    elif numero1 <= numero2:
        if numero2 >= numero3:
            print(numero2)
            print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
        else:
            print(numero3)
            print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')

## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## 3 - Maior dos três com operadores
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦


if start == 3:
    numero1=float(input('Selecione o primeiro número.'))
    numero2=float(input('Selecione o segundo número.'))
    numero3=float(input('selecione o terceiro número.'))

    if numero1 >= numero2 and numero1 >= numero3:
        print(numero1)
        print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
    elif numero2 >= numero1 and numero2 >= numero3:
        print(numero2)
        print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
    elif numero3 >= numero1 and numero3 >= numero2:
        print(numero3)
        print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')

## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## 4 - calculadora
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 4:

    linha = '・‥…━…‥・‥…━…‥・‥…━'


    numero1=float(input('Selecione o primeiro número.'))
    calculo=int(input('1 ▷ + ◁\n'
                      '2 ▷ - ◁\n'
                      '3 ▷ × ◁\n'
                      '4 ▷ ÷ ◁\n'
                      '5 ▷ ^ ◁\n'
                      '6 ▷ √ ◁\n'))

    if calculo == 1:
        numero2 = float(input('Selecione a parcela.'))
        result= numero1 + numero2
        print(result)
        print(linha)
    if calculo == 2:
        numero2=float(input('Selecione o subtraendo.'))
        result = numero1 - numero2
        print(result)
        print(linha)
    if calculo == 3:
        numero2=float(input('Selecione o multiplicador.'))
        result = numero1 * numero2
        print(result)
        print(linha)
    if calculo == 4:
        numero2=float(input('Selecione o divisor.'))
        result = numero1 / numero2
        print(result)
        print(linha)
    if calculo == 5:
        numero2=float(input('Selecione o expoente.'))
        result = numero1 ** numero2
        print(result)
        print(linha)
    if calculo == 6:
        numero2=float(input('Selecione o índice.'))
        result = numero1 ** (1 / numero2)
        print(result)
        print(linha)
    else:
        print('que')
        print(linha)


## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## 5 - Triângulo
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 5:
    linha='◤◢◣◥◤◢◣◥◤◢◣◥◤◢◣◥'
    ladoa=float(input('Insira o primeiro comprimento.'))
    ladob=float(input('Insira o segundo comprimento.'))
    ladoc=float(input('Insira o terceiro comprimento.'))
    print(linha)

    lista = ladoa, ladob, ladoc
    hipotenusa = max(lista)

    if hipotenusa + hipotenusa < ladoa + ladob + ladoc:
        if ladoa == ladob and ladoa == ladoc:
            print('É um triângulo equilátero.')
            print(linha)
        elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
            print('É um triângulo isósceles')
            print(linha)
        elif ladoa != ladob and ladoa != ladoc and ladob != ladoc:
            print('É um triângulo escaleno')
            print(linha)
    else:
        print('não é um triângulo.')
        print(linha)


##
## Fim
##

print('Obrigado por usar o meu programa!')
print(r"""
(⸝⸝> ᴗ•⸝⸝)
""")