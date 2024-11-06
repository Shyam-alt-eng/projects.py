import random
import operator

print("Hey there....")
user = input("Select mode (easy, medium, hard): ").strip().lower()
count = 0

# Function to generate expressions
def generator():
    random_number1 = random.randrange(1, 100)
    random_number2 = random.randrange(1, 100)
    
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    
    operator1 = random.choice(list(operations.keys()))
    operator2 = random.choice(list(operations.keys()))  # Changed to random.choice

    expression_easy = f"{random_number1} {operator1} {random_number2}"
    expression2 = f"({expression_easy}) {operator2} {random_number2}"
    expression3 = f"{random_number1} {operator1} {expression2}"
    expression_hard = f"{expression3} {operator2} {expression2}"
    
    expression_medium = [expression2, expression3]
    random_medium = random.choice(expression_medium)  # Choose a random medium expression
    
    return expression_easy, random_medium, expression_hard

def hard():
    global count
    while True:
        _, _, expression_hard = generator()
        result = eval(expression_hard.replace('/', '//'))  # Integer division
        guess = int(input(f"Guess the answer {expression_hard}: "))
        if result == guess:
            count += 1
            if count == 20:
                print("Congratulations! You have completed all the levels.")
                break
            else:
                print("Perfect guess!")
        else:
            print(f"Oops! Wrong answer. The correct answer is {result}.")

def medium():
    global count
    while True:
        _, random_medium, _ = generator()
        result = eval(random_medium.replace('/', '//'))  # Integer division
        guess = int(input(f"Guess the answer {random_medium}: "))
        if result == guess:
            count += 1
            if count == 15:
                print("You deserve a level up! Level upgraded to hard.")
                hard()
                return  # Exit medium level loop
            else:
                print("Perfect guess!")
        else:
            print(f"Oops! Wrong answer. The correct answer is {result}.")

def easy():
    global count
    while True:
        expression_easy, _, _ = generator()
        result = eval(expression_easy.replace('/', '//'))  # Integer division
        guess = int(input(f"Guess the answer {expression_easy}: "))
        if result == guess:
            count += 1
            if count == 10:
                print("You deserve a level up! Level upgraded to medium.")
                medium()
                return  # Exit easy level loop
            else:
                print("Perfect guess!")
        else:
            print(f"Oops! Wrong answer. The correct answer is {result}.")

# Start the game based on user-selected mode
while True:
    try:
        if user == "easy":
            easy()
        elif user == "medium":
            medium()
        elif user == 'hard':
            hard()
        else:
            print("please enter a valid mode")
            break

    except Exception as e:
        print("Enter a valid input") 
