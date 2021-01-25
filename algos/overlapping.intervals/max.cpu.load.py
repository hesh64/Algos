from heapq import *

"""
Maximum CPU Load (hard) #
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal 
is to find the maximum CPU load at any time if all the jobs are running on the same machine.

"""


class Job:
    def __init__(self, start, end, load):
        self.start = start
        self.end = end
        self.load = load

    def __lt__(self, other):
        return self.end < other.end


# ok so take the minimum meeting root problem.
# abstract away the concept of having something to measure by from the start
# end values into some other value /
# that's what we are doing here.
# it's the same problem, we are putting into a heap, except that when the heap
# is in correct state, it's gonna hold all active jobs -- kinda like with meetings -- all active meetings
# but we are interested in the cost of those meetings, so doesn't matter how many there are
# just sum up all this load cost
def max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)

    min_heap = []
    max_load = 0
    load = 0
    for job in jobs:
        heappush(min_heap, job)
        load += job.load
        while len(min_heap) and min_heap[0].end <= job.start:
            outjob = heappop(min_heap)
            # we followed this style of var tracking in the sliding window
            # problems.
            load -= outjob.load

        max_load = max(max_load, load)

    return max_load


def main():
    jobs = [Job(s, e, l) for s, e, l in [[1, 4, 3], [2, 5, 4], [7, 9, 6]]]

    result = max_cpu_load(jobs)
    print(result)
    jobs = [Job(s, e, l) for s, e, l in [[1, 4, 2], [2, 4, 1], [3, 6, 5]]]

    result = max_cpu_load(jobs)
    print(result)


main()
