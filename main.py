import pygame
from classes import *
#Initialize the game
pygame.init()
global gameScreen 
gameScreen = pygame.display.set_mode((1000,600))
deck = Deck()
deck.shuffle()

after_deck =[]

spade_deck=[]
club_deck=[]
diamond_deck=[]
heart_deck=[]
final_deck=[diamond_deck,club_deck,heart_deck,spade_deck]

c7 =deck.pile(7)
c6 = deck.pile(6)
c5 =deck.pile(5)
c4 = deck.pile(4)
c3 =deck.pile(3)
c2 =deck.pile(2)
c1 = deck.pile(1)
pile_lst = [c1,c2,c3,c4,c5,c6,c7]

black = [7,99,36]
col = [87,105,47]

delete_check = []
clicked_lst = []
cover=[]

availible_clicks_lst1 = [c1[-1]]
availible_clicks_lst2 = [c2[-1]]
availible_clicks_lst3 = [c3[-1]]
availible_clicks_lst4 = [c4[-1]]
availible_clicks_lst5 = [c5[-1]]
availible_clicks_lst6 = [c6[-1]]
availible_clicks_lst7 = [c7[-1]]
screen_lst = [availible_clicks_lst1,availible_clicks_lst2,availible_clicks_lst3,availible_clicks_lst4,availible_clicks_lst5,availible_clicks_lst6,availible_clicks_lst7]

clock = pygame.time.Clock()
crash = False
x = 770
y = 30



def draw(pile_lst,screen_lst,after_deck,cover,final_deck):

    start=0
    imageK = pygame.image.load('cards/back_suit.png')
    pygame.draw.rect(gameScreen,black,[0,0,1000,600])

    for c in range(7):
        if c>0:
            for i in range(len(pile_lst[c])-1):
                    i-=1
                    image = pygame.image.load('cards/back_suit.png')
                    gameScreen.blit(image,(pile_lst[c][i+1][1],pile_lst[c][i+1][2]))

        for k in range(len(screen_lst[c])):
            if len(screen_lst[c]) ==0:
                return True
            else:
                card_image = pygame.image.load(screen_lst[c][k][0])
                gameScreen.blit(card_image,(screen_lst[c][k][1],screen_lst[c][k][2]))

    if len(after_deck) > 0:
        after_deck_image = pygame.image.load(after_deck[-1])
        gameScreen.blit(after_deck_image,(50,200))

    if len(after_deck)==0:

        pygame.draw.rect(gameScreen,col,[50,200,74,107])
        pygame.draw.rect(gameScreen,col,[50,75,74,107])

    if len(deck.deck_lst)==0:
        pygame.draw.rect(gameScreen,col,[50,75,74,107])

    else:
        gameScreen.blit(imageK,(50,75))

    fin_y = 75

    for item in final_deck:
        if len(item) == 0:
             pygame.draw.rect(gameScreen,col,[850,fin_y,74,107])

        else:
            final_image = pygame.image.load(item[-1][0])
            gameScreen.blit(final_image,(850,fin_y))

        fin_y+=120


def is_clicked(screen_lst,c_lst,after_deck):
    
    if event.type==pygame.MOUSEBUTTONDOWN:
      
        mx,my = pygame.mouse.get_pos()

        for i in screen_lst:

            if len(i)>0:
            
                if  mx <i[-1][1]+74 and mx>i[-1][1] and my<i[-1][2]+107 and my>i[-1][2]:

                    c_lst.append(i[-1])

                else:
                    if len(i)>1:
                        for b in range(len(i)-1):
                            if mx <i[b][1]+74 and mx>i[b][1] and my<i[b][2]+25 and my>i[b][2]:
                                for q in i[b:]:

                                    c_lst.append(q)

        if mx <50+74 and mx>50 and my<200+107 and my>200:
            if len(after_deck)>0:
                c_lst.append([after_deck[-1],50,200])

        for pile in final_deck:
            if len(pile)>0:
                if mx <pile[-1][1]+74 and mx>pile[-1][1] and my<pile[-1][2]+107 and my>pile[-1][2]:
                    c_lst.append(pile[-1])

                  


def is_second_clicked(screen_lst,clicked_lst,pile_lst,delete_check,final_deck):

    c = 0
      
    ax,ay = pygame.mouse.get_pos()

    for i in screen_lst:

        if len(i) == 0 and is_king(clicked_lst)==True and ax<120+((c+1)*90)+74 and ax>120+((c+1)*90):
            delete_check.append('a')
            for b in range(len(clicked_lst)):
                if len(screen_lst[c])>0:
                    screen_lst[c].append([clicked_lst[b][0],screen_lst[c][-1][1],screen_lst[c][-1][2]+25])
                else:
                    screen_lst[c].append([clicked_lst[b][0],120+((c+1)*90),75])

        elif len(i)>0:
            if  ax <i[-1][1]+74 and ax>i[-1][1] and ay<i[-1][2]+107 and ay>i[-1][2] and colour_check(i[-1][0],clicked_lst[0][0])==True and down_order(i[-1][0],clicked_lst[0][0])==True:
                delete_check.append('a')                   
                for b in range(len(clicked_lst)):
                    screen_lst[c].append([clicked_lst[b][0],screen_lst[c][-1][1],screen_lst[c][-1][2]+25])
        c+=1

    if ax<850+74 and ax>850 and len(clicked_lst) == 1:
        for j in range(4):
            print(clicked_lst[0][0][0])
            if ay<75+107+(j*120) and ay>75+(j*120):
                if len(final_deck[j])>0 and suit_check(clicked_lst[0][0],final_deck[j][0][0]) == True and down_order(clicked_lst[0][0],final_deck[j][-1][0])==True:
                    delete_check.append('a')
                    final_deck[j].append([clicked_lst[0][0],850,75+(j*120)])    
                if len(final_deck[j])==0 and clicked_lst[0][0][6]=='1':
                    delete_check.append('a')
                    final_deck[j].append([clicked_lst[0][0],850,75+(j*120)])  





