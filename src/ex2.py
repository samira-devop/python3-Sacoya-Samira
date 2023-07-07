import csv

def find_total_visits():
    total = 0
    files = ["./files/week-1.csv", "./files/week-2.csv", "./files/week-3.csv"]
    for file in files:
        with open(file, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                visits = sum([int(row[day]) for day in reader.fieldnames[1:]])
                total += visits
    return total

def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")
ex2()