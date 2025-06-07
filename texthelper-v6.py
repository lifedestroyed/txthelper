# Created by life destroyed. https://github.com/lifedestroyed/txthelper/

import random
import time

def calculator():
    print("\n📟 Calculator Mode")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator: ")
            num2 = float(input("Enter second number: "))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator! Please use +, -, *, /")
                continue
                
            print(f"Result: {result}")
            break
        except ValueError:
            print("Invalid input! Please enter numbers.")

def html_quiz():
    print("\n🌐 HTML Quiz (5/50 questions)")
    questions = [
        {
            "question": "1. What does HTML stand for?",
            "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Hyperlinks and Text Markup Language"],
            "answer": 1
        },
        {
            "question": "2. Which tag is used for a paragraph?",
            "options": ["<p>", "<para>", "<paragraph>"],
            "answer": 1
        },
        {
            "question": "3. What is the correct HTML for creating a hyperlink?",
            "options": ["<a href='https://example.com'>link</a>", "<link>https://example.com</link>", "<a>https://example.com</a>"],
            "answer": 1
        },
        {
            "question": "4. Which attribute specifies an alternate text for an image?",
            "options": ["src", "alt", "title"],
            "answer": 2
        },
        {
            "question": "5. What is the correct HTML for inserting a line break?",
            "options": ["<br>", "<break>", "<lb>"],
            "answer": 1
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        print(f"\n{q['question']}")
        for j, option in enumerate(q['options']):
            print(f"   {j+1}. {option}")
            
        try:
            answer = int(input("Your answer (number): "))
            if answer == q['answer'] + 1:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']+1}")
        except:
            print("Invalid input! Please enter a number.")
    
    print(f"\nYour score: {score}/{len(questions)}")
    time.sleep(1)

def three_doors_game():
    print("\n🚪 Three Doors Game")
    print("You stand before three mysterious doors...")
    time.sleep(1)
    print("One leads to treasure, one to a monster, and one is empty.")
    time.sleep(1)
    
    doors = {
        1: "💰 Treasure! You win 1000 gold coins!",
        2: "👾 Monster! You lose 500 health points!",
        3: "🚪 An empty room... nothing happens."
    }
    
    prize_door = random.randint(1, 3)
    
    while True:
        try:
            choice = int(input("Choose a door (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                break
            print("Please enter 1, 2, or 3!")
        except:
            print("Invalid input! Please enter a number.")
    
    time.sleep(1)
    print("\nOpening door...")
    time.sleep(2)
    print(doors[prize_door])
    time.sleep(1)

def lottery():
    print("\n🎱 Lottery Draw")
    participants = int(input("Enter number of participants: "))
    
    winner = random.randint(1, participants)
    
    print("\nAnd the grand winner is...")
    time.sleep(2)
    print("Participant number...")
    time.sleep(3)
    print(winner)
    print("🎉 Congratulations!")
    time.sleep(1)

def main():
    print("="*50)
    print("🌟 Text Assistant v2.0")
    print("Created by life destroyed. https://github.com/lifedestroyed/txthelper/")
    print("="*50)
    
    while True:
        print("\nMain Menu:")
        print("1. Calculator")
        print("2. HTML Quiz")
        print("3. Three Doors Game")
        print("4. Lottery")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            calculator()
        elif choice == '2':
            html_quiz()
        elif choice == '3':
            three_doors_game()
        elif choice == '4':
            lottery()
        elif choice == '5':
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()
