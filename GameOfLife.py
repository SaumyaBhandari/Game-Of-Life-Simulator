import pygame
import random
import time

GRID_WIDTH = 50
GRID_HEIGHT = 50
CELL_SIZE = 15

WHITE = (255, 255, 255)
BLACK = (22, 22, 29)

pygame.init()

WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + 40
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def empty_grid():
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    return grid


def count_neighbors(grid, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT and grid[ny][nx] == 1:
                count += 1
    return count



def update_grid(grid):
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = 1
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
    return new_grid



def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = WHITE if grid[y][x] == 1 else BLACK
            pygame.draw.rect(window, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))



def draw_button(drawing_mode):
    button_color = (0, 255, 0) if drawing_mode else (255, 0, 0)
    pygame.draw.rect(window, button_color, (0, GRID_HEIGHT * CELL_SIZE, WINDOW_WIDTH, 40))
    font = pygame.font.SysFont(None, 30)
    text = font.render("DRAWING MODE" if drawing_mode else "RUNNING MODE", True, (255, 255, 255))
    window.blit(text, (10, GRID_HEIGHT * CELL_SIZE + 10))



def main():
    grid = empty_grid()

    running = True
    drawing_mode = True 
    drawing = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x = x // CELL_SIZE
                y = y // CELL_SIZE
                if y > GRID_HEIGHT: 
                    drawing_mode = not drawing_mode
                else:
                    drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.MOUSEMOTION and drawing:
                x, y = pygame.mouse.get_pos()
                x = x // CELL_SIZE
                y = y // CELL_SIZE
                if y < GRID_HEIGHT:
                    grid[y][x] = 1 if drawing_mode else 0

        window.fill(BLACK)

        draw_grid(grid)
        draw_button(drawing_mode)
        if not drawing_mode:
            grid = update_grid(grid)

        pygame.display.update()

        time.sleep(0.1)

    pygame.quit()

if __name__ == "__main__":
    main()
