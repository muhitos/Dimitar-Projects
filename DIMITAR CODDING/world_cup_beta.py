# Добавям библиотека за произволни числа, необходима за резултатите от мачовете
import random

# Приветствени съобщения
print("Welcome to the group stage of world cup 2022!")
print("Please enter the four teams who is in the list!")

# Въвеждане на отборите в групата
team1 = input()
team2 = input()
team3 = input()
team4 = input()

# Извеждане на отборите от групата
print("Your group of finalist is:")
print(team1, team2, team3, team4)

# първоначални данни за резултатите на отборите
team1_points = 0
team2_points = 0
team3_points = 0
team4_points = 0

goals_scored_team1 = 0
goals_scored_team2 = 0
goals_scored_team3 = 0
goals_scored_team4 = 0

recieved_goals_team1 = 0
recieved_goals_team2 = 0
recieved_goals_team3 = 0
recieved_goals_team4 = 0

# създаване на лист от възможни реализирани голове за всяка среща
list1 = [0, 1, 2, 3, 4, 5]

# въвеждаме цикъл, който ще отговаря за всяка една среща
for i in range(0, 6):

    # Тъй като искаме да проследим всеки един мач в групата си правя цикъл, като всяка стъпка от цикълът ще
    # е за отделен мач в групата

    if i == 0:

        # За пригледност преди всеки мач искаме потребителят да въведе текст, с който да стартира логиката
        print("To proceed to the match type PLAY on the board")
        action = input()
        if action == "PLAY":

            # за всеки един мач от групата ще искаме да тегли число, което е произволно от цикълът
            # с възможни числа, който ще показва вкараните голове от всеки един участващ отбор в срещата
            score1 = random.choice(list1)
            score2 = random.choice(list1)

            # Добавяме към първоначалните променливи за вкарани и получени голове на всеки един участващ
            # отбор в срещата
            goals_scored_team1 += score1
            goals_scored_team2 += score2
            recieved_goals_team1 += score2
            recieved_goals_team2 += score1

            # Правим проверка, кой отбор е спечелил срещата или е била на равно, за да добавим точките към
            # статистиката на отборите
            if score1 > score2:
                team1_points += 3
            elif score1 == score2:
                team1_points += 1
                team2_points += 1
            elif score1 < score2:
                team2_points += 3

            # За пригледност отпечатваме резултата от конкретният мач, като повтаряме цикълът за всяка
            # една отделна среща
            print(f"{team1} {score1} : {score2} {team2}")

    if i == 1:
        print("To proceed to the match type PLAY on the board")
        action = input()
        if action == "PLAY":

            score3 = random.choice(list1)
            score4 = random.choice(list1)
            goals_scored_team3 += score3
            goals_scored_team4 += score4
            recieved_goals_team3 += score4
            recieved_goals_team4 += score3

            if score3 > score4:
                team3_points += 3
            elif score3 == score4:
                team3_points += 1
                team4_points += 1
            elif score3 < score4:
                team4_points += 3

            print(f"{team3} {score3} : {score4} {team4}")

    if i == 2:
        print("To proceed to the match type PLAY on the board")
        action = input()
        if action == "PLAY":

            score1 = random.choice(list1)
            score3 = random.choice(list1)
            goals_scored_team1 += score1
            goals_scored_team3 += score3
            recieved_goals_team1 += score3
            recieved_goals_team3 += score1

            if score1 > score3:
                team1_points += 3
            elif score1 == score3:
                team1_points += 1
                team3_points += 1
            elif score1 < score3:
                team3_points += 3

            print(f"{team1} {score1} : {score3} {team3}")

    if i == 3:
        print("To proceed to the match type PLAY on the board")
        action = input()
        if action == "PLAY":

            score2 = random.choice(list1)
            score4 = random.choice(list1)
            goals_scored_team2 += score2
            goals_scored_team4 += score4
            recieved_goals_team2 += score4
            recieved_goals_team4 += score2

            if score2 > score4:
                team2_points += 3
            elif score2 == score4:
                team2_points += 1
                team4_points += 1
            elif score2 < score4:
                team4_points += 3

            print(f"{team2} {score2} : {score4} {team4}")

    if i == 4:
        print("To proceed to the match type PLAY on the board")
        action = input()
        if action == "PLAY":

            score1 = random.choice(list1)
            score4 = random.choice(list1)
            goals_scored_team1 += score1
            goals_scored_team4 += score4
            recieved_goals_team1 += score4
            recieved_goals_team4 += score1

            if score1 > score4:
                team1_points += 3
            elif score1 == score4:
                team1_points += 1
                team4_points += 1
            elif score1 < score4:
                team4_points += 3

            print(f"{team1} {score1} : {score4} {team4}")

    if i == 5:
        print("To proceed to the match type PLAY on the board")
        action = input()
        if action == "PLAY":

            score2 = random.choice(list1)
            score3 = random.choice(list1)
            goals_scored_team2 += score2
            goals_scored_team3 += score3
            recieved_goals_team2 += score3
            recieved_goals_team3 += score2

            if score2 > score3:
                team2_points += 3
            elif score2 == score3:
                team2_points += 1
                team3_points += 1
            elif score2 < score3:
                team3_points += 3

            print(f"{team2} {score2} : {score3} {team3}")

# За по-голяма интуитивност добавих и команда за извеждане на резултатите
print("To proceed to the results of the teams, type SCORE")
action = input()
if action == "SCORE":
    # Тук отпечатвам резултатите за всеки един отбор, като отпечатвам натрупаните точки от срещите и отделно пресмятам
    # головата разлика между вкарани и получени голове за всеки един отбор
    print(f"{team1} has {team1_points} points with goal diff {goals_scored_team1 - recieved_goals_team1}")
    print(f"{team2} has {team2_points} points with goal diff {goals_scored_team2 - recieved_goals_team2}")
    print(f"{team3} has {team3_points} points with goal diff {goals_scored_team3 - recieved_goals_team3}")
    print(f"{team4} has {team4_points} points with goal diff {goals_scored_team4 - recieved_goals_team4}")