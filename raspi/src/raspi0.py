import pygame
import io
import picamera
import picamera.streams

from pygame.math import *

def main():
    pygame.init()
    #screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((640,480))

    try:
        camera = picamera.PiCamera()
        camera.resolution = (1024,768)

        frame_size = camera.resolution[0] * camera.resolution[1] * 3;
        stream = picamera.streams.PiCameraCircularIO(camera,seconds=1)
        rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3)

        camera.start_recording(stream, format='rgb', resize=(320,240))

        while True:
            #stream = io.BytesIO()
            #camera.capture(stream, use_video_port=True, format='rgb', resize=(320,240))
            #stream.seek(0)
            #stream.readinto(rgb)
            #stream.close()

            # start video recording
            camera.wait_recording()
            i=0
            for frame in stream.frames:
                i+=1
                #print(frame)
            #print(i)
            len(stream.frames)

            #img = pygame.image.frombuffer(rgb[0:(320*240*3)], (320,240), 'RGB')
            #screen.blit(img, (0,0))

            pygame.display.update()
    finally:
        #stream.close()
        camera.stop_recording()
        camera.close()

if __name__ == "__main__":
    main()
