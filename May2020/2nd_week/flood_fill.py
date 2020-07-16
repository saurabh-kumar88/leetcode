from ctypes import *

class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        self.image = image
        self.newColor = newColor
        self.row = len(image) 
        self.col = len(image[0])  
        self.sr = sr
        self.sc = sc
        self.starting_pixel = image[sr][sc]

        
        return self.changeColor()

    #____________ Helper method __________________
    def changeColor(self):
        image = self.image
        starting_pixel = self.starting_pixel
        print("starting_pixel", starting_pixel)
        # create a dummy copy
        image_copy = [ [False for x in range(self.col)] for x in range(self.row) ] 
        
        #_____________ Mapping coordinates which satisfies condition of 4-directional neighbors _____________

        for i in range(len(image)):
            for j in range(len(image[i])):
                isNeighbor = False
                neighbor_count = 0
                if image[i][j] == starting_pixel:
                    # col underflow
                    if (j - 1) > 0:
                        if image[i][j - 1] == starting_pixel:
                            # image_copy[i][j-1] = True
                            isNeighbor = True
                            neighbor_count += 1 

                    # col overflow
                    if (j + 1) < self.col:
                        if image[i][j + 1] == starting_pixel:
                            # image_copy[i][j+1] = True
                            isNeighbor = True
                            neighbor_count += 1

                    # row underflow
                    if (i - 1) > 0:
                        if image[i -1 ][j] == starting_pixel:
                            # image_copy[i-1][j] = True
                            isNeighbor = True
                            neighbor_count += 1

                    # row overflow
                    if (i + 1) < self.row:
                        if image[i+1][j] == starting_pixel:
                            # image_copy[i+1][j] = True
                            isNeighbor = True
                            neighbor_count += 1
                    
                    if isNeighbor:
                        image_copy[i][j] = True

                    if neighbor_count == 0:
                        image_copy[self.sr][self.sc] = True
                
        
        print(image_copy)

        #________________________  Changing pixles _______________
        for i in range(len(image_copy)):
            for j in range(len(image_copy[i])):
                if image_copy[i][j]:
                    image[i][j] = self.newColor

        return image

    # def changeColor(self, r, c):
    #     prevColor = self.image[r][c]
    #     Solution._row.append(r)
    #     Solution._row.append(c)
    #     if (c - 1) > 0:
    #         if self.image[r][c -1] == prevColor:
    #             self.changeColor(r, c-1)
    #     elif (c + 1) < self.col:
    #         if self.image[r][c+1] == prevColor:
    #             self.changeColor(r, c+1)
    #     elif (r - 1) > 0:
    #         if self.image[r-1][c] == prevColor:
    #             self.changeColor(r-1, c)
    #     elif (r + 1) < self.row:
    #         if self.image[r+1][c] == prevColor:
    #             self.changeColor(r+1, c)
    #     return 
        


arr = [[0,0,0], [0,0,1]]


if __name__ == "__main__":
    obj = Solution()
    print( obj.floodFill(arr, sr=0, sc=0, newColor=2) )

    
        
        

    
    
    


    
        

        
    
     
        


         

    