

def surroundingRegions(Matrix):
  
  
  R = len(board)
  if R == 0:
    return
  C = len(Matrix[0])

  ImageMatrix = [[0 for i in range(C) ] for j in range(R)]
  for x in range(R-1):
    for y in range(C-1):
      if x == 0 or x == R-1 or y == 0 or y == C-1:
        pass
      elif board[x][y] == "O":
        if board[x+1][y] == "O" and (x+1 != R-1):
          # update these coordinated of image matrix
          ImageMatrix[x][y] = 1
        if board[x-1][y] == "O" and (x-1 != 0 ):
          # update these coordinated of image matrix
          ImageMatrix[x][y] = 1
        if board[x][y-1] == "O" and (y-1 != 0 ):
          # update these coordinated of image matrix
          ImageMatrix[x][y] = 1
        if board[x][y+1] == "O" and (y+1 != C-1):
          ImageMatrix[x][y] = 1

  for i in range(R):
    for j in range(C):
      if ImageMatrix[i][j] == 1:
        board[i][j] = "X"



# driver code
board = [["O", "O"],
         ["O", "O"]]

if __name__ == "__main__":
    
  surroundingRegions(board)

  print ("Updated board after call to floodFill:") 
  for i in range(len(board)): 
    for j in range(len(board[0])): 
      print(board[i][j], end = ' ') 
    print() 


