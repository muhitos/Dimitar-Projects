# Линейно извлечение на елемент
# Масиви
names = ["Volodq", "Valera", "Vasq", "Sasha",
         "Anton", "Qkov"]
search_for = "Anton"  # кой елемент искаме


def linear_seаrch(where, what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0]  # връщаме индекса

    return None  # или None ,ако не е намерено


print("Исканият елемент", search_for, "е под индекс"
      , linear_seаrch(names, search_for))
