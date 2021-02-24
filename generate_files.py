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
        writer = csv.writer(final, quoting=csv.QUOTE_ALL, delimiter=",")
        writer.writerow(
            [
                "Source ID",
                "Source",
                "ISO Code",
                "Country",
                "Digits",
                "Last Modification",
                "Source Type",
                "Mask",
                "Mask Active",
                "CPC",
                "NumA",
                "Group Country NumA",
                "Business Unit",
                "MNC",
                "Rate",
                "Billing Increments",
            ]
        )
        for rows in reader:
            writer.writerow(
                [
                    "MEX99",
                    "DDI-Bidirectional",
                    "52",
                    "MEXICO",
                    rows[0],
                    "",
                    "Fixed",
                    rows[0],
                    "1",
                    "0",
                    "",
                    "",
                    "",
                    rows[1],
                    "0,0",
                    "1/1",
                ]
            )
