"""
CP1404/CP5632 - Practical
Broken program to determine score status

Pseudocode:
import random

main function:
    Get score
    result = evaluate_score()
    print result

    random_score = random.uniform(0, 100)
    random_result = evaluate_score(random_score)
    print random_score
    print random_result

evaluate_score function:

    if score < 0 or score > 100
        print error
    else:
        if score>=90
            print Excellent
        elif score >= 50:
            print Passable
        else:
            print("Bad")
"""


import random

def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

    random_score = random.uniform(0, 100)
    random_result = evaluate_score(random_score)
    print(f"Random score: {random_score:.2f}")
    print(random_result)

def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
