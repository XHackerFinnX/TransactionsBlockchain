import csv

from db.database import Database
from db.models.tx import Transaction

db = Database()
tx_model = Transaction(db)

def csv_transaction(data):
    headers = ["hash", "type_wallet", "wallet", "volume", "datetime"]
    
    with open(file='src/db/base/btc_transactions.csv', mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(headers)
        writer.writerows(data)

    print(f"Данные успешно записаны в файл")
    
try:
    data = tx_model.get_all_transactions()
    csv_transaction(data)
finally:
    db.close()