def health_diagnosis_system():
    diseases = {
        "influenza": {
            "symptoms": ["fever", "headache", "cough", "sore throat"],
            "treatment": "Rest and hydration"
        },
        "diabetes": {
            "symptoms": ["frequent urination", "increased thirst", "weight loss"],
            "treatment": "Consult a doctor for insulin or medication"
        },
        "hypertension": {
            "symptoms": ["headache", "dizziness", "blurred vision"],
            "treatment": "Reduce salt intake, regular exercise"
        }
    }

    symptoms = input("Enter symptoms (comma-separated): ").lower().split(", ")
    age = input("Enter age: ")
    medical_history = input("Enter medical history: ").lower()

    try:
        age = int(age)
        diagnosis = None

        for disease, info in diseases.items():
            if all(symptom in info["symptoms"] for symptom in symptoms):
                diagnosis = disease.capitalize()
                treatment = info["treatment"]
                break

        if diagnosis:
            print(f"Recommended Diagnosis: {diagnosis}")
            print(f"Suggested Treatment: {treatment}")
        else:
            print("No matching diagnosis found. Please consult a doctor.")
    except ValueError:
        print("Invalid age entered. Please enter a numeric value.")

def personal_finance_planner():
    def calculate_leftover_income(income, expenses, savings_goal):
        return income - expenses - savings_goal

    try:
        income = float(input("Enter your monthly income: $"))
        expenses = float(input("Enter your fixed expenses: $"))
        savings_goal = float(input("Enter your savings goal: $"))

        leftover = calculate_leftover_income(income, expenses, savings_goal)

        if leftover > 0:
            print(f"You can save ${leftover:.2f} beyond your goal.")
        elif leftover == 0:
            print("You are meeting your savings goal exactly.")
        else:
            print(f"Reduce discretionary spending by ${-leftover:.2f} to meet your savings goal.")
    except ValueError:
        print("Invalid input. Please enter numeric values for income, expenses, and savings goal.")

while True:
    print("\nChoose a system to run:")
    print("1. Health Diagnosis System")
    print("2. Personal Finance Planner")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        health_diagnosis_system()
    elif choice == "2":
        personal_finance_planner()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
