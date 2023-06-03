# create class for process and set info for each process
class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
 
 
def priority_scheduling(processes):
    # sort process based on priority
    sorted_processes = sorted(processes, key=lambda p: p.priority, reverse=True)
    # define time with zero value
    time = 0
    for process in sorted_processes:
        print("Processing", process.pid, "at time", time)
        time += process.burst_time
        print("Process", process.pid, "completed at time", time)

if __name__ == "__main__":
    # object of Process class
    p1 = Process(1, 10, 2)
    p2 = Process(2, 5, 1)
    p3 = Process(3, 8, 3)
    processes = [p1, p2, p3]
    priority_scheduling(processes)