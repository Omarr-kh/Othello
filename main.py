import pygame

from game.board import Board
from game.constants import (FPS, HEIGHT, SEARCH_DEPTH, WHITE, WIDTH,
                            get_coordinate_mouse)
from game.controller import Game
from minimax.minimaxAlgo import minimax

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Othello')


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)
    s = 1
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:

            if len(game.board.get_moves(WHITE)) == 0:
                game.change_turn()
                continue

            value, new_board = minimax(game.get_board(), SEARCH_DEPTH, WHITE)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            # display the winner in GUI
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_coordinate_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
