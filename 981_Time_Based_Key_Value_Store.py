class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append((timestamp, value))
        else:
            self.hashMap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""

        arr = self.hashMap[key]
        res = ""

        left = 0
        right = len(arr) - 1

        while(left <= right):
            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                left = mid + 1
                res = arr[mid][1]
            else:
                right = mid - 1

        return res

"""
Time: O(log n)
Space: O(nm)
"""
