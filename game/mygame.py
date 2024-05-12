import pygame

from .board import Board
from .constants import BLACK, BLUE, SQUARE_SIZE, WHITE
from .piece import Piece


class Game:
    def __init__(self, window):
        self._init()
        self.window = window

    def update(self):
        self.board.draw(self.window)
        #
        self.get_vaild_moves() # i want the piece to draw for it self the vaild moves that it could get

        self.draw_valid_moves(self.valid_moves)

        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = set()

    def get_vaild_moves(self):
        self.valid_moves = self.board.get_moves(self.turn)
        print(self.valid_moves)

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        move = (row , col)
        if move in self.valid_moves:
            self.board.insert_piece(row,  col , self.turn)
            # flip the turn
            self.turn = WHITE if self.turn == BLACK else BLACK

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, self.turn, (col * SQUARE_SIZE + SQUARE_SIZE//2,
                                                        row * SQUARE_SIZE + SQUARE_SIZE//2), 40, width=1)

    def change_turn(self):
        """changing turn between opponents"""
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def get_board(self):
        return self.board

    # def ai_move(self, board):
    #     self.board = board
    #     self.change_turn()
