def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print()


def check_winner(board):
    lines = []
    lines.extend(board)
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0]
    return None


def board_full(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter row and column (1-3 separated by space): ").strip().split()
            if len(move) != 2:
                print("Please enter two numbers.")
                continue
            row, col = int(move[0]) - 1, int(move[1]) - 1
            if row not in range(3) or col not in range(3):
                print("Row and column must be between 1 and 3.")
                continue
            if board[row][col] != " ":
                print("That cell is already taken.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Enter numeric values.")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player, board)
        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if board_full(board):
            print_board(board)
            print("The game is a draw.")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
