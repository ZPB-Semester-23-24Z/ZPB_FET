import curses
import pandas as pd
from MeasurementMenager import MeasurementMenager


def print_center(stdscr, text):
    # Wyśrodkuj tekst
    height, width = stdscr.getmaxyx()
    x = max(0, (width - len(text)) // 2)
    y = height // 2
    stdscr.addstr(y, x, text)

def print_up(stdscr, text):
    # Wyśrodkuj tekst w górnym lewym rogu
    stdscr.addstr(1, 1, text)

def draw_frame(stdscr):
    # Rysuj ramkę
    stdscr.border(0)

def main(stdscr):
    MeasurementMenagerList = []
    user_input = ""
    # Ustawienia terminala
    curses.curs_set(0)  # Ukryj kursor
    stdscr.clear()      # Wyczyść ekran
    stdscr.refresh()

    # Pobierz rozmiary terminala
    height, width = stdscr.getmaxyx()

    # Rysuj ramkę
    draw_frame(stdscr)
    help_text = "Komendy: [Help] [Clear] [Quit]"
    stdscr.addstr(height - 2, 1, help_text)

    # Wyśrodkuj tekst
    text_center = "Witaj w ZDP FET! Wpisz 'help' aby zobaczyć dostępne komendy."
    print_center(stdscr, text_center)

    # Pętla główna TUI
    while True:
        # Pobierz rozmiary terminala
        height, width = stdscr.getmaxyx()

        # Rysuj ramkę
        draw_frame(stdscr)
        help_text = "Komendy: [Help] [Clear] [Quit]"
        stdscr.addstr(height - 2, 1, help_text)

        # Pobierz komendę od użytkownika
        stdscr.addstr(height - 4, 1, f"Wpisywana Komenda: {user_input}")
        stdscr.refresh()
        user_input = stdscr.getstr(height - 1, len(help_text) + 2, 255).decode('utf-8')

        # Obsługa komend
        if user_input.lower() == 'help':
            help_message = "Dostępne komendy:\n [Help] - Wyświetl dostępne komendy\n [Clear] - Wyczyść ekran\n [LoadData] - Załaduj plik z parametrami Tranzystora\n [PrintChars] - Wyświetl wykresy\n [DisplayData] - Wyświelt parametry tranzystora\n [Quit] - Zakończ program"
            stdscr.clear()
            stdscr.refresh()
            draw_frame(stdscr)
            print_up(stdscr, help_message)  # Przywróć tekst w górnym lewym rogu
        elif user_input.lower() == 'clear':
            stdscr.clear()
            stdscr.refresh()
            draw_frame(stdscr)
        elif user_input.split(" ")[0].lower() == 'loaddata':
            stdscr.clear()
            stdscr.refresh()
            MeasurementMenagerList.append(MeasurementMenager(user_input.split(" ")[1]))
            readed_file = f'Wczytano plik: {user_input.split(" ")[1]}'
            print_center(stdscr, readed_file)
        elif user_input.lower() == 'displaydata':
            stdscr.clear()
            stdscr.refresh()
            draw_frame(stdscr)
            data = MeasurementMenagerList[0].Display(0)
            print_up(stdscr, str(data))  # Przywróć tekst w górnym lewym rogu 
        elif user_input.lower() == 'printchars':
            stdscr.clear()
            stdscr.refresh()
            draw_frame(stdscr)
            ret = MeasurementMenagerList[0].GenerateChars(0)
            if ret == 0:
                print_center(stdscr, "Wygenerowano wykresy w nowych oknach!")
            else:
                print_center(stdscr, "Błąd podaj poprawny numer pomiaru!")
        elif user_input.lower() == 'quit':
            break
        else:
            incorrect_command = "Niepoprawna komenda!"
            help_message = "Dostępne komendy:\n [Help] - Wyświetl dostępne komendy\n [Clear] - Wyczyść ekran\n [LoadData] - Załaduj plik z parametrami Tranzystora\n [PrintChars] - Wyświetl wykresy\n [DisplayData] - Wyświelt parametry tranzystora\n [Quit] - Zakończ program"
            stdscr.clear()
            stdscr.refresh()
            draw_frame(stdscr)
            print_up(stdscr, help_message) 
            print_center(stdscr, incorrect_command)

        # Odśwież ekran
        stdscr.refresh()

if __name__ == "__main__":
    # Uruchom TUI
    curses.wrapper(main)

