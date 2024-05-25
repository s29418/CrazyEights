from CrazyEightsGame import CrazyEightsGame


def show_instructions():
    instructions = [
        "\n=== Crazy Eights (Szalone Ósemki) ==="
        "\nCrazy Eights to gra karciana, podobna do UNO, w której celem jest pozbycie się wszystkich swoich kart. "
        
        "\nGracz, który jako pierwszy pozbędzie się wszystkich swoich kart, wygrywa!",

        "\n=== Zasady gry: ==="
        "\n1. == Rozdanie kart: =="
        "\n   - Każdemu z graczy rozdaje się po 8 kart."
        "\n   - Jedna karta zostaje odłożona na stos jako karta początkowa.",

        "\n2. == Przebieg gry: =="
        "\n    - Gracz w swojej turze musi wyłożyć kartę, która zgadza się numerem lub kolorem z kartą na górze stosu. "
        "Jeśli nie ma odpowiedniej karty, musi dobrać jedną kartę z talii."
        "\n    - Wyłożona karta staje się nową kartą na górze stosu.",

        "\n3. == Karty specjalne: =="
        "\n    - Ósemki (8): Karta z numerem 8 dowolnego koloru jest kartą specjalną. Można ją położyć na dowolną inną "
        "kartę. Po zagraniu ósemki, gracz wybiera nowy kolor, który musi być zagrany przez następnych graczy.",

        "\n4. == Zakończenie gry: =="
        "\n   - Gra kończy się, gdy jeden z graczy pozbędzie się wszystkich swoich kart. Ten gracz wygrywa.",
    ]

    i = 0
    while i < len(instructions):
        print(instructions[i])
        user_input = input("\nNaciśnij 'd', aby przejść dalej, lub 'q' aby wyjść do menu: ")
        if user_input.lower() == 'q':
            return
        i += 1


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
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main_menu()
