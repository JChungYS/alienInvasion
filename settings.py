class Settings:
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen Settings
        self.screen_width = 1200
        self.screen_heigth= 800
        self.bg_color = (230,230,230)
        # Ship setting
        self.ship_speed = 1.5