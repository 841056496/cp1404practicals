"""
Pseudocode:
Set menu

main function:
score = get_valid_score()
choice = ''
while choice != 'Q':
        print(menu)
        Get choice.strip().upper()
        if choice == 'G':
            score = get_valid_score()
        if choice == 'P':
            result = evaluate_score(score)
        if choice == 'S':
            show_stars(score)
        if choice == 'Q':
            print("Farewell!")
        else:
            print("Invalid choice. Please select a valid option from the menu.")

get_valid_score function:
Get score
while 0 > score or score > 100:
    print error
    Get score
else:
    return score

evaluate_score function:
if score >= 90:
    return "Excellent"
if score >= 50:
        return "Passable"
else:
    return "Bad"

show_stars function:
print('*' * int(score))

main()
"""

menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = get_valid_score()
    choice = ''
    while choice != 'Q':
        print("\nMenu:")
        print(menu)
        choice = input("Enter your choice: ").strip().upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = evaluate_score(score)
            print(result)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
        else:
            print("Invalid choice. Please select a valid option from the menu.")

def get_valid_score():
    score = float(input("Enter a score between 0 and 100: "))
    while 0 > score or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
        score = float(input("Enter a score between 0 and 100: "))
    else:
        return score

def evaluate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print('*' * int(score))

main()