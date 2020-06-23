import csv


with open('NEW.csv', encoding='utf-8') as csv_file: # file from Injazz with data to change for import
    csv_reader = csv.reader(csv_file, delimiter=';')
    with open("injazz2import.csv", "w", encoding='utf-8', newline='') as import_file:
        fieldnames = ['Артикул', 'Цена', 'Наличие', 'Поставщик']
        writer = csv.DictWriter(import_file, fieldnames=fieldnames, delimiter=',')

        writer.writeheader()
        # row[5] - price, row[1] - article. if article or price is empty - skip, is price lower than 3 - skip
        for row in csv_reader:
            if (row[1]!='') and (row[5]!='') and (float(row[5].replace(',','.')) > 3.0):
                art_value = row[1]
                with open('article-injazz.csv', 'r') as arts_file:  # articles to change, if we have other articles for these models
                    arts = csv.DictReader(arts_file, delimiter=';')
                    for roww in arts:
                        if art_value == roww['InJazz']:
                            art_value = roww['EU']
                # change stock statuses
                if row[4] == "есть":
                    inStock = "В наличии"
                elif row[4] == "нет":
                    inStock = "Нет в наличии"
                else:
                    inStock = "Ожидается"
                writer.writerow({'Артикул' : art_value, 'Цена' : row[5], 'Наличие' : inStock, 'Поставщик' : 'Ін-Джаз'})