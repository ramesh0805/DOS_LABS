import threading
import time

database = {'x': 100, 'y': 200}
committed = []

class Transaction:
    def __init__(self, name):
        self.name = name
        self.local = {}

    def read(self, key):
        self.local[key] = database[key]
        print(f"{self.name}: Read {key} = {self.local[key]}")

    def write(self, key, value):
        self.local[key] = value
        print(f"{self.name}: Write {key} = {value}")

    def validate_and_commit(self):
        for key in self.local:
            if database[key] != self.local[key]:
                print(f"{self.name}: Validation failed on {key}, aborting...")
                return False
        for key in self.local:
            database[key] = self.local[key]
        committed.append(self.name)
        print(f"{self.name}: Committed successfully")
        return True

T1 = Transaction("T1")
T2 = Transaction("T2")

T1.read('x')
T1.write('x', 150)

time.sleep(1)

T2.read('x')
T2.write('x', 200)

T1.validate_and_commit()
T2.validate_and_commit()

print("\nFinal Database State:", database)
