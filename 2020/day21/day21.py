from collections import deque

def parse_file(file):
    foods = []
    with open(file, 'r') as f:
        while (line := f.readline()):
            # trh fvjkl sbzzf mxmxvkd (contains dairy)
            line = line.strip()[:-1].split(' (contains ')
            ingredients = line[0].split(' ')
            allergens = line[1].split(', ')
            foods.append({'ingredients':ingredients, 'allergens':allergens})
    return foods

def map_allergen_to_ingredients(foods):
    a2i_map = {}
    ingredient_count = {}
    for food in foods:
        for allergen in food['allergens']:
            a2i_update = a2i_map.get(allergen, {'count':0})
            for ingredient in food['ingredients']:
                a2i_update[ingredient] = a2i_update.get(ingredient, 0) + 1
            a2i_update['count'] += 1
            a2i_map[allergen] = a2i_update
        for ingredient in food['ingredients']:
            ingredient_count[ingredient] = ingredient_count.get(ingredient, 0) + 1
    return a2i_map, ingredient_count

def filter_ingredients(a2i, ing_count):
    impossible_ingredients = set(ing_count.keys())
    allergens = []
    for allergen, ingredients in a2i.items():
        occurances = ingredients.pop('count')
        possible_ingredients = {k for k,v in ingredients.items() if v == occurances}
        allergens.append(
            {'allergen' : allergen, 'possible_ingredients': possible_ingredients}
        )
        for possible in possible_ingredients:
            if possible in impossible_ingredients:
                impossible_ingredients.remove(possible)
    allergens.sort(key=lambda x: len(x['possible_ingredients']))
    return impossible_ingredients, allergens

def part1(impossible_ingredients, ing_count):
    answer = 0
    for ing in impossible_ingredients:
        answer += ing_count[ing]
    print(f'P1 Answer: {answer}')

def part2(possible_ingredients, allergens):
    results = []
    allergens = deque(allergens)
    while allergens:
        allergen = allergens.popleft()
        ingredients = allergen['possible_ingredients'] & possible_ingredients
        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            possible_ingredients.remove(ingredient)
            results.append((allergen['allergen'], ingredient))
        else:
            allergen['possible_ingredients'] = ingredients
            allergens.append(allergen)
    results.sort(key=lambda x: x[0])
    results = ''.join([x[1] + ',' for x in results])
    print(f'P2 Anwer: {results[:-1]}')

def main():
    foods = parse_file('input.txt')
    a2i, ing_count = map_allergen_to_ingredients(foods)
    impossible_ingredients, allergens = filter_ingredients(a2i, ing_count)
    part1(impossible_ingredients, ing_count)
    possible_ingredients = set(ing_count.keys()).difference(impossible_ingredients)
    part2(possible_ingredients, allergens)

if __name__ == '__main__':
    main()
