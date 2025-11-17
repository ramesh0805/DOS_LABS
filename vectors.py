from turtledemo import clock


def update_on_receive(receiver_clock, sender_clock, receiver_id):
    for i in range(len(receiver_clock)):
        receiver_clock[i] = max(receiver_clock[i],sender_clock[i])
    receiver_clock[receiver_id] = receiver_clock[receiver_id] + 1
    return receiver_clock
def vector_clock_simulation(num_processes):
    clocks=[[0 for _ in range(num_processes)] for _ in range(num_processes)]
    events = [
        ("send", 0, 1),
        ("internal", 0, None),
        ("receive", 1, 0),
        ("internal", 2, None)
    ]

    for e in events:
        etype, p1, p2 = e
        if etype == "internal":
            clocks[p1][p1] += 1
            print(f"Internal event in P{p1+1}: {clocks[p1]}")
        elif etype == "send":
            clocks[p1][p1] += 1
            print(f"P{p1+1}Sends message to P{p2+1} with clock{clocks[p1]}")
            sender_clock = clocks[p1][:]
        elif etype == "receive":
            clocks[p1] = update_on_receive(clocks[p1], clocks[p2], p1)
            print(f"P{p1+1} received message from P{p2 + 1} : {clocks[p1]}")

    print("\nFinal Vector Clocks:")
    for i,c in enumerate(clocks):
        print(f"P{i+1} : {c}")

vector_clock_simulation(3)