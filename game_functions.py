import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets): # Respond to key presses and mouse events
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Responds to key presses
    if event.key == pygame.K_RIGHT:
        # Move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    # Fire a bullet if limit is not reached
    # Create a bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    # Respond to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False  

def update_screen(ai_settings, screen, ship, bullets): 
    # Updates images on the screen and flip to the new screen
    # Redraw screen during eadh pass through the loop
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
            
    # Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    # Updates the position of bullets
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy(): # Create a copy of bullets to iterate
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)