import threading
counter = 0
lock = threading.Lock()

def increment(n):
  global counter
  for _ in range(n):
    lock.acquire()
    counter += 1
    lock.release()

num_threads = 5
increments_per_thread = 1000
threads = []

for i in range(num_threads):
  t = threading.Thread(target=increment, args=(increments_per_thread,))
  threads.append(t)
  t.start()

for t in threads:
  t.join()

print(f"Final counter value: {counter}")
