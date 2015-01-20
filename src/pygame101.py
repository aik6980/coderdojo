# pygame101
import pygame
from pygame.locals import *

SCREEN_SIZE = [400, 400]
SCREEN = None

class App:
	m_active = True

	def on_execute(self):
		pygame.init()
		SCREEN = pygame.display.set_mode(SCREEN_SIZE) #

		while self.m_active == True:
			# update input
			self.handle_input()
			#update logic/simulation

			#update rendering
			SCREEN.fill((0, 0, 0))
			pygame.display.flip()

		pygame.quit()

	def handle_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.m_active = False

		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]:
			print("Key pressed")

if __name__ == "__main__":
	theApp = App()
	theApp.on_execute()