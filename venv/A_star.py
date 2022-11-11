import pygame
import Objects
import math

pygame.init()


class cell:
   def __init__(self, y, x):
       self.X = x
       self.Y = y
       self.G = 0
       self.H = 0
       self.F = 0
       #### C - close / O - Open / N - not used ####
       self.state = "N"
       #### L / R / U/ D / N - not used  ####
       self.direction = "N"

   ####     Caltulating cell parameters: G / H / F_score    ####
   ####     A - starting point / B - ending point           ####
   def CaltulateGHF(self, A, B, pre_cell, direction):
       G = pre_cell.G + 1
       H = math.sqrt((B[0] - self.X) ** 2 + (B[1] - self.Y) ** 2)
       F = G + H
       if self.F == 0 and self.state != "START":
           self.G = G
           self.H = H
           self.F = F
           self.state = "O"
           self.direction = direction

       elif self.F > 0 and self.F > F and self.state != "START":
           self.G = G
           self.H = H
           self.F = F
           self.state = "O"
           self.direction = direction

   ####     Temporary print    ####
   def CellPrint(self):
       print("X: ", self.X)
       print("Y: ", self.Y)
       print("G: ", self.G)
       print("H: ", self.H)
       print("F: ", self.F)
       print("State: ", self.state)
       print("Direction: ", self.direction)


################################################################################
######################           CHECK          ################################
# Checking area for point with lowest F score value
# x, y - current x, y coordinates
# m - game map
# m_c - map with cells
# A / B - starting point / goal point
# l_c - list with open cells
################################################################################
def Check(x, y, m, m_c, A, B, list_cells):
   x_res = len(m)
   y_res = len(m[0])
   reach_the_goal = False
   ####     L    ####
   ####     Reach the goal    ####
   if x - 1 > 0:
       if m_c[x - 1][y].state == "END":
           m_c[x - 1][y].direction = "R"
           reach_the_goal = True
           print("L reach_the_goal = True")
       #### Value in range / no obstackles / not closed cell ####
       elif x - 1 > 0 and m[x - 1][y] == "0" and m_c[x - 1][y].state != "C" and m_c[x - 1][y].state != "START":
           m_c[x - 1][y].CaltulateGHF(A, B, m_c[x][y], "R")
           list_cells.append(m_c[x - 1][y])

   ####     R    ####
   ####     Reach the goal    ####
   if x + 1 < 21:
       if m_c[x + 1][y].state == "END":
           m_c[x + 1][y].direction = "L"
           reach_the_goal = True
           print("R reach_the_goal = True")

       #### Value in range / no obstackles / not closed cell ####
       elif x + 1 < 21 and m[x + 1][y] == "0" and m_c[x + 1][y].state != "C" and m_c[x + 1][y].state != "START":
           m_c[x + 1][y].CaltulateGHF(A, B, m_c[x][y], "L")
           list_cells.append(m_c[x + 1][y])

   ####     U    ####
   ####     Reach the goal    ####
   if y - 1 > 0:
       if m_c[x][y - 1].state == "END":
           m_c[x][y - 1].direction = "D"
           reach_the_goal = True
           print("U reach_the_goal = True")
       #### Value in range / no obstackles / not closed cell ####
       elif y - 1 > 0 and m[x][y - 1] == "0" and m_c[x][y - 1].state != "C" and m_c[x][y - 1].state != "START":
           m_c[x][y - 1].CaltulateGHF(A, B, m_c[x][y], "D")
           list_cells.append(m_c[x][y - 1])

   ####     D    ####
   ####     Reach the goal    ####
   if y + 1 < 16:
       if m_c[x][y + 1].state == "END":
           m_c[x][y + 1].direction = "U"
           reach_the_goal = True
           print("D reach_the_goal = True")
       #### Value in range / no obstackles / not closed cell ####
       elif y + 1 < 16 and m[x][y + 1] == "0" and m_c[x][y + 1].state != "C" and m_c[x][y + 1].state != "START":
           m_c[x][y + 1].CaltulateGHF(A, B, m_c[x][y], "U")
           list_cells.append(m_c[x][y + 1])

   ####    Closing cell - all cells around were checked    ####
   if m_c[x][y].state != "START":
       m_c[x][y].state = "C"

   return (reach_the_goal)


