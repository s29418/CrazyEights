import random
from Player import Player
from Deck import Deck


def add_players():
    while True:
        num_players = int(input("Podaj liczbę graczy (1 lub 2): "))
        if num_players not in [1, 2]:
            raise ValueError("Niepoprawna liczba graczy.")
        break

    players = []

    for i in range(num_players):
        player_name = input(f"Podaj nazwę dla Gracza {i + 1}: ")
        players.append(Player(player_name))

    if num_players == 1:
        max_bots = 3
        min_bots = 1
    else:
        max_bots = 2
        min_bots = 0

    while True:
        num_bots = int(input(f"Podaj liczbę botów ({min_bots} do {max_bots}): "))
        if num_bots not in range(min_bots, max_bots + 1):
            raise ValueError(f"Niepoprawna liczba botów.")
        break

    players += [Player(f"Bot {i + 1}") for i in range(num_bots)]
    return players


class CrazyEightsGame:

    def __init__(self):
        self.deck = Deck()
        self.players = add_players()
        self.current_player = 0
        self.start_game()

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
        print(f"\n{player.name}({player.get_number_of_cards()}), twoja kolej!")
        print(f"Karta na wierzchu: {top_card}")

        if not player.name.startswith("Bot"):
            self.player_turn(player, top_card)
        else:
            self.bot_turn(player, top_card)

    def player_turn(self, player, top_card):
        while True:
            print("\nTwoje karty: " + player.show_hand())
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
                                    self.deck.discard_pile[-1] = (rank, new_suit)
                                    break
                                else:
                                    print("Niepoprawny kolor. Proszę wybrać pik, kier, trefl lub karo.")
                        break
                    else:
                        print("Nie możesz zagrać tej karty.")
                except ValueError:
                    print("Podałeś kartę w niepoprawnym formacie. Proszę podać kartę jeszcze raz.")

    def bot_turn(self, player, top_card):
        if player.has_playable_card(top_card):
            playable_cards = player.get_playable_cards(top_card)
            card = random.choice(playable_cards)
            print(f"{player.name} wykłada kartę: {card}")
            self.deck.add_to_discard_pile(player.play_card(card))
            if card[0] == '8':
                new_suit = player.get_most_common_suit()
                self.deck.change_top_discard_suit(new_suit)
                print(f"{player.name} zmienia kolor na {new_suit}.")
        else:
            print(f"{player.name}({player.get_number_of_cards()}) dobiera karte.")
            player.draw_card(self.deck)

    def check_winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                print(f"{player.name} wygrywa!")
                return True
        return False
