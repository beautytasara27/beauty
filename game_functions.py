import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, a1_settings, screen, ship, bullets):

   if event.key == pygame.K_RIGHT:
       ship.moving_right = True
   elif event.key == pygame.K_LEFT:
       ship.moving_left = True
   elif event.key == pygame.K_SPACE:
       fire_bullet(a1_settings, screen, ship, bullets)

def fire_bullet(a1_settings, screen, ship, bullets):

   if len(bullets) < a1_settings.bullets_allowed:
       new_bullet = Bullet(a1_settings, screen, ship)
       bullets.add(new_bullet)

def check_keyup_events(event, ship):

   if event.key == pygame.K_RIGHT:
       ship.moving_right = False
   elif event.key == pygame.K_LEFT:
       ship.moving_left = False
       ship.rect.centerx += 1

def check_events(event, a1_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, a1_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(a1_settings, screen, ship, bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            print(len(bullets))