################################################################################

################################################################################
def FindPath(map, map_cells, list_cells, A, B):

   move = "N"
   print ("126: A[0], A[1], B[0], B[1]  ", A[0], A[1], B[0], B[1] )

   if A[0]==B[0] and A[1]==B[1]:
       move = "HIT"
       reach_the_goal = True
   elif A[0]==B[0] and A[1]==B[1]-1:
       move = "D"
       reach_the_goal = True
   elif A[0]==B[0] and A[1]==B[1]+1:
       move = "U"
       reach_the_goal = True
   elif A[1]==B[1] and A[0]==B[0]-1:
       move = "R"
       reach_the_goal = True
   elif A[1]==B[1] and A[0]==B[0]+1:
       move = "L"
       reach_the_goal = True
   else:
       reach_the_goal = False

       while reach_the_goal == False:
           ####     FINDING LOWEST F_score VALUE    ####
           i = 0
           indicator = 0
           lowest_f = list_cells[0].F
           for c in list_cells:
               if lowest_f > c.F:
                   lowest_f = c.F
                   indicator = i
               i += 1
           list_cells[indicator].CellPrint()

           ####     REMOVING CLOSE CELL FROM LIST    ####
           x_d = list_cells[indicator].X
           y_d = list_cells[indicator].Y
           i = 0
           for c in list_cells:
               if c.X == x_d and c.Y == y_d:
                   del list_cells[i]
               i += 1
           ####     Calculating new GHF values for new point    ####
           reach_the_goal = Check(x_d, y_d, map, map_cells, A, B, list_cells)
           print("168 Value reach_the_goal: ", reach_the_goal)

           ######################################### DISPLAY OFF
           if VISIBILITY == True:
               DisplayMaps(map, map_cells)

       ####    Finding first step    ####
       x = B[0]
       y = B[1]
       find = False

       while find == False:

           ######################################### CLOCK OFF
           if VISIBILITY == True:
               pygame.time.Clock().tick(1)

           if map_cells[x][y].direction == "L":
               if map_cells[x - 1][y].state == "START":
                   move = "R"
                   find = True
               else:
                   x -= 1
           elif map_cells[x][y].direction == "R":
               if map_cells[x + 1][y].state == "START":
                   move = "L"
                   find = True
               else:
                   x += 1
           elif map_cells[x][y].direction == "U":
               if map_cells[x][y - 1].state == "START":
                   move = "D"
                   find = True
               else:
                   y -= 1
           elif map_cells[x][y].direction == "D":
               if map_cells[x][y + 1].state == "START":
                   move = "U"
                   find = True
               else:
                   y += 1

       if A[0]==B[0] and A[1] == B[1]:
           move = "HIT"

   return (move)


