import pygame

from pygame.locals import *
from pygame.math import *

import py_global as glob


class PhyParticleInstance:
    m_pos = Vector2(0, 0)
    m_prev_pos = Vector2(0, 0)
    m_vel = Vector2(0, 0)
    m_acc = Vector2(0, 0)

    m_fixed = False

    def __init__(self, x: float, y: float):
        self.m_pos = Vector2(x,y)
        self.m_prev_pos = self.m_pos

    def draw(self, surface: pygame.Surface):
        color = [glob.COLOR_WHITE, glob.COLOR_RED][self.m_fixed]
        pygame.draw.circle(surface, color, glob.to_tuple_i32(self.m_pos), 2, 0)


class PhyConstraint:
    m_Particle0 = None
    m_Particle1 = None
    m_Target = 0

    def __init__(self, a: PhyParticleInstance, b: PhyParticleInstance):
        self.m_Particle0 = a
        self.m_Particle1 = b
        self.m_Target = self.m_Particle0.m_pos.distance_to(self.m_Particle1.m_pos)

    def draw(self, surface: pygame.Surface):
        pygame.draw.line(surface, glob.COLOR_WHITE, glob.to_tuple_i32(self.m_Particle0.m_pos),
                         glob.to_tuple_i32(self.m_Particle1.m_pos), 1)


class PhySimulation:
    MAX_INSTANCES = 128
    m_InstanceBuffer = [None] * MAX_INSTANCES
    m_ConstraintBuffer = [None] * MAX_INSTANCES

    m_InstanceCounter = 0
    m_ConstraintCounter = 0

    def __init__(self):
        print(self.m_InstanceBuffer)

    def add_instance(self, p: PhyParticleInstance):
        self.m_InstanceBuffer[self.m_InstanceCounter] = p
        self.m_InstanceCounter += 1

    def add_constraint(self, c: PhyConstraint):
        self.m_ConstraintBuffer[self.m_ConstraintCounter] = c
        self.m_ConstraintCounter += 1

    def update(self):
        delta_time = glob.GAME_CLOCK.get_time() * 0.001;

        step = delta_time/1
        for i in range(0, 1):

            for ii in range(0, self.m_InstanceCounter):
                self.m_InstanceBuffer[ii].m_acc += Vector2(0, 20)
                self.step_simulation_verlet(self.m_InstanceBuffer[ii], step)

            for ii in range(0, self.m_ConstraintCounter):
                self.step_resolve(self.m_ConstraintBuffer[ii])

    def render(self):
        # draw all phyParticles
        for i in range(self.m_InstanceCounter):
            self.m_InstanceBuffer[i].draw(glob.MAIN_SURFACE)

        for i in range(self.m_ConstraintCounter):
            self.m_ConstraintBuffer[i].draw(glob.MAIN_SURFACE)

    @staticmethod
    def step_simulation(p: PhyParticleInstance, dt: float):

        if p.m_fixed:
            p.m_acc = Vector2(0, 0)
            return

        p.m_pos += p.m_vel * dt
        p.m_vel += p.m_acc * dt

        p.m_acc = Vector2(0, 0)

    @staticmethod
    def step_simulation_verlet(p: PhyParticleInstance, dt: float):

        if p.m_fixed:
            p.m_acc = Vector2(0, 0)
            return

        pos = 2.0 * p.m_pos - p.m_prev_pos + p.m_acc * dt * dt
        p.m_prev_pos = p.m_pos
        p.m_pos = pos

        p.m_acc = Vector2(0, 0)


    @staticmethod
    def step_resolve(c: PhyConstraint):
        delta_pos = c.m_Particle1.m_pos - c.m_Particle0.m_pos
        dist = delta_pos.length()
        dir = delta_pos.normalize()

        factor = (dist - c.m_Target) * 0.5

        if not c.m_Particle0.m_fixed:
            c.m_Particle0.m_pos += factor * dir
        if not c.m_Particle1.m_fixed:
            c.m_Particle1.m_pos += factor * dir * -1.0


