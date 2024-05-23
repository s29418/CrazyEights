class Player:


    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, card):
        self.hand.pop(card)

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        return ", ".join([f"{rank}{suit}" for rank, suit in self.hand])