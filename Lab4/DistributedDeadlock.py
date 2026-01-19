class Process:
  def __init__(self,name):
    self.name = name
    self.waiting_for = None
def send_probe(initiator,sender,receiver,processes,visited):
  if receiver is None:
    return False
  print(f"Probe: ({initiator},{sender},{receiver})")

  if receiver == initiator:
    print(f"Deadlock detected! Cycle returned to {initiator}")
    return True
  
  next_proc = processes[receiver].waiting_for
  if next_proc and (initiator,receiver,next_proc) not in visited:
    visited.add((initiator,receiver,next_proc))
    return send_probe(initiator,receiver,next_proc,processes,visited)
  return False

processes = {
  'P1' : Process('P1'),
  'P2' : Process('P2'),
  'P3' : Process('P3')

}
processes['P1'].waiting_for = "P2"
processes['P2'].waiting_for = "P3"
processes['P3'].waiting_for = "P1"


visited = set()
deadlock_found = send_probe('P1','P1',processes['P1'].waiting_for,processes,visited)
if not deadlock_found:
  print("No deadloclk detected")