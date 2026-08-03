class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        heap = [(-1, i) for i in range(n)]
        numMeetings = [0]*n
        for start, meetEnd in meetings:
            if heap[0][0] <= start:
                openRooms = {}
                minRoom = n
                while heap and heap[0][0] <= start:
                    end, room = heapq.heappop(heap)
                    minRoom = min(room, minRoom)
                    openRooms[room] = end
                numMeetings[minRoom] += 1
                heapq.heappush(heap, (meetEnd, minRoom))
                openRooms.pop(minRoom)
                for room, end in openRooms.items():
                    heapq.heappush(heap, (end, room))
            else:
                roomEnd, room = heapq.heappop(heap)
                numMeetings[room] += 1
                heapq.heappush(heap, (roomEnd + meetEnd - start, room))                

        return numMeetings.index(max(numMeetings))