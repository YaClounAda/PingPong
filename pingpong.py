from pygame import *

class GameObject(sprite.Sprite):

    def __init__(self, _image, width, height, movement_speed, start_x, start_y):

        super().__init__()

        self.width = width
        self.height = height
        self.image = transform.scale(image.load(_image), (width, height))
        self.speed = movement_speed
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
    
    def Draw(self):

        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameObject):

    def UpdateLeftPlayer(self):

        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 0:

            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < winHeight - self.height:
            
            self.rect.y += self.speed

    def UpdateRightPlayer(self):

        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:

            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < winHeight - self.height:
            
            self.rect.y += self.speed

class Ball(GameObject):

    def __init__(self, _image, width, height, movement_speed, start_x, start_y):

        super().__init__(_image, width, height, movement_speed, start_x, start_y)

        self.xDirection = "Left"
        self.yDirection = "Down"

    def Update(self):

        # Передвижение

        if self.xDirection == "Left":

            self.rect.x -= self.speed

        elif self.xDirection == "Right":

            self.rect.x += self.speed

        if self.yDirection == "Down":

            self.rect.y += self.speed

        elif self.yDirection == "Up":

            self.rect.y -= self.speed

        # Изменение направления

        if sprite.collide_rect(self, leftPlayer):

            self.xDirection = "Right"

        if sprite.collide_rect(self, rightPlayer):

            self.xDirection = "Left"

        if self.rect.y >= winHeight - self.height:

            self.yDirection = "Up"

        if self.rect.y <= 0:

            self.yDirection = "Down"

winWidth = 640
winHeight = 480

window = display.set_mode((winWidth, winHeight))

clock = time.Clock()

FPS = 60

leftPlayer = Player("racket.png", 39, 136, 5, 0, winHeight / 2 - 68)
rightPlayer = Player("racket.png", 39, 136, 5, winWidth - 40, winHeight / 2 - 68)
ball = Ball("tenis_ball.png", 50, 50, 5, winWidth / 2 - 25, winHeight / 2 - 25)

game = True
finish = False

while game:

    for _event in event.get():

        if _event.type == QUIT:

            game = False

    if not finish:

        leftPlayer.UpdateLeftPlayer()
        rightPlayer.UpdateRightPlayer()
        ball.Update()

        window.fill((127, 127, 127))

        ball.Draw()
        leftPlayer.Draw()
        rightPlayer.Draw()

    display.update()
    clock.tick(FPS)