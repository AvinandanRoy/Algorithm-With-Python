

def findWaitingTime(processes , n , bt , wt ):
    wt[0] = 0 
    
    for i in range(1 , n):
        wt[i] = bt[i-1] + wt[i-1]

def findTurnAroundTime(processes , n , bt , wt , tat):
    
    for i in range(n):
        tat[i] = bt[i] + wt[i]
        
def findAverageTime(processes , n , bt ):
    
    wt = [0]*n
    tat = [0]*n
    
    total_wt = 0 
    total_tat = 0 
    
    findWaitingTime(processes, n , bt , wt )
    findTurnAroundTime(processes , n, bt, wt , tat )
    
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
    
    print("Average Waiting Time :", total_wt / n )
    print("AAverage Turn Around Time : ", total_tat / n)
    
def userInput():
    processes = []
    brust_time = []

    n = int(input("Enter The Number of Processes : "))

    for i in range(n):
        process_no = int(input("Enter the process number consequently : "))
        processes.append(process_no)

    for i in range(n):
        brust_time_per_process = int(input("Enter the p-{i}'s brust time : "))
        brust_time.append(brust_time_per_process)

    findAverageTime(processes , n , brust_time)

userInput()
    