class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    box = (r // 3) * 3 + c // 3

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def backtrack():

            if not empty:
                return True

            best = -1
            best_options = None

            for i in range(len(empty)):

                r, c = empty[i]
                box = (r // 3) * 3 + c // 3

                options = []

                for num in "123456789":
                    if (num not in rows[r] and
                        num not in cols[c] and
                        num not in boxes[box]):
                        options.append(num)

                if best_options is None or len(options) < len(best_options):
                    best = i
                    best_options = options

            r, c = empty.pop(best)
            box = (r // 3) * 3 + c // 3

            for num in best_options:

                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if backtrack():
                    return True

                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            empty.append((r, c))

            return False

        backtrack()