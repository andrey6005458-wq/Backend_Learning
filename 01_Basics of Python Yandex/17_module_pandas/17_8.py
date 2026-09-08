import pandas as pd

def update(journal):
    j = journal.copy()
    for i in range(len(j.loc[:, 'name'])):
        j.loc[:, 'average'] = (j['maths'] + j['physics'] + j['computer science']) / 3
    return j.sort_values(by=['average', 'name'], ascending=(False, True))

columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)