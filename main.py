from pygame import *
import sys

init()

mixer.init()

rigbymordecai_img = image.load('rigbymordecai.png')
rigbymordecai_img = transform.scale(rigbymordecai_img, (225, 200))

rigbymordecai_font = font.Font('IceCreamPartySolid.ttf', 50)

mixer.music.load('partytonight.mp3')
mixer.music.play(-1)



window = display.set_mode((1280,720))

nuvem_x = 0
velocidade = 3
clock = time.Clock()

window.fill((209, 245, 255))



while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit
    
    nuvem_x += velocidade
    if (850 + nuvem_x) > (1280 + 300):
        nuvem_x = 0

    window.fill((209, 245, 255))
    
    # Desenhar a partir daqui

    # Desenhar primitivas geométricas
    draw.rect(window, (159, 212, 101), (0, 600, 1280, 350))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.circle(window, (255, 247, 185), (140, 100), 55)
    
    draw.polygon(window, (118, 139, 126), ((350, 350), (468, 150), (585, 350)))

    draw.rect(window, (170, 131, 140), (830, 450, 40, 150)) 
    draw.circle(window, (156, 204, 86), (850, 400), 100) 
    
    draw.circle(window, (255, 255, 255), (850 + nuvem_x, 100), 50)
    draw.circle(window, (255, 255, 255), (920 + nuvem_x, 100), 60)
    draw.circle(window, (255, 255, 255), (990 + nuvem_x, 100), 55)
    draw.circle(window, (255, 255, 255), (1060 + nuvem_x, 100), 50)

    draw.line(window, (255, 247, 185), (140, 45), (140, -10), 5)
    draw.line(window, (255, 247, 185), (140, 155), (140, 210), 5)
    draw.line(window, (255, 247, 185), (85, 100), (30, 100), 5)
    draw.line(window, (255, 247, 185), (195, 100), (250, 100), 5)
    draw.line(window, (255, 247, 185), (100, 60), (55, 15), 5)
    draw.line(window, (255, 247, 185), (180, 140), (225, 185), 5)
    draw.line(window, (255, 247, 185), (100, 140), (55, 185), 5)
    draw.line(window, (255, 247, 185), (180, 60), (225, 15), 5)

    draw.rect(window, (255, 255, 255), (480, 460, 80, 140))
    draw.circle(window, (184, 191, 174), (490, 535), 5) 
    draw.rect(window, (171, 186, 179), (375, 430, 80, 100)) 
    

    
    # Desenhar imagens
    window.blit(rigbymordecai_img, (50, 410))

    # Desenhar texto
    rigbymordecai_text = rigbymordecai_font.render('REGULAR SHOW', True, (0,0,0))
    window.blit(rigbymordecai_text, (500, 0))
    
    display.update()
    clock.tick(60)