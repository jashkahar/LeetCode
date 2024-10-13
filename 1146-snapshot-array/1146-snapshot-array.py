class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.data = [{} for _ in range(length)]  # Each element is a dictionary of changes

    def set(self, index: int, val: int) -> None:
        # Store the value with the current snap_id
        self.data[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # If the snap_id exists, return it; else search for the nearest smaller snap_id
        while snap_id >= 0:
            if snap_id in self.data[index]:
                return self.data[index][snap_id]
            snap_id -= 1
        return 0  # Return 0 if no previous value is found

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)