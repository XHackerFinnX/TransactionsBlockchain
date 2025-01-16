import schedule
import time
import logging

from datetime import datetime
from db.database import Database
from db.models.tx import Transaction
from utils.transactions import get_transactions

db = Database()
tx_model = Transaction(db)
start_time = time.time()
WORK_TIME = 6 * 60 * 60

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Соединение с базой данных открыто.")


def start_transactions():
    
    data = get_transactions()
    
    for hash_txs, sender, recipient in data:
        date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        
        for addr, value in sender.items():
            tx_model.insert_transaction(hash_txs, 'Исходящие', addr, value, date)
        
        for addr, value in recipient.items():
            tx_model.insert_transaction(hash_txs, 'Входящие', addr, value, date)
            
    logging.info("Транзакции успешно записаны.")


schedule.every(10).minutes.do(start_transactions)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

        if time.time() - start_time > WORK_TIME:
            logging.info("Программа завершена: прошло 6 часов.")
            break
finally:
    db.close()
    logging.info("Соединение с базой данных закрыто.")