from copy import deepcopy

from game.board import Board
from game.constants import BLACK, WHITE


# minimax => board , depth , max_player
def minimax(board, depth, max_player):
    if depth == 0 or board.winner() != None:
        return board.evaluate(), board

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(board, WHITE):

            # check the evalution of this move
            evaluation = minimax(board, depth-1, False)[0]
            maxEval = max(maxEval, evaluation)

            # if this move is the max evalution
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move

    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(board, BLACK):

            evaluation = minimax(board, depth - 1, True)[0]

            minEval = min(minEval, evaluation)

            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def simulate_move(row, col, board, color):
    board.insert_piece(row, col, color)
    return board


def get_all_moves(board: Board, color):
    moves = []
    for row, col in board.get_moves(color):
        # draw_moves(game, board, piece)
        temp_board = deepcopy(board)
        new_board = simulate_move(row, col, temp_board, color)
        moves.append(new_board)

    return moves


# def draw_moves(game, board, piece):
#     valid_moves = board.get_valid_moves(piece)
#     board.draw(game.win)
#     pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
#     game.draw_valid_moves(valid_moves.keys())
#     pygame.display.update()
#     pygame.time.delay(50)