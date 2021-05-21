import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Card Game: War")

class card:
  def __init__(self, suit, number):
        self.suit = suit
        self.number = number
  def draw(self, x, y):
        pygame.draw.rect(screen, (255,255,255), (x, y, 100, 180))
        pygame.draw.rect(screen, (0,0,0), (x, y, 100, 180),3)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text1 = font.render(str (self.number), 1, (0, 0, 0))
        text2 = font.render(str(self.suit), 1, (250, 0, 0))
        screen.blit(text1, (x+30,y+30))
        screen.blit(text2, (x+10,y+60))

deck = list()
for j in range(4):
  for i in range(13):
    deck.append(card(j,i))

random.shuffle(deck)
p1hand = list()
p2hand = list()
p1discard = list()
P2discard = list()
for i in range(26):
  p1hand.append(deck[i])
for j in range(26,52):
  p2hand.append(deck[j])


turn = False







doExit = False
clock = pygame.time.Clock()
while not doExit:
  clock.tick(60)
  event = pygame.event.wait()

  if event.type == pygame.QUIT:
    doExit = True

  if event.type == pygame.MOUSEBUTTONDOWN:
    turn = True

  if event.type == pygame.MOUSEBUTTONUP:
    turn = False

  if event.type == pygame.MOUSEMOTION:
    mousePos=event.pos

  #------Game Logic--------
  if len(p1hand)>0 or len(p2hand)>0:
    if p1discard > P2discard:
      print("player 1 wins")
    else:
      print("player 2 wins")
    doExit = True
  if turn and len(p1hand)>0 and len(p2hand)>0:
  
    if p1hand[len(p1hand)-1].number>  p2hand[len(p2hand)-1].number:
      print("player 1 wins round!")
      p1discard.append(p1hand[len(p1hand)-1])
      p1discard.append(p2hand[len(p2hand)]-1)
      p1hand.pop(p1hand[len(p1hand)]-1)
      p2hand.pop(p2hand[len(p2hand)]-1)
    else:
      print("player 2 wins round")
      P2discard.append(p1hand[len(p1hand)-1])
      P2discard.append(p2hand[len(p2hand)]-1)
      p1hand.pop(p1hand[len(p1hand)]-1)
      p2hand.pop(p2hand[len(p2hand)]-1)



  screen.fill((0,150,0))
  
  #for i in range(52):
    #deck[i].draw(20+i*5,20+i*3)

  for i in range(0, 26):
    p1hand[i].draw(200,50)


  for i in range(0, 26):
    p2hand[i].draw(200,250)

  for i in range(0,len(p1hand)):
    p1hand[i].draw(200,50)

  for i in range(0,len(p2hand)):
    p2hand[i].draw(200,250)

  for i in range(0,len(p1discard)):
    p1discard[i].draw(400+4*i,50)
  
  for i in range(0,len(P2discard)):
    P2discard[i].draw(400+4*i,250)


  pygame.display.flip()



pygame.quit()
