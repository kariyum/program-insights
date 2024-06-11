import json

f = open("duration.json")
payload = json.load(f)
f.close()

startEndTimes = payload["startEndTime"]

# check if there are some calls are running in parallel
def checkParallelism(arr):
    # sort by start_time
    # check if there is an occurence of start_time < end_time
    sorted_arr = sorted(arr, key= lambda x : x[0])
    parallel_execution = 0
    for a, b in zip(sorted_arr, sorted_arr[1:]):
        if (a[1] > b[0]):
            parallel_execution += 1
            print((a[1] - a[0]) / 1000)
    print(f"Parallel execution: {parallel_execution}")
    duration = sum(x[1] - x[0] for x in startEndTimes)
    print(f"Execution duration: {duration/1000000}s")


def plot_normal_distribution(arr):
    import matplotlib.pyplot as plt
    # Create a histogram
    execution_times = [x[1] - x[0] for x in arr]
    plt.hist(execution_times, bins=1000, edgecolor='black', alpha=0.7)
    plt.xlabel('Execution Time (ms)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Function Execution Times')
    plt.grid(True)
    plt.show()
    
def plot_seaborn(arr):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    # Apply log transformation
    execution_times = [x[1] - x[0] for x in arr]
    log_execution_times = [et for et in execution_times]

    # Create a KDE plot
    sns.kdeplot(log_execution_times, fill=True, color='skyblue', label='KDE')
    plt.xlabel('Log Execution Time (ln(ms))')
    plt.ylabel('Density')
    plt.title('Kernel Density Estimation of Execution Times')
    plt.grid(True)
    plt.legend()
    plt.show()
    
if __name__ == '__main__':
    # execution_times = [(x[1] - x[0])/1e6 for x in startEndTimes]
    # sorted_execution_times = sorted(execution_times, reverse=True)
    # print(sorted_execution_times[:50])
    # import time
    # start_time = time.perf_counter()
    # for i in range(5000):
    #     for j in range(5000):
    #         continue
    # print(time.perf_counter() - start_time)
    l = [[10, 11], [12, 19], [14, 20]]
    buckets = [l[0]]
    for (startTime, endTime) in l[1:]:
        added = False
        for i in range(len(buckets)):
            (bucket_start, bucket_end) = buckets[i]
            if (startTime <= bucket_end): 
                buckets[i][1] = max(bucket_end, endTime)
                added = True
        if not added: buckets.append([startTime, endTime])

    print(buckets)
            