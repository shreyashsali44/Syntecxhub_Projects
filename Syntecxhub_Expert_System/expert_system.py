# Rule-Based Expert System using Forward Chaining

# Knowledge Base (Rules)
rules = [
    {
        "if": ["fever", "cough"],
        "then": "flu"
    },
    {
        "if": ["flu", "body_pain"],
        "then": "viral_infection"
    },
    {
        "if": ["headache", "fever"],
        "then": "migraine"
    },
    {
        "if": ["viral_infection"],
        "then": "doctor_consultation"
    }
]


# Forward Chaining Function
def forward_chaining(facts):

    inferred = set(facts)
    applied_rules = []

    changed = True

    while changed:
        changed = False

        for rule in rules:

            conditions = rule["if"]
            conclusion = rule["then"]

            # Check if all conditions are true
            if all(condition in inferred for condition in conditions):

                if conclusion not in inferred:
                    inferred.add(conclusion)
                    applied_rules.append(rule)

                    print(f"Rule Applied: IF {conditions} THEN {conclusion}")

                    changed = True

    return inferred


# User Input
print("=== Rule-Based Expert System ===")

user_input = input("Enter symptoms separated by commas: ")

facts = [fact.strip().lower() for fact in user_input.split(",")]

# Run Expert System
results = forward_chaining(facts)

# Final Conclusions
print("\nFinal Facts and Conclusions:")

for item in results:
    print("-", item)