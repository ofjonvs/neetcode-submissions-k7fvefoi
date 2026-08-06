class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        heapq.heapify(tasks)
        time = 0
        procOrder = []
        availableTasks = []
        while tasks or availableTasks:

            while tasks and (time >= tasks[0][0] or not availableTasks):
                task = heapq.heappop(tasks)
                heapq.heappush(availableTasks, (task[1], task[2], task[0]))
            task = heapq.heappop(availableTasks)
            procOrder.append(task[1])
            time = max(time, task[2]) + task[0]
        
        return procOrder