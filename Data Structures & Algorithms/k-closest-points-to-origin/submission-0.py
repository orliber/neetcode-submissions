class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []

        for i in range(len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappush(dist, (distance, points[i]))

            res = []

        for i in range(k):
            distance, point = heapq.heappop(dist)
            res.append(point)

        return res