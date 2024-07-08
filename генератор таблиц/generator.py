table = [
    ["Никита", 24, 165],
    ["Арсен", 19, 170],
    ["Арсен", 28, 160],
    ["Талер Дерден", 22, 190]
]
headers = ["Имя", "Возраст", "Рост"]

max_col_widths = [max(len(str(row[i])) for row in table) for i in range(len(headers))]

header_row = ' | '.join(headers)
print(header_row)

divider = '-+-'.join('-' * width for width in max_col_widths)
print(divider)

for row in table:
    formatted_row = ' | '.join(f"{str(row[i]):<{max_col_widths[i]}}" for i in range(len(headers)))
    print(formatted_row)