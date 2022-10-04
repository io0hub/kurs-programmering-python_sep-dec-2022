QUESTIONS = {
    "Fråga 1. Vilken funktion används för att skriva ut saker på skärmen?":["print", "input", "len"],
    "Fråga 2. Hur tar man fram längden på listan i variablen \"fruits\"?": ["len(fruits)" , "for _in range(10)", "input(fruits)"],
    "Fråga 3. Vad heter nyckelordet för att göra en loop i Python?": ["for" , "in", "return"]
}


num_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    viewing = []
    for label, alternative in enumerate(sorted(alternatives), 1):
        viewing.append(alternative)
        print(f"  {label}) {alternative}")
    answer_label = input("\nsvar: ")
    if int(answer_label) <= len(viewing):
        answer = viewing[int(answer_label)-1]
        if answer == correct_answer:
            num_correct += 1
            print(f"\nDitt svar: {answer!r}")
            print("Rätt!")
        else:
            print(f"Ditt svar: {answer!r}")
            print(f"Fel! Rätt svar är: {correct_answer!r}")
    else:
        print("\nSaknas i listan")


print("\n***RESULTAT***")
print(f"\nDu fick {num_correct} rätt av {num} möjliga.")