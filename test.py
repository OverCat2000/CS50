import copy
import math

EMPTY = None

# arr =  [["X", "X", EMPTY],
#         ["O", "X", "X"],
#         ["O", EMPTY, "O"]]

# arr = [["O", EMPTY, EMPTY],
#          ["X", "O", "X"],
#          ["O", EMPTY, "X"]]
arr = [["X", "O", "X"],
       [EMPTY, "O", EMPTY],
       ["X", EMPTY, EMPTY]]



def player(board):
    xcount = 0
    ocount = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == "X"):
                xcount += 1
            if (board[i][j] =="O"):
                ocount += 1
    if (xcount > ocount):
        return "O"
    elif (xcount == ocount):
        return "X"

def actions(board):
    acts = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == None):
                temp = (i, j)
                acts.add(temp)
    return acts

def terminal(board):
    for i in range(len(board)):
        if (set(board[i]) == {"X"} or set(board[i]) == {"O"}):
            return True
        
    for i in range(len(board)):
        temp = set()
        for j in range(len(board[i])):
            temp.add(board[j][i])
        if (temp == {"X"} or temp == {"O"}):
            return True
        
    temp1 = set()
    temp2 = set()
    allFilled = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i == j):
                temp1.add(board[i][j])
            if ((i + j) == 2):
                temp2.add(board[i][j])
            if (board[i][j] == None):
                allFilled = False
    if (temp1 == {"X"} or temp1 == {"O"}):
        return True
    if (temp2 == {"X"} or temp2 == {"O"}):
        return True

    return allFilled

def utility(board):
    if (terminal(board) == True):
        for i in range(len(board)):
            if (set(board[i]) == {"X"}):
                return 1
            if (set(board[i]) == {"O"}):
                return -1
            
        for i in range(len(board)):
            temp = set()
            for j in range(len(board[i])):
                temp.add(board[j][i])
            if (temp == {"X"}):
                return 1
            if (temp == {"O"}):
                return -1
            
        temp1 = set()
        temp2 = set()
        allFilled = True
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i == j):
                    temp1.add(board[i][j])
                if ((i + j) == 2):
                    temp2.add(board[i][j])
                if (board[i][j] == None):
                    allFilled = False
        if (temp1 == {"X"} or temp2 == {"X"}):
            return 1
        if (temp1 == {"O"} or temp2 == {"O"}):
            return -1

        if (allFilled):
            return 0
        

def result(board, action):
    boardCopy = copy.deepcopy(board)
    s = player(boardCopy)

    if (s == "X"):
        boardCopy[action[0]][action[1]] = "X"
    elif (s == "O"):
        boardCopy[action[0]][action[1]] = "O"

    return boardCopy



def minimax(board):
    def maxValue(board):
        if (terminal(board)):
            if (utility(board) == None):
                print("alert")
                print(board)
            return utility(board), ()
        value = []
        moves = []
        for i in actions(board):
            temp = result(board, i)
            score = minValue(temp)[0]
            value.append(score)
            moves.append(i)
            # if (score > v):
            #     v = score
        print(value)
        v = max(value)
        m = moves[value.index(v)]
        return v, m


    def minValue(board):
        if (terminal(board)):
            if (utility(board) == None):
                print("alert")
                print(board)
            return utility(board), ()
        value = []
        moves = []
        for i in actions(board):
            temp = result(board, i)
            score = maxValue(temp)[0]
            value.append(score)
            moves.append(i)
        print(value)
        v = min(value)
        m = moves[value.index(v)]
        return v, m
    
    if (player(board) == "X"):
        v = maxValue(board)
    elif (player(board) == "O"):
        v = minValue(board)
    print("hell")
    return v[1]

        

print(minimax(arr))

