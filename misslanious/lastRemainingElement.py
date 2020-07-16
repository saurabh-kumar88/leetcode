def lastRemainginElement(array):

  while(True):
    if(len(array)==1):
      break
    first_max = max(array)
    array.remove(first_max)
    
    second_max = max(array)
    array.remove(second_max)

    array.append(second_max - first_max)
  
  return array

# driver code
if __name__ == "__main__":
    A = [3,5,2,7]
    print( lastRemainginElement(A) ) 