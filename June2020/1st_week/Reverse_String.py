
class Solution:
  def reverseString(self, s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    #  base case
    if len(s)==0 or len(s)==1:
      return None
    
    Right_ptr = len(s)-1
    Left_ptr = 0
        
    while(Left_ptr < Right_ptr):    
      if s[Left_ptr] == s[Right_ptr]:
        pass
      else:
        self.swap(s, Left_ptr, Right_ptr)
          
      Left_ptr += 1
      Right_ptr -= 1

  # helper method to swap elements
  def swap(self, A, elem1, elem2):
    A[elem1], A[elem2] = A[elem2], A[elem1]
    return A
        
            
string = ["H","a","n","n","a","h"]
# string = ["h","e","l","l","o"]
# string = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
  
if __name__ == "__main__":
  # obj = Solution()
  # obj.reverseString(string)
  # print(string)

  new_arr =  string[::-1]
  print(new_arr)


  



  

    
  

    
      
   
    


    