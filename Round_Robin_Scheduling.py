# create class for process and set info for each process
class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time

# Round Robin Alorithem
def round_robin_scheduling(processes, quantum):
    # create a queue for processes
    queue = []
    # define time with zero value
    time = 0
    while True:
        for process in processes:
            if process.remaining_time > 0:
                if process.remaining_time <= quantum:
                    time += process.remaining_time
                    process.remaining_time = 0
                    print("Processing", process.pid, "at time", time)
                else:
                    time += quantum
                    process.remaining_time -= quantum
                    print("Processing", process.pid, "at time", time)
                if process not in queue and process.remaining_time > 0:
                    queue.append(process)
        # if queue is empty, means we don't have process
        if not queue:
            break
        processes = queue
        # queu became empty for next iteration
        queue = []

if __name__ == "__main__":
    # object of Process class
    p1 = Process(1, 10)
    p2 = Process(2, 5)
    p3 = Process(3, 8)
    processes = [p1, p2, p3]
    quantum = 2
    round_robin_scheduling(processes, quantum)
 