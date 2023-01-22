from Ultrafinale2 import Question


question_prompts = [
    "Who am I?\n(A) Probably human\n(B) Mason\n(C) Water",
    "What is my favorite fruit!\n(A) Apple\n(B) Blueberry\n(C) Watermelon",
    "Lastly what color is my buggati?\n(A) YOU GOT NONE\n(B) Rainbow\n(C) Blue",
]

question = [
    Question(question_prompts[0], "B"),
    Question(question_prompts[1], "C"),
    Question(question_prompts[2], "A"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + "correct")


run_test(question)