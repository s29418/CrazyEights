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
                                new_suit = input("Wybierz nowy kolor (Pik, Kier, Trefl, Karo): ")
                                self.discard_pile[-1] = (rank, new_suit)
                            break
                        else:
                            print("Nie możesz zagrać tej karty.")
                    except:
                        print("Podałeś kartę w niepoprawnym formacie. Proszę podać kartę jeszcze raz.")
        else:
            print("Brak możliwych ruchów, dobierasz kartę.")
            player.draw_card(self.deck)


    def check_winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                print(f"{player.name} wygrywa!")
                return True
        return False
