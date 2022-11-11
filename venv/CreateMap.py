import pygame
pygame.font.init()

xs = 200
ys = 62
size = 60

X_res = 1200
Y_res = 900

matrix = [[0 for x in range(16)] for y in range(21)]

def MousePos(win):
  red = (200, 0, 0)
  font = pygame.font.SysFont("arial",25)
  pos=pygame.mouse.get_pos()

  napis = font.render("MOUSE POSITION"+str(pygame.mouse.get_pos()),True,red)
  napis2= font.render("buttons:"+str(pygame.mouse.get_pressed()),True,red)
  win.blit(napis, [10, 10])
  win.blit(napis2, [10, 50])

def MouseFuntcion (win,button, tab):
  print(button)
  XY=pygame.mouse.get_pos()
  Xs= int((XY[0]-140)/60)
  Ys= int((XY[1]-2)/60 )
  print (Xs,Ys )

  # Prawy  przycisk
  if button==3 and Xs<21 and Ys<16:
      if tab[Xs][Ys] == 0:
          tab[Xs][Ys] = 1
      else:
          tab[Xs][Ys] = 0

  # Lewy przycisk
  elif button == 1:
      run2 = True
      solution = True

      while run2:
          pygame.time.Clock().tick(60)  # maksymalnie 60 fps

          XYe = pygame.mouse.get_pos()
          Xe = int((XYe[0] - 140) / 60)
          Ye = int((XYe[1] - 2) / 60)

          # WYświetlenie ekranu, pola gry, matrix
          window.fill((100, 100, 100))
          pygame.draw.rect(window, (220, 200, 20), PoleGry)
          DrawSquare(window, tab)

          if (Xe-Xs>=0):
              ix=1
          else:
              ix=-1
          if (Ye-Ys>=0):
              iy=1
          else:
              iy=-1

          tab2 = [[0 for x in range(16)] for y in range(21)]

          if (0<Xe<21 and 0<Ye<16):
              tab2[Xs][Ys] = 1
              if solution == True:
                  a=Xs
                  while a!=Xe:
                      a+=ix
                      SquareTemp = pygame.rect.Rect(a * 60 + 140, Ys * 60 + 2, 60, 60)
                      pygame.draw.rect(window, (150, 150, 150), SquareTemp)
                      tab2[a][Ys]=1

                  a=Ys
                  while a!=Ye:
                      a+=iy
                      SquareTemp = pygame.rect.Rect(Xe * 60 + 140, a * 60 + 2, 60, 60)
                      pygame.draw.rect(window, (150, 150, 150), SquareTemp)
                      tab2[Xe][a]=1
              else:
                  a = Ys
                  while a != Ye:
                      a += iy
                      SquareTemp = pygame.rect.Rect(Xs * 60 + 140, a * 60 + 2, 60, 60)
                      pygame.draw.rect(window, (150, 150, 150), SquareTemp)
                      tab2[Xs][a]=1

                  a = Xs
                  while a != Xe:
                      a += ix
                      SquareTemp = pygame.rect.Rect(a * 60 + 140, Ye * 60 + 2, 60, 60)
                      pygame.draw.rect(window, (150, 150, 150), SquareTemp)
                      tab2[a][Ye]=1

              SquareTemp = pygame.rect.Rect(Xs * 60 + 140, Ys * 60 + 2, 60, 60)
              pygame.draw.rect(window, (150, 150, 150), SquareTemp)



          drawline(window)
          pygame.display.update()

          for event in pygame.event.get():
              if event.type == pygame.MOUSEBUTTONUP and event.button == 3:  # wyjście z trybu
                  run2 = False
              elif event.type == pygame.MOUSEBUTTONUP and event.button == 2: #zmiana solution
                  solution = not solution
              elif event.type == pygame.MOUSEBUTTONUP:  # zapisanie rozwiązania
                  for i in range(0,21):
                      for j in range(0,16):
                          if tab2[i][j]:
                              tab[i][j]=tab2[i][j]
                  run2 = False

def DrawSquare(win,tab):
  for i in range (1,21):
      for j in range(1,16):
          if tab[i][j] == 1:
              square = pygame.rect.Rect(200+60*(i-1), 62+60*(j-1), 60, 60)  # tworzy prostokąt
              pygame.draw.rect(win, (20, 220, 20), square)

def drawline (win):
  red = (200,0,0)
  for i in range (1,21):
      pygame.draw.line(win,red, (200+60*i,62),(200+60*i,962) )
  for i in range (1,16):
      pygame.draw.line(win,red, (200,62+60*i),(1400,62+60*i) )

def SaveMaps(lista):
    #    filepath = "files\\1map.txt"
    #    f = open(filepath, "r", encoding="utf-8")
  filepath = "C:\\Users\\home\\PycharmProjects\\GAME_ONE\\files\\map.txt"
  # f = open("xxxxx.txt", "w")
  f = open(filepath, "w")
  for x in lista:
      for y in x:
          f.write(str(y))
      f.write("\n")
  print("SAVE DONE")


pygame.init()
window = pygame.display.set_mode((1600, 1024))
window.fill((100,100,100))

PoleGry = pygame.rect.Rect(xs, ys, X_res, Y_res)  # tworzy Pole Gry


run = True
while run:
  pygame.time.Clock().tick(60)  # maksymalnie 60 fps
  window.fill((100, 100, 100))




  for event in pygame.event.get():
      if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
          run = False
      elif event.type == pygame.MOUSEBUTTONUP:  # jeśli gracz zamknie okienko
          MouseFuntcion(window, event.button, matrix)

  # Pole gry
  pygame.draw.rect(window, (220, 200, 20), PoleGry)
  # Rysowanie oznaczonych kwadratów
  DrawSquare(window, matrix)
  # Siatka
  drawline(window) # funkcja
  MousePos(window) # funkcja
  pygame.display.update()

  # SaveMaps(matrix)



SaveMaps(matrix)


