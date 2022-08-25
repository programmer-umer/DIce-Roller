import pygame
import random
pygame.init()

HEIGHT = 150
WIDTH  = 250

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
AQUA = "aqua"

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roller")
window.fill(WHITE)

font = pygame.font.SysFont('arail', 25)
text = font.render("Roll", True, BLACK)

class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.x <= mouse_x <= self.width + self.x and self.y <= mouse_y <= self.height + self.y:
            return True

button = Button(100, 100, 50, 30)

side1 = pygame.image.load('1.png')
side2 = pygame.image.load('2.png')
side3 = pygame.image.load('3.png')
side4 = pygame.image.load('4.png')
side5 = pygame.image.load('5.png')
side6 = pygame.image.load('6.png')

def select_side(window):
    side = random.randint(1,6) 
    if side == 1:
        window.blit(side1, (70,0))
    if side == 2:
        window.blit(side2, (70,0))
    if side == 3:
        window.blit(side3, (70,0))
    if side == 4:
        window.blit(side4, (70,0))
    if side == 5:
        window.blit(side5, (70,0))
    if side == 6:
        window.blit(side6, (70,0))

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.clicked():
                    select_side(window)
                    
        pygame.draw.rect(window, AQUA, pygame.Rect(button.x, button.y, button.width, button.height))
        window.blit(text, (button.x + 6, button.y + 7))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
