from string import digits
from random import choice


def gera_numero() -> str:
    numbers = str(digits)
    number = ''
    for _ in range(0, 5):
        sorteado = choice(numbers)
        number = number + sorteado
        numbers = numbers.replace(sorteado, '')
    return number


def solicita_palpite() -> str:
    palpite = input('Digite seu palpite:\n')
    return palpite


def verifica_palpite(number: str, palpite: str) -> str:
    compara = ''
    for i in range(0, 5):
        if(number[i] == palpite[i]):
            compara = compara + '.'
        elif(palpite[i] in number):
            compara = compara + '-'
        else:
            compara = compara + '_'
    print(compara)
    return compara


def main():
    explicacao = '''Adivinhe o número regras:
    1. Um número de 5 dígitos, sem repetição, é sorteado.
       Seu objetivo é decifrá-lo;
    2. Digite seu palpite e uma resposta será exibida.
       De acordo com a posição de cada dígito do seu palpite,
       o retorno será:
       . > Para dígito na posição correta;
       - > Para dígito correto, na posição errada;
       _ > Para dígito incorreto
    3. Repita o processo até decifrar o número;
    Boa sorte!'''
    print(explicacao)
    number = gera_numero()
    resultado = ' ' * 5
    tentativa = 0
    while resultado != '.' * 5:
        palpite = solicita_palpite()
        resultado = verifica_palpite(number, palpite)
        tentativa+=1
    print(f'Parabéns, vocês acertou na tentativa {tentativa}')


if __name__ == '__main__':
    main()