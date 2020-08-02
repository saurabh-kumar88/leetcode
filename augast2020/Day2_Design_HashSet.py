class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Map = {}
        

    def add(self, key: int) -> None:
        if not key in self.Map.keys():
            self.Map[key] = key
            
    def remove(self, key: int) -> None:
        if key in self.Map.keys():
            del self.Map[key]
            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.Map.keys():
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)