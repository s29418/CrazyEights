import random
from Player import Player
from Deck import Deck


def add_players():
    """
    Dodaje graczy do gry.

    Zwraca:
    -------
    list: Lista obiektów klasy Player reprezentujących graczy i botów.
    """
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
    """
    Klasa reprezentująca grę w Crazy Eights.

    Atrybuty:
    ----------
    deck : Deck
        Talia kart używana w grze.
    players : list
        Lista obiektów klasy Player reprezentujących graczy.
    current_player : int
        Indeks aktualnego gracza.

    Metody:
    -------
    start_game():
        Rozpoczyna grę poprzez rozdanie kart i ustawienie pierwszej karty na stosie kart odrzuconych.
    play_game():
        Przeprowadza główną pętlę gry, aż do wyłonienia zwycięzcy.
    play_turn(player: Player):
        Rozgrywa turę danego gracza.
    player_turn(player: Player, top_card: tuple):
        Rozgrywa turę gracza.
    bot_turn(player: Player, top_card: tuple):
        Rozgrywa turę bota.
    check_winner() -> bool:
        Sprawdza, czy któryś z graczy wygrał grę.
    """

    def __init__(self):
        """
        Inicjalizuje nową grę w Crazy Eights.
        """
        self.deck = Deck()
        self.players = add_players()
        self.current_player = 0
        self.start_game()

    def start_game(self):
        """
        Rozpoczyna grę poprzez rozdanie kart i ustawienie pierwszej karty na stosie kart odrzuconych.
        """
        players_cards = self.deck.deal_cards(len(self.players))
        for i in range(len(self.players)):
            self.players[i].hand = players_cards[i]
        self.deck.add_to_discard_pile(self.deck.draw_card())
        self.play_game()

    def play_game(self):
        """
        Przeprowadza główną pętlę gry, aż do wyłonienia zwycięzcy.
        """
        while not self.check_winner():
            self.play_turn(self.players[self.current_player])
            self.current_player = (self.current_player + 1) % len(self.players)

    def play_turn(self, player):
        """
        Rozgrywa turę danego gracza.

        Parametry:
        ----------
        player : Player
            Gracz, którego tura jest rozgrywana.
        """
        top_card = self.deck.top_discard_card()
        print(f"\n{player.name}({player.get_number_of_cards()}), twoja kolej!")
        print(f"Karta na wierzchu: {top_card}")

        if not player.name.startswith("Bot"):
            self.player_turn(player, top_card)
        else:
            self.bot_turn(player, top_card)

    def player_turn(self, player, top_card):
        """
        Rozgrywa turę gracza.

        Parametry:
        ----------
        player : Player
            Gracz, którego tura jest rozgrywana.
        top_card : tuple
            Karta na wierzchu stosu kart odrzuconych.
        """
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
        """
        Rozgrywa turę bota.

        Parametry:
        ----------
        player : Player
            Gracz, którego tura jest rozgrywana.
        top_card : tuple
            Karta na wierzchu stosu kart odrzuconych.
        """
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
        """
        Sprawdza, czy któryś z graczy wygrał grę.

        Zwraca:
        -------
        bool: True, jeśli któryś z graczy wygrał, False w przeciwnym razie.
        """
        for player in self.players:
            if len(player.hand) == 0:
                print(f"{player.name} wygrywa!")
                return True
        return False
