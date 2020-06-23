import csv

# articles to change
with open('article-injazz.csv', 'r') as arts_file:
    arts = csv.DictReader(arts_file, delimiter=';')

    with open('NEW.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        with open("injazz2import.csv", "w", encoding='utf-8', newline='') as file:
            fieldnames = ['Артикул', 'Цена', 'Наличие', 'Поставщик']
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

            writer.writeheader()

            for row in csv_reader:
                if (row[5]!='') and (float(row[5].replace(',','.')) > 3.0) and (row[1]!=''):
                    art_value = row[1]
                    for roww in arts:
                        if art_value == roww['InJazz']:
                            art_value = roww['EU']

                    if row[4] == "есть":
                        inStock = "В наличии"
                    elif row[4] == "нет":
                        inStock = "Нет в наличии"
                    else:
                        inStock = "Ожидается"
                    writer.writerow({'Артикул' : art_value, 'Цена' : row[5], 'Наличие' : inStock, 'Поставщик' : 'Ін-Джаз'})
