import random
import Deck
import Player


class CrazyEightsGame:

    def __init__(self, number_of_bots):
        self.deck = Deck()
        self.players = self.add_bots(number_of_bots)
        self.discard_pile = []
        self.current_player = 0

    def add_bots(self, number_of_bots):
        return [Player("Gracz")] + [Player(f"Bot {i + 1}") for i in range(number_of_bots)]

    def start_game(self):
        players_cards = self.deck.deal_cards(len(self.players))
        for i in range(len(self.players)):
            self.players[i].hand = players_cards[i]
        self.discard_pile.append(self.deck.draw_card())

    def player_turn(self, player, top_card):
        if player.has_playable_card(top_card):
            print(player.show_hand())
            while True:
                choice = input("Wybierz kartę, którą chcesz zagrać (w formacie: wartość, kolor. np. '4 Kier') lub "
                               "'dobierz', aby dobrać kartę")
                if choice.lower() == 'dobierz':
                    player.draw_card(self.deck)
                    break
                else:
                    try:
                        rank, suit = choice.split(' ')
                        card = (rank, suit)
                        if card in player.get_playable_cards(top_card):
                            self.discard_pile.append(player.play_card(card))
                            if rank == '8':
                                valid_suits = ['pik', 'kier', 'trefl', 'karo']
                                while True:
                                    new_suit = input("Wybierz nowy kolor (Pik, Kier, Trefl, Karo): ")
                                    if new_suit.lower() in valid_suits:
                                        self.discard_pile[-1] = (rank, new_suit)
                                        break
                                    else:
                                        print("Niepoprawny kolor. Proszę wybrać Pik, Kier, Trefl lub Karo.")
                        else:
                            print("Nie możesz zagrać tej karty.")
                    except:
                        print("Podałeś kartę w niepoprawnym formacie. Proszę podać kartę jeszcze raz.")
        else:
            print("Brak możliwych ruchów, dobierasz kartę.")
            player.draw_card(self.deck)

    def bot_turn(self, player, top_card):
        if(player.has_playable_card(top_card)):
            playable_cards = player.get_playable_cards(top_card)
            card = random.choice(playable_cards)
            print(f"{player.name} wykłada kartę: {card}")
            self.discard_pile.append(player.play_card(card))
            if card[0] == '8':
                new_suit = random.choice(['H', 'D', 'C', 'S'])
                self.discard_pile[-1] = (card[0], new_suit)
                print(f"{player.name} zmienia kolor na {new_suit}.")
        else:
            print(f"{player.name} dobiera karte.")
            player.draw_card(self.deck)

    def check_winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                print(f"{player.name} wygrywa!")
                return True
        return False
