# pygame101
import pygame

from pygame.locals import *
from pygame.math import *

import py_global as glob

class Box:
    m_pos   = (0, 0, 0)
    m_size  = 8
    m_color = (255, 255, 255)

class BoxPackerNode:
    pass

class BoxPacker:
    pass

class BaseApp:
    m_active = True

    def on_execute(self):
        pygame.init()
        glob.MAIN_SURFACE = pygame.display.set_mode(glob.SCREEN_SIZE)

        glob.GAME_CLOCK = pygame.time.Clock()
        glob.GAME_CLOCK.tick()

        self.init()

        while self.m_active:
            # update input
            self.update()
            # update logic/simulation

            #update rendering
            glob.MAIN_SURFACE.fill((0, 0, 0))
            self.render()

            #print some debug info

            pygame.display.flip()
            glob.GAME_CLOCK.tick()

        self.destroy()
        pygame.quit()

    def init(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def destroy(self):
        pass



