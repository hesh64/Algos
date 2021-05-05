def visit_times(task_times):
    task_range = range(task_times[0][0], task_times[0][1])

    count = 1
    for task in task_times:
        if task[0] not in task_range:
            task_range = range(task[0], task[1])
            count += 1

    return count


print(visit_times([[0, 3], [2, 6], [3, 4], [6, 9]]))
