import csv

# brand-list to search in
with open('brands.csv', 'r') as brands_file:
    brands = list(csv.reader(brands_file))

#data file: title - description like "Group"+"Brand"+"Model". Need to extract Brand and Model to columns
    with open('fff3.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        with open("fff.csv", "w", encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for row in csv_reader:
                if line_count == 0:
                    writer.writerow(row)  # header-row
                    line_count += 1
                else:
                    for [x] in brands:
                        if x.lower() in row[0].lower():  # compare lowercase
                            brand = x
                            posit = row[0].lower().find(x.lower()) + len(x) + 1  # where "Model" starts
                            model = row[0][posit:]
                            writer.writerow([row[0], brand, model])
                            line_count += 1
