board = [
    [7,0,0,0,2,5,0,0,0],
    [0,0,8,9,0,4,2,0,7],
    [0,3,0,0,8,1,0,0,0],
    [6,0,1,0,0,0,8,5,0],
    [0,0,0,0,0,0,0,0,0],
    [0,8,4,0,0,0,3,0,2],
    [0,0,0,2,5,0,0,3,0],
    [4,0,2,3,0,7,9,0,0],
    [0,0,0,1,4,0,0,0,5]
]


def print_board(bd):
    for i in range(len(bd)): #rows
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for w in range(len(bd[i])): # columns
            if w % 3 == 0 and w != 0:
                print(" | ", end = "")
            
            if w != 8:
                print(bd[i][w], end = " ")
            else:
                print(bd[i][w])

def find_empty(bd):
    for i in range(len(bd)):
        for w in range(len(bd[i])):
            if bd[i][w] == 0:
                return (i,w) #row, column
    return False

def valid(bd, num, pos):
    #pos = (row, column)
    #row
    for i in range(len(bd[pos[0]])):
        if num == bd[pos[0]][i] and pos[1] != i:
            return False
    #column
    for i in range(len(bd)):
        if num == bd[i][pos[1]] and pos[0] != i:
            return False
    #square
    r, c = pos
    box_x = c // 3
    box_y = r // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for w in range(box_x * 3, box_x * 3 + 3):
            if num == bd[i][w] and (i,w) != pos:
                return False
    
    return True

def solve(bd):
    find = find_empty(bd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bd, i, (row, col)):
            bd[row][col] = i

            if solve(bd):
                return True
            bd[row][col] = 0
    return False




print_board(board)
solve(board)
print("________________")
print_board(board)