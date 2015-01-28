# pygame101
import pygame

from pygame.locals import *
from pygame.math import *

from pygame_appentry import *
import py_global as glob
import py_physics.py_physics_simulation as physics


class App(BaseApp):
    def init(self):
        glob.PHYSIC_SIMULATION = physics.PhySimulation()

        # init scene
        self.init_beam(50, 10, 40, 10)
        pass

    def update(self):
        self.handle_input()
        # game update

        # physic simulation
        glob.PHYSIC_SIMULATION.update()

    def render(self):
        glob.PHYSIC_SIMULATION.render()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.m_active = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            print("Key pressed")

    def init_beam(self, x, y, length, segments):
        top = physics.PhyParticleInstance()
        bottom = physics.PhyParticleInstance()

        top.m_fixed = True
        bottom.m_fixed = True
        top.m_pos = Vector2(x, y)
        bottom.m_pos = Vector2(x, y + length)

        glob.PHYSIC_SIMULATION.add_instance(top)
        glob.PHYSIC_SIMULATION.add_instance(bottom)

        for i in range(1, segments):
            new_top = physics.PhyParticleInstance()
            new_bottom = physics.PhyParticleInstance()
            new_top.m_pos = Vector2(x + i * length, y)
            new_bottom.m_pos = Vector2(x + i * length, y + length)

            c = [physics.PhyConstraint(top, new_top), physics.PhyConstraint(bottom, new_bottom),
                 physics.PhyConstraint(new_top, new_bottom), physics.PhyConstraint(top, new_bottom)]

            for ii in c:
                glob.PHYSIC_SIMULATION.add_constraint(ii)

            glob.PHYSIC_SIMULATION.add_instance(new_top)
            glob.PHYSIC_SIMULATION.add_instance(new_bottom)

            top = new_top
            bottom = new_bottom


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()