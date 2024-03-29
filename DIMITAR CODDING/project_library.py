import random

fantasy_horror = ["Дракула, Брам Стокър", "Отмъстиел, В. Е. Шуаб", "Петима в едно тяло, Гай Морпъс", "Институтът, Стивън Кинг",
                      "Всички наши грешни дни, Илан Мастаи", "Властелинът на плъстените, Дж. Р. Толкин", "Били Съмърс, Стивън Кинг",
                      "Пътеводител на галактическия стопаджия, Дъглас Адамс"]
crime_thriller = ["Пациент 488, Никола Бьогле", "Кестеновия човек, Сьорен Свайструп", "Десет малки негърчета, Агата Кристи", "Ад, Дан Браун",
                  "Ако има кръв, Стивън Кинг", "Убийство в Ориент експрес, Агата Кристи", "Тъмната материя, Блейк Крауч", "Бягащият човек, Стивън Кинг"]
romance = ["158 удара в минута, Димитър Калбуров", "Родена в огъня, Нора Робъртс", "В случай на чудо, Л. Дж. Шен", "Верити, Колийн Хувър",
           "Аз преди теб, Джоджо Мойс", "Сутрешно кафе в Рим, Диего Галдино", "Коледна тайна, Карън Суан", "Завръщане Никълъс Спаркс"]
other_prose = ["Живот в скалите, Мария Лалева", "Където пеят раците, Дилия Оуенс", "Глина, Виктория Бешлийска", "Татуировчикът на Аушвиц, Хедър Морис",
               "Аз ще броя дните, Георги Бърданов", "1984, Джорд Оуел", "Тревожни хора, Фредерик Бакман", "Да убиеш присмехулник, Харпър Ли"]
humor = ["Завижели обидено, Георги Блажев", "Лейди Гергана, Цветелина Цветкова", "Дневник от панелените блокове, Никола Крумов",
         "Моето семейство и други животни, Джералд Даръл", "Фалшивата брада на Дядо Коледа, Тери Пратчет", "Северозападен романь, Стоян Николов",
         "Прахосмукачката на вещицата, Тери Пратчет", "Как да живеем с изтрещялата си половинка, Асен Сираков"]
science = ['Кратки отговори на големи въпроси, Стивн Хокинг', "Мисленето, Даниъл Канема", "21 урока за 21 век, Ювал Ноа Харари",
           "Геномът, Мат Ридли", "Тялото. Наръчник за употреба, Бил Брайсън", "Кратка история на поччти всичко, Бил Брайсън"]
history_and_journalism = ["Изкуството на войната, Сун Дзъ", "Мишел Обама. Моята история, Мишел Обама", "Последна спирка Аушвиц, Еди де Винд",
                          "Леонардо да Винчи, Уолтър Айзъксън", "Човекът в търсене на смисъл, Виктор Франкъл", "Менгеле: Ангелът на смъртта, Дейвид Маруел",
                          "48те закона на властта, Робърт Грийн", "Цинкови момчета, Светлана Алексиевич"]
children_literature = ["Хари Потър, Дж. к. Роулинг", "Пук и Чук, Турбьорн Егнер", "Мили бате!... Писма на един дакел, Станка Пенчева",
                       "Пипи дългото чорапче, Астрид Линдгрен", "Матилда, Роалд Дал", "Хвърчащата класна стая, Ерих Кестнер",
                       "Софийски магьосници, Мартин Колев", 'Емил от Льонеберя, Астрид Линдгрен']
print("\033[93mЗа изход от прграмата въведете - \033[1mКрай\033[0m")
print(f"Въведете номер на жанр от следният списък:\n1.Научна фантастика, фентъзи и хорър\n2.Криминални и трилъри\n3.Романтични\n"
          f"4.Друга проза\n5.Хумор\n6.Наука\n7.История и публицистика\n8.Детска литература")
genre = input('\033[1m->\033[0m')
read_books = []
read_books_count = 0
current_book = ""
fantasy_count = 0
crime_count = 0
romance_count = 0
other_count = 0
humor_count = 0
science_count = 0
history_count = 0
children_count = 0


while genre != "Край":
    genre = int(genre)
    if read_books_count == 62:
        print("Браво! Успяяхте да прочетете цялата библиотека!")
        break
    if genre == 1:
        current_book = random.choice(fantasy_horror)
        if fantasy_count >= 8:
            print("Няма повече книги от тази категория. Моля изберете друга категория.")
            genre = input('\033[1m->\033[0m')
        if current_book not in read_books:
            read_books.append(current_book)
        else:
            continue
        fantasy_count += 1

    elif genre == 2:
        current_book = random.choice(crime_thriller)
        if crime_count >= 8:
            print("Няма повече книги от тази категория. Моля изберете друга категория.")
            genre = input('\033[1m->\033[0m')
        if current_book not in read_books:
            read_books.append(current_book)
        else:
            continue
        crime_count += 1
    elif genre == 3:
        current_book = random.choice(romance)
        if romance_count >= 8:
            print("Няма повече книги от тази категория. Моля изберете друга категория.")
            genre = input('\033[1m->\033[0m')
        if current_book not in read_books:
            read_books.append(current_book)
        else:
            continue
        romance_count += 1
    elif genre == 4:
        current_book = random.choice(other_prose)
        if other_count >= 8:
            print("Няма повече книги от тази категория. Моля изберете друга категория.")
            genre = input('\033[1m->\033[0m')
        if current_book not in read_books:
            read_books.append(current_book)
        else:
            continue
        other_count += 1
    elif genre == 5:
        current_book = random.choice(humor)
        if humor_count >= 8:
            print("Няма повече книги от тази категория. Моля изберете друга категория.")
            genre = input('\033[1m->\033[0m')
        if current_book not in read_books:
            read_books.append(current_book)
        else:
            continue
        humor_count += 1
    elif genre == 6:
        current_book = random.choice(science)
        if science_count >= 8:
            print("Няма повече книги от тази категория. Моля изберете друга категория.")
            genre = input('\033[1m->\033[0m')
        if current_book not in read_books:
            read_books.append(current_book)
        else:
            continue
        science_count += 1
    elif genre == 7:
        current_book = random.choice(history_and_journalism)
        if history_count >= 8:
            print("Няма повече книги от тази категория. Моля изберете друга категория.")
            genre = input('\033[1m->\033[0m')
        if current_book not in read_books:
            read_books.append(current_book)
        else:
            continue
        history_count += 1
    elif genre == 8:
        current_book = random.choice(children_literature)
        if children_count >= 8:
            print("Няма повече книги от тази категория. Моля изберете друга категория.")
            genre = input('\033[1m->\033[0m')
        if current_book not in read_books:
            read_books.append(current_book)
        else:
            continue
        children_count += 1

    read_books_count += 1
    print(f"\033[94m{current_book}\033[0m")
    print(f'\033[93mПрочетени книги до момента: \033[1m{read_books_count}\033[0m')
    genre = input('\033[1m->\033[0m')