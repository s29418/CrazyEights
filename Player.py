class Player:
    """
    Klasa reprezentująca gracza.

    Atrybuty:
    ----------
    name : str
        Nazwa gracza.
    hand : List[Tuple[str, str]]
        Karty w ręku gracza.

    Metody:
    -------
    play_card(card: Tuple[str, str]) -> Tuple[str, str]:
        Gra wybraną kartę z ręki.
    draw_card(deck: Deck):
        Dobiera kartę z talii.
    show_hand() -> str:
        Wyświetla karty w ręku gracza.
    has_playable_card(top_card: Tuple[str, str]) -> bool:
        Sprawdza, czy gracz ma kartę, którą może zagrać.
    get_playable_cards(top_card: Tuple[str, str]) -> List[Tuple[str, str]]:
        Zwraca listę kart, które gracz może zagrać.
    get_most_common_suit() -> str:
        Zwraca kolor, którego gracz ma najwięcej w ręce (bez ósemek).
    get_number_of_cards() -> int:
        Zwraca liczbę kart w ręce gracza.
    """

    def __init__(self, name):
        """
        Inicjalizuje gracza z podaną nazwą i pustą ręką.

        Parametry:
        ----------
        name : str
            Nazwa gracza.
        """
        self.name = name
        self.hand = []

    def play_card(self, card):
        """
        Gra wybraną kartą z ręki.

        Parametry:
        ----------
        card : Tuple[str, str]
            Karta do zagrania.

        Zwraca:
        -------
        Tuple[str, str]: Zagrana karta.
        """
        card = (card[0].lower(), card[1].lower())
        hand_lower = [(rank.lower(), suit.lower()) for rank, suit in self.hand]
        card_index = hand_lower.index(card)
        return self.hand.pop(card_index)

    def draw_card(self, deck):
        """
        Dobiera kartę z talii.

        Parametry:
        ----------
        deck : Deck
            Talia, z której dobierana jest karta.
        """
        self.hand.append(deck.draw_card())

    def show_hand(self):
        """
        Wyświetla karty w ręku gracza.

        Zwraca:
        -------
        str: string reprezentujący karty w ręku gracza.
        """
        in_hand = ""
        for rank, suit in self.hand:
            in_hand += f"{rank} {suit}, "
        return in_hand

    def has_playable_card(self, top_card):
        """
        Sprawdza, czy gracz ma kartę, którą może zagrać.

        Parametry:
        ----------
        top_card : Tuple[str, str]
            Karta na wierzchu stosu.

        Zwraca:
        -------
        bool: True, jeśli gracz ma kartę do zagrania, False jeśli nie ma żadnej takiej karty.
        """
        for rank, suit in self.hand:
            if rank == '8' or rank == top_card[0] or suit == top_card[1]:
                return True
        return False

    def get_playable_cards(self, top_card):
        """
        Zwraca listę kart, które gracz może zagrać.

        Parametry:
        ----------
        top_card : Tuple[str, str]
            Karta na wierzchu stosu.

        Zwraca:
        -------
        List[Tuple[str, str]]: Lista kart możliwych do zagrania.
        """
        playable_cards = []
        for rank, suit in self.hand:
            if rank == '8' or rank == top_card[0] or suit == top_card[1]:
                playable_cards.append((rank.lower(), suit.lower()))
        return playable_cards

    def get_most_common_suit(self):
        """
        Zwraca kolor, którego gracz ma najwięcej w ręce (bez ósemek).

        Zwraca:
        -------
        str: Kolor, którego gracz ma najwięcej.
        """
        suit_counts = {'pik': 0, 'kier': 0, 'trefl': 0, 'karo': 0}
        for rank, suit in self.hand:
            if rank != '8':
                suit_counts[suit] += 1
        return max(suit_counts, key=suit_counts.get)

    def get_number_of_cards(self):
        """
        Zwraca liczbę kart w ręce gracza.

        Zwraca:
        -------
        int: Liczba kart w ręce gracza.
        """
        return len(self.hand)
