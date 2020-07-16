from functools import reduce

num = 10

arr = [4,14,65,46,31,26]

def cal_square(n):
    return n*n

def cal_ascii(char):
    return ord(char)



class FoodItems(object):
    COUNT = 0
    def __init__(self, name, isVagitarian):
        self.name = name
        self.isVagitarian = False
        FoodItems.COUNT += 1




if __name__ == "__main__":

    # print("Original : ", arr)
    # data = map(cal_square, arr)
    # print("map : ", list(data) )
    
    # result_ascii = map(cal_ascii, "We can also use lambda expressions with map to achieve above result.")
    # print("map : ",  list(result_ascii) )

    # print("reduce with lambda : ", reduce(lambda x,y : x+y, arr))

    food = FoodItems("Ham burger", isVagitarian = False )
    food = FoodItems("Salad", isVagitarian = True )
    food = FoodItems("Chicked Chowmin", isVagitarian = False )
    food = FoodItems("Samosa", isVagitarian = True )

    print( food.name, food.isVagitarian )

    # print( "lambda filter : ", list(filter( lambda x : (x is True), food.isVagitarian ))  )

