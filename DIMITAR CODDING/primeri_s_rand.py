import random

# вариант 1
# numbers = random.randint(1,3)
#
# guess_number =  int(input('Въведи яисло от 1 до 3 '))
#
# if numbers == guess_number:
#     print('Ти спечели играта')
# else:
#     print('Ти загуби')
##################################################################
# ASCII таблица random връща пройзволна буква от ascii таблицата.
# ascii_value = random.randint(65, 90)
# letter = chr()
# print(letter)

#################################################################################
# weekdays = ['Monday', 'Sunday','Wednesday', 'Thusday']
#
# day =  random.choice(weekdays)
#
# print(day)
#####################################################################

questions = ['Кога е основана България?', 'Колко е 2 * 2?']
points = 0
quess_custin_counter = 0
answered_questions = []

for _ in range(10):
    question = random.choice(questions)

    # if questions not in answered_questions:
    #     answered_questions.append(questions)  # функцията append() складира информацията
    #     # в примера горе в "answered_questions = []"
    # else:
    #     continue

    if question == 'Кога е основана България?':
        user_answer = input('Въведете отговор: ')

        if user_answer == '681':
            print('Ти позна')
            quess_custin_counter += 1

    # elif questions == 'Колко е 2 * 2?':
    #     user_answer = input('Въведете отговор: ')
    #
    #     if user_answer == '4':
    #         print('Ти позна')
    #         points += 4
    #         quess_custin_counter += 1
    #
    # if quess_custin_counter == 2:
    #     print('Ти спечели играта!!!')
