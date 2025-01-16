import httpx

from collections import defaultdict, namedtuple

limit = 100
API_URL = f"https://blockchain.info/unconfirmed-transactions?format=json&limit={limit}"

def get_transactions():
    with httpx.Client() as client:
        response = client.get(API_URL)
        data = response.json()

        transactions_list = []
        incoming_transactions = defaultdict(int)
        outgoing_transactions = defaultdict(int)
        Transact = namedtuple('Transact', ['hash', 'sender', 'recipient'])
        
        for txs in data['txs']:
            hash_txs = txs['hash']
            
            # Исходящие транзакции
            for sender in txs['inputs']:
                try:
                    addr = sender['prev_out']['addr']
                    value = sender['prev_out']['value']
                    
                    outgoing_transactions[addr] += value
                except:
                    continue
            
            # Входящие транзакции 
            for recipient in txs['out']:
                try:
                    addr = recipient['addr']
                    value = recipient['value']
                    
                    incoming_transactions[addr] += value
                except:
                    continue
            
            transactions_list.append(
                Transact(
                    hash_txs,
                    outgoing_transactions,
                    incoming_transactions
                )
            )
            
    return transactions_list