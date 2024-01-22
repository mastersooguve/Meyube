def ask_question(question, options, answer):

    # Asks a multiple-choice question and checks the user's answer.

    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    while True:
        try:
            user_answer = int(input("Enter your answer (1-4): "))           # Getting user Input
            if 1 <= user_answer <= 4:
                break 
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")                  # error control

    if options[user_answer - 1] == answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is", answer)
        return False

def quiz_game():

    score = 0
    questions = [                                                           # Additional questions can be added here
        ("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], "Paris"),

        ("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Saturn"], "Jupiter"),

        ("What is the chemical symbol for gold?", ["Ag", "Au", "Fe", "Cu"], "Au"),

        ("Who is the greatest football player of all time?", ["Cristiano Ronaldo", "Lionel Messi", "Pele", "Maradona"], "Cristiano Ronaldo")
    ]

    for question, options, answer in questions:
        if ask_question(question, options, answer):                         #Calling the ask_question function defined above
            score += 1                                                      # Adds the score for each correct answer

    print("You scored", score, "out of", len(questions))                    # print the score

if __name__=="__main__":
    quiz_game()                                                             # calling the quiz fucntioin

