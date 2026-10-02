class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        maxHeap = stones
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap) * -1
            stone2 = heapq.heappop(maxHeap) * -1
            value = abs(stone1 - stone2)
            if stone1 != stone2:
                heapq.heappush(maxHeap, value * -1)
            
        if len(maxHeap) == 1:
            return maxHeap[0] * -1

        return 0