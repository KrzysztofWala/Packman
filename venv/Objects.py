import pygame

def LoadMap ():
   matrix = [[0 for x in range(16)] for y in range(21)]
   filepath = "C:\\Users\\home\\PycharmProjects\\GAME_ONE\\files\\map.txt"
   f = open(filepath, "r", encoding="utf-8")
   znak = f.read(1)
   x=0
   Xpp="dd"
   y=0
   while znak:
       if znak != "1" and znak != "0":
           x+=1
           y=0
       else:
           matrix[x][y]=znak
           y+=1
       znak = f.read(1)
   return(matrix)

def CreateGoldList(matrix, pic):
   x_res = len(matrix)
   y_res = len(matrix[0])
   gold_list = []

   for i in range(1,x_res):
       for j in range(1, y_res):
           if matrix[i][j] == "0":
               # gold_list.append(O_Gold((140+i*60+20),(2+j*60+20),pic))
               gold_list.append(O_Gold(i,j,pic))
   return (gold_list)

def DrawMap(matrix, window):
   red = pygame.image.load("files\\red.png")
   green = pygame.image.load("files\\green.png")
   x_res = len(matrix)
   y_res = len(matrix[0])

   for i in range(1,x_res):
       for j in range(1, y_res):
           if matrix[i][j] == "0":
               window.blit(green, (140+i*60,2+j*60))
           else:
               window.blit(red, (140 + i * 60, 2 + j * 60))


class Figure:
   def __init__(self, x, y, pic):
       self.acc = 15
       self.x_pos = x
       self.y_pos = y
       self.x_cord = 140+60*x
       self.y_cord = 2+60*y
       self.x_des = 0
       self.y_des = 0
       self.destination = "stop"
       self.next_destination = "stop"
       self.picture = pygame.image.load(pic)

   def MoveKeyboard(self, pressed_key, map_matrix):
       #############################################
       #####   Choosing direction of movement   ####
       #############################################
       self.acc = 30
       ###  Button RIGHT ###
       if pressed_key[pygame.K_RIGHT]:
           if self.destination == "U":
               if map_matrix[self.x_pos+1][self.y_pos-1]=="0":
                   self.next_destination="R"
               else:
                   self.next_destination = "stop"
           elif self.destination == "D":
               if map_matrix[self.x_pos+1][self.y_pos+1]=="0":
                   self.next_destination="R"
               else:
                   self.next_destination = "stop"
           elif self.destination == "L":
               self.destination = "R"
               self.x_des = self.x_pos
               self.y_des = self.y_pos
           elif self.destination == "stop" and map_matrix[self.x_pos+1][self.y_pos] == "0":
               self.destination = "R"
               self.x_des = self.x_pos+1
               self.y_des = self.y_pos
       ###  Button LEFT ###
       elif pressed_key[pygame.K_LEFT]:
           if self.destination == "U":
               if map_matrix[self.x_pos-1][self.y_pos-1]=="0":
                   self.next_destination="L"
               else:
                   self.next_destination = "stop"
           elif self.destination == "D":
               if map_matrix[self.x_pos-1][self.y_pos+1]=="0":
                   self.next_destination="L"
               else:
                   self.next_destination = "stop"
           elif self.destination == "R":
               self.destination = "L"
               self.x_des = self.x_pos
               self.y_des = self.y_pos
           elif self.destination == "stop" and map_matrix[self.x_pos-1][self.y_pos] == "0":
               self.destination = "L"
               self.x_des = self.x_pos-1
               self.y_des = self.y_pos
       ###  Button UP ###
       elif pressed_key[pygame.K_UP]:
           if self.destination == "L":
               if map_matrix[self.x_pos-1][self.y_pos-1]=="0":
                   self.next_destination="U"
               else:
                   self.next_destination = "stop"
           elif self.destination == "R":
               if map_matrix[self.x_pos+1][self.y_pos-1]=="0":
                   self.next_destination="U"
               else:
                   self.next_destination = "stop"
           elif self.destination == "D":
               self.destination = "U"
               self.x_des = self.x_pos
               self.y_des = self.y_pos
           elif self.destination == "stop" and map_matrix[self.x_pos][self.y_pos-1] == "0":
               self.destination = "U"
               self.x_des = self.x_pos
               self.y_des = self.y_pos-1
       ###  Button DOWN ###
       elif pressed_key[pygame.K_DOWN]:
           if self.destination == "L":
               if map_matrix[self.x_pos-1][self.y_pos+1]=="0":
                   self.next_destination="D"
               else:
                   self.next_destination = "stop"
           elif self.destination == "R":
               if map_matrix[self.x_pos+1][self.y_pos+1]=="0":
                   self.next_destination="D"
               else:
                   self.next_destination = "stop"
           elif self.destination == "U":
               self.destination = "D"
               self.x_des = self.x_pos
               self.y_des = self.y_pos
           elif self.destination == "stop" and map_matrix[self.x_pos][self.y_pos+1] == "0":
               self.destination = "D"
               self.x_des = self.x_pos
               self.y_des = self.y_pos+1

       ###############################################
       #####   Defining destination cordinates    ####
       ###############################################
       ###  Moving RIGHT ###
       if self.destination == "R":
           self.x_cord+=self.acc
           if self.x_cord==self.x_des*60+140:
               self.x_pos = self.x_des
               self.y_pos = self.y_des
               self.destination = self.next_destination
               ### Defining cordinates for new destination ###
               if self.next_destination == "L":
                   self.x_des -= 1
               elif self.next_destination == "R":
                   self.x_des += 1
               elif self.next_destination == "U":
                   self.y_des -= 1
               elif self.next_destination == "D":
                   self.y_des += 1
               self.next_destination = "stop"
       ###  Moving RIGHT ###
       if self.destination == "L":
           self.x_cord-=self.acc
           if self.x_cord==self.x_des*60+140:
               self.x_pos = self.x_des
               self.y_pos = self.y_des
               self.destination = self.next_destination
               ### Defining cordinates for new destination ###
               if self.next_destination == "L":
                   self.x_des -= 1
               elif self.next_destination == "R":
                   self.x_des += 1
               elif self.next_destination == "U":
                   self.y_des -= 1
               elif self.next_destination == "D":
                   self.y_des += 1
               self.next_destination = "stop"
       ###  Moving UP ###
       if self.destination == "U":
           self.y_cord-=self.acc
           if self.y_cord==self.y_des*60+2:
               self.x_pos = self.x_des
               self.y_pos = self.y_des
               self.destination = self.next_destination
               ### Defining cordinates for new destination ###
               if self.next_destination == "L":
                   self.x_des -= 1
               elif self.next_destination == "R":
                   self.x_des += 1
               elif self.next_destination == "U":
                   self.y_des -= 1
               elif self.next_destination == "D":
                   self.y_des += 1
           self.next_destination = "stop"
       ###  Moving DOWN ###
       if self.destination == "D":
           self.y_cord+=self.acc
           if self.y_cord==self.y_des*60+2:
               self.x_pos = self.x_des
               self.y_pos = self.y_des
               self.destination = self.next_destination
               ### Defining cordinates for new destination ###
               if self.next_destination == "L":
                   self.x_des -= 1
               elif self.next_destination == "R":
                   self.x_des += 1
               elif self.next_destination == "U":
                   self.y_des -= 1
               elif self.next_destination == "D":
                   self.y_des += 1
               self.next_destination = "stop"

   def MoveDirection(self, direction, map_matrix):
       ###############################################
       #####   Defining destination cordinates    ####
       ###############################################
       if self.destination == "stop":
           self.destination = direction

       ###  Moving RIGHT ###
       if self.destination == "R":
           self.x_cord+=self.acc
           if self.x_cord==self.x_pos*60+140+60:
               self.destination = "stop"
               self.x_pos+=1
       ###  Moving LEFT ###
       if self.destination == "L":
           self.x_cord-=self.acc
           if self.x_cord==self.x_pos*60+140-60:
               self.destination = "stop"
               self.x_pos -= 1
       ###  Moving UP ###
       if self.destination == "U":
           self.y_cord-=self.acc
           if self.y_cord==self.y_pos*60+2-60:
               self.destination = "stop"
               self.y_pos -= 1
       ###  Moving DOWN ###
       if self.destination == "D":
           self.y_cord+=self.acc
           if self.y_cord==self.y_pos*60+2+60:
               self.destination = "stop"
               self.y_pos += 1

   def Display(self, window):
       window.blit(self.picture, (self.x_cord,self.y_cord))

