import pygame
import constants as c
from player import Player
from logger import log_state


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print("Screen width: " + str(c.SCREEN_WIDTH))
    print("Screen height: " + str(c.SCREEN_HEIGHT))

    # Setup the game
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    running = True

    updatable =pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    player = Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    

    # Main game loop
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