################################################################################
##################     Display maps -  only for checking    ####################
################################################################################
def DisplayMaps(map, map_cells):
   ##########################################################################################################
   xs = 200
   ys = 62
   size = 60
   X_res = 1200
   Y_res = 900

   pygame.init()
   window = pygame.display.set_mode((1600, 1024))
   window.fill((200, 100, 100))

   PoleGry = pygame.rect.Rect(xs, ys, X_res, Y_res)  # tworzy Pole Gry

   run = True
   while run:
       pygame.time.Clock().tick(30)  # maksymalnie 60 fps
       window.fill((100, 100, 100))

       ################ Drawing map ################
       for i in range(1, len(map)):
           for j in range(1, len(map[0])):
               if map[i][j] == "0":
                   color = [200, 200, 200]
               else:
                   color = [255, 0, 255]
               square = pygame.rect.Rect(200 + 60 * (i - 1), 62 + 60 * (j - 1), 60, 60)  # tworzy prostokąt
               pygame.draw.rect(window, color, square)
       ################ Drawing map of cells ################

       for i in range(1, len(map_cells)):
           for j in range(1, len(map_cells[0])):
               if map_cells[i][j].state == "START":
                   color = [255, 255, 200]
                   display = True
               elif map_cells[i][j].state == "END":
                   color = [0, 0, 255]
                   display = True
               elif map_cells[i][j].state == "O":
                   color = [0, 255, 0]
                   display = True
               elif map_cells[i][j].state == "C":
                   color = [255, 0, 0]
                   display = True
               else:
                   display = False
               if display == True:
                   square = pygame.rect.Rect(200 + 60 * (i - 1), 62 + 60 * (j - 1), 60, 60)  # tworzy prostokąt
                   pygame.draw.rect(window, color, square)
               ###########################################
               if map_cells[i][j].state != "N":
                   font_color = (0, 150, 250)
                   font_obj = pygame.font.Font("C:\Windows\Fonts\segoeprb.ttf", 15)
                   STATE = font_obj.render(str(map_cells[i][j].state) + " D: " + str(map_cells[i][j].direction), True,
                                           font_color)
                   G = font_obj.render("G: " + str(map_cells[i][j].G), True, font_color)
                   H = font_obj.render("H: " + str(round(map_cells[i][j].H, 1)), True, font_color)
                   F = font_obj.render("F: " + str(round(map_cells[i][j].F, 1)), True, font_color)
                   window.blit(STATE, (200 + 60 * (i - 1), 62 - 5 + 60 * (j - 1)))
                   window.blit(G, (200 + 60 * (i - 1), 15 + 62 - 5 + 60 * (j - 1)))
                   window.blit(H, (200 + 60 * (i - 1), 30 + 62 - 5 + 60 * (j - 1)))
                   window.blit(F, (200 + 60 * (i - 1), 45 + 62 - 5 + 60 * (j - 1)))
           ###########################################
       for event in pygame.event.get():
           if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
               run = False
       ### MANUAL/AUTOMATIC SKIP
       run = False
       pygame.display.update()
   ##########################################################################################################


################################################################################


def A_Star_alghorytm(map, Ax, Ay, Bx, By):
   ########################################
   ############# MAIN PROGRAM #############
   ########################################
   #### Chcecking map size ####
   x_res = len(map)
   y_res = len(map[0])

   if Ax==Bx and Ay==By:
       FirstMove = "HIT"
   elif Ax==Bx and Ay==By-1:
       FirstMove = "D"
   elif Ax==Bx and Ay==By+1:
       FirstMove = "U"
   elif Ay==By and Ax==Bx-1:
       FirstMove = "R"
   elif Ay==By and Ax==Bx+1:
       FirstMove = "L"

   else:
       #### Creating empty map of cells ####
       map_cells = [[cell(a, b) for a in range(16)] for b in range(21)]
       #### Creating list of OPEN cells ####
       list_cells = []

       #### Definition of start and end position ####
       A = (Ax, Ay)
       map_cells[A[0]][A[1]].state = "START"
       B = (Bx, By)
       map_cells[B[0]][B[1]].state = "END"

       #########################################
       ############ START ALGHORYTM ############
       #########################################

       ####   INITIAL STEP   ####
       Check(A[0], A[1], map, map_cells, A, B, list_cells)

       ######################################### DISPLAY OFF
       if VISIBILITY == True:
           DisplayMaps(map, map_cells)

       #####   Finding path from A to B   #####
       FirstMove = FindPath(map, map_cells, list_cells,A, B)

   return (FirstMove)


###########################################
###  FOR ALGHORYTM PRESENTATION ONLY  #####
###########################################

map = Objects.LoadMap() # loading from file

# VISIBILITY = False
VISIBILITY = True

move = A_Star_alghorytm(map, 10, 10, 4, 3)
