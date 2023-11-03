import pygame
import random
import math
from pygame import mixer
# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("Ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Background.jpg")

#add music
mixer.music.load('background_music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# player variables
img_player = pygame.image.load("Rocket.png")
player_x = 368
player_y = 536
player_x_change = 0

# enemy variables
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 8

for e in range(number_of_enemies):
    img_enemy.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.5)
    enemy_y_change.append(50)

# bullet variables
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 3
visible_bullet = False

#Score
score = 0
my_font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

#End of game text
end_font = pygame.font.Font('fastest.ttf', 40)

def final_text():
    my_final_font = end_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(my_final_font, (200, 200))

#show score function
def show_score(x,y):
    text = my_font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (x,y))

# Player function
def player(x,y):
    screen.blit(img_player, (x, y))
# Enemy function
# Enemy function
def enemy(x, y, en):
    screen.blit(img_enemy[en], (x, y))

#Shoot bullet
def shoot_bullet(x,y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x+16, y+10))

#Detect collision function
def there_is_a_collision(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distance < 27:
        return True
    else:
        return False


#Game loop
is_running = True
while is_running:
    #Background Image
    screen.blit(background, (0,0))
    #Event iteration
    for event in pygame.event.get():
        #closing event
        if event.type == pygame.QUIT:
            is_running = False
        # Press key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('shot.mp3')
                bullet_sound.play()
                if not visible_bullet:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)
        # Release key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Modify player location
    player_x += player_x_change

    #keep player inside screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Modify enemy location
    for enem in range(number_of_enemies):
        # end of game
        if enemy_y[enem] > 500:
            for k in range(number_of_enemies):
                enemy_y[k] = 1000
            final_text()
            break
        enemy_x[enem] += enemy_x_change[enem]

    # Keep enemy inside screen
        if enemy_x[enem] <= 0:
            enemy_x_change[enem] = 1
            enemy_y[enem] += enemy_y_change[enem]
        elif enemy_x[enem] >= 736:
            enemy_x_change[enem] = -1
            enemy_y[enem] += enemy_y_change[enem]

        # Collision
        collision = there_is_a_collision(enemy_x[enem], enemy_y[enem], bullet_x, bullet_y)
        if collision:
            collision_sound = mixer.Sound('punch.mp3')
            collision_sound.play()
            bullet_y = 500
            visible_bullet = False
            score += 1
            enemy_x[enem] = random.randint(0, 736)
            enemy_y[enem] = random.randint(50, 200)

        enemy(enemy_x[enem], enemy_y[enem], enem)


    #Bullets Movement
    if bullet_y <= 64:
        bullet_y = 500
        visible_bullet = False
    if visible_bullet:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)

    #show score
    show_score(text_x, text_y)

    #update
    pygame.display.update()