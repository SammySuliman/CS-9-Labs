from Stack import Stack

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

def solveMaze(maze, startX, startY):
    s = Stack()
    counter = 1
    s.push([startX, startY])
    maze[startX][startY] = counter
    t = [startX, startY]
    while maze[t[0]][t[1]] != 'G':
        printMaze(maze)
        print('\n')
        print(s.peek())
        t = s.peek()
        if maze[t[0] - 1][t[1]] != ' ':
            print('not north')
            if maze[t[0] - 1][t[1]] == 'G':
                return True
            if maze[t[0]][t[1] + 1] != ' ':
                print('not east')
                if maze[t[0]][t[1] + 1] == 'G':
                    return True
                if maze[t[0] + 1][t[1]] != ' ':
                    print('not south')
                    if maze[t[0] + 1][t[1]] == 'G':
                        return True
                    if maze[t[0]][t[1] - 1] != ' ':
                        print('not west')
                        if maze[t[0]][t[1] - 1] == 'G':
                            return True
                        s.pop()
                        if s.isEmpty() == True:
                            return False
                        t = s.peek()
                    else:
                        s.push([t[0], t[1] - 1])
                        counter += 1
                        maze[t[0]][t[1] - 1] = counter
                        print('west')
                else:
                    s.push([t[0] + 1, t[1]])
                    counter += 1
                    maze[t[0] + 1][t[1]] = counter
                    print('south')
            else:
                s.push([t[0], t[1] + 1])
                counter += 1
                maze[t[0]][t[1] + 1] = counter
                print('east')
        else:
            s.push([t[0] - 1, t[1]])
            counter += 1
            maze[t[0] - 1][t[1]] = counter
            print('north')

