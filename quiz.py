def run_quiz():
    print("Welcome to the Geography Quiz!")
    print("Answer each question by entering A, B, or C\n")
    
    questions = [
        {
            "question": "What food is typically served with naan?",
            "options": ["A) Butter Chicken", "B) Fish and Chips", "C) Pizza"],
            "answer": "A"
        },
        {
            "question": "What sport requires you to dribble?",
            "options": ["A) Basketball", "B) Volleyball", "C) Netball"],
            "answer": "A"
        },
        {
            "question": "How do falcons typically fly?",
            "options": ["A) High", "B) Low to the ground", "C) Standing still"],
            "answer": "A"
        },
        {
            "question": "Which of these is a fruit?",
            "options": ["A) Mango", "B) Carrot", "C) Bread"],
            "answer": "A"
        },
        {
            "question": "What sport rewards a try with 5 points and conversion with 2?",
            "options": ["A) Soccer", "B) Rugby", "C) NRL (National Rugby League)"],
            "answer": "B"
        }
    ]
    
    score = 0
    
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        while True:
            user_answer = input("\nYour answer (A/B/C): ").upper()
            if user_answer in ["A", "B", "C"]:
                break
            print("Invalid input. Please enter A, B, or C.")
        
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")
    
    print(f"Quiz complete! Your score: {score}/{len(questions)}")
    if score == len(questions):
        print("Perfect! You're a geography expert!")
    elif score >= len(questions)/2:
        print("Good job! You know your geography!")
    else:
        print("Keep studying geography!")

# Run the quiz
run_quiz()