class O_Packman(Figure):
   def __init__(self,x, y, pic):
       super().__init__(x, y, pic)
       self.hitbox = pygame.Rect(self.x_cord+15, self.y_cord+15, 30, 30)
       self.img_R = pygame.image.load("files\\packman.png")
       self.img_L = pygame.image.load("files\\packman_L.png")
       self.img_U = pygame.image.load("files\\packman_U.png")
       self.img_D = pygame.image.load("files\\packman_D.png")

   def Display(self, window):
       self.hitbox = pygame.Rect(self.x_cord + 15, self.y_cord + 15, 30, 30)
       # pygame.draw.rect(window, (20, 200, 20), self.hitbox)
       if self.destination == "L":
           self.picture = self.img_L
       elif self.destination == "R":
           self.picture = self.img_R
       elif self.destination == "D":
           self.picture = self.img_D
       elif self.destination == "U":
           self.picture = self.img_U
       window.blit(self.picture, (self.x_cord, self.y_cord))

class O_Gold(Figure):
   def __init__(self,x, y, pic):
       super().__init__(x, y, pic)
       self.hitbox = pygame.Rect(self.x_cord + 15, self.y_cord + 15, 30, 30)
   def Display(self, window):
       self.hitbox = pygame.Rect(self.x_cord + 15, self.y_cord + 15, 30, 30)
       # pygame.draw.rect(window, (220, 200, 220), self.hitbox)
       window.blit(self.picture, (self.x_cord, self.y_cord))

class O_Ghost(Figure):
   def __init__(self,x, y, pic):
       super().__init__(x, y, pic)
       self.hitbox = pygame.Rect(self.x_cord+15, self.y_cord+15, 30, 30)
       self.img_R = pygame.image.load("files\\packman.png")
       self.img_L = pygame.image.load("files\\packman_L.png")
       self.img_U = pygame.image.load("files\\packman_U.png")
       self.img_D = pygame.image.load("files\\packman_D.png")

   def Display(self, window):
       self.hitbox = pygame.Rect(self.x_cord + 15, self.y_cord + 15, 30, 30)
       window.blit(self.picture, (self.x_cord+5, self.y_cord+5))
