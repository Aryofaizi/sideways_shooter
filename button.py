import pygame.font


class Button:
    """make any button with this class."""
    
    def __init__(self, game, msg):
        """initialize button attributes."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # set bg color and font color
        self.bg = (255, 255, 255)
        self.color = (0 ,255 , 0)
        
        # set rectangle height and width
        self.width, self.height = 200, 50
        
        # set font type and size
        self.font = pygame.font.SysFont(None, 42)
        
        # make rect and set position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        
    def _prep_msg(self, msg):
        """make message image to render."""
        self.msg_image = self.font.render(msg, True, self.color, self.bg)
        
        # set msg_image rect
        self.msg_image_rect = self.msg_image.get_rect()
        # set the image_rect on button
        self.msg_image_rect.center = self.rect.center
        
        
    def draw_button(self):
        """make button visible on screen."""
        self.screen.fill(self.bg, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)