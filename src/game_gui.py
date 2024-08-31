import pygame
import sys
from tictactoe import TicTacToe

SCREEN_SIZE = 600
BOARD_SIZE = 3
CELL_SIZE = SCREEN_SIZE // BOARD_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
HIGHLIGHT = (0, 255, 0)
TITLE_BAR_HEIGHT = 50

class TicTacToeGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + TITLE_BAR_HEIGHT))
        pygame.display.set_caption('Othello')
        self.font = pygame.font.SysFont(None, 48)
        self.tictactoe = TicTacToe()

    def draw_title_bar(self):
        pygame.draw.rect(self.screen, BLACK, (0, 0, SCREEN_SIZE, TITLE_BAR_HEIGHT))
        turn_text = "X's Turn" if self.tictactoe.current_player == 1 else "O's Turn"
        turn_surface = self.font.render(turn_text, True, WHITE)
        text_rect = turn_surface.get_rect(center=(SCREEN_SIZE // 2, TITLE_BAR_HEIGHT // 2))
        self.screen.blit(turn_surface, text_rect)

    def draw_board(self):
        for x in range(3):
            for y in range(3):
                rect = pygame.Rect(x * CELL_SIZE, TITLE_BAR_HEIGHT + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)
                piece = self.tictactoe.board[x][y]
                if piece == 1:
                    pygame.draw.circle(self.screen, BLACK, rect.center, 90, 10)
                elif piece == -1:
                    pygame.draw.circle(self.screen, WHITE, rect.center, 90, 10)

    def draw_text(self, text, color, x, y):
        img = self.font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def handle_click(self, x, y):
        if self.tictactoe.board[x][y] == 0:
            self.tictactoe.make_move(x, y)
            if self.tictactoe.is_game_over():
                self.display_winner()

    def display_winner(self):
        if self.tictactoe.check_winner() == 1:
            text = "X wins!"
        elif self.tictactoe.check_winner() == -1:
            text = "O wins!"
        else:
            text = "It's a tie!"
        self.draw_text(text, BLACK, SCREEN_SIZE // 2, TITLE_BAR_HEIGHT // 2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    board_x = x // CELL_SIZE
                    board_y = (y - TITLE_BAR_HEIGHT) // CELL_SIZE
                    self.handle_click(board_x, board_y)

            self.screen.fill(GREEN)
            self.draw_board()
            self.draw_title_bar()
            pygame.display.flip()

if __name__ == '__main__':
    TicTacToeGUI().run()