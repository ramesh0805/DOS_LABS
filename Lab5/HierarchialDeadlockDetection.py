def detect_cycle(graph):
  """Detects a cycle in a directed graph using DFS."""
  visited = set()
  stack = set()

  def dfs(node):
    visited.add(node)
    stack.add(node)
    for neighbor in graph.get(node, []):
      if neighbor not in visited and dfs(neighbor):
        return True
      elif neighbor in stack:
        return True
    stack.remove(node)
    return False
  
  for node in graph:
    if node not in visited:
      if dfs(node):
        return True
  return False


cluster_A = {
  'P1' : ['P2'],
  'P2' : []
}

cluster_B= {
  'P3' : ['P4'],
  'P4' : []
}

print("Checking local deadlocks...")
if detect_cycle(cluster_A):
  print("Deadlock in cluster A")
else:
  print("No local deadlock in cluster A")

if detect_cycle(cluster_B):
  print("Deadlock detected in Cluster B")
else:
  print("No local deadlock in cluster B")

global_graph =  {
  'P2' : ['P3'],
  'P4' : ['P1'],
  'P1' : ['P2'],
  'P3' : ['P4']
}

print("\nChecking global deadlocks across clusters...")
if detect_cycle(global_graph):
  print("Global deadlock detected!")
else:
  print("No Global Deadlock.")