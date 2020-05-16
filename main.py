
# Pygame template - skeleton for a new pygame project
import pygame, random, process, animation, time
imsize = 160
ratio = imsize/100
x,y = (20,20)
WIDTH = 900
HEIGHT = (imsize*4)+y*2+4
FPS = 30

# define colors
WHITE = (255, 255, 255)
WHITEbg = (240,240,240)
life_col = (77, 38, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
BLUE = (0, 0, 255)
img_name = "img/Konoha/konoha__0"
name = "img/Konoha/konoha.jpg"

GREEN = (0, 51, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slide Puzzel")
clock = pygame.time.Clock()
lst_pos = [(0,0),(0,1),(0,2),(0,3), (1,0),(1,1),(1,2),(1,3) ,(2,0),(2,1),(2,2),(2,3) ,(3,0),(3,1),(3,2)]
all_sprites = pygame.sprite.Group()

# last piece
image = pygame.image.load((img_name+"4_04.png"))
image.set_alpha(50)
#border background
bim = pygame.image.load(r"img/background/bor.png").convert()
bim = pygame.transform.scale(bim, (656,656))
bim_rect = bim.get_rect()
bim_rect.x, bim_rect.y = (x-5, y-5)
# background
imbg = pygame.image.load(r"img/background/background4.jpg").convert()
imbg = pygame.transform.scale(imbg, (WIDTH,HEIGHT))

bg_rect = imbg.get_rect()

# Decleration of tile sprite
def rand_posi():
    p = random.choice(lst_pos)
    lst_pos.remove(p)
    return p
class Box(pygame.sprite.Sprite):
    def __init__(self, i, j,center):
        pygame.sprite.Sprite.__init__(self)
        if (i == 3 and j == 3):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.center = center
        else:
            self.image = pygame.image.load((img_name+str(i+1)+"_0"+str(j+1)+".png"))
            ri,rj = rand_posi()
            self.rect = self.image.get_rect()
            # print(self.rect.size)
            self.rect.x = x + 160*rj + 2*rj
            self.rect.y = y + 160*ri + 2*ri
        #set its actual center
        self.org_center = center

    def update(self):
        if self.org_center != self.rect.center:
            global solved
            solved = False
               

# Swaping of tiles if correctly clicked
def swap (img):
    temp = img.center
    img.center = ref.rect.center
    ref.rect.center = temp
def move_box (click):
    print("clicked")
    for img in all_sprites:
        if(img.rect.collidepoint(click)):
            x = ref.rect.centerx - img.rect.centerx
            y = ref.rect.centery - img.rect.centery
            # print(x,y)
            if(x == 0):
                if( -162 <= y <= 162):
                    # print("IN1")
                    swap(img.rect)
                
            if(y == 0):
                if( -162 <= x <= 162):
                    # print("IN2")
                    swap(img.rect)


# Declaring image position
ref = None
for i in range (0,4):
    for j in range (0,4):
        x_ = x + 160*j + 2*j
        y_ = y + 160*i + 2*i
        box_ = pygame.Rect((x_, y_, 160.2, 160.2))
        img = Box(i,j,box_.center)
        all_sprites.add(img)
        if(i == 3 and j == 3):
            ref = img
            frst = False
            # print(ref.rect.right)

sp = animation.side_process(screen, globals()) #sending main varialbles to animation 
###################################################
# Image hint background 
imsd = pygame.image.load("img/hint_txt.png").convert()
side_bg = imsd.get_rect()
side_bg.left = bim_rect.right + 50
side_bg.y = bim_rect.y
# Hint_left tile
font = pygame.font.Font("font/SEVESBRG.TTF", 28)
life_title = font.render("Hints Left :", True, life_col)
Ltrect = life_title.get_rect()
Ltrect.centerx = side_bg.centerx
Ltrect.centery = side_bg.bottom + 40
#Life background
life = pygame.image.load("img/background/bg.jpg").convert()
life = pygame.transform.scale(life, ((side_bg.right-side_bg.centerx),60))
life.set_alpha(120)
Lrect =life.get_rect()
Lrect.left = side_bg.centerx
Lrect.right = side_bg.right - 20
Lrect.top = Ltrect.bottom + 2
# # Text Timer
# Time_title = font.render("Time Taken :", True, GREEN)
# Trect = Time_title.get_rect()
# Trect.left = side_bg.left - 20
# Trect.top = Lrect.bottom + (60*4)+10
# # Timer background
# bg_time = pygame.image.load("img/bg.jpg")
# bg_time = pygame.transform.scale(bg_time, (side_bg.right-side_bg.right,60))
# bg_time.set_alpha(120)
# rect_time = bg_time.get_rect()
# rect_time.centerx = side_bg.centerx
# rect_time.centery =  Trect.bottom +2
# # Timer

#add created animations
animation.join_animation()
#
###################################################

# Game loop
mouse_up = True
hint_clicked = False
running = True  
help_ = 3
ok = False #check statement
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    solved = True
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(solved)
            move_box(event.pos)
            # ok = True
            if side_bg.collidepoint(event.pos):
                if help_ > 0: 
                    mouse_up = False
                    hint_clicked = True
                    help_ -= 1
        if event.type == pygame.MOUSEBUTTONUP:
            if not mouse_up:
                mouse_up = True
                hint_clicked = False
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    animation.side_screen.update()
    # if ok:
    #     print(solved)    # Check for solved value
    #     ok = False

    # Draw / render
    screen.blit(imbg, bg_rect)
    screen.blit(bim, bim_rect)
    screen.blit(imsd, side_bg)
    screen.blit(life_title, Ltrect)
    #screen.blit(Time_title, Trect)
    #screen.blit(bg_time, rect_time)
    screen.blit(life, Lrect)
    pygame.draw.rect(screen, WHITE, ref.rect)
    all_sprites.draw(screen)
    animation.side_screen.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()
    if solved == True:
        running = False
        pygame.draw.rect(screen, WHITE, bim_rect)
        screen.blit(bim, bim_rect)
        sp.endit()

pygame.quit()

