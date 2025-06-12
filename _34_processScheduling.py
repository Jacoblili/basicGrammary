import queue


# 定义进程类
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid  # 进程ID
        self.arrival_time = arrival_time  # 到达时间
        self.burst_time = burst_time  # 执行时间（CPU时间）
        self.remaining_time = burst_time  # 剩余执行时间
        self.priority = priority  # 优先级（数值越小，优先级越高）
        self.completion_time = 0  # 完成时间
        self.turnaround_time = 0  # 周转时间
        self.waiting_time = 0  # 等待时间


# 先来先服务调度（FCFS）
def fcfs(processes):
    processes.sort(key=lambda p: p.arrival_time)  # 按照到达时间排序
    time = 0
    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time  # 如果CPU空闲，跳到进程到达时间
        p.waiting_time = time - p.arrival_time  # 计算等待时间
        time += p.burst_time  # 更新当前时间，进程执行完
        p.completion_time = time  # 计算完成时间
        p.turnaround_time = p.completion_time - p.arrival_time  # 计算周转时间
    return processes
# 先来先服务调度（FCFS）：
#
# 按照进程到达时间进行排序。
# 遍历进程，逐个执行，计算每个进程的等待时间、完成时间和周转时间。
# 如果当前时间小于进程的到达时间，则跳到进程的到达时间。

# 时间片轮转调度（Round Robin）
def round_robin(processes, time_slice):
    queue_rr = queue.Queue()  # 使用队列来模拟时间片轮转
    time = 0
    processes_left = len(processes)

    processes.sort(key=lambda p: p.arrival_time)  # 按照到达时间排序

    for p in processes:
        queue_rr.put(p)  # 将进程放入队列

    while not queue_rr.empty():
        p = queue_rr.get()  # 获取队列中的下一个进程
        if p.remaining_time > time_slice:
            time += time_slice
            p.remaining_time -= time_slice  # 执行时间片
            queue_rr.put(p)  # 执行未完成的进程，重新放入队列
        else:
            time += p.remaining_time  # 执行剩余时间
            p.remaining_time = 0
            p.completion_time = time  # 计算完成时间
            p.turnaround_time = p.completion_time - p.arrival_time  # 计算周转时间
            p.waiting_time = p.turnaround_time - p.burst_time  # 计算等待时间
            processes_left -= 1

    return processes
# 时间片轮转调度（Round Robin）：
#
# 使用一个队列模拟时间片轮转。
# 每个进程被分配一个时间片，如果进程执行完，则更新其完成时间；如果进程没有执行完，则将其剩余时间重新放回队列。

# 优先级调度（Priority Scheduling）
def priority_scheduling(processes):
    processes.sort(key=lambda p: (p.arrival_time, p.priority))  # 按照到达时间和优先级排序
    time = 0
    completed_processes = []

    while len(completed_processes) < len(processes):
        ready_queue = [p for p in processes if p.arrival_time <= time and p not in completed_processes]

        if ready_queue:
            # 选择优先级最高的进程（优先级越低的数字优先级越高）
            ready_queue.sort(key=lambda p: p.priority)
            p = ready_queue[0]
            p.completion_time = time + p.burst_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            completed_processes.append(p)
            time += p.burst_time
        else:
            time += 1  # 如果没有进程就空转1个时间单位

    return completed_processes
# 优先级调度（Priority Scheduling）：
#
# 按照进程到达时间和优先级排序。
# 在所有到达并未执行的进程中，选择优先级最高的进程（优先级数值最小）。
# 执行完后，计算其周转时间和等待时间

# 打印进程调度信息
def print_process_info(processes):
    print(
        f"{'PID':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Priority':<10}{'Completion Time':<20}{'Turnaround Time':<20}{'Waiting Time':<15}")
    for p in processes:
        print(
            f"{p.pid:<10}{p.arrival_time:<15}{p.burst_time:<15}{p.priority:<10}{p.completion_time:<20}{p.turnaround_time:<20}{p.waiting_time:<15}")


# 主函数，测试不同调度算法
if __name__ == "__main__":
    # 创建进程列表
    processes = [
        Process(pid=1, arrival_time=0, burst_time=5, priority=2),
        Process(pid=2, arrival_time=1, burst_time=3, priority=1),
        Process(pid=3, arrival_time=2, burst_time=8, priority=3),
        Process(pid=4, arrival_time=3, burst_time=6, priority=2),
        Process(pid=5, arrival_time=4, burst_time=2, priority=4)
    ]

    # 先来先服务调度（FCFS）
    print("FCFS Scheduling:")
    fcfs_processes = fcfs(processes.copy())
    print_process_info(fcfs_processes)
    print("\n")

    # 时间片轮转调度（Round Robin）
    print("Round Robin Scheduling (Time slice = 3):")
    rr_processes = round_robin(processes.copy(), time_slice=3)
    print_process_info(rr_processes)
    print("\n")

    # 优先级调度（Priority Scheduling）
    print("Priority Scheduling:")
    priority_processes = priority_scheduling(processes.copy())
    print_process_info(priority_processes)
