class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)
        print(n)
        row = { i : set() for i in range(n)}
        column = { i : set() for i in range(n)}
        grid = { (i//3,j//3) : set() for i in range(n) for j in range(n)}


        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i].add(board[i][j])

                    if board[i][j] in column[j]:
                        return False
                    else:
                        column[j].add(board[i][j])

                    if board[i][j] in grid[(i//3,j//3)]:
                        return False
                    else:
                        grid[(i//3,j//3)].add(board[i][j])

        print(row,column,grid)
        return True





        