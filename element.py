import pygame

WHITE = (255, 255, 255)


class Element(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.image = pygame.image.load('assets/proton.png').convert_alpha()
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.dragging = False

        self.pos = (self.rect.x + x/2, self.rect.y + y/2)

        pass

    def get_pos(self):
        return self.pos
