import pygame

def load_assets():
    assets = {}
    assets['background_forest'] = pygame.image.load('assets/background_forest.png')
    assets['background_dojo'] = pygame.image.load('assets/background_dojo.png')
    assets['background_city'] = pygame.image.load('assets/background_city.png')
    assets['panda'] = pygame.image.load('assets/panda.png')
    assets['hat1'] = pygame.image.load('assets/hat1.png')
    assets['paddle1'] = pygame.image.load('assets/paddle1.png')
    assets['ball'] = pygame.image.load('assets/ball.png')
    return assets

def draw_panda(win, x, y, assets, hat=None):
    win.blit(assets['panda'], (x, y))
    if hat:
        win.blit(assets[hat], (x, y - 20))  # Offset hat above panda

def draw_paddle(win, paddle_rect, assets):
    win.blit(assets['paddle1'], paddle_rect.topleft)

def draw_ball(win, ball_rect, assets):
    win.blit(assets['ball'], ball_rect.topleft)

def draw_background(win, assets, level):
    if level == 0:
        win.blit(assets['background_forest'], (0, 0))
    elif level == 1:
        win.blit(assets['background_dojo'], (0, 0))
    elif level == 2:
        win.blit(assets['background_city'], (0, 0))
