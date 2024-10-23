import random

def play_game(min_number, max_number, attempts, initial_capital):
    capital = initial_capital
    print(f"Ваш стартовый капитал: {capital}")

    for attempt in range(attempts):
        if capital <= 0:
            print("У вас больше нет денег!")
            break

        guess = int(input(f"Попытка {attempt + 1}: Угадайте число от {min_number} до {max_number}: "))
        bet = int(input(f"Введите вашу ставку (доступно: {capital}): "))

        if bet > capital:
            print("Ставка превышает ваш капитал!")
            continue

        number_to_guess = random.randint(min_number, max_number)

        if guess == number_to_guess:
            capital += bet
            print(f"Поздравляем! Вы угадали число {number_to_guess}. Ваш новый капитал: {capital}")
        else:
            capital -= bet
            print(f"Вы не угадали. Загаданное число: {number_to_guess}. Ваш капитал: {capital}")

    if capital > 0:
        print(f"Игра окончена! У вас осталось {capital}.")
    else:
        print("Вы разорены!")
