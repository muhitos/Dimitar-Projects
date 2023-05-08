import random
print("Fitness knowledge test")
print("Every question gives you one point.")
print("You should select from options 'A', 'B' or 'C'")
print("If you score eight points or more, you have a good knowledge foundation\n"
      "for potential fitness and health results!")
print("Good luck!")
print("")
questions_list = ["What's the amount of calories in 1 gram of protein?", "What is the amount of calories in 1 gram of fat?",
                  "What is the amount of calories in 1 gram of carbohydrates?", "Which body part is the main mover in the bench press?",
                  "What is the main macronutrient in a banana?", "What is the main macronutrient in a chicken fillet?",
                  "Which part of the body is the main mover in the pull-up.", "What is the main macronutrient in rice?",
                  "What is the main macronutrient in almonds?", "What is the main focus of a set if it's in the repetition range from 1 to 6?",
                  "What is the main focus of a set if it's in the repetition range from 6 to 15?"]

len_list = len(questions_list)
points = 0
for question in range(len_list):
    current_question = random.choice(questions_list)
    if current_question == "What's the amount of calories in 1 gram of protein?":
        print(current_question)
        print("A: 4\nB: 2\nC: 7")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "a":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'A'.")
    elif current_question == "What is the amount of calories in 1 gram of fat?":
        print(current_question)
        print("A: 15\nB: 9\nC: 3")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "b":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'B'")
    elif current_question == "What is the amount of calories in 1 gram of carbohydrates?":
        print(current_question)
        print("A: 4\nB: 8\nC: 5")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "a":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'A'")
    elif current_question == "Which body part is the main mover in the bench press?":
        print(current_question)
        print("A: Legs\nB: Triceps\nC: Chest")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "c":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'C'")
    elif current_question == "What is the main macronutrient in a banana?":
        print(current_question)
        print("A: Protein\nB: Carbohydrate\nC: Fat")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "b":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'B'")
    elif current_question == "What is the main macronutrient in a chicken fillet?":
        print(current_question)
        print("A: Fat\nB: Carbohydrate\nC: Protein")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "c":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'c'")
    elif current_question == "Which part of the body is the main mover in the pull-up.":
        print(current_question)
        print("A: Shoulders\nB: Biceps\nC: Back")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "c":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'C'")
    elif current_question == "What is the main macronutrient in rice?":
        print(current_question)
        print("A: Carbohydrate\nB: Protein\nC: Fat")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "a":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'A'")
    elif current_question == "What is the main macronutrient in almonds?":
        print(current_question)
        print("A: Protein\nB: Carbohydrate\nC: Fat")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "c":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'C'")
    elif current_question == "What is the main focus of a set if it's in the repetition range from 1 to 6?":
        print(current_question)
        print("A: Strength\nB: Hypertrophy\nC: Repetition range is irrelevant")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "a":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'A'")
    elif current_question == "What is the main focus of a set if it's in the repetition range from 6 to 15?":
        print(current_question)
        print("A: Strength\nB: Hypertrophy\nC: Endurance")
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "b":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'B'")
if points >= 8:
    print("You can start your fitness journey!")
elif points < 8:
    print("You need some more learning.")