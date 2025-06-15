# game.py
# Simple logic for the Tic-Tac-Toe game environment.

import numpy as np

class TicTacToe:
    """
    This class will represent the game environment and rules in one
    """
    def __init__(self):
        """
        This constructor will initialize the board as a 3x3 grid of zeros where
        0 represents an empty cell
        1 represents player X'
        -1 represent player 'O'
        """
        self.board = np.zeros((3,3))
        self.winner = None

    def get_available_actions(self):
        """
        Returns an array of 2 tuples
        each tuple contains the row and column of an empty space
        ex: [(0, 0), (0, 1)] represents the first two top left spaces being empty
        """
        return list(zip(*np.where(self.board == 0)))
    
    def is_game_over(self):
        # Checks for horizontal win
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3:
                self.winner = self.board[i, 0]
                return True
        
        # Checks for vertical win
        for i in range(3):
            if abs(sum(self.board[:, i])) == 3:
                self.winner = self.board[0, i]
                return True
            
        # Checks for horizontal win
        diag1 = self.board[0, 0] + self.board[1, 1] + self.board[2, 2]
        diag2 = self.board[2, 0] + self.board[1, 1] + self.board[0, 2]

        if abs(diag1) == 3 or abs(diag2) == 3:
            self.winner = self.board[1, 1]
            return True
        
        # Checks for draw
        if len(self.get_available_actions()) == 0:
            self.winner = 0
            return True
        
        #If none of the above, the game is still going
        return False
    
    def make_move(self, action, player):
        if self.board[action] == 0:
            self.board[action] = player
            return True
        return False # Move was invalid
    
    def print_board(self):
        """
        Prints a human-readable version of the board.
        """
        print("-------------")
        for row in self.board:
            row_str = "| "
            for cell in row:
                if cell == 1:
                    row_str += "X | "
                elif cell == -1:
                    row_str += "O | "
                else:
                    row_str += "  | " # Two spaces for an empty cell
            print(row_str)
            print("-------------")
