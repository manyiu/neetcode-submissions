class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)] 
        column_check = [set() for _ in range(9)]
        box_check = [[set() for _ in range(3)] for _ in range(3)]

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue

                if cell in row_check[i] or cell in column_check[j] or cell in box_check[i // 3][j // 3]:
                    return False
                
                row_check[i].add(cell)
                column_check[j].add(cell)
                box_check[i // 3][j // 3].add(cell)


        return True