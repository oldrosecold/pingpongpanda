import pygame
from visuals import draw_background, draw_panda, draw_paddle, draw_ball

def pong_match(win, assets, hat, abilities, level):
    # Set up positions
    paddle = pygame.Rect(50, 250, 15, 100)
    ball = pygame.Rect(400, 300, 20, 20)
    ball_speed_x, ball_speed_y = 7, 7
    score = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and paddle.top > 0:
            paddle.y -= 10
        if keys[pygame.K_DOWN] and paddle.bottom < 600:
            paddle.y += 10

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Bounce
        if ball.top <= 0 or ball.bottom >= 600:
            ball_speed_y *= -1
        if ball.colliderect(paddle):
            ball_speed_x *= -1
            score += 1
        if ball.right >= 800:
            ball_speed_x *= -1
        if ball.left <= 0:
            running = False  # End match

        # Draw everything
        draw_background(win, assets, level)
        draw_panda(win, 50, paddle.y, assets, hat)
        draw_paddle(win, paddle, assets)
        draw_ball(win, ball, assets)
        font = pygame.font.SysFont("comicsansms", 32)
        score_text = font.render(f"Score: {score}", True, (0,0,0))
        win.blit(score_text, (350, 20))
        pygame.display.update()
    return score

def training_reaction(win, assets):
    # Simple reaction game: press space when ball glows
    import random, time
    ball = pygame.Rect(400, 300, 20, 20)
    font = pygame.font.SysFont("comicsansms", 32)
    win.fill((255,255,255))
    win.blit(font.render("Get Ready...", True, (0,0,0)), (300, 200))
    pygame.display.update()
    pygame.time.wait(1000 + random.randint(500, 1000))
    glow_time = pygame.time.get_ticks()
    win.fill((255,255,255))
    pygame.draw.ellipse(win, (255,255,0), ball)  # Glowing ball
    win.blit(font.render("Press SPACE!", True, (0,0,0)), (300, 200))
    pygame.display.update()
    reacted = False
    while not reacted:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                reaction = pygame.time.get_ticks() - glow_time
                reacted = True
    return reaction
