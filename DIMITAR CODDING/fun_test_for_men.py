import random
#name of test
print("Въпроси, на които мъжете трябва да са особено внимателни с отговора си!")
#the rules
print("Правила: Възмони отговори Да/Не\n")
questions = ['Как мислиш, може ли някой да спре да обича някого завинаги?',
             'Смяташ ли, че всички мъже изневеряват на своите половинки?',
             'Мислил ли си някога да се разделим?',
             'Разсъбличал ли си някога момиче с очи?',
             'Обсъждате ли с приятелите момичетата, с които сте спали?', 'Някога обичал ли си някоя колкото мен?',
             'Обичаш ли да ходиш на стриптийз клубове?', 'Фантазираш ли за други момичета?',
             'Ще ме зарежеш ли заради по-слабо момиче?', 'Много ли съм напълняла?',
             'Ако те напусна, бързо ли ще си намериш друга?', 'Омръзнах ли ти?',
             'Дразнят ли те моите въпроси?']
list_of_answer = 0
answered_questions = []

while True:
    current_question = random.choice(questions)
    if current_question not in answered_questions:
        answered_questions.append(current_question)
        print(current_question)
    else:
        continue

    answer = input()

    if answer == 'Не':
        print('На прав път си!\n')
        list_of_answer += 1
        if list_of_answer == 13:
            print("Това е само началото!")
            break
    else:
        print("Загази!!!")
        break
