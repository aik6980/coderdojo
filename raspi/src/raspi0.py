import pygame
import io
import picamera

from pygame.math import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    camera = picamera.PiCamera()
    camera.resolution = (1024,768)

    rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3)

    while True:
        stream = io.BytesIO()
        camera.capture(stream, use_video_port=True, format='rgb', resize=(320,240))
        stream.seek(0)
        stream.readinto(rgb)
        stream.close()

        img = pygame.image.frombuffer(rgb[0:(320*240*3)], (320,240), 'RGB')
        screen.blit(img, (0,0))

        pygame.display.update()

if __name__ == "__main__":
    main()
