from pygame import *

init()

mixer.init()
window = display.set_mode((1280,720))
running = True
clock = time.Clock()

rigbymordecai_img = image.load('rigbymordecai.png')
rigbymordecai_img = transform.scale(rigbymordecai_img, (225, 200))

rigbymordecai_font = font.Font('IceCreamPartySolid.ttf', 50)

mixer.music.load('partytonight.mp3')
mixer.music.play(-1)

sol_x = 140
nuvem_x = 850
velocidade_nuvem = 3


window.fill((209, 245, 255))



while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
            
    
    nuvem_x += velocidade_nuvem
    
    if nuvem_x <=45 or nuvem_x>=1025:
       velocidade_nuvem = -velocidade_nuvem

    
    dt = clock.get_time()/1000
    keys = key.get_pressed()

    if keys[K_d]:
       sol_x = sol_x + 300 * dt
    elif keys[K_a]:
       sol_x = sol_x + -300 * dt


    window.fill((209, 245, 255))
    
    # Desenhar a partir daqui

    # Desenhar primitivas geométricas
    draw.rect(window, (159, 212, 101), (0, 600, 1280, 350))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.circle(window, (255, 247, 185), (sol_x, 100), 55)
    
    draw.polygon(window, (118, 139, 126), ((350, 350), (468, 150), (585, 350)))

    draw.rect(window, (170, 131, 140), (830, 450, 40, 150)) 
    draw.circle(window, (156, 204, 86), (850, 400), 100) 
    
    draw.circle(window, (255, 255, 255), (nuvem_x, 100), 50)
    draw.circle(window, (255, 255, 255), (nuvem_x + 70, 100), 60)
    draw.circle(window, (255, 255, 255), (nuvem_x + 140, 100), 55)
    draw.circle(window, (255, 255, 255), (nuvem_x + 210, 100), 50)

    draw.line(window, (255, 247, 185), (sol_x, 45), (sol_x, -10), 5)
    draw.line(window, (255, 247, 185), (sol_x, 155), (sol_x, 210), 5)
    draw.line(window, (255, 247, 185), (sol_x - 55, 100), (sol_x - 110, 100), 5)
    draw.line(window, (255, 247, 185), (sol_x + 55, 100), (sol_x + 110, 100), 5)
    draw.line(window, (255, 247, 185), (sol_x - 40, 60), (sol_x - 85, 15), 5)
    draw.line(window, (255, 247, 185), (sol_x + 40, 140), (sol_x + 85, 185), 5)
    draw.line(window, (255, 247, 185), (sol_x - 40, 140), (sol_x - 85, 185), 5)
    draw.line(window, (255, 247, 185), (sol_x + 40, 60), (sol_x + 85, 15), 5)

    draw.rect(window, (255, 255, 255), (480, 460, 80, 140))
    draw.circle(window, (184, 191, 174), (490, 535), 5) 
    draw.rect(window, (171, 186, 179), (375, 430, 80, 100)) 
    

    
    # Desenhar imagens
    window.blit(rigbymordecai_img, (50, 410))

    # Desenhar texto
    rigbymordecai_text = rigbymordecai_font.render('REGULAR SHOW', True, (0,0,0))
    window.blit(rigbymordecai_text, (500, 0))
    
    display.update()
    