import random
from Player import Player
from Deck import Deck


class CrazyEightsGame:

    def __init__(self, number_of_bots, player_name):
        self.deck = Deck()
        self.players = self.add_bots(number_of_bots, player_name)
        self.current_player = 0
        self.start_game()

    def add_bots(self, number_of_bots, player_name):
        return [Player(player_name)] + [Player(f"Bot {i + 1}") for i in range(number_of_bots)]

    def start_game(self):
        players_cards = self.deck.deal_cards(len(self.players))
        for i in range(len(self.players)):
            self.players[i].hand = players_cards[i]
        self.deck.add_to_discard_pile(self.deck.draw_card())
        self.play_game()

    def play_game(self):
        while not self.check_winner():
            self.play_turn(self.players[self.current_player])
            self.current_player = (self.current_player + 1) % len(self.players)

    def play_turn(self, player):
        top_card = self.deck.top_discard_card()
        print(f"\n{player.name}, twoja kolej!")
        print(f"Karta na wierzchu: {top_card}")

        if not player.name.startswith("Bot"):
            self.player_turn(player, top_card)
        else:
            self.bot_turn(player, top_card)

    def player_turn(self, player, top_card):
        if player.has_playable_card(top_card):
            print("\nTwoje karty: " + player.show_hand())
            while True:
                choice = input("Wybierz kartę, którą chcesz zagrać (w formacie: wartość kolor np. '4 kier') \n"
                               "LUB 'dobierz', aby dobrać kartę: ").strip().lower()
                if choice == 'dobierz':
                    player.draw_card(self.deck)
                    break
                else:
                    try:
                        rank, suit = choice.split()
                        card = (rank, suit)
                        playable_cards = player.get_playable_cards(top_card)
                        playable_cards = [(r.lower(), s.lower()) for r, s in playable_cards]
                        if card in playable_cards:
                            self.deck.add_to_discard_pile(player.play_card(card))
                            if rank == '8':
                                valid_suits = ['pik', 'kier', 'trefl', 'karo']
                                while True:
                                    new_suit = input("Wybierz nowy kolor (pik, kier, trefl, karo): ").strip().lower()
                                    if new_suit in valid_suits:
                                        self.deck.change_top_discard_suit(new_suit)
                                        break
                                    else:
                                        print("Niepoprawny kolor. Proszę wybrać pik, kier, trefl lub karo.")
                            break
                        else:
                            print("Nie możesz zagrać tej karty.")
                    except ValueError:
                        print("Podałeś kartę w niepoprawnym formacie. Proszę podać kartę jeszcze raz.")
        else:
            print("Brak możliwych ruchów, dobierasz kartę.")
            player.draw_card(self.deck)

    def bot_turn(self, player, top_card):
        if player.has_playable_card(top_card):
            playable_cards = player.get_playable_cards(top_card)
            card = random.choice(playable_cards)
            print(f"{player.name} wykłada kartę: {card}")
            self.deck.add_to_discard_pile(player.play_card(card))
            if card[0] == '8':
                new_suit = random.choice(['pik', 'kier', 'trefl', 'karo'])
                self.deck.change_top_discard_suit(new_suit)
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
