import time

database = {'x': 100, 'y': 200}
read_ts = {'x': 0, 'y': 0}
write_ts = {'x': 0, 'y': 0}

ts_counter = 1

def start_transaction():
    global ts_counter
    ts = ts_counter
    ts_counter += 1
    return ts

def read(transaction_ts, data_item):
    if transaction_ts < write_ts[data_item]:
        print(f"Transaction {transaction_ts}: Read rejected on {data_item} (rollback)")
        return False
    else:
        read_ts[data_item] = max(read_ts[data_item], transaction_ts)
        print(f"Transaction {transaction_ts}: Read {data_item} = {database[data_item]}")
        return True

def write(transaction_ts, data_item, value):
    if transaction_ts < read_ts[data_item] or transaction_ts < write_ts[data_item]:
        print(f"Transaction {transaction_ts}: Write rejected on {data_item} (rollback)")
        return False
    else:
        database[data_item] = value
        write_ts[data_item] = transaction_ts
        print(f"Transaction {transaction_ts}: Wrote {value} to {data_item}")
        return True

T1 = start_transaction()
T2 = start_transaction()

read(T1, 'x')
write(T2, 'x', 150)
write(T1, 'y', 250)
read(T2, 'y')

print("\nFinal Database State:", database)
