from pygame.math import *


class PhyParticleInstance:
	m_pos = Vector2(0, 0)
	m_vel = Vector2(0, 0)
	m_acc = Vector2(0, 0)


class PhyConstraint:
	m_Particle0 = None
	m_Particle1 = None
	m_Target = 0

	def __init__(self, a: PhyParticleInstance, b: PhyParticleInstance):
		self.m_Particle0 = a
		self.m_Particle1 = b
		self.m_Target = self.m_Particle0.m_pos.distance_to(self.m_Particle1.m_pos)


class PhySimulation:
	MAX_INSTANCES = 128
	m_InstanceBuffer = [None] * MAX_INSTANCES
	m_ConstraintBuffer = [None] * MAX_INSTANCES

	def __init__(self):
		print(self.m_InstanceBuffer)

	@staticmethod
	def step_simulation(p: PhyParticleInstance, dt: float):

		p.m_pos += p.m_vel * dt
		p.m_vel += p.m_acc * dt

		p.m_acc = 0

	@staticmethod
	def step_resolve(c: PhyConstraint):
		delta_pos = c.m_Particle0.m_pos - c.m_Particle1.m_pos
		force_size = c.m_Target - delta_pos.length()

		dir = delta_pos.normalize()
		force = dir * force_size

		c.m_Particle0.m_acc += force
		c.m_Particle1.m_acc += force * -1.0
