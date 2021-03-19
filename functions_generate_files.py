import requests
import csv
import phonenumbers
import mysql.connector
import shutil
import os

from datetime import date, datetime

from constants import CONFIG_DB, DDI_FILE, INPUT_FILE, HISTORY_PATH


def save_output_file():
    current_date_time = datetime.now().strftime("%d%m%Y_%H%M%S")
    ddi_file_record = DDI_FILE.rstrip(".csv") + f"_{current_date_time}" + ".csv"
    filename = os.path.join(HISTORY_PATH, ddi_file_record)
    shutil.copyfile(DDI_FILE, filename)


def get_data_aramis(phone):
    x = phonenumbers.parse(f"+{phone}", None)
    cc = str(x.country_code)
    mydb = mysql.connector.connect(**CONFIG_DB)
    cursor = mydb.cursor()
    query = "SELECT source_id, country_name FROM country WHERE cc=%s"
    cursor.execute(query, (cc,))
    result = list(cursor.fetchone())
    mydb.close()
    return result, cc


def create_file_DDI(input_file=INPUT_FILE):
    with open(DDI_FILE, "w", newline="") as final:
        with open(input_file, newline="") as original:
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
                data, cc = get_data_aramis(rows[0])
                writer.writerow(
                    [
                        data[0],
                        "DDI-Bidirectional",
                        cc,
                        data[1],
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