import pygame
import sprite_class

#iniciar o pygame
pygame.init()

#criando as dimensoes da tela
screen_width = 500
screnn_height = 500

#criando a janela do jogo
screen = pygame.display.set_mode((screen_width, screnn_height))
pygame.display.set_caption('spritesheets')

sprite_sheets_image = pygame.image.load("animacoes frente e verso mario.png").convert_alpha()
sprite_sheet = sprite_class.SpriteSheet(sprite_sheets_image)

BG = (0,0,0)
black = (0,0,0)
roxo = (146, 144,255)

#criar uma lsita de frames
animation_list = []
animation_steps = [4,1,4,1]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 160
frame = 0
step_counter = 0
posicao_x = 20
azul = (0, 219, 255)

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_images_from_spritesheets(step_counter, 16, 16, 3, roxo))
        step_counter += 1
    animation_list.append(temp_img_list)


run = True
while run:

    #preencher a tela
    screen.fill(BG)

    #atualizar a animacao
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0


    #mostrar um dos sprites
    screen.blit(animation_list[action][frame], (posicao_x,250-16))

    

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list)-1:
                action += 1
                frame = 0
            
        
                   
                



    
    pygame.display.update()

pygame.quit

