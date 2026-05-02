class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        condition1 = condition2 = condition3 = False
        
        # --- Condition 1: Check Rows ---
        for row in board:
            row_dict = {}
            for char in row:
                if char != '.':
                    # Using .get() prevents KeyError if the number isn't in the dict yet
                    row_dict[char] = row_dict.get(char, 0) + 1
                    if row_dict[char] > 1:
                        return False
        condition1 = True

        # --- Condition 2: Check Columns ---
        for c in range(9):
            col_dict = {}
            for r in range(9):
                char = board[r][c]
                if char != '.':
                    col_dict[char] = col_dict.get(char, 0) + 1
                    if col_dict[char] > 1:
                        return False
        condition2 = True

        # --- Condition 3: Check 3x3 Sub-boxes ---
        # We jump by 3 to get the top-left corner of each square
        for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
                box_dict = {}
                for r in range(r_start, r_start + 3):
                    for c in range(c_start, c_start + 3):
                        char = board[r][c]
                        if char != '.':
                            box_dict[char] = box_dict.get(char, 0) + 1
                            if box_dict[char] > 1:
                                return False
        condition3 = True

        return condition1 and condition2 and condition3