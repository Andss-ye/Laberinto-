from Global_Var import *
class Juego:
    def __init__(self, laberinto, personaje, meta):
        self.laberinto = laberinto
        self.personaje = personaje
        self.meta = meta

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Laberinto Pygame")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                pass 
            elif keys[pygame.K_RIGHT]:
                pass 
            elif keys[pygame.K_UP]:
                pass  
            elif keys[pygame.K_DOWN]:
                pass 

            screen.fill((255, 255, 255))
            self.laberinto.draw(screen)
            self.personaje.draw(screen)
            self.meta.draw(screen)
            pygame.display.update()