import threading 
import time

database = {'x': 100, 'y' : 200 }

lock_table = {
    'x': threading.Lock(),
    'y': threading.Lock()
}

def transaction_1():
  print("Transaction 1: Trying to acquire lock on x")
  lock_table['x'].acquire()
  print("Transaction 1: Lock acquired on x")
  database['x'] += 50
  time.sleep(1)  # Simulate some processing time
  print("Transaction 1: Releasing lock on x")
  lock_table['x'].release()

def transaction_2():
  print("\nTransaction 2: Trying to acquire lock on x")
  lock_table['x'].acquire()
  print("\nTransaction 2: Lock acquired on x")
  database['x'] -= 30
  time.sleep(1)  # Simulate some processing time
  print("Transaction 2: Releasing lock on x")
  lock_table['x'].release()

t1 = threading.Thread(target=transaction_1)
t2 = threading.Thread(target=transaction_2)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Final Database State:", database)