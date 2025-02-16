# Input : Processes along with their burst time (bt).
# Output : Waiting time, turnaround time for all processes.

############################################################


# First Step---> Find Waiting time 
def findWaitingTime(processes ,  n , bt , wt):
    # wating time for first process is always zero 
    wt[0] = 0 
    # calculate waiting time
    for i in range(1, n):
        wt[i] = bt[i-1] + wt[i-1]

# Second step---> Find Turn Around Time 
def findTurnAroundTime(processes, n , bt, wt , tat):
    # calculate tat
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    
# third step----> Find Average time and Turn Around Time
def findAverageTime(processes , n , bt ):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0 
    
    findWaitingTime(processes , n , bt , wt )
    findTurnAroundTime(processes , n , bt , wt , tat)
    
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" + 
                    str(bt[i]) + "\t " + 
                    str(wt[i]) + "\t\t " + 
                    str(tat[i]))
    
    print("Average Waiting Time :" , total_wt/n )
    print("Average Turn Around Time :", total_tat/n)
    
# Driver code 

if __name__ == "__main__":
    processes = [1,2,3]
    n= len(processes)
    
    brust_time = [10, 5, 8]
    
    findAverageTime(processes , n , brust_time)














# steps:
# As first process that comes need not to wait so waiting time for process 1 will be 0 i.e. wt[0] = 0.
# Find waiting time for all other processes i.e. for process i:
# wt[i] = bt[i-1] + wt[i-1] .
# Find turnaround time = waiting_time + burst_time for all processes.
# Find average waiting time = total_waiting_time / no_of_processes.
# Similarly, find average turnaround time = total_turn_around_time / no_of_processes