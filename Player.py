class Player:


    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, card):
        self.hand.pop(card)

