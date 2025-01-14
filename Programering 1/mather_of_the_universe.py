questions = [
    "What is x: x * 6 = 42 \nAnswer: ",
    "What is x: 4 * 9 = x \nAnswer: ",
    "What is x: x + 4 = 10 \nAnswer: ",
    "What is x: 2x = 18 \nAnswer: ",
    "What is x: x - 3 = 18\nAnswer: ",
    "What is x: 5x + 2 = 17 \nAnswer: ",
    "What is x: x/2 = 5 \nAnswer: ",
    "What is x: 3x - 9 = 0 \nAnswer: ",
    "What is x: 6x = 48 \nAnswer: ",
    "What is x: x - 4 = 10 \nAnswer: ", 
]

answers = [
    7,
    36,
    6, 
    9, 
    11, 
    3, 
    10, 
    3, 
    8, 
    14
]

points = 0

def no_points(points):
    print(f"You got 0 points. You have {points} points.\n")

def incorrect_answer(guess, correct_answer):
    print(f"You are incorrect. Your guess was {guess}, but the correct answer was {correct_answer}.")
    return

def answer_check(guess, correct_answer, points):
    if guess == correct_answer:
        print("You are correct!")
        points += 1
        print(f"You got 1 point. In total you have {points} points.\n")
    elif guess > correct_answer:
        print(f"You are incorrect. {guess} is too high")
        incorrect_answer(guess, correct_answer)
        no_points(points)
    elif guess < correct_answer:
        print(f"You are incorrect. {guess} is too low")
        incorrect_answer(guess, correct_answer)
        no_points(points)
    return points

for current_round in range(10):
    while True:
        try:
            guess = int(input(questions[current_round]))
            points = answer_check(guess, answers[current_round], points)
            break
        except ValueError:
            print("Please answer only in numbers.\n")

print(f"Game over you scored {points} points.")
