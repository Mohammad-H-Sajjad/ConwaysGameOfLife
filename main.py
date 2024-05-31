gridlyr1 = [".",".",".",".",".",".",".",".",".","."]
gridlyr2 = [".",".",".",".",".",".",".",".",".","."]
gridlyr3 = [".",".",".",".",".",".",".",".",".","."]
gridlyr4 = [".",".",".",".","O",".",".",".",".","."]
gridlyr5 = [".",".",".",".","O",".",".",".",".","."]
gridlyr6 = [".",".",".",".","O",".",".",".",".","."]
gridlyr7 = [".",".",".",".",".",".",".",".",".","."]
gridlyr8 = [".",".",".",".",".",".",".",".",".","."]
gridlyr9 = [".",".",".",".",".",".",".",".",".","."]
gridlyr10 = [".",".",".",".",".",".",".",".",".","."]
grid = [gridlyr1,gridlyr2,gridlyr3,gridlyr4,gridlyr5,gridlyr6,gridlyr7,gridlyr8,gridlyr9,gridlyr10,]

neighborhood = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]

changecell = [[0,0,"."]]

def Printgrid():
  for x in grid:
    print(x) 
  print("top left corner is 0,0\nPress enter to advance generations\nInput coordinates like this to flip cell -> x,y") #print grind one line at a time

def checkforneighbors(x,y):
  aliveneighbors = 0 #set neighbors to zero
  for z in neighborhood:
    if (grid[x+z[0]][y+z[1]] == "O"): #check on all neighbors
      aliveneighbors += 1
  if (aliveneighbors == 3 and grid[x][y] == "."): #Birthing function
      changecell.append([x,y,"O"])
  elif (aliveneighbors == 3  or aliveneighbors == 2 and grid[x][y] == "O"): #survive function
    changecell.append([x,y,"O"])
  elif (grid[x][y] == "O"): changecell.append([x,y,"."])#kill the rest

def checkallcell():
  global changecell
  changecell = [] #what to change

  for a in range(len(grid)):
    for b in range(len(grid[0])):
      if a == 0 or a == len(grid)-1 or b == 0 or b == len(grid[0])-1: #Edges dont get triggered
        continue
      checkforneighbors(a,b) #check the rest

def changeallcells():
  for a in range(len(changecell)): #for every item to change:
    grid[changecell[a][0]][changecell[a][1]] = changecell[a][2] #set X,Y to ITEM

while (True): #game loop
  Printgrid() #print the grid
  advance = input("") #ask if wanting to advance or not
  if advance == (""): #if no numbers
    checkallcell()
    changeallcells()#advance
  else: 
    advance = list(advance) #else, make it a list
    if grid[int(advance[2])][int(advance[0])] == "O":
      grid[int(advance[2])][int(advance[0])] = "."# flip case for "O" state
    else: grid[int(advance[2])][int(advance[0])] = "O"#flip case for "." state