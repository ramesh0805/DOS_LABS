def lamport_clock(events):
    num_processes = len(events)
    clocks = [0] * num_processes
    timestamps = [[] for _ in range(num_processes)]
    messages = []

    for i, process_events in enumerate(events):
        for event in process_events:
            clocks[i] += 1

            if event.startswith('s'):
                msg_to = int(event[1]) - 1
                messages.append((i, msg_to, clocks[i]))

            elif event.startswith('r'):
                msg_from = int(event[1]) - 1
                for m in messages:
                    if m[0] == msg_from and m[1] == i:
                        clocks[i] = max(clocks[i], m[2]) + 1

            timestamps[i].append(clocks[i])

    return timestamps


events = [
    ['e1', 's2'],
    ['e3', 'r1'],
    ['r2', 'e4', 'e5']
]

timestamps = lamport_clock(events)

for i, ts in enumerate(timestamps):
    print(f"P{i+1} event timestamps: {ts}")



def detect_deadlock(wfg):
  visited = set()
  rec_stack = set()

  def dfs(process):
    visited.add(process)
    rec_stack.add(process)
    for neighbor in wfg.get(process, []) :
      if neighbor in rec_stack:
        return True
      if neighbor not in visited:
        if dfs(neighbor):
          return True
    rec_stack.remove(process)
    return False
  for process in wfg:
    if process not in visited:
      if dfs(process):
        return True
  return False

wfg = {
  'P1': ['P2'],
  'P2': ['P3'],
  'P3': ['P1']
}

if detect_deadlock(wfg):
  print("Deadlock detected(Centralized)")
else:
  print("No deadlock detected")



  import random

random.seed(1)

nodes = {
    "Node1": random.randint(1, 13),
    "Node2": random.randint(2, 9),
}

THRESHOLD = 7

print("Initial Node Loads:")
for node, load in nodes.items():
    print(f"{node}: {load}")

def migrate_task(nodes):
    overloaded = [n for n, l in nodes.items() if l > THRESHOLD]
    underloaded = [n for n, l in nodes.items() if l < THRESHOLD - 2]

    if overloaded and underloaded:
        src = random.choice(overloaded)
        dest = random.choice(underloaded)
        nodes[src] -= 1
        nodes[dest] += 1
        print(f"\nTask migrated from {src} ➜ {dest}")
    else:
        print("\nNo migration needed")

for round_no in range(1, 4):
    print(f"\n--- Round {round_no} ---")
    migrate_task(nodes)
    print("Updated Loads:", nodes)


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
