import csv

# with open("D:\\demo1.csv", newline="") as csvfile:
#     spamreader = csv.reader(csvfile, delimiter="\t")
#     for row in spamreader:
#         print(row)

with open("D:\\DDI-Bidirectional.csv", "w", newline="") as final:
    with open("D:\\demo1.csv", newline="") as original:
        reader = csv.reader(
            original,
            delimiter="\t",
        )
        for rows in reader:
            writer = csv.writer(final, quoting=csv.QUOTE_ALL, delimiter=",")
            writer.writerow(rows)
