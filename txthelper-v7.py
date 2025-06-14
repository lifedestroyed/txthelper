import random
import time
from datetime import datetime
import math

def clock():
    """Программа-часы с текущим временем и датой"""
    while True:
        now = datetime.now()
        print(f"\nТекущее время: {now.strftime('%H:%M:%S')}")
        print(f"Дата: {now.strftime('%d.%m.%Y')}")
        print("Нажмите Ctrl+C для возврата в меню")
        time.sleep(1)

def greeting():
    """Приветствие пользователя в зависимости от времени суток"""
    hour = datetime.now().hour
    
    name = input("Как вас зовут? ")
    
    if 5 <= hour < 12:
        print(f"Доброе утро, {name}!")
    elif 12 <= hour < 18:
        print(f"Добрый день, {name}!")
    elif 18 <= hour < 23:
        print(f"Добрый вечер, {name}!")
    else:
        print(f"Доброй ночи, {name}! Почему вы не спите?")

def jokes():
    """Случайные анекдоты"""
    jokes_list = [
        "Почему программисты так плохо паркуются? Потому что они всегда ищут идеальное место!",
        "Заходит как-то нейросеть в бар... а там все места заняты нулями и единицами.",
        "Почему математики не любят леса? Потому что там слишком много корней!",
        "Что сказал один байт другому байту? Будем битами!",
        "Почему Python не смог устроиться на работу? Потому что у него не было опыта работы с змеями!",
        "Какой язык программирования самый романтичный? Python, потому что он всегда говорит 'I love you' с отступом!"
    ]
    
    print("\n" + random.choice(jokes_list))

