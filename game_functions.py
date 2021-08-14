import sys
import pygame

def check_events(ship): # Respond to key presses and mouse events

    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship to the right
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                # Move ship to the left
                ship.moving_left = True
        
        elif event.type == pygame.KEYUP:
            # Player releases key
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
                
            if event.key == pygame.K_LEFT:
                ship.moving_left = False



def update_screen(ai_settings, screen, ship): # Updates images on the screen and flip to the new screen
    
    # Redraw screen during eadh pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
            
    # Make the most recently drawn screen visible
    pygame.display.flip()