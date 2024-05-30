import random


def create_deck():
    """
    Tworzy pełną talię kart (52 karty).

    Zwraca:
    -------
    List[Tuple[str, str]]: Lista kart w talii.
    """
    suits = ['pik', 'kier', 'trefl', 'karo']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [(rank, suit) for suit in suits for rank in ranks]


class Deck:
    """
    Klasa reprezentująca talię kart.

    Atrybuty:
    ----------
    cards : List[Tuple[str, str]]
        Lista kart w talii.
    discard_pile : List[Tuple[str, str]]
        (Lista) - stos kart odrzuconych (wyłożonych przez graczy).

    Metody:
    -------
    create_deck() -> List[Tuple[str, str]]:
        Tworzy pełną talię kart (52 karty).
    draw_card() -> Tuple[str, str]:
        Dobiera kartę z talii. Jeśli talia jest pusta, przetasowuje stos kart odrzuconych.
    deal_cards(number_of_players: int) -> List[List[Tuple[str, str]]]:
        Rozdaje karty graczom na początku rozgrywki.
    reshuffle_deck() -> None:
        Przetasowuje stos kart odrzuconych, gdy talia jest pusta.
    add_to_discard_pile(card: Tuple[str, str]) -> None:
        Dodaje kartę do stosu kart odrzuconych.
    top_discard_card() -> Tuple[str, str]:
        Zwraca kartę na wierzchu stosu kart odrzuconych.
    change_top_discard_suit(new_suit: str):
        Zmienia kolor karty na stosie kart odrzuconych.
    """

    def __init__(self):
        """
        Inicjalizuje talię kart, tworząc i tasując ją oraz inicjalizuje stos kart odrzuconych.
        """
        self.cards = create_deck()
        random.shuffle(self.cards)
        self.discard_pile = []

    def draw_card(self):
        """
        Dobiera kartę z talii. Jeśli talia jest pusta, przetasowuje stos kart odrzuconych.

        Zwraca:
        -------
        Tuple[str, str]: Dobierana karta.
        """
        if not self.cards:
            self.reshuffle_deck()
        return self.cards.pop()

    def deal_cards(self, number_of_players):
        """
        Rozdaje karty graczom.

        Parametry:
        ----------
        number_of_players : int
            Liczba graczy.

        Zwraca:
        -------
        List[List[Tuple[str, str]]]: Lista kart dla każdego gracza.
        """
        player_cards = [[] for _ in range(number_of_players)]
        for c in range(8):
            for player in player_cards:
                player.append(self.draw_card())
        return player_cards

    def reshuffle_deck(self):
        """
        Przetasowuje stos kart odrzuconych, gdy talia jest pusta.
        """
        top_card = self.discard_pile.pop()
        self.cards = self.discard_pile
        random.shuffle(self.cards)
        self.discard_pile = [top_card]

    def add_to_discard_pile(self, card):
        """
        Dodaje kartę do stosu kart.

        Parametry:
        ----------
        card : Tuple[str, str]
            Karta do dodania do stosu.
        """
        self.discard_pile.append(card)

    def top_discard_card(self):
        """
        Zwraca kartę na wierzchu stosu.

        Zwraca:
        -------
        Tuple[str, str]: Karta na wierzchu stosu.
        """
        return self.discard_pile[-1]

    def change_top_discard_suit(self, new_suit):
        """
        Zmienia kolor karty na wierzchu na stosie kart odrzuconych.

        Parametry:
        ----------
        new_suit : str
            Nowy kolor do ustawienia.
        """
        rank, _ = self.discard_pile[-1]
        self.discard_pile[-1] = (rank, new_suit)
