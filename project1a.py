questions = {
    "What is your preferred fighting style?": {
        "A": "Hand-to-hand combat",
        "B": "Long-range attacks",
        "C": "Agility and speed",
        "D": "Strength and durability"
    },
    "What motivates you to fight?": {
        "A": "Justice and protecting the innocent",
        "B": "Revenge and personal vendettas",
        "C": "Duty and responsibility",
        "D": "Power and conquest"
    },
    "Which of these values is most important to you?": {
        "A": "Honesty",
        "B": "Intelligence",
        "C": "Loyalty",
        "D": "Courage"
    }
}
avengers = {
    "Captain America": {
        "A": 3,
        "B": 3,
        "C": 3,
        "D": 1
    },
    "Iron Man": {
        "A": 1,
        "B": 3,
        "C": 1,
        "D": 3
    },
    "Black Widow": {
        "A": 3,
        "B": 1,
        "C": 3,
        "D": 2
    },
    "Hulk": {
        "A": 2,
        "B": 1,
        "C": 2,
        "D": 3
    },
    "Thor": {
        "A": 2,
        "B": 3,
        "C": 2,
        "D": 2
    }
}
def ask_question(question):
    print(question)
    for answer in questions[question]:
        print(answer + ": " + questions[question][answer])
    user_answer = input("Enter your answer (A/B/C/D): ")
    return user_answer
def calculate_score(answers):
    scores = {
        "Captain America": 0,
        "Iron Man": 0,
        "Black Widow": 0,
        "Hulk": 0,
        "Thor": 0
    }
    for answer in answers:
        for avenger in avengers:
            scores[avenger]+= avengers[avenger][answer]
    return scores
def find_result(scores):
    result = ""
    max_score = 0
    for avenger in scores:
        if scores[avenger] > max_score:
            result = avenger
            max_score = scores[avenger]
    return result
def run_quiz():
    answers = []
    for question in questions:
        answer = ask_question(question)
        answers.append(answer)
    scores = calculate_score(answers)
    result = find_result(scores)
    print("You are most like " + result + "!")
run_quiz()