def calculator():
    """Простой калькулятор"""
    print("\nКалькулятор (поддерживает +, -, *, /, ^, sqrt)")
    
    try:
        num1 = float(input("Введите первое число: "))
        operation = input("Выберите операцию (+, -, *, /, ^, sqrt): ")
        
        if operation != 'sqrt':
            num2 = float(input("Введите второе число: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                return
            result = num1 / num2
        elif operation == '^':
            result = num1 ** num2
        elif operation == 'sqrt':
            if num1 < 0:
                print("Ошибка: нельзя извлечь корень из отрицательного числа!")
                return
            result = math.sqrt(num1)
        else:
            print("Неизвестная операция!")
            return
            
        print(f"Результат: {result}")
        
    except ValueError:
        print("Ошибка: введите корректные числа!")

def rock_paper_scissors():
    """Игра Камень-ножницы-бумага"""
    player_score = 0
    comp_score = 0
    rounds_to_win = 3
    
    choices = {'к': 'Камень', 'н': 'Ножницы', 'б': 'Бумага'}
    
    print("\n=== Камень-ножницы-бумага ===")
    print("Первым до 3 побед!")
    
    while player_score < rounds_to_win and comp_score < rounds_to_win:
        print(f"\nСчет: Вы {player_score} - {comp_score} Компьютер")
        
        player_choice = input("Выберите: (к)амень, (н)ожницы, (б)умага или (в)ыход: ").lower()
        
        if player_choice == 'в':
            print("Игра завершена!")
            break
        
        if player_choice not in ['к', 'н', 'б']:
            print("Некорректный ввод! Попробуйте снова.")
            continue
        
        comp_choice = random.choice(['к', 'н', 'б'])
        
        print(f"\nВаш выбор: {choices[player_choice]}")
        print(f"Выбор компьютера: {choices[comp_choice]}")
        
        # Определение победителя
        if player_choice == comp_choice:
            print("Ничья!")
        elif (player_choice == 'к' and comp_choice == 'н') or \
             (player_choice == 'н' and comp_choice == 'б') or \
             (player_choice == 'б' and comp_choice == 'к'):
            print("Вы выиграли раунд!")
            player_score += 1
        else:
            print("Компьютер выиграл раунд!")
            comp_score += 1
    
    # Финальный результат
    print("\n=== ИГРА ОКОНЧЕНА ===")
    print(f"Финальный счет: Вы {player_score} - {comp_score} Компьютер")
    
    if player_score > comp_score:
        print("Поздравляем! Вы выиграли матч!")
    elif comp_score > player_score:
        print("Компьютер выиграл матч!")
    else:
        print("Матч завершился вничью!")

def quiz():
    """Викторина с вопросами"""
    questions = [
        {
            "question": "Какая планета известна как Красная планета?",
            "options": ["Венера", "Марс", "Юпитер", "Сатурн"],
            "answer": 1
        },
        {
            "question": "Сколько элементов в периодической таблице?",
            "options": ["118", "102", "94", "126"],
            "answer": 0
        },
        {
            "question": "Какая самая длинная река в мире?",
            "options": ["Амазонка", "Нил", "Янцзы", "Миссисипи"],
            "answer": 0
        },
        {
            "question": "Кто написал 'Войну и мир'?",
            "options": ["Достоевский", "Толстой", "Пушкин", "Чехов"],
            "answer": 1
        },
        {
            "question": "Как называется самая большая кость в человеческом теле?",
            "options": ["Лучевая", "Бедренная", "Большеберцовая", "Плечевая"],
            "answer": 1
        }
    ]
    
    score = 0
    
    print("\n=== ВИКТОРИНА ===")
    print("Ответьте на 5 вопросов!")
    
    for i, q in enumerate(questions, 1):
        print(f"\nВопрос {i}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{j+1}. {option}")
        
        try:
            user_answer = int(input("Ваш ответ (1-4): ")) - 1
            if user_answer == q['answer']:
                print("Правильно!")
                score += 1
            else:
                print(f"Неправильно! Правильный ответ: {q['options'][q['answer']]}")
        except:
            print("Некорректный ввод!")
    
    print(f"\nВаш результат: {score}/{len(questions)}")
    if score == len(questions):
        print("Отлично! Вы знаток!")
    elif score >= len(questions) // 2:
        print("Хороший результат!")
    else:
        print("Попробуйте еще раз!")

def guess_number():
    """Игра Угадай число"""
    print("\n=== УГАДАЙ ЧИСЛО ===")
    print("Компьютер загадал число от 1 до 100. Угадайте за 7 попыток!")
    
    secret = random.randint(1, 100)
    attempts = 7
    
    while attempts > 0:
        try:
            guess = int(input(f"\nПопыток осталось: {attempts}. Ваша догадка: "))
            
            if guess == secret:
                print(f"Поздравляем! Вы угадали число {secret}!")
                return
            elif guess < secret:
                print("Загаданное число больше!")
            else:
                print("Загаданное число меньше!")
            
            attempts -= 1
        except ValueError:
            print("Пожалуйста, введите число!")
    
    print(f"\nК сожалению, вы проиграли. Загаданное число было: {secret}")

def lottery():
    """Лотерея с случайными числами"""
    print("\n=== ЛОТЕРЕЯ ===")
    print("Попробуйте удачу! Выигрышные номера генерируются случайно.")
    
    # Генерация выигрышных номеров
    winning_numbers = sorted(random.sample(range(1, 51), 5))
    winning_powerball = random.randint(1, 10)
    
    # Выбор игрока
    player_numbers = []
    for i in range(1, 6):
        while True:
            try:
                num = int(input(f"Выберите число {i} (1-50): "))
                if 1 <= num <= 50 and num not in player_numbers:
                    player_numbers.append(num)
                    break
                else:
                    print("Некорректное число или повтор!")
            except:
                print("Введите число!")
    
    player_powerball = int(input("Выберите PowerBall (1-10): "))
    player_numbers.sort()
    
    # Определение выигрыша
    matches = len(set(player_numbers) & set(winning_numbers))
    powerball_match = player_powerball == winning_powerball
    
    print("\n=== РЕЗУЛЬТАТЫ ===")
    print(f"Ваши числа: {player_numbers} + PowerBall: {player_powerball}")
    print(f"Выигрышные числа: {winning_numbers} + PowerBall: {winning_powerball}")
    
    if matches == 5 and powerball_match:
        print("Джекпот! Вы выиграли 1 000 000$!")
    elif matches == 5:
        print("Суперприз! Вы выиграли 500 000$!")
    elif matches == 4 and powerball_match:
        print("Большой выигрыш! 10 000$!")
    elif matches == 4 or (matches == 3 and powerball_match):
        print("Вы выиграли 100$!")
    elif matches == 3 or (matches == 2 and powerball_match):
        print("Маленький выигрыш! 10$!")
    else:
        print("К сожалению, вы не выиграли. Попробуйте еще раз!")

def main_menu():
    """Главное меню программы"""
    while True:
        print("\n" + "=" * 40)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 40)
        print("1. Часы")
        print("2. Приветствие")
        print("3. Анекдоты")
        print("4. Калькулятор")
        print("5. Камень-ножницы-бумага")
        print("6. Викторина")
        print("7. Угадай число")
        print("8. Лотерея")
        print("9. Выход")
        print("=" * 40)
        
        choice = input("Выберите программу (1-9): ")
        
        if choice == '1':
            try:
                clock()
            except KeyboardInterrupt:
                print("\nВозвращаемся в меню...")
        elif choice == '2':
            greeting()
        elif choice == '3':
            jokes()
        elif choice == '4':
            calculator()
        elif choice == '5':
            rock_paper_scissors()
        elif choice == '6':
            quiz()
        elif choice == '7':
            guess_number()
        elif choice == '8':
            lottery()
        elif choice == '9':
            print("\nСпасибо за использование программы! До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main_menu()
