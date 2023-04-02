import pygame


class Cat:

    def __init__(self, screen):
        """Инициализация кошки"""
        self.screen = screen
        self.image = pygame.image.load('pngwing.com.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        """Рисование кошки"""
        self.screen.blit(self.image, self.rect)

    def update_cat(self):
        """обновление позиции кошки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 3
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 3
        if self.mup:
            self.rect.bottom -= 3
        if self.mdown:
            self.rect.bottom += 3
