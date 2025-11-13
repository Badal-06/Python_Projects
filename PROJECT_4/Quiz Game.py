questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. O2", "B. CO2", "C. H2O", "D. HO"],
        "answer": "C"
    }
]

score = 0

for i, q in enumerate(questions, start=1):
    print(f"\nQ{i}: {q['question']}")
    for opt in q['options']:
        print(opt)
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == q['answer']:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")

if {score}=={len(questions)}:
    print("\nCongrats 🎉🎉, Your all answers are Right!!")
    print(f"Your final score: {score}/{len(questions)}")
else:
    print(f"\nYour final score: {score}/{len(questions)}")