from decouple import Config, RepositoryIni
from logic import play_game

config = Config(RepositoryIni('settings.ini'))

min_number = config('min_number', cast=int)
max_number = config('max_number', cast=int)
attempts = config('attempts', cast=int)
initial_capital = config('initial_capital', cast=int)

if __name__ == "__main__":
    play_game(min_number, max_number, attempts, initial_capital)
