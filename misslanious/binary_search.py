import random
nums = [-1,0,3,5,9,12]

def bs(arr, sub):

    l = 0
    r = len(arr) -1 

    while l <= r:
        mid = l + (r - l)//2
        
        if sub == arr[mid]:
            return arr.index(mid)
        elif sub > arr[mid]  :
            l = mid + 1
        elif sub < arr[mid]:
            r = mid - 1
    return -1

def gen_array():
    array = set([])
    for i in range(0, 99):
        array.add(random.randint(-99, 99))

    arr = []
    for i in array:
        arr.append(i)
    
    arr.sort()
    return arr


if __name__ == "__main__":
    # arr = gen_array()
    # print(arr)

    result = bs(nums , 2)
    print( result )
     
    
    
        