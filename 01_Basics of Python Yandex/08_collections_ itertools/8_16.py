from itertools import combinations

suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

must_suit = input().strip()
ban_rank = input().strip()

must_suit_genitive = suits[must_suit]

deck = [f"{rank} {suits[suit]}" for suit in suits for rank in ranks]
deck.sort()

count = 0
for combo in combinations(deck, 3):
    if must_suit_genitive in str(combo) and ban_rank not in str(combo):
        print(", ".join(combo))
        count += 1
        if count == 10:
            break
