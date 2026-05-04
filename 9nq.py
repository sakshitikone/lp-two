class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.cols = set()
        self.diag1 = set()
        self.diag2 = set()

    def solve(self, row=0, board=None):
        if board is None:
            board = []
        if row == self.n:
            self.solutions.append(board[:])
            return
        for col in range(self.n):
            if col in self.cols or (row - col) in self.diag1 or (row + col) in self.diag2:
                continue
            self.cols.add(col); self.diag1.add(row - col); self.diag2.add(row + col)
            board.append(col)
            self.solve(row + 1, board)
            board.pop()
            self.cols.remove(col); self.diag1.remove(row - col); self.diag2.remove(row + col)

    def print_board(self, solution):
        for r in range(self.n):
            print(" ".join("Q" if solution[r] == c else "." for c in range(self.n)))
        print()


n = int(input("Enter value of N: "))

solver = NQueens(n)
solver.solve()

print(f"Total solutions for {n}-Queens: {len(solver.solutions)}")

if solver.solutions:
    print("First Solution:")
    solver.print_board(solver.solutions[0])
