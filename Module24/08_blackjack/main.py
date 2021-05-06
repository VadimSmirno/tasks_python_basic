import random


class Card:

    def __init__(self, rank):
        self.rank = rank

    def card_value(self):
        if self.rank in ['десять', 'валет', 'дама', 'король']:
            return (10, self.rank)
        else:
            return ('A23456789'.index(self.rank) + 1, self.rank)


    # , метод get_rank дублирует метод __str__.
    #  Предлагаю или сделать их разными, или убрать один из них =)
    def get_rank(self):
        return self.rank

    def __str__(self):
        return (self.rank)  # () получились лишние


class Hand:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_cards(self, card):
        self.cards.append(card)

    def get_value(self):
        result = 0
        aces = 0
        for card in self.cards:
            if card.get_rank() == 'A':
                aces += 1
            else:
                result += int(card.card_value()[0])
        if result + aces * 10 <= 21:
            result += aces * 10
        return result


class Deck:

    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'десять', 'валет', 'дама', 'король']
        self.cards = [Card(r) for r in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


def card_hand(lst, name):
    print('\nКакты на руках', name, end=' ')
    for i_cards in lst:
        print(i_cards, end=' ')


def game():
    deck = Deck()

    player_hand = Hand('Игрок')
    dealer_hand = Hand('Диллер')

    player_hand.add_cards(deck.deal_card())
    player_hand.add_cards(deck.deal_card())
    dealer_hand.add_cards(deck.deal_card())
    print('Выпала карта:', dealer_hand.cards[0], ',очков у диллера', dealer_hand.get_value())
    print()
    print('Выпали карты', player_hand.cards[0], 'и', player_hand.cards[1], 'Очков у Вас ', player_hand.get_value())

    flag = True

    while player_hand.get_value() < 21:
        answer = input('Еще? да/нет ')
        if answer == 'да':
            count_pleyr = 2
            player_hand.add_cards(deck.deal_card())
            print('Выпала карта', player_hand.cards[count_pleyr], 'очков у Вас ', player_hand.get_value())
            count_pleyr += 1
            if player_hand.get_value() > 21:
                print('У Вас перебор! диллер выиграл!')
                flag = False
        else:
            print('Себе')
            break

    if flag:
        while dealer_hand.get_value() < 17:
            count_dealer = 1
            dealer_hand.add_cards(deck.deal_card())
            print('Выпала карта', dealer_hand.cards[count_dealer], 'Очков у диллера', dealer_hand.get_value())
            count_dealer += 1
            if dealer_hand.get_value() > 21:
                print('У диллера перебор, Вы выиграли!')
                flag = False
    if flag:
        if player_hand.get_value() > dealer_hand.get_value():
            print('Вы выиграли')
        else:
            print('Диллер выиграл')

    card_hand(dealer_hand.cards, 'Диллера')
    card_hand(player_hand.cards, 'Игрока')


game()

# зачёт!
