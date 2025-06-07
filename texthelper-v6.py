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
    print("\n🌐 HTML Quiz (50 questions)")
    questions = [
        {
            "question": "1. What does HTML stand for?",
            "options": ["Hyper Text Markup Language", "High Tech Modern Language",
                        "Hyperlinks and Text Markup Language"],
            "answer": 1
        },
        {
            "question": "2. Which tag is used for a paragraph?",
            "options": ["<p>", "<para>", "<paragraph>"],
            "answer": 1
        },
        {
            "question": "3. What is the correct HTML for creating a hyperlink?",
            "options": ["<a href='https://example.com'>link</a>", "<link>https://example.com</link>",
                        "<a>https://example.com</a>"],
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
        },
        {
            "question": "6. Which tag defines an unordered list?",
            "options": ["<ol>", "<ul>", "<list>"],
            "answer": 2
        },
        {
            "question": "7. Which attribute specifies a unique id for an element?",
            "options": ["class", "id", "name"],
            "answer": 2
        },
        {
            "question": "8. What is the correct HTML for making a checkbox?",
            "options": ["<input type='check'>", "<checkbox>", "<input type='checkbox'>"],
            "answer": 3
        },
        {
            "question": "9. Which tag defines a table row?",
            "options": ["<td>", "<tr>", "<table-row>"],
            "answer": 2
        },
        {
            "question": "10. Which tag defines a table header cell?",
            "options": ["<td>", "<th>", "<header>"],
            "answer": 2
        },
        {
            "question": "11. What is the correct HTML for adding a background color?",
            "options": ["<body bg='yellow'>", "<body style='background-color:yellow;'>",
                        "<background>yellow</background>"],
            "answer": 2
        },
        {
            "question": "12. Which character is used to indicate an end tag?",
            "options": ["*", "^", "/"],
            "answer": 3
        },
        {
            "question": "13. Which tag defines the root of an HTML document?",
            "options": ["<root>", "<html>", "<head>"],
            "answer": 2
        },
        {
            "question": "14. Which element defines navigation links?",
            "options": ["<nav>", "<navigate>", "<navigation>"],
            "answer": 1
        },
        {
            "question": "15. What is the correct HTML for creating a dropdown list?",
            "options": ["<input type='dropdown'>", "<list>", "<select>"],
            "answer": 3
        },
        {
            "question": "16. Which tag defines a footer for a document?",
            "options": ["<bottom>", "<footer>", "<foot>"],
            "answer": 2
        },
        {
            "question": "17. Which tag defines an image?",
            "options": ["<img>", "<image>", "<pic>"],
            "answer": 1
        },
        {
            "question": "18. Which attribute specifies the image source?",
            "options": ["src", "source", "href"],
            "answer": 1
        },
        {
            "question": "19. What is the correct HTML for making a text area?",
            "options": ["<input type='textarea'>", "<text>", "<textarea>"],
            "answer": 3
        },
        {
            "question": "20. Which tag defines a section in a document?",
            "options": ["<div>", "<section>", "Both <div> and <section>"],
            "answer": 3
        },
        {
            "question": "21. Which tag defines bold text?",
            "options": ["<b>", "<bold>", "<strong>"],
            "answer": 1
        },
        {
            "question": "22. Which tag defines italic text?",
            "options": ["<i>", "<italic>", "<em>"],
            "answer": 1
        },
        {
            "question": "23. What is the correct HTML for creating a button?",
            "options": ["<button>", "<btn>", "<input type='button'>"],
            "answer": 1
        },
        {
            "question": "24. Which tag defines the document's body?",
            "options": ["<main>", "<body>", "<content>"],
            "answer": 2
        },
        {
            "question": "25. Which tag defines a header for a document?",
            "options": ["<header>", "<head>", "<top>"],
            "answer": 1
        },
        {
            "question": "26. Which tag defines metadata about an HTML document?",
            "options": ["<meta>", "<metadata>", "<info>"],
            "answer": 1
        },
        {
            "question": "27. What is the purpose of the <head> element?",
            "options": ["To contain the visible content", "To contain metadata and links", "To define the main header"],
            "answer": 2
        },
        {
            "question": "28. Which tag defines a description list?",
            "options": ["<dl>", "<desc>", "<dlist>"],
            "answer": 1
        },
        {
            "question": "29. Which tag defines a term in a description list?",
            "options": ["<term>", "<dt>", "<dd>"],
            "answer": 2
        },
        {
            "question": "30. Which tag defines a description in a description list?",
            "options": ["<desc>", "<dd>", "<dl>"],
            "answer": 2
        },
        {
            "question": "31. What is the correct HTML for inserting an image with alt text?",
            "options": ["<img src='image.jpg' alt='My Image'>", "<image src='image.jpg' text='My Image'>",
                        "<img href='image.jpg' alt='My Image'>"],
            "answer": 1
        },
        {
            "question": "32. Which tag defines a clickable button?",
            "options": ["<btn>", "<button>", "<click>"],
            "answer": 2
        },
        {
            "question": "33. Which tag defines a form?",
            "options": ["<form>", "<input-form>", "<web-form>"],
            "answer": 1
        },
        {
            "question": "34. Which input type defines a slider control?",
            "options": ["<input type='slider'>", "<input type='range'>", "<input type='control'>"],
            "answer": 2
        },
        {
            "question": "35. Which tag defines a container for SVG graphics?",
            "options": ["<svg>", "<graphic>", "<canvas>"],
            "answer": 1
        },
        {
            "question": "36. Which tag defines a container for graphics?",
            "options": ["<svg>", "<canvas>", "<graphics>"],
            "answer": 2
        },
        {
            "question": "37. Which tag defines a progress bar?",
            "options": ["<progress>", "<bar>", "<status>"],
            "answer": 1
        },
        {
            "question": "38. Which tag defines a section?",
            "options": ["<div>", "<section>", "<area>"],
            "answer": 2
        },
        {
            "question": "39. Which tag defines an article?",
            "options": ["<post>", "<article>", "<story>"],
            "answer": 2
        },
        {
            "question": "40. Which tag defines content aside from the page content?",
            "options": ["<aside>", "<sidebar>", "<extra>"],
            "answer": 1
        },
        {
            "question": "41. Which tag defines details that the user can view or hide?",
            "options": ["<details>", "<toggle>", "<expand>"],
            "answer": 1
        },
        {
            "question": "42. Which tag defines a dialog box?",
            "options": ["<dialog>", "<popup>", "<modal>"],
            "answer": 1
        },
        {
            "question": "43. Which tag defines a summary/caption for <details>?",
            "options": ["<caption>", "<summary>", "<title>"],
            "answer": 2
        },
        {
            "question": "44. Which tag defines data?",
            "options": ["<info>", "<data>", "<value>"],
            "answer": 2
        },
        {
            "question": "45. Which tag defines ruby annotations?",
            "options": ["<ruby>", "<annotation>", "<rt>"],
            "answer": 1
        },
        {
            "question": "46. Which tag defines what to show in browsers that don't support ruby?",
            "options": ["<rp>", "<fallback>", "<no-ruby>"],
            "answer": 1
        },
        {
            "question": "47. Which tag defines text tracks for media?",
            "options": ["<track>", "<texttrack>", "<caption>"],
            "answer": 1
        },
        {
            "question": "48. Which tag defines a template?",
            "options": ["<template>", "<layout>", "<pattern>"],
            "answer": 1
        },
        {
            "question": "49. Which tag defines a circle?",
            "options": ["<circle>", "<svg-circle>", "<round>"],
            "answer": 1
        },
        {
            "question": "50. Which tag defines a rectangle?",
            "options": ["<rect>", "<square>", "<box>"],
            "answer": 1
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        print(f"\n{q['question']}")
        for j, option in enumerate(q['options']):
            print(f"   {j + 1}. {option}")

        try:
            answer = int(input("Your answer (number): "))
            if answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except:
            print("Invalid input! Please enter a number.")

    print(f"\nYour final score: {score}/50")
    if score == 50:
        print("🎉 Perfect score! HTML Master!")
    elif score >= 40:
        print("👍 Excellent! You know HTML very well!")
    elif score >= 30:
        print("💪 Good job! Solid HTML knowledge!")
    else:
        print("📚 Keep learning HTML!")

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
    print("=" * 50)
    print("🌟 Text Assistant v2.0")
    print("Created by life destroyed. https://github.com/lifedestroyed/txthelper/")
    print("=" * 50)

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
