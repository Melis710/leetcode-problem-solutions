import heapq
# time complexity: O(N*logN)
# space complexity: O(1) if in-place like here, O(N) with new array allocation
def minCostToConnectSticks(sticks: list) -> int:
    if len(sticks) <= 1:
        return 0

    total_cost = 0
    heapq.heapify(sticks)

    while len(sticks) >= 2:
        min_stick1 = heapq.heappop(sticks)
        min_stick2 = heapq.heappop(sticks)

        cost = min_stick1 + min_stick2

        total_cost += cost
        heapq.heappush(sticks, cost)
       
    return total_cost

print(minCostToConnectSticks([5]))
# if the input list was given already in sorted order, it would be possible to solve in O(N) time using two Queues 