import random
class RandomizedSet:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.Data = { -89:True, 23:True, 13:True, 40:True, 56:True, 96:True }
    
      

  def insert(self, val: int) -> bool:
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    """
    if val not in self.Data.keys():
      self.Data[val] = True
      return True
    else:
      return False
      

  def remove(self, val: int) -> bool:
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    """
    if val in self.Data.keys():
      del self.Data[val]
      return True
    else:
      return False
      
      

  def getRandom(self) -> int:
    """
    Get a random element from the set.
    """
    return  random.choice( list(self.Data.keys()) )
        


# Your RandomizedSet object will be instantiated and called as such:


if __name__ == "__main__":
  obj = RandomizedSet()
  print( obj.insert(-89) )
  print(obj.Data)

  # print( obj.remove(40) ) 
  # print(obj.Data)
  
  # while(True):
  #   print(obj.getRandom(), end=" ")

  

  

  

  




  