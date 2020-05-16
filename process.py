import cv2
import image_slicer
import pygame, time
# from urllib import request
# from selenium import webdriver as webd
# from selenium.webdriver.common.by import By


def make_image (img):
    image_slicer.slice(img, 16)

def resize():
    path = "img/Konoha/konoha.jpg"
    img = cv2.imread(path)
    img = cv2.resize(img, (640,640), interpolation = cv2.INTER_AREA)
    cv2.imwrite("img/Konoha/konoha_.jpg",img)
    return "img/Konoha/konoha_.jpg"

make_image(resize())

def show_fade(screen, image, pos_dim, x,y,speed = 0.1, type_=0 ):
    
    rect = pygame.Rect(pos_dim)
    rec =  image.get_rect()
    rec.centerx = rect.centerx + x
    rec.centery = rect.centery + y
    if type_ == 0:
        for i in range(0,255,10):
            image.set_alpha(i)
            screen.blit(image,rec)
            pygame.display.flip()
            time.sleep(speed)
        
    else:
        i = 0
        while i <= 255:
            image.set_alpha(i)
            screen.blit(image,rect)
            pygame.display.flip()
            time.sleep(speed)
            i = (i+1)*2
    if y == -30:
        image.set_alpha(0)
        screen.blit(image,rec)
        pygame.display.flip()


# def image_download(url="https://www.shutterstock.com/image-vector/easy-open-lock-icon-vector-white-1050513854"):
#     # Open the webpage
#     # browser = webd.Chrome(executable_path = r'C:\Chrome\chromedriver')
#     # browser.get(url)
#     # images = browser.find_elements_by_tag_name('img')   #-----------> Find img tags form the source
#     # img = images[2].get_attribute('src')
#     img = "https://image.shutterstock.com/image-vector/easy-open-lock-icon-vector-260nw-1050513854.jpg"
#     request.urlretrieve(img,r"C:\Users\Satwat\Desktop\img.png")   #-----------> Downloadig Image



# def show_zoom(screen, image, pos_dim, speed = 0.1):
#     rect = pygame.Rect(pos_dim)
#     x,y,w,h = pos_dim
#     w,h = (w//20,h//20)
#     image.set_colorkey(image.get_at((0,0)))
#     for i in range(0,255,10):
#         img = pygame.transform.scale(image, (w,h))
#         image.set_alpha(i)
#         act = img.get_rect()
#         act.center = rect.center
#         screen.blit(image,act)
#         pygame.display.flip()
#         time.sleep(speed)
#         w,h = (w+15,h+15)

