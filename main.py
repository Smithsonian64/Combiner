import pygame
import numpy as np
from scipy.spatial import distance
from element import Element
import sys

screensize = (800, 480)



def main():




    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(screensize)
    screen.fill((0, 0, 0))
    pygame.display.update()

    sprite_list = pygame.sprite.Group()

    sprite_list.add(Element(100, 100, 'proton'))

    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            for sprite in sprite_list:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print(np.linalg.norm(np.asarray(pygame.mouse.get_pos()) - np.asarray(sprite.get_pos())))
                        if np.linalg.norm(np.asarray(pygame.mouse.get_pos()) - np.asarray(sprite.get_pos())) < 5 and sprite.dragging == False:
                            print("hello")
                            pass
                            #rectangle_draging = True
                            #mouse_x, mouse_y = event.pos
                            #offset_x = rectangle.x - mouse_x
                            #offset_y = rectangle.y - mouse_y

        sprite_list.update()
        sprite_list.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit(0)

    #pygame.draw.rect(screen, BLUE, (0, 0, 100, 100))


if __name__ == "__main__":
    main()
