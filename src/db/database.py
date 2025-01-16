import sqlite3

class Database:
    def __init__(self):
        self.db_path = 'src/db/base/bitcoin_transaction.db'
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                hash TEXT,
                type_wallet TEXT,
                wallet TEXT,
                volume INTEGER,
                datetime TEXT
            );
        """)
        self.connection.commit()
        
    def execute_query(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()
        
    def fetchall_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()