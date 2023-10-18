from Global_Var import *
class Laberinto:
    def __init__(self, filename):
        # Carga el laberinto desde el archivo
        self.maze = self.load_maze(filename)
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])

    def load_maze(self, filename):
        # Carga el laberinto desde el archivo de texto
        with open(filename, "r") as file:
            maze = [list(line.strip()) for line in file]
        return maze

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col] == '1':
                    pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif self.maze[row][col] == '0':
                    pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                # Agregar más condiciones para dibujar 'X' y 'W' si lo deseas
