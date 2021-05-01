import random

class Card:

    def __init__(self,rank):
        self.rank = rank


    def card_value(self):
        if self.rank in ['десять', 'валет','дама','король']:
            return 10
        else:
            return 'A23456789'.index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return (self.rank)

class Hand:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_cards(self,card):
        self.cards.append(card)

    def get_value(self):
        result = 0
        aces = 0
        for card in self.cards:
            if card.get_rank() == 'A':
                aces += 1
            else:
                result += int(card.card_value())
        if result + aces *10 <= 21:
            result += aces*10
        return result

class Deck:

    def __init__(self):
        ranks = ['2','3','4','5','6','7','8','9','десять', 'валет','дама','король']
        self.cards = [Card(r) for r in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return  self.cards.pop()

def game():
    deck = Deck()

    player_hand = Hand('Игрок')
    dealer_hand = Hand('Диллер')

    player_hand.add_cards(deck.deal_card())
    player_hand.add_cards(deck.deal_card())
    dealer_hand.add_cards(deck.deal_card())
    print ('Очков у диллера',dealer_hand.get_value())
    print()
    print('Очков у Вас ',player_hand.get_value())

    flag = True

    while player_hand.get_value() < 21:
        answer = input('Еще? да/нет ')
        if answer == 'да':
            player_hand.add_cards(deck.deal_card())
            print ('Очков у Вас ', player_hand.get_value())
            if player_hand.get_value() > 21:
                print('У Вас перебор!')
                flag = False
        else:
            print ('Себе')
            break

    if flag:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_cards(deck.deal_card())
            print ('Очков у диллера', dealer_hand.get_value())

            if dealer_hand.get_value() > 21:
                print ('У диллера перебор')
                flag = False
    if flag:
        if player_hand.get_value() > dealer_hand.get_value():
            print ('Вы ваиграли')
        else:
            print ('Диллер выиграл')

game()