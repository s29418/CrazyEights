from CrazyEightsGame import CrazyEightsGame


def show_instructions():
    instructions = (
        "\n=== Crazy Eights (Szalone Ósemki) ===\n"
        "Crazy Eights to gra karciana, podobna do UNO, w której celem jest pozbycie się wszystkich swoich kart. "
        "Gracz, który jako pierwszy pozbędzie się wszystkich swoich kart, wygrywa!\n"

        "\n=== Zasady gry: ===\n"
        "1. == Rozdanie kart: ==\n"
        "   - Każdemu z graczy rozdaje się po 8 kart.\n"
        "   - Jedna karta zostaje odłożona na stos jako karta początkowa.\n"

        "2. == Przebieg gry: ==\n"
        "   - Gracz w swojej turze musi wyłożyć kartę, która zgadza się numerem lub kolorem z kartą na górze stosu.\n"
        "     Jeśli nie ma odpowiedniej karty, musi dobrać jedną kartę z talii.\n"
        "   - Wyłożona karta staje się nową kartą na górze stosu.\n"

        "3. == Karty specjalne: ==\n"
        "   - Ósemki (8): Karta z numerem 8 dowolnego koloru jest kartą specjalną. Można ją położyć na dowolną inną\n"
        "     kartę. Po zagraniu ósemki, gracz wybiera nowy kolor, który musi być zagrany przez następnych graczy.\n"

        "4. == Zakończenie gry: ==\n"
        "   - Gra kończy się, gdy jeden z graczy pozbędzie się wszystkich swoich kart. Ten gracz wygrywa.\n"

        "\n== Ustawienia gry: ==\n"
        "   - Gra pozwala na wybór ilości przeciwników: od jednego do trzech botów. Miłej zabawy!\n"
    )

    print(instructions)
    user_input = input("\nNaciśnij 'q' i zatwierdź, aby wrócić do menu: ")
    while user_input.lower() != 'q':
        user_input = input("\nNiepoprawny klawisz. Naciśnij 'q', aby wrócić do menu: ")


def main_menu():
    while True:
        print("\n=== Crazy Eights ===")
        print("1. Nowa gra")
        print("2. Instrukcja")
        print("3. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            CrazyEightsGame()
        elif choice == '2':
            show_instructions()
        elif choice == '3':
            print("Dziękujemy za grę! Do zobaczenia!")
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main_menu()
