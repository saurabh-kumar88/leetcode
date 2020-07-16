import copy


def rotLeft(arr, d):
  n = len(arr) - 1

  for j in range(d):
    temp = arr[0]
    for i in range(n):
      arr[i] = arr[i+1]
    arr[n] = temp
  
  return arr

# Juggling algorithm

def RoteLeft(arr, d):
  n  = len(arr)
  # d = d % n # to handel if d >= n 
  
  # gcd = getHCF(n,d)
  gcd = getGCD(n,d)
  # print(gcd)

  for i in range(gcd-1):
    temp = arr[i] # move i-th values of blocks to temp variable
    j = i 
    
    while(1):
      k = j + d

      if(k >= n):
        k = k - n

      # break out case
      if(k == i):
        break
      arr[j] = arr[k]
      j = k
    arr[j] = temp
  
  return arr
      
def getHCF(a, b):
   
  minimum = min(a,b)

  if(a%minimum == 0 and b%minimum==0):
    return minimum
  
  for i in range(minimum//2, 1, -1):
    if(a%i==0 and b%i==0):
      return i
    
    # default
  return 1

def getGCD(a, b):
  if(b == 0):
    return a
  else:
    return getGCD(b, a % b)




arr = [1,2,3,4,5,6]

if __name__ == "__main__":
    
    print("basic   ",  rotLeft(arr, 1) )
    # print(getHCF(12,5))
    print("advance ", RoteLeft(arr, 1) )
    
    

    
    