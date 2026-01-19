import random
import time

def static_load_balancing(tasks, num_nodes):
  nodes = [[] for _ in range(num_nodes)]
  for i, task in enumerate(tasks):
    nodes[i % num_nodes].append(task)
  return nodes

def dynamic_load_balancing(tasks, num_nodes, threshold=5):
  loads = [random.randint(0,10) for _ in range(num_nodes)]
  print(f"Initial loads: {loads}")

  for task in tasks:
    overloaded = [i for i in range(num_nodes) if loads[i]>threshold]
    underloaded = [i for i in range(num_nodes) if loads[i]<threshold]

    if overloaded and underloaded:
      sender = random.choice(overloaded)
      receiver = random.choice(underloaded)
      loads[sender] -= 1
      loads[receiver] += 1

    loads[random.randint(0, num_nodes-1)] += 1
  return loads

tasks = [f"T{i}" for i in range(15)]
num_nodes = 3

print("\n ---Static Load Balancing(Round Robin) ---")
static_nodes = static_load_balancing(tasks, num_nodes)
for i,node in enumerate(static_nodes):
  print(f"Node {i+1}: {node}")

print("\n ---Dynamic Load Balancing(Sender_Initiated) ---")
final_loads = dynamic_load_balancing(tasks,num_nodes)
print(f"Final loads after balancing: {final_loads}")








