from itertools import combinations

# Данные
suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

# Ввод
must_suit = input().strip()
ban_rank = input().strip()
previous = input().strip()  # строка с предыдущей комбинацией

# Преобразуем предыдущую комбинацию в кортеж для сравнения
previous_combo = tuple(card.strip() for card in previous.split(","))

# Создаём колоду
must_suit_genitive = suits[must_suit]
deck = [f"{rank} {suits[suit]}" for suit in suits for rank in ranks]
deck.sort()

# Ищем следующую комбинацию
found_previous = False
for combo in combinations(deck, 3):
    if must_suit_genitive in str(combo) and ban_rank not in str(combo):
        if not found_previous:
            if combo == previous_combo:
                found_previous = True
        else:
            print(", ".join(combo))
            break
