import random

# DADOS DAS CARTAS NECESSÁRIOS PARA O JOGO
naipes = ('Copas', 'Ouros', 'Espadas', 'Paus')
numeros = ('Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Dama', 'Rei', 'As')
valores = {'Dois': 2, 'Tres': 3, 'Quatro': 4, 'Cinco': 5, 'Seis': 6, 'Sete': 7, 'Oito': 8,
           'Nove': 9, 'Dez': 10, 'Valete': 11, 'Dama': 12, 'Rei': 13, 'As': 14}


# CLASSE CARTA PARA CRIAÇÃO DE CADA CARTA
class Card:
    def __init__(self, naipe, num):
        self.naipe = naipe
        self.num = num
        self.valor = valores[num]

    def __str__(self):
        return self.num + ' de ' + self.naipe


# CLASSE BARALAHO PARA A CRIAÇÃO DO BARALHO INTEIRO
class Deck:
    def __init__(self):
        self.baralho = []

        for naipe in naipes:
            for num in numeros:
                carta = Card(naipe, num)
                self.baralho.append(carta)

    def embaralhar(self):
        random.shuffle(self.baralho)

    def puxar_carta(self):
        return self.baralho.pop()


# CLASSE JOGADOR PARA PODER REALIZAR OS EVENTOS DO JOGADOR
class Player:
    def __init__(self, nome):
        self.nome = nome
        self.baralho_j = []

    def remover_uma(self):
        return self.baralho_j.pop(0)

    def add_cartas(self, novas_cartas):
        if type(novas_cartas) == type([]):
            self.baralho_j.extend(novas_cartas)
        else:
            self.baralho_j.append(novas_cartas)

    def __str__(self):
        return f'Jogador {self.nome} tem {len(self.baralho_j)} cartas'


# ------------SETUP DO JOGO--------------

# CRIAÇÃO DOS JOGADORES
jogador_1 = Player('JOGADOR 1')
jogador_2 = Player('JOGADOR 2')

# CRIAÇÃO DO BARALHO E SEU EMBARALHAMENTO
baralho = Deck()
baralho.embaralhar()

# DIVIDINDO METADE DO BARALHO PARA CADA JOGADOR
for c in range(26):
    jogador_1.add_cartas(baralho.puxar_carta())
    jogador_2.add_cartas(baralho.puxar_carta())

# ------------EXECUÇÃO DO JOGO----------------
rodada = 0
game_on = True
# LOOP PARA O JOGO ACONTECER QUANTAS VEZES FOREM NECESSÁRIAS:
while game_on:
    rodada += 1
    print(f'{rodada}ª RODADA')

    # VERIFICANDO SE ALGUM DOS PLAYERS JÁ VENCEU
    if len(jogador_1.baralho_j) == 0:
        print(f'{jogador_1.nome} está sem cartas!\n'
              f'{jogador_2.nome} venceu!')
        break
    elif len(jogador_2.baralho_j) == 0:
        print(f'{jogador_2.nome} está sem cartas!\n'
              f'{jogador_1.nome} venceu')
        break

    # COMEÇANDO A RODADA
    cartas_j1 = list()
    cartas_j1.append(jogador_1.remover_uma())

    cartas_j2 = list()
    cartas_j2.append(jogador_2.remover_uma())

    # LOOP PARA CHECAR SE ESTÁ EM WAR OU SE ALGUM JOGADOR VENCEU A RODADA
    while True:
        if cartas_j1[-1].valor > cartas_j2[-1].valor:
            jogador_1.add_cartas(cartas_j1)
            jogador_1.add_cartas(cartas_j2)
            print(f'{jogador_1.nome.upper()} RECEBE CARTAS DO {jogador_2.nome.upper()}')
            break
        elif cartas_j2[-1].valor > cartas_j1[-1].valor:
            jogador_2.add_cartas(cartas_j2)
            jogador_2.add_cartas(cartas_j1)
            print(f'{jogador_2.nome.upper()} RECEBE CARTAS DO {jogador_1.nome.upper()}')
            break
        else:
            print('GUERRA!')

            if len(jogador_1.baralho_j) < 3:
                print(f'{jogador_1.nome} não pode declarar GUERRA')
                print(f'{jogador_2.nome.upper()} GANHOU!')
                game_on = False
                break
            elif len(jogador_2.baralho_j) < 3:
                print(f'{jogador_2.nome} não pode declarar GUERRA')
                print(f'{jogador_1.nome.upper()} GANHOU!')
                game_on = False
                break
            else:
                for n in range(3):
                    cartas_j1.append(jogador_1.remover_uma())
                    cartas_j2.append(jogador_2.remover_uma())
