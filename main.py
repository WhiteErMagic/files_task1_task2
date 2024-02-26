
cook_book = {}

with open('cook_book.txt', 'r', encoding='utf-8') as f:

    while True:
        line = f.readline()
        if line == '\n':
            continue
        if not line:
            break

        dish = line.strip()
        cook_book[dish] = []
        count_lines = int(f.readline())
        for ind in range(count_lines):
            mass = f.readline().strip().split("|")
            cook_book[dish] += [{'ingredient_name': mass[0], 'quantity': int(mass[1]), 'measure': mass[2]}]


print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            if ing['ingredient_name'] in ingredients:
                ingredients[ing['ingredient_name']]['quantity'] += ing['quantity']*person_count
            else:
                ingredients[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': ing['quantity']*person_count}

    print(ingredients)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)