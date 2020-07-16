import pygame
from Rounding import RoundToNearestMultiple

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
ControlPanelValues = (0, 550, 600, 50)
ColorValues = []
Colors = [(0,0,0),(255,255,255),(255,0,0),(255,165,0),(255,255,0),(0,128,0),(0,0,255),(75,0,130),(238,130,238),(0,255,255)]
ColorsStartingX = 250
BrushSliderX, BrushSliderY, BrushSliderWidth, BrushSliderHeight = 10, 555, 10, 40
BackgroundColor = (0, 0, 0)
CurrentPaintColor = (255, 255, 255)
BrushDiameter = 5

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Barty's Paint Program")

for i in range(len(Colors)):
    ColorValues.append((Colors[i], ColorsStartingX + (i * 35), 562, 30, 30))

def ClearScreen(window):
    window.fill(BackgroundColor)


def DrawDot(window, position):
    pygame.draw.circle(window, CurrentPaintColor, position, BrushDiameter)


def DrawBottomControlPanel(window):
    #Background
    pygame.draw.rect(window, (200,200,200), ControlPanelValues)
    #Brush Slider
    pygame.draw.rect(window, (225, 225, 225), (5, 570, 200, 10))
    pygame.draw.rect(window, (0, 0, 0), (BrushSliderX, BrushSliderY, BrushSliderWidth, BrushSliderHeight))
    #Colors
    for i in range(len(ColorValues)):
        pygame.draw.rect(window, ColorValues[i][0], (ColorValues[i][1], ColorValues[i][2], ColorValues[i][3], ColorValues[i][4]))


mainGameLoop = True

while mainGameLoop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGameLoop = False

    if pygame.mouse.get_pressed()[0]:
        CurrentMousePosition = pygame.mouse.get_pos()
        if CurrentMousePosition[1] < ControlPanelValues[1]:
            DrawDot(window, pygame.mouse.get_pos())
        elif CurrentMousePosition[0] < 205 and CurrentMousePosition[0] > 5 and CurrentMousePosition[1] < 595 and CurrentMousePosition[1] > 555:
            BrushSliderX = RoundToNearestMultiple(CurrentMousePosition[0], 4)
            BrushDiameter = int((BrushSliderX - 5) / 4)
        else:
            for i in range(len(ColorValues)):
                if CurrentMousePosition[0] < (ColorValues[i][1] + 30) and CurrentMousePosition[0] > ColorValues[i][1] and CurrentMousePosition[1] < (ColorValues[i][2] + 30) and CurrentMousePosition[1] > ColorValues[i][2]:
                    CurrentPaintColor = ColorValues[i][0]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:
        ClearScreen(window)

    DrawBottomControlPanel(window)
    pygame.display.update()