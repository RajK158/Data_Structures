# Problem: Time Based Key-Value Store
# Pattern: HashMap + Binary Search
# Time:
# set -> O(1)
# get -> O(log n)
# Space: O(n)

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""

        values = self.store[key]

        l, r = 0, len(values) - 1
        res = ""

        while l <= r:

            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1

            else:
                r = mid - 1

        return res


if __name__ == "__main__":

    timeMap = TimeMap()

    timeMap.set("alice", "happy", 1)

    print(timeMap.get("alice", 1))  # happy
    print(timeMap.get("alice", 2))  # happy

    timeMap.set("alice", "sad", 3)

    print(timeMap.get("alice", 3))  # sad
    print(timeMap.get("alice", 0))  # ""