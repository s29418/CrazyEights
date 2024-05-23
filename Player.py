class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, card):
        self.hand.pop(card)

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        for rank, suit in self.hand:
            return ", ".join([f"{rank}{suit}"])

    def has_playable_card(self, top_card):
        for rank, suit in self.hand:
            if any(rank == '8' or rank == top_card[0] or suit == top_card[1]):
                return True
        return False
