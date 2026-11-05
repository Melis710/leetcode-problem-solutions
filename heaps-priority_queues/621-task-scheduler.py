import heapq
from collections import deque
class Solution:
    # Max Heap & Queue solution
    # max heap used as Ready Queue, deque used as Waiting Queue
    # max heap to consume max frequent task
    # queue used as waiting queue storing tasks with their availability time

    # time complexity: O(T) where T is time and N (len(tasks)) <= T
    # space complexity: O(1), only 26 uppercase English letters 
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # create frequency map
        freq_map = dict()
        for task in tasks:
            freq_map[task] = freq_map.get(task, 0) + 1

        # create max heap (ready queue) based on frequencies
        max_heap = [-freq for freq in freq_map.values()]  # ready queue
        heapq.heapify(max_heap)

        # create a waiting queue 
        waiting_queue = deque()
        time = 0

        while max_heap or waiting_queue:
            time += 1
            # if any available tasks
            if max_heap:
                remaining = heapq.heappop(max_heap) + 1  # decrement remaining count (since negative we add 1)
                if remaining:  # if same task left, append it to waiting queue
                    waiting_queue.append((remaining, time + n))
            # if any tasks become available again, add it to ready queue
            if waiting_queue and waiting_queue[0][1] == time:
                heapq.heappush(max_heap, waiting_queue.popleft()[0])

        return time

from collections import Counter
class Solution:
    # Mathematical Greedy Solution
    # time complexity: O(N)
    # space complexity: O(1)
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # 1. Count task frequencies (Time: O(N))
        counts = Counter(tasks)
        
        # 2. Find the maximum frequency among all tasks (Time: O(26) -> O(1))
        max_freq = max(counts.values())
        
        # 3. Count how many tasks share this maximum frequency
        max_freq_count = sum(1 for v in counts.values() if v == max_freq)
        
        # 4. Apply the greedy framing formula:
        # (max_freq - 1) * (n + 1) covers full blocks including cooldown slots,
        # + max_freq_count appends the final occurrences of the most frequent tasks
        calculated_time = (max_freq - 1) * (n + 1) + max_freq_count
        
        # 5. If tasks exceed available slots, no idle time is needed
        return max(len(tasks), calculated_time)