def detect_deadlock(wfg):
  visited = set()
  rec_stack = set()

  def dfs(process):
    visited.add(process)
    rec_stack.add(process)
    for neighbor in wfg.get(process, []) :
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