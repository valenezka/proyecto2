# import time
# tiempo=time.time()
# print(tiempo)
# import pygame
# gif="gif.gif"
# gif_imagen=pygame.image.load(gif)
# gif_surface=gif_imagen.convert()
# gif_surface.set_colorkey((0,0,0))
# screen.blit(gif_surface,(0,0))
# pygame.display.flip()
import itertools
import os
import sys
import pygame


class AnimatedBackground(pygame.sprite.Sprite):
    def __init__(self, position, images, delay):
        super(AnimatedBackground, self).__init__()

        self.images = itertools.cycle(images)
        self.image = next(self.images)
        self.rect = pygame.Rect(position,  self.image.get_rect().size)

        self.animation_time = delay
        self.current_time = 0

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.image = next(self.images)


def load_images(path):
    images =  [pygame.image.load(path + os.sep + file_name).convert() for file_name in sorted(os.listdir(path))]
    return images

def main():
    pygame.init()
    SIZE = WIDTH, HEIGHT = 800, 600
    BACKGROUND_COLOR = pygame.Color('black')
    FPS = 60
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    images = load_images(path='gif') 
    background = AnimatedBackground(position=(0, 0), images=images, delay = 0.03)
    all_sprites = pygame.sprite.Group(background)

    while True:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        all_sprites.update(dt)

        screen.fill(BACKGROUND_COLOR)
        screen.blit(background.image, background.rect)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()