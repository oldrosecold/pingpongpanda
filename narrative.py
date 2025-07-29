import pygame

def show_story(win, level):
    font = pygame.font.SysFont("comicsansms", 32)
    stories = [
        "In a peaceful forest, Panda dreams of ping pong glory.",
        "With newfound skill, Panda climbs to the Mountain Dojo.",
        "City lights shimmer as Panda enters the big tournament.",
        "Triumphant, Panda becomes a professional. The journey continues!"
    ]
    win.fill((255,255,255))
    text = font.render(stories[level], True, (0,0,0))
    win.blit(text, (50, 250))
    pygame.display.update()
    pygame.time.wait(2000)
