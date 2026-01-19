import random
nodes = {
  "Node1" : random.randint(5, 10),
  "Node2" : random.randint(0, 5),
  "Node3" : random.randint(0, 5)
}

THRESHOLD = 7

print("Initial Node Loads")
for node, load in nodes.items():
  print(f"{node} : {load}")

def migrate_task(nodes):
  overloaded = [n for n, l in nodes.items() if l > THRESHOLD]
  underloaded = [n for n, l in nodes.items() if l < THRESHOLD - 2]

  if overloaded and underloaded:
    src = random.choice(overloaded)
    dest = random.choice(underloaded)

    nodes[src] -= 1
    nodes[dest] += 1

    print("f\nTask migrated from {src} -> {dest}")

  else:
    print("\nNo migration needed")

for _ in range(3):
  migrate_task(nodes)
  print("Updated Loads: ", nodes)