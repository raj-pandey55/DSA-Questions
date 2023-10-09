#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (58.64%)
# Likes:    9776
# Dislikes: 1009
# Total Accepted:    1.3M
# Total Submissions: 2.1M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# 
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
# 
# 
# Note:
# 
# 
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
# 
# 
# 
# Example 1:
# 
# 
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
# is invalid.
# 
# 
# 
# Constraints:
# 
# 
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
# 
# 
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(row,col):
            duprow,dupcol=row,col
            duprow+=1
            while(duprow<9):
                
                if(board[row][col]==board[duprow][col]):
                    return False
                duprow+=1
                

            duprow,dupcol=row,col
            duprow-=1
            while(duprow>=0):
                
                if(board[row][col]==board[duprow][col]):
                    return False
                duprow-=1
                

            duprow,dupcol=row,col
            dupcol+=1
            while(dupcol<9):
                
                if(board[row][col]==board[row][dupcol]):
                    return False
                dupcol+=1
        

            duprow,dupcol=row,col
            dupcol-=1
            while(dupcol>=0):
                
                if(board[row][col]==board[row][dupcol]):
                    return False
                dupcol-=1
                

            if(row>=0 and row<=2):
                duprow = 0
            elif(row>=3 and row<=5):
                duprow = 3
            else:
                duprow = 6
            
            if(col>=0 and col<=2):
                dupcol = 0
            elif(col>=3 and col<=5):
                dupcol = 3
            else:
                dupcol = 6
            
            x = dupcol 

            countRow = 0
            countCol = 0
            while(countRow<3):
                countCol = 0
                x = dupcol
                while(countCol<3):
                    if(duprow == row and x == col):
                        countCol+=1
                        x+=1
                        continue
                    if(board[row][col]==board[duprow][x]):
                        return False
                    countCol+=1
                    x+=1
                countRow+=1
                duprow+=1

            return True
            

            
        row=0
        col=0
        while(col<9):
            
            if(board[row][col]!='.' and check(row,col) == False):
                
                return False


            if(row==8):
                row=-1
                col+=1

            row+=1

        return True
        
# @lc code=end

