# 单标志法
"""

int turn = 0;
P0 进程：                        P1 进程：
while (turn != 0);              while (turn != 1); // 进入区
critical section;               critical section;  // 临界区
turn = 1;                       turn = 0;		   // 退出区
remainder section;              remainder section; // 剩余区


"""
# 互斥锁
# acquire();
# release();