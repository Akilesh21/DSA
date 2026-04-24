# in this problem we are going to print all the paths in the maze and we will be backtracking concept here
def printPathhelper(x,y,maze,n,solution):
    if x == n-1 and y == n-1 :
        solution[x][y] = 1
        print(solution)
    if x <0 or y <0 or x>=n or y>=n or maze[x][y] == 0 or solution[x][y] ==1:
        return 
    solution[x][y] = 1
    printPathhelper(x+1,y,maze,n,solution)
    printPathhelper(x,y+1,maze,n,solution)
    printPathhelper(x-1,y,maze,n,solution)
    printPathhelper(x,y-1,maze,n,solution)
    solution[x][y] = 0
    return
def printPath(maze):
    n = len(maze)
    solution = [[0 for j in range(n)]for i in range(n)]
    printPathhelper(0,0,maze,n,solution)
n = int(input())
maze = []
for i in range(n):
    row = [int(ele) for ele in input().split()]
    maze.append(row)
printPath(maze)   