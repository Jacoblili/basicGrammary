class Process:
    def __init__(self, pid, burst_time, priority=0, arrival_time=0):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.started = False

    def __str__(self):
        return f"PID: {self.pid}, Burst Time: {self.burst_time}, Priority: {self.priority}, Arrival Time: {self.arrival_time}"


def fcfs_scheduling(processes):
    print("先来先服务 (FCFS) 调度：")
    # 按到达时间排序，如果到达时间相同，则按执行时间（burst_time）排序
    processes.sort(key=lambda p: (p.arrival_time, p.burst_time))

    time = 0
    for p in processes:
        start_time = max(time, p.arrival_time)
        time = start_time + p.burst_time
        p.completion_time = time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.weighted_turnaround_time = p.turnaround_time / p.burst_time
        print(f"进程 {p.pid}：开始时间 {start_time}，结束时间 {p.completion_time}，周转时间 {p.turnaround_time}，带权周转时间 {p.weighted_turnaround_time:.2f}")

    avg_tat = sum(p.turnaround_time for p in processes) / len(processes)
    avg_wtat = sum(p.weighted_turnaround_time for p in processes) / len(processes)
    print(f"平均周转时间: {avg_tat:.2f}")
    print(f"平均带权周转时间: {avg_wtat:.2f}")

def rr_scheduling(processes, time_quantum):
    # 按到达时间排序，若到达时间相同则按执行时间排序
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))

    print(f"时间片轮转 (RR) 调度，时间片 = {time_quantum}：")
    time = 0  # 当前时间
    queue = []  # 就绪队列
    index = 0  # 当前处理到的进程

    while index < len(processes) or queue:
        # 将所有到达时间 <= 当前时间的进程加入队列
        while index < len(processes) and processes[index].arrival_time <= time:
            queue.append(processes[index])
            index += 1

        if queue:
            # 轮转调度，取队首进程
            p = queue.pop(0)
            # 如果进程从未开始执行过，记录其开始时间
            if not p.started:
                p.started = True
                start_time = max(time, p.arrival_time)  # 进程的开始时间是到达时间和当前时间的最大值
                print(f"进程 p{p.pid}：开始时间 {start_time}")
            else:
                start_time = time  # 后续执行的进程使用当前时间作为开始时间

            # 如果该进程的剩余执行时间大于时间片
            if p.remaining_time > time_quantum:
                time += time_quantum
                p.remaining_time -= time_quantum
                queue.append(p)  # 将进程放回队列末尾
            else:
                # 如果进程执行完毕
                time += p.remaining_time
                p.remaining_time = 0
                p.completion_time = time
                p.turnaround_time = p.completion_time - p.arrival_time
                p.weighted_turnaround_time = p.turnaround_time / p.burst_time
                print(f"进程 p{p.pid}：结束时间 {p.completion_time}")
        else:
            # 如果队列为空，则推进时间，直到下一个进程到达
            time = processes[index].arrival_time

    # 计算并输出平均周转时间和带权周转时间
    avg_tat = sum(p.turnaround_time for p in processes) / len(processes)
    avg_wtat = sum(p.weighted_turnaround_time for p in processes) / len(processes)
    print(f"平均周转时间: {avg_tat:.2f}")
    print(f"平均带权周转时间: {avg_wtat:.2f}")


def non_preemptive_priority_scheduling(processes):
    print("非抢占式优先级调度：")
    processes.sort(key=lambda p: p.priority)

    time = 0
    for p in processes:
        start_time = time
        time += p.burst_time
        p.completion_time = time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.weighted_turnaround_time = p.turnaround_time / p.burst_time
        print(f"进程 {p.pid}：开始时间 {start_time}，结束时间 {p.completion_time}")

    avg_tat = sum(p.turnaround_time for p in processes) / len(processes)
    avg_wtat = sum(p.weighted_turnaround_time for p in processes) / len(processes)
    print(f"平均周转时间: {avg_tat:.2f}")
    print(f"平均带权周转时间: {avg_wtat:.2f}")



def main():
    # 输入进程数
    n = int(input("请输入进程数量："))

    # 输入进程信息
    processes = []
    for i in range(n):
        pid = input(f"请输入第 {i + 1} 个进程的PID：")
        burst_time = int(input(f"请输入进程 {i + 1} 的执行时间："))
        priority = int(input(f"请输入进程 {i + 1} 的优先级（默认为 0）：") or 0)
        arrival_time = int(input(f"请输入进程 {i + 1} 的到达时间（默认为 0）：") or 0)
        processes.append(Process(pid, burst_time, priority, arrival_time))

    # 选择调度算法
    while True:
        print("请选择调度算法：")
        print("1. 先来先服务 (FCFS)")
        print("2. 时间片轮转 (RR)")
        print("3. 非抢占式优先级调度")
        print("4. 退出")

        choice = int(input("请输入您的选择："))

        if choice == 1:
            fcfs_scheduling(processes)
        elif choice == 2:
            time_quantum = int(input("请输入时间片（仅在RR调度算法中使用）："))
            rr_scheduling(processes, time_quantum)
        elif choice == 3:
            non_preemptive_priority_scheduling(processes)
        elif choice == 4:
            break
        else:
            print("无效的选择！")


if __name__ == "__main__":
    main()