def del_card(screen_lst,clicked_lst,pile_lst,delete_check,after_deck):

    k=0
    if len(delete_check) ==1:
        for item in range(len(screen_lst)):
            if clicked_lst[0] in screen_lst[item]:
                del_pos = screen_lst[item].index(clicked_lst[0])
                lst_track = item
                k+=1

                for count in range(len(screen_lst[lst_track])-del_pos):
                    screen_lst[lst_track].pop(del_pos)

        if clicked_lst[0][0] in after_deck:
            k+=1
            after_deck.pop(-1)

        for item in range(len(final_deck)):
            if len(final_deck[item])>0 and k==0:
                if clicked_lst[0][0] in final_deck[item][-1]:                
                    final_deck[item].pop(-1)


def next_card(screen_lst,pile_lst):

    for card in range(len(screen_lst)):
        if len(screen_lst[card]) == 0:
            if len(pile_lst[card])>=2:
                screen_lst[card].append([pile_lst[card][-2][0],210+(90*card),75+(25*(-2+len(pile_lst[card])))])
                pile_lst[card].pop(-2)


def colour_check(c1,c2):

    pos1 = c1.index('_')+1
    pos2 = c2.index('_')+1
    black = ['c','s']
    red = ['d','h']

    count1=0
    count2=0

    for term1 in c1:
        if count1 ==pos1:
            c1_val = term1
        count1+=1

    for term2 in c2:
        if count2 == pos2:
            c2_val = term2
        count2+=1

    if c1_val in black and c2_val in red:
        return True
    elif c2_val in black and c1_val in red:
        return True
    else:
        return False


def suit_check(c1,c2):

    pos1 = c1.index('_')+1
    pos2 = c2.index('_')+1
    black = ['c','s']
    red = ['d','h']

    count1=0
    count2=0

    for term1 in c1:
        if count1 ==pos1:
            c1_val = term1
        count1+=1
    for term2 in c2:
        if count2 == pos2:
            c2_val = term2
        count2+=1

    if c1_val==c2_val:
        return True

    else:
        return False

def down_order(c2,c1):

    num=['1','2','3','4','5','6','7','8','9','10','jack','queen','king']

    pos1 = c1.index('_')
    pos2 = c2.index('_')

    check1 = num.index(c1[6:pos1])
    check2 = num.index(c2[6:pos2])

    if check1+1 ==check2:
        return True
    else:
        return False

def is_king(clicked_lst):

    name= clicked_lst[0][0].index('_')

    if clicked_lst[0][0][:name]== 'cards/king':
        return True
    else:
        return False


def deck_clicked(deck,after_deck,cover):

    if event.type==pygame.MOUSEBUTTONDOWN:
        mx,my = pygame.mouse.get_pos() 
        if mx <50+74 and mx>50 and my<75+107 and my>75:
            if len(deck.deck_lst)>0:
                a = deck.pop_card()
                after_deck.append(a)
            else:
                for card in reversed(after_deck):
                    deck.add_card(card)
                for i in range(len((after_deck))):
                    after_deck.pop(0)


def win(final_deck):
    for i in final_deck:
        if not len(i)==13:
            return False
    return True

def win_draw():

    mx,my=pygame.mouse.get_pos()
    pygame.draw.rect(gameScreen,black,[0,0,1000,600])
    pygame.draw.rect(gameScreen,col,[mx,my,74,107])



while not crash:

    for event in pygame.event.get():

        if win(final_deck)==False:

            if len(clicked_lst) == 0:

                is_clicked(screen_lst,clicked_lst,after_deck)
                
            if len(clicked_lst)>0 and event.type == pygame.MOUSEBUTTONUP :

                is_second_clicked(screen_lst,clicked_lst,pile_lst,delete_check,final_deck)
                del_card(screen_lst,clicked_lst,pile_lst,delete_check,after_deck)
                next_card(screen_lst,pile_lst)

                clicked_lst=[]
                delete_check=[]

            deck_clicked(deck,after_deck,cover)
            draw(pile_lst,screen_lst,after_deck,cover,final_deck)

        elif win(final_deck) == True:
            win_draw()

        if event.type == pygame.QUIT:
            crash = True

    
    pygame.display.update()
    clock.tick(60)



       
















