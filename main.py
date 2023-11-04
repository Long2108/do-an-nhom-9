import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)
pygame.display.set_caption("Et Bi 99 - NHA CAI DEN TU CHAU A")
clock = pygame.time.Clock()

# Coin
coin = 0
font = pygame.font.Font(None, 50)
text = font.render("COIN: ", True,  "#f06e4b")
text_rect = text.get_rect(center = (100, 50))

game_state = 0
class Txt():
    def __init__(self, x, y, content, color):
        font = pygame.font.Font(None, 50)
        self.text = font.render(content, True, color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)

    def render(self):
        screen.blit(self.text, self.rect)

class Img():
    def __init__(self, x, y, image, scale):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Button():
    def __init__(self, x, y, image, scale):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def isClick(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            return True
        else:
            return False  

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

pygame.mixer.init()
pygame.mixer.music.load("BG-Music.mp3")
pygame.mixer.music.play(-1, 0, 0)

bg_1_x = -1000

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
            
    if game_state == 0:
        w, h = pygame.display.get_surface().get_size()
        bg = Img(0, 0, "BG.png", (w, h))
        bg_text = Img(100, 100, "BG-Title.png", (500, 100))

        bg_1_x += 2
        if bg_1_x >= 0:
            bg_1_x = -1000
        bg_1 = Img(bg_1_x, h - 250, "BG3.png", (4000, 250))

        bg.draw()
        bg_text.draw()
        bg_1.draw()

        btn_play = Button(w / 2 - 150, h / 2 - 20, "BTN-Play.png", (300, 100))
        btn_play.draw()

        btn_minigame = Button(w / 2 - 150, h / 2 + 100 , "BTN-Minigame.png", (300, 100))
        btn_minigame.draw()

        data_file = open("Inventory.txt", "r")
        data = data_file.readlines()
        coin = data[0]
        data_file.close()

        text = Txt(50, 50, "COIN: " + str(coin), "#f06e4b")
        text.render()

        if (btn_minigame.isClick()):
            game_state = 2

    elif game_state == 2:
        screen.fill("WHITE")
        pygame.mixer.music.stop()
    
    pygame.display.update()
    clock.tick(60)