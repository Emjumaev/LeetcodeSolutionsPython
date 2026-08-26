class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            hashSet = set()
            for j in range(0, 9):
                if board[i][j] != "." and board[i][j] in hashSet:
                    return False
                else:
                    hashSet.add(board[i][j])

        for j in range(0, 9):
            hashSet = set()
            for i in range(0, 9):
                if board[i][j] != "." and board[i][j] in hashSet:
                    return False
                else:
                    hashSet.add(board[i][j])

        i = 0
        while(i < 9):
            j = 0
            while(j < 9):
                hashSet = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] != "." and board[k][l] in hashSet:
                            return False
                        else:
                            hashSet.add(board[k][l])
                j += 3
            i += 3

        return True
