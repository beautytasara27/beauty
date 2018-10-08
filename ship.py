import pygame


class Ship:

    def __init__(self, a1_settings, screen):
        self.screen = screen
        self.a1_settings = a1_settings

        self.image = pygame.image.load('C:\\Users\\TATENDA!\\PycharmProjects\\pygame\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centrex = self.screen_rect.centrex
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.a1_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.a1_settings.ship_speed_factor

    def blitme(self):
        #draw ship at current position
        self.screen.blit(self.image, self.rect)


