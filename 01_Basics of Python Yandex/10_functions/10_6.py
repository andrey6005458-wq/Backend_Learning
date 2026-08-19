__final_number = 0


def move(player, number):
    global __final_number
    if player == "Петя":
        __final_number += number
    elif player == "Ваня":
        __final_number -= number


def game_over():
    if __final_number > 0:
        return "Петя"
    elif __final_number < 0:
        return "Ваня"
    else:
        return "Ничья"


move("Петя", 3)
move("Ваня", 4)
move("Петя", 4)
move("Ваня", 3)
print(game_over())
