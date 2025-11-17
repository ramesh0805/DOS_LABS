def lamport_clock(events, messages):
    clocks = [0 for _ in events]
    timestamps = [[] for _ in events]

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
    ['e1', 's2', 'e2'],
    ['r1', 'e3', 's3'],
    ['r2', 'e4']           
]

timestamps = lamport_clock(events, [])

for i, ts in enumerate(timestamps):
    print(f"P{i+1} event timestamps: {ts}")
