"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided
import time
#import codeskulptor
#codeskulptor.set_timeout(30)

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    This function takes a current board and the next player 
    to move. The function should play a game starting with 
    the given player by making random moves, alternating 
    between players. The function should return when the 
    game is over. The modified board will contain the 
    state of the game, so the function does not return 
    anything. In other words, the function should modify 
    the board input.
    """
    empty_squares = board.get_empty_squares()
    len_empsq = len(empty_squares)
    board_dim = board.get_dim()
    uplim = board_dim*(board_dim-1)
    random.shuffle(empty_squares)
    bmove = board.move
    bcheck = board.check_win
    for idx, (row,col) in enumerate(empty_squares):
        bmove(row,col,player)
        player = provided.switch_player(player)
        if (len_empsq - idx <= uplim ) and bcheck() != None:
            return
#        if bcheck() != None:
#            return
        
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) 
    with the same dimensions as the Tic-Tac-Toe board, 
    a board from a completed game, and which player the 
    machine player is. The function should score the 
    completed board and update the scores grid. As the 
    function updates the scores grid directly, it does 
    not return anything.
    """
    board_dim = board.get_dim()
    winner = board.check_win()
    other = provided.switch_player(player)

    if winner == player:
        score_current = SCORE_CURRENT
        score_other = -1 * SCORE_OTHER
    elif winner == other:
        score_current = -1 * SCORE_CURRENT
        score_other = SCORE_OTHER
    else:
        return
    
    bsquare = board.square
    for row in range(board_dim):
        for col in range(board_dim):
            status = bsquare(row, col)
            if status == player:
                scores[row][col] += score_current
            elif status == other:
                scores[row][col] += score_other

def get_best_move(board, scores):
    """
    This function takes a current board and a grid of 
    scores. The function should find all of the empty 
    squares with the maximum score and randomly return 
    one of them as a (row, column) tuple. It is an error 
    to call this function with a board that has no empty 
    squares (there is no possible next move), so your 
    function may do whatever it wants in that case. 
    The case where the board is full will not be tested.
    """
    empty_squares = board.get_empty_squares()
    if empty_squares == []:
        return
    maxval = -float('inf')
    maxidx = []
    idxapd = maxidx.append
    for idx,(row,col) in enumerate(empty_squares):
        score = scores[row][col]
        if score > maxval:
            maxval = score
            maxidx = [idx]
        elif score == maxval:
            idxapd(idx)
    return empty_squares[random.choice(maxidx)]
            
def mc_move(board, player, trials):
    """
    This function takes a current board, which player 
    the machine player is, and the number of trials to 
    run. The function should use the Monte Carlo 
    simulation described above to return a move for the 
    machine player in the form of a (row, column) tuple. 
    """
    board_dim = board.get_dim()
    scores = [[0 for _ in range(board_dim)] for _ in range(board_dim)]
    bclone = board.clone
    for _ in xrange(trials):
        trial_board = bclone()
        mc_trial(trial_board, player)
        mc_update_scores(scores, trial_board, player)
    return get_best_move(board, scores)
    
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
