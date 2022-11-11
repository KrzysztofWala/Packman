import pygame
import Objects
import A_star
pygame.init()

xs = 200
ys = 62
size = 60

X_res = 1200
Y_res = 900

points = 0

#############   Loading Map   #############
map_matrix = Objects.LoadMap()

#############   Creating gold   #############
gold_pic = "files\\gold.png"
gold_list=Objects.CreateGoldList(map_matrix, gold_pic)

#############   Create Enemy   #############
ghost_pic = "files\\ghost.png"
enemy = Objects.O_Ghost(5,5,ghost_pic)

#############   Create Packman   #############
packman_pic = "files\\packman.png"
packman = Objects.O_Packman(2,3,packman_pic)


#############   Screen definition   #############
window = pygame.display.set_mode((1600, 1024))
window.fill((100,100,100))

##############################################
#############   Game main loop   #############
##############################################
run = True
while run:
   pygame.time.Clock().tick(20)  # maksymalnie 60 fps
   window.fill((100, 100, 100))

   for event in pygame.event.get():
       if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
           run = False
   key = pygame.key.get_pressed()

   #####   PACKAMN MOVEMENT   #####
   packman.MoveKeyboard(key,map_matrix)

   #####   ENEMY  MOVEMENT   #####
   EnemyMoveDirection = A_star.A_Star_alghorytm(map_matrix,enemy.x_pos, enemy.y_pos, packman.x_pos, packman.y_pos)
   if EnemyMoveDirection != "HIT":
       enemy.MoveDirection(EnemyMoveDirection,map_matrix)

   ######  Display all objects ######
   Objects.DrawMap(map_matrix, window)   # Map drawing
   packman.Display(window)               # Packman drawing



   for x in gold_list:                   # Gold drawing
       x.Display(window)
   for x in gold_list:
       if packman.hitbox.colliderect(x.hitbox):
           gold_list.remove(x)
           points += 1

   enemy.Display(window)                 # Enemy drawing


###########################################
   font_color = (0, 150, 250)
   font_obj = pygame.font.Font("C:\Windows\Fonts\segoeprb.ttf", 25)
   enemy_destination = font_obj.render("enemy.destination: "+str(enemy.destination), True, font_color)
   enemy_x_pos = font_obj.render("enemy.x_pos: "+str(enemy.x_pos), True, font_color)
   enemy_y_pos = font_obj.render("enemy.y_pos: "+str(enemy.y_pos), True, font_color)
   px = font_obj.render("packman.x_cord: "+str(packman.x_pos), True, font_color)
   py = font_obj.render("packman.y_cord: "+str(packman.y_pos), True, font_color)
   # pt = font_obj.render("POINTS: " + str(points), True, font_color)
   window.blit(enemy_destination, (22, 0))
   window.blit(enemy_x_pos, (22, 50))
   window.blit(enemy_y_pos, (22, 100))
   window.blit(px, (22, 150))
   window.blit(py, (22, 200))

###########################################

   pygame.display.update()






