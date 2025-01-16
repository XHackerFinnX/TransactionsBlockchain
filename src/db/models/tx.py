class Transaction:
    def __init__(self, db):
        self.db = db

    def insert_transaction(self, hash_txs, type_wallet, wallet, volume, datetime):
        query = """
            INSERT INTO transactions (hash, type_wallet, wallet, volume, datetime)
            VALUES (?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (hash_txs, type_wallet, wallet, volume, datetime))
        
    def get_all_transactions(self):
        query = "SELECT * FROM transactions"
        return self.db.fetchall_query(query)