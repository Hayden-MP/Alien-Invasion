class Settings():

    # A class to store all settings for Alien Invasion

    def __init__(self):
        # Initialize the game's settings

        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230) # Pygame uses RGB values from 0-255

        # Ship settings
        self.ship_speed_factor = 3.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10
        # Fleet direct of 1 represents right; -1 represents left
        self.fleet_direction = 1

    
