import time,pygame,process

side_screen = pygame.sprite.Group()

def show(count):
    if count == 1:
        rect_op = ( Main_var['x'], Main_var['y'], 646, 646)
        image = pygame.image.load("img/anj/"+str(count)+".png").convert()
        process.show_fade(Main_var['screen'], image, rect_op, -10,-30)
        time.sleep(1)
        image.set_alpha(0)
        Main_var['screen'].blit(image,(4,4))
        pygame.display.flip()
    else:
        rect_op = ( Main_var['x'], Main_var['y'], 646, 646)
        image = pygame.image.load("img/anj/"+str(count)+".png").convert()
        process.show_fade(Main_var['screen'], image, rect_op, -10,-20)

class hint_box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Main_var['name']).convert()
        w,h = Main_var["side_bg"].size
        self.image = pygame.transform.scale(self.image, (w-10,h-10))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = Main_var["side_bg"].center
        self.displayed = False
        self.count = 0
    def update(self):
        if(Main_var['hint_clicked'] and not Main_var['mouse_up']):
            if(self.count <= 3):
                self.image.set_alpha(255)
        else:
            self.image.set_alpha(0)
class disp_life(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/numbers/3.png").convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.dim_trans = (40, Main_var['Lrect'].bottom - Main_var['Lrect'].top-7)
        self.image = pygame.transform.scale(self.image, self.dim_trans)
        self.rect = self.image.get_rect()
        self.rect.center = Main_var['Lrect'].center
        
    def update(self):
        if Main_var['mouse_up']:
            self.image = image_[Main_var['help_']]  
       
def join_animation():
    global image_
    image_ = [pygame.image.load("img/numbers/0.png").convert(),
             pygame.image.load("img/numbers/1.png").convert(),
             pygame.image.load("img/numbers/2.png").convert(),
             pygame.image.load("img/numbers/3.png").convert()]
   
    dim = (40, Main_var['Lrect'].bottom - Main_var['Lrect'].top-7)
    i = 0    
    l = len(image_)    
    while i < l: 
        image_[i].set_colorkey(image_[i].get_at((0,0)))
        image_[i] = pygame.transform.scale(image_[i], dim)
        i += 1 
    side_screen.add(hint_box())
    side_screen.add(disp_life())


class side_process():
    def __init__(self,screen, Gvar):
        self.screen = screen
        global Main_var
        Main_var = Gvar

    def endit(self):
        rect_op = ( Main_var['x'], Main_var['y'], 646, 646)
        image = pygame.image.load(Main_var['name']).convert()
        # image.set_colorkey((image.get_at((0,0))))
        process.show_fade(Main_var['screen'], image, rect_op, 0,0)
        
    
