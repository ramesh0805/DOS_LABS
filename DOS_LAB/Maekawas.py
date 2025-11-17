import time
import random

class Maekawas:
    def __init__(self,pid,quorum):
        self.pid = pid
        self.voted = False
        self.queue = []
        self.quorum = quorum
    def request_cs(self,processes):
        print(f"P{self.pid} requesting CS")
        votes = 0
        for q in self.quorum:
            if not processes[q].voted:
                processes[q].voted = True
                votes += 1
            if votes == len(self.quorum):
                print(f"P{self.pid} enters CS")
                time.sleep(1)
                self.release_cs(processes)
    def release_cs(self,processes):
        print(f"P{self.pid} releases CS")
        for q in self.quorum:
            processes[q].voted = False

def simulate_maekawa():
        processes = [Maekawas(i,quorum=[i, (i+1)%3]) for i in range(3)]
        for p in processes:
            p.request_cs(processes)
            time.sleep(random.uniform(0.5, 1.0))

simulate_maekawa()