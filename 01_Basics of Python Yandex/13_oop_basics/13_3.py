class RedButton:
    def __init__(self):
        self.counter = 0

    def click(self):
        print (f'Тревога!')
        self.counter += 1

    def count(self):
        return self.counter


first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())



