import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x450")
        self.window.resizable(False, False)

        # Initialize board and player
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # Player always starts as 'X'

        # Create GUI elements
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

        self.window.mainloop()

    def create_board(self):
        """Creates the Tic Tac Toe grid and a restart button."""
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=("Arial", 20),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.player_move(row, col),
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        # Restart button
        restart_btn = tk.Button(
            self.window,
            text="Restart Game",
            font=("Arial", 12),
            command=self.reset_game,
        )
        restart_btn.grid(row=3, column=0, columnspan=3, pady=10)

    def player_move(self, row, col):
        """Handles player's move."""
        if self.board[row][col] == "" and self.current_player == "X":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state="disabled")
            if self.check_winner("X"):
                messagebox.showinfo("Game Over", "You win!")
                self.disable_all_buttons()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_all_buttons()
            else:
                self.current_player = "O"
                self.computer_move()

    def computer_move(self):
        """Handles computer's move using the Minimax algorithm."""
        best_score = float("-inf")
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", state="disabled")
            if self.check_winner("O"):
                messagebox.showinfo("Game Over", "Computer wins!")
                self.disable_all_buttons()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_all_buttons()
            else:
                self.current_player = "X"

    def minimax(self, board, depth, is_maximizing):
        """Minimax algorithm for AI decision-making."""
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        """Checks if a player has won."""
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(
                self.board[j][i] == player for j in range(3)
            ):
                return True
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False

    def is_draw(self):
        """Checks if the game is a draw."""
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def disable_all_buttons(self):
        """Disables all buttons after the game ends."""
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

    def reset_game(self):
        """Resets the game board."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")


if __name__ == "__main__":
    TicTacToe()