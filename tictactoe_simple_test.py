import numpy as np
from game import TicTacToe # Import the TicTacToe class from game.py

def test_initial_board_is_empty():
    """
    Tests if the board is correctly initialized to all zeros,
    all actions are available, and no winner is set.
    """
    game = TicTacToe()
    # Check if the board is equal to a 3x3 array of zeros
    assert np.array_equal(game.board, np.zeros((3, 3)))
    # Check if all 9 initial positions are available actions
    assert game.get_available_actions() == [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]
    # Ensure no winner is declared at the start
    assert game.winner is None

def test_make_move_and_available_actions():
    """
    Tests the make_move function's ability to place a mark
    and if the moved position is removed from available actions.
    Also tests invalid moves.
    """
    game = TicTacToe()
    # Make a valid move for player 1 at (0,0)
    assert game.make_move((0, 0), 1) # Expect make_move to return True for success
    # Check if the board position is updated correctly
    assert game.board[0, 0] == 1
    # Check if the moved position is no longer in available actions
    assert (0, 0) not in game.get_available_actions()
    # Try to make an invalid move (position already taken)
    assert not game.make_move((0, 0), -1) # Expect make_move to return False for failure

def test_horizontal_win():
    """
    Tests a horizontal win scenario for player 1.
    """
    game = TicTacToe()
    # Player 1 makes moves to create a horizontal win in the first row
    game.make_move((0, 0), 1)
    game.make_move((0, 1), 1)
    game.make_move((0, 2), 1)
    # Assert that the game is over
    assert game.is_game_over()
    # Assert that player 1 is declared the winner
    assert game.winner == 1

def test_vertical_win():
    """
    Tests a vertical win scenario for player -1.
    """
    game = TicTacToe()
    # Player -1 makes moves to create a vertical win in the second column
    game.make_move((0, 1), -1)
    game.make_move((1, 1), -1)
    game.make_move((2, 1), -1)
    # Assert that the game is over
    assert game.is_game_over()
    # Assert that player -1 is declared the winner
    assert game.winner == -1

def test_diagonal_win():
    """
    Tests a main diagonal win scenario for player 1.
    """
    game = TicTacToe()
    # Player 1 makes moves to create a win on the main diagonal
    game.make_move((0, 0), 1)
    game.make_move((1, 1), 1)
    game.make_move((2, 2), 1)
    # Assert that the game is over
    assert game.is_game_over()
    # Assert that player 1 is declared the winner
    assert game.winner == 1

def test_anti_diagonal_win():
    """
    Tests an anti-diagonal win scenario for player -1.
    """
    game = TicTacToe()
    # Player -1 makes moves to create a win on the anti-diagonal
    game.make_move((2, 0), -1)
    game.make_move((1, 1), -1)
    game.make_move((0, 2), -1)
    # Assert that the game is over
    assert game.is_game_over()
    # Assert that player -1 is declared the winner
    assert game.winner == -1

def test_draw():
    """
    Tests a draw scenario where the board is full but no player has won.
    """
    game = TicTacToe()
    # A sequence of moves that results in a draw
    moves = [
        ((0, 0), 1), ((0, 1), -1), ((0, 2), 1),
        ((1, 0), 1), ((1, 1), -1), ((1, 2), -1),
        ((2, 0), -1), ((2, 1), 1), ((2, 2), 1)
    ]
    for pos, player in moves:
        game.make_move(pos, player)
    # Assert that the game is over
    assert game.is_game_over()
    # Assert that the winner is 0 (indicating a draw)
    assert game.winner == 0

def test_game_not_over_initially():
    """
    Tests that the game is not over at initialization and no winner is set.
    """
    game = TicTacToe()
    # Assert that is_game_over returns False initially
    assert not game.is_game_over()
    # Assert that winner is None initially
    assert game.winner is None
