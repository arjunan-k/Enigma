import pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(1)

# This class helps to read the encoded morse code.
class Music:

    @staticmethod
    def dot():
        pygame.mixer.music.load("music/Dot.mp3")
        pygame.mixer.music.play(loops=0)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    @staticmethod
    def slash():
        pygame.mixer.music.load("music/Slash.mp3")
        pygame.mixer.music.play(loops=0)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    @staticmethod
    def space():
        pygame.mixer.music.load("music/Space.mp3")
        pygame.mixer.music.play(loops=0)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    @staticmethod
    def bar():
        pygame.mixer.music.load("music/Bar.mp3")
        pygame.mixer.music.play(loops=0)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)