import re
def delDuplicates(table):
    checked = []
    for e in table:
        if e not in checked:
            checked.append(e)
    return checked


def transpose(table):
    s = []
    # We need to assume that each inner list has the same size for this to work
    size = len(table[0])
    for col in range(size):
        inner = []
        for row in range(len(table)):
            inner.append(table[row][col])
        s.append(inner)
    return s


def delAllNones(table):
    i = 0
    while i < len(table):
        count = 0
        for j in range(len(table[i])):
            if table[i][j] is None:
                count += 1
            else:
                break
        if count == len(table[i]):
            table.remove(table[i])
            i -= 1
        i += 1
    return table


def changeSpelling(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] is not None:
                table[i][j] = table[i][j].replace('[at]', '@').replace('-', '').replace('Выполнено', 'да').replace(
                    'Не выполнено', 'нет')
    return table


def f23(table):
    table = delDuplicates(table)
    table = transpose(table)
    table = delDuplicates(table)
    table = delAllNones(table)
    table = changeSpelling(table)
    return table


x = [['08/08/2004', None, 'Руцевяк, В.Г.', 0.38],
     ['05/11/2004', None, 'Рузачяк, И.Р.', 0.90],
     ['09/06/2002', None, 'Лорич, В.Ф.', 0.35]]

print(re.sub('\w+,\s\w\.\w\.', re.search('\w+', 'Руцевяк, В.Г.').group(0), 'Руцевяк, В.Г.'))

print('0.38'.isdigit())