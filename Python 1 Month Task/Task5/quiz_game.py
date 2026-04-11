import random

questions = [
    {
        "question": "What does HTML stand for?",
        "options": [
            "1. Hyper Text Markup Language",
            "2. High Text Makeup Language",
            "3. Hyper Text Markup Leveler",
            "4. Hyper Text Makeup Leveler"
        ],
        "answer": "1"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["1. Python", "2. Java", "3. JavaScript", "4. All"],
        "answer": "4"
    },
    {
        "question": "Which is used for data analysis?",
        "options": ["1. Pandas", "2. NumPy", "3. Matplotlib", "4. All"],
        "answer": "4"
    },
    {
        "question": "Which company developed Python?",
        "options": ["1. Google", "2. Microsoft", "3. Guido van Rossum", "4. Facebook"],
        "answer": "3"
    },
    {
        "question": "What is AI?",
        "options": ["1. Artificial Intelligence", "2. Automated Input", "3. Advanced Internet", "4. None"],
        "answer": "1"
    }
]

def run_quiz():
    score = 0

    random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print("\n" + "="*40)
        print(f"Question {i}: {q['question']}")
        print("="*40)

        for option in q["options"]:
            print(option)

        answer = input("\nEnter your answer (1-4): ")

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is option {q['answer']}")

        input("\nPress Enter to continue...") 

    print("\n" + "="*40)
    print("##--Quiz Completed!--##")
    print(f"Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")
    print("="*40)


if __name__ == "__main__":
    run_quiz()