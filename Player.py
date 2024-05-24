class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, card):
        card = (card[0].lower(), card[1].lower())  # Normalizacja do małych liter
        print(f"Debug: Karta do zagrania: {card}")  # Debug
        hand_lower = [(rank.lower(), suit.lower()) for rank, suit in self.hand]  # Normalizacja rąk
        print(f"Debug: Ręka przed zagraniem: {hand_lower}")  # Debug
        card_index = hand_lower.index(card)
        return self.hand.pop(card_index)

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        in_hand = ""
        for rank, suit in self.hand:
            in_hand += f"{rank} {suit}, "
        return in_hand

    def has_playable_card(self, top_card):
        for rank, suit in self.hand:
            if rank == '8' or rank == top_card[0] or suit == top_card[1]:
                return True
        return False

    def get_playable_cards(self, top_card):
        playable_cards = []
        for rank, suit in self.hand:
            if rank == '8' or rank == top_card[0] or suit == top_card[1]:
                playable_cards.append((rank.lower(), suit.lower()))
        print(f"Debug: Dla karty na wierzchu {top_card} możliwe karty do zagrania to: {playable_cards}")
        return playable_cards
