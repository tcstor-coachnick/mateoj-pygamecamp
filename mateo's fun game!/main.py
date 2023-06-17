import pygame
import random
class Enemy:
    def __init__(self, image):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        self.image = image
        self.width = 100
        self.height = 100
        self.hp = 1
        self.damage = 1

def loadimage(path):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (100, 100))
    return image 

def iscolliding(thing):
    if thing.y > (y + height):
        return False
    elif(thing.y + thing.height) < y:
        return False
    if thing.x > (x + width):
        return False
    elif(thing.x + thing.width) < x:
        return False
    return True
pygame.init()
window = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("cat life rpg")
clock = pygame.time.Clock()
standing = pygame.image.load("mateo's fun game!/cat left.png")
standing = pygame.transform.scale(standing,(100, 100))
walkingleft = [loadimage("mateo's fun game!/cat walking left.png"), loadimage("mateo's fun game!/cat walking left 2.png")]
walkingright = [loadimage("mateo's fun game!/cat walking right 1.png"), loadimage("mateo's fun game!/cat walking right 2.png")]
walkingup = [loadimage("mateo's fun game!/cat up.png"), loadimage("mateo's fun game!/cat up.png")]
walkingdown = [loadimage("mateo's fun game!/cat down.png"), loadimage("mateo's fun game!/cat down.png")]
attackright = [loadimage("mateo's fun game!/bite.png"), loadimage("mateo's fun game!/bite 2.png")]
dead = [loadimage("mateo's fun game!/dead .png"), loadimage("mateo's fun game!/dead 0.png"),loadimage("mateo's fun game!/dead 4.png"),loadimage("mateo's fun game!/dead 5.png"),loadimage("mateo's fun game!/dead 6.png"),loadimage("mateo's fun game!/dead 7.png")]
back = pygame.image.load("mateo's fun game!/back.png")
back = pygame.transform.scale(back,(1000, 1000))
bad = pygame.image.load("mateo's fun game!/bad.png")
bad = pygame.transform.scale(bad,(100, 100))
#x is left and right 
x = 0
#y is up and down 
y = 0
width = 100
height = 100
speed= 5
hp = 1300
damage = 1
direction = "left"
framenumber = 0
enemies = []
attacking = False
death = False
run = True 
while run:
    clock.tick(60)
    if death:
        window.blit(back, (0, 0))
        window.blit(dead[framenumber // 10], (x, y))
        pygame.display.update()
        if framenumber == 59:
            pygame.time.delay(100)
            break
        else:
            framenumber += 1
            continue
    framenumber += 1
    if framenumber == 1:
        enemy = Enemy(bad)
        enemies.append(enemy)
    if framenumber == 23:
        framenumber = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    direction = "none"
    attacking = False
    if keys[pygame.K_RIGHT]:
        x += speed
        direction = "right"
        standing = loadimage("mateo's fun game!/cat right.png")
    if keys[pygame.K_LEFT]:
        x -= speed
        direction = "left"
        standing = loadimage("mateo's fun game!/cat left.png")
    if keys[pygame.K_UP]:
        y -= speed
        direction = 'up'
    if keys[pygame.K_DOWN]:
        y  += speed  
        direction = "down"
    if keys [pygame.K_SPACE]:
        attacking = True
    window.fill((0, 0, 0))
    #pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    window.blit(back, (0, 0))
    if attacking:
        if direction == "right":
            window.blit(attackright[framenumber// 12], (x, y))
    elif direction == "left":
        window.blit(walkingleft[framenumber // 12], (x, y)) 
    elif direction == "right":  
        window.blit(walkingright[framenumber // 12], (x, y))
    elif direction == "up":
        window.blit (walkingup[framenumber // 12], (x, y))
    elif direction == "down":
        window.blit (walkingdown[framenumber // 12], (x, y))    
    else:
        window.blit(standing, (x, y))
    for enemy in enemies:
        window.blit(enemy.image, (enemy.x, enemy.y))
        if iscolliding(enemy):
            if attacking:
                enemy.hp -= damage
                if enemy.hp < 1:
                     enemies.remove(enemy)
            else:
                hp -= enemy.damage 
                if hp < 1:
                    death = True
                    framenumber  = 0

    pygame.display.update()
pygame.quit()