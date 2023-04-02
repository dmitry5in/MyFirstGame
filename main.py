import pygame, controls
from cat import Cat


def run():
    pygame.init()
    W = 1024
    H = 768
    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    pygame.display.set_caption("Игра про кошек")
    pygame.display.set_icon(pygame.image.load("koshechka.jpg"))
    bg_color = (150, 150, 0)
    cat = Cat(screen)
    clock = pygame.time.Clock()
    FPS = 60
    x = W // 2
    y = H // 2
    speed = 4

    while True:
        controls.get_event(cat)
        cat.update_cat()
        screen.fill(bg_color)
        cat.output()
        pygame.display.update()
        clock.tick(FPS)


run()