import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics
    stats = GameStats(ai_settings)

    # Make the ship, a grou of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start with main loop for the game
    while True:
        # Checks for key presses and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            #bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets) # Want to update aliens after bullets to check for hits
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        


run_game()