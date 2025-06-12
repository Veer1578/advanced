import pygame
import random

SCREENWIDTH, SCREENHEIGHT = 500, 400
MOVEMENTSPEED = 5
FONTSIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load('flappy.png'), (SCREENWIDTH, SCREENHEIGHT))
font = pygame.font.SysFont('Times New Roman', FONTSIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change,SCREENWIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREENHEIGHT - self.rect.height), 0)

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Color changing sprite collision')
sprite_list = pygame.sprite.Group()

sp1 = Sprite(pygame.Color('Black'), 20, 30)
sp1.rect.x, sp1.rect.y = random.randint(0, SCREENWIDTH - sp1.rect.width), random.randint(0, SCREENHEIGHT - sp1.rect.height)
sprite_list.add(sp1)

sp2 = Sprite(pygame.Color('Red'), 20, 30)
sp2.rect.x, sp2.rect.y = random.randint(0, SCREENWIDTH - sp2.rect.width), random.randint(0, SCREENHEIGHT - sp2.rect.height)
sprite_list.add(sp2)

running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT + 1:
            sp1.image.fill((random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)))
            sp2.image.fill((random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)))
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] -
                    keys[pygame.K_LEFT]) * MOVEMENTSPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENTSPEED
        sp1.move(x_change, y_change)

        if sp1.rect.colliderect(sp2):
            pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))
            won = True
    screen.blit(background_image, (0, 0))
    sprite_list.draw(screen)

    if won:
        win_text = font.render('You won!', True, pygame.Color('black'))
        screen.blit(win_text, ((SCREENWIDTH - win_text.get_width()) //
                    2, (SCREENHEIGHT - win_text.get_height()) // 2))
    pygame.display.flip()
    clock.tick(90)

pygame.quit()
