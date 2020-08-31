import pygame
import os
import random
import sys
import time
from pygame.locals import *
import itertools


pygame.init()

screen = pygame.display.set_mode((1500,750))

play =True

pygame.display.set_caption("RUMMY")


xc=50
y_u=100
y_d=500
x_change=0
y_change=0
z=0
y=0


suits = ["c" , "d" , "h" , "s"]
cards_num = []
for i in range(1,14):
    if i<10:
        cards_num.append("0"+str(i))
    else:
        cards_num.append(str(i))

deck=[]

for j in cards_num:
    for k in suits:
        t=j+k
        deck.append(t)
        deck.append(t)

random.shuffle(deck)

sample_p=[]
sample_c=[]
deck_dis=[]

for i  in range(13):
    sample_p.append(deck[i])
    deck.pop(i)

for i in range(13):
    sample_c.append(deck[i])
    deck.pop(i)

m=deck.pop()
deck_dis.append(m)


c3_1_p=[]
c3_2_p=[]
c3_3_p=[]
c4_p=[]

c3_1_c=[]
c3_2_c=[]
c3_3_c=[]
c4_c=[]
v_3=[]
v_4=[]


c3_sets_c=[]
c3_sets_d=[]
c3_sets_h=[]
c3_sets_s=[]
c3_sets_id1=[]
c3_sets_id2=[]
c3_sets_id3=[]
c3_sets_id4=[]


for i in range(1,12):
    c3_sets_c.append([str(i),str(i+1),str(i+2)])
c3_sets_c.append([str(1),str(12),str(13)])
for j in c3_sets_c:
    for i in range(3):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c3_sets_c:
    for j in range(3):
        i[j]=i[j]+suits[0]


for i in range(1,12):
    c3_sets_d.append([str(i),str(i+1),str(i+2)])
c3_sets_d.append([str(1),str(12),str(13)])
for j in c3_sets_d:
    for i in range(3):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c3_sets_d:
    for j in range(3):
        i[j]=i[j]+suits[1]



for i in range(1,12):
    c3_sets_h.append([str(i),str(i+1),str(i+2)])
c3_sets_h.append([str(1),str(12),str(13)])
for j in c3_sets_h:
    for i in range(3):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c3_sets_h:
    for j in range(3):
        i[j]=i[j]+suits[2]





for i in range(1,12):
    c3_sets_s.append([str(i),str(i+1),str(i+2)])
c3_sets_s.append([str(1),str(12),str(13)])
for j in c3_sets_s:
    for i in range(3):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c3_sets_s:
    for j in range(3):
        i[j]=i[j]+suits[3]




for i in range(1,14):
    c3_sets_id1.append([str(i),str(i),str(i)])
for j in c3_sets_id1:
    for i in range(3):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c3_sets_id1:
    i[0] = i[0]+ suits[0]
    i[1] = i[1]+ suits[1]
    i[2] = i[2]+ suits[2]



for i in range(1,14):
    c3_sets_id2.append([str(i),str(i),str(i)])
for j in c3_sets_id2:
    for i in range(3):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c3_sets_id2:
    i[0] = i[0]+ suits[0]
    i[1] = i[1]+ suits[1]
    i[2] = i[2]+ suits[3]



for i in range(1,14):
    c3_sets_id3.append([str(i),str(i),str(i)])
for j in c3_sets_id3:
    for i in range(3):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c3_sets_id3:
    i[0] = i[0]+ suits[0]
    i[1] = i[1]+ suits[2]
    i[2] = i[2]+ suits[3]



for i in range(1,14):
    c3_sets_id4.append([str(i),str(i),str(i)])
for j in c3_sets_id4:
    for i in range(3):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c3_sets_id4:
    i[0] = i[0]+ suits[1]
    i[1] = i[1]+ suits[2]
    i[2] = i[2]+ suits[3]


f_3_sets=c3_sets_c +c3_sets_d+c3_sets_h+c3_sets_s+c3_sets_id1+c3_sets_id2+c3_sets_id3+c3_sets_id4


c4_sets_c=[]
c4_sets_d=[]
c4_sets_h=[]
c4_sets_s=[]
c4_sets_id=[]


for i in range(1,11):
    c4_sets_c.append([str(i),str(i+1),str(i+2),str(i+3)])
c4_sets_c.append([str(1),str(11),str(12),str(13)])
for j in c4_sets_c:
    for i in range(4):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c4_sets_c:
    for j in range(4):
        i[j]=i[j]+suits[0]



for i in range(1,11):
    c4_sets_d.append([str(i),str(i+1),str(i+2),str(i+3)])
c4_sets_d.append([str(1),str(11),str(12),str(13)])
for j in c4_sets_d:
    for i in range(4):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c4_sets_d:
    for j in range(4):
        i[j]=i[j]+suits[1]


for i in range(1,11):
    c4_sets_h.append([str(i),str(i+1),str(i+2),str(i+3)])
c4_sets_h.append([str(1),str(11),str(12),str(13)])
for j in c4_sets_h:
    for i in range(4):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c4_sets_h:
    for j in range(4):
        i[j]=i[j]+suits[2]


for i in range(1,11):
    c4_sets_s.append([str(i),str(i+1),str(i+2),str(i+3)])
c4_sets_s.append([str(1),str(11),str(12),str(13)])
for j in c4_sets_s:
    for i in range(4):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c4_sets_s:
    for j in range(4):
        i[j]=i[j]+suits[3]



for i in range(1,14):
    c4_sets_id.append([str(i),str(i),str(i),str(i)])
for j in c4_sets_id:
    for i in range(3):
        if int(j[i])<10:
            j[i]= '0'+j[i]
for i in c4_sets_id:
    i[0] = i[0]+ suits[0]
    i[1] = i[1]+ suits[1]
    i[2] = i[2]+ suits[2]
    i[3] = i[3]+ suits[3]


f_4_sets  = c4_sets_c+c4_sets_d+c4_sets_h+c4_sets_s+c4_sets_id


def disp():


    myfont = pygame.font.Font("FreeSansBold.ttf",34)
    mytext = myfont.render("CPU", True, (0,0,0))
    screen.blit(mytext, (200,60))


    myfont = pygame.font.Font("FreeSansBold.ttf",34)
    mytext = myfont.render("YOU", True, (0,0,0))
    screen.blit(mytext, (200,620))

    
    myfont = pygame.font.Font("FreeSansBold.ttf",28)
    mytext = myfont.render("Points:", True, (191,13,182))
    screen.blit(mytext, (100,670))

    myfont = pygame.font.Font("FreeSansBold.ttf",28)
    mytext = myfont.render(str(sy), True, (23,15,186))
    screen.blit(mytext, (250,670))

    myfont = pygame.font.Font("FreeSansBold.ttf",28)
    mytext = myfont.render("Points:", True, (191,13,182))
    screen.blit(mytext, (100,20))

    myfont = pygame.font.Font("FreeSansBold.ttf",28)
    mytext = myfont.render(str(sc), True, (23,15,186))
    screen.blit(mytext, (250,20))

    myfont = pygame.font.Font("FreeSansBold.ttf",14)
    mytext = myfont.render("1st 3 Cards Set", True, (0,0,0))
    screen.blit(mytext, (550,630))

    myfont = pygame.font.Font("FreeSansBold.ttf",14)
    mytext = myfont.render("2nd 3 Cards Set", True, (0,0,0))
    screen.blit(mytext, (800,630))

    myfont = pygame.font.Font("FreeSansBold.ttf",14)
    mytext = myfont.render("3rd 3 Cards Set", True, (0,0,0))
    screen.blit(mytext, (1050,630))

    myfont = pygame.font.Font("FreeSansBold.ttf",14)
    mytext = myfont.render("4 Cards Set", True, (0,0,0))
    screen.blit(mytext, (1325,630))


    myfont = pygame.font.Font("FreeSansBold.ttf",14)
    mytext = myfont.render("1st 3 Cards Set", True, (0,0,0))
    screen.blit(mytext, (550,75))

    myfont = pygame.font.Font("FreeSansBold.ttf",14)
    mytext = myfont.render("2nd 3 Cards Set", True, (0,0,0))
    screen.blit(mytext, (800,75))

    myfont = pygame.font.Font("FreeSansBold.ttf",14)
    mytext = myfont.render("3rd 3 Cards Set", True, (0,0,0))
    screen.blit(mytext, (1050,75))

    myfont = pygame.font.Font("FreeSansBold.ttf",14)
    mytext = myfont.render("4 Cards Set", True, (0,0,0))
    screen.blit(mytext, (1325,75))

    screen.blit(pygame.image.load('Image/back111.gif'),(400,300))
    #screen.blit(pygame.image.load('Image/done.png'),(50,300))
    screen.blit(pygame.image.load('Image/declare.png'),(900,325))

    

    if z==0 :
        myfont = pygame.font.Font("FreeSansBold.ttf",38)
        mytext = myfont.render("Pick a Card", True, (255,0,0))
        screen.blit(mytext, (800,670))


    if z==1 :
        myfont = pygame.font.Font("FreeSansBold.ttf",38)
        mytext = myfont.render("Throw a Card", True, (255,0,0))
        screen.blit(mytext, (800,670))
        


    if y%2==0 and y!=0:
        myfont = pygame.font.Font("FreeSansBold.ttf",38)
        mytext = myfont.render("CPU's Turn", True, (255,0,0))
        screen.blit(mytext, (800,20))
        
        

    if game_lost:
        screen.blit(pygame.image.load('Image/you_lose.jpeg'),(0,0))
        
        
    if game_won:
        screen.blit(pygame.image.load('Image/you_won.jpg'),(0,0))
        


game_won = False
game_lost =False



while play:

    screen.fill((30,150,35))

    mx,my = pygame.mouse.get_pos()

    score_you=[]
    score_cpu=[]

    
        
    for i in range(len(deck)):
        screen.blit(pygame.image.load('Image/'+deck[i]+'.gif'),(400,300))


    for i in range(len(sample_p)):
        screen.blit(pygame.image.load('Image/'+sample_p[i]+'.gif'),(xc + 25* i,y_d))


    for i in sample_p:
        k=int(i[0:2])
        if 2<=k<=9:
            score_you.append(k)
        if 10<= k <=13 or k==1:
            score_you.append(10)
    sy=sum(score_you)



    for i in range(len(sample_c)):
        screen.blit(pygame.image.load('Image/'+sample_c[i]+'.gif'),(xc + 25* i,y_u))
        screen.blit(pygame.image.load('Image/back111.gif'),(xc + 25* i,y_u))


    for i in sample_c:
        k=int(i[0:2])
        if 2<=k<=9:
            score_cpu.append(k)
        if 10<= k <=13 or k==1:
            score_cpu.append(10)
    sc=sum(score_cpu)


    if len(deck_dis) >0:
        screen.blit(pygame.image.load('Image/'+deck_dis[len(deck_dis)-1]+'.gif'),(650,300))
    else:
        screen.blit(pygame.image.load('Image/bottom01.gif'),(650,300))

    
    if len(c3_1_p)==4:
        r_1=c3_1_p.pop(0)
        sample_p.append(r_1)
    for i in range(len(c3_1_p)):
        screen.blit(pygame.image.load('Image/'+c3_1_p[i]+'.gif'),(500 + 50*i,500))



    if len(c3_2_p)==4:
        r_2=c3_2_p.pop(0)
        sample_p.append(r_2)
    for i in range(len(c3_2_p)):
        screen.blit(pygame.image.load('Image/'+c3_2_p[i]+'.gif'),(750 + 50*i,500))



    if len(c3_3_p)==4:
        r_3=c3_3_p.pop(0)
        sample_p.append(r_3)
    for i in range(len(c3_3_p)):
        screen.blit(pygame.image.load('Image/'+c3_3_p[i]+'.gif'),(1000 + 50*i,500))


    if len(c4_p)==5:
        r_4=c4_p.pop(0)
        sample_p.append(r_4)
    for i in range(len(c4_p)):
        screen.blit(pygame.image.load('Image/'+c4_p[i]+'.gif'),(1250 + 50*i,500))




    if y%2==0 and y!=0:
        y=0
        sample_c.append(deck[len(deck)-1])
        deck.pop()

        a=sample_c.pop(0)
        deck_dis.append(a)



    t_3 = list(itertools.combinations(set(sample_c),3))
    u_3 = list(map(list,t_3))
    for  i in u_3:
        v_3.append(sorted(i))



    t_4 = list(itertools.combinations(set(sample_c),4))
    u_4 = list(map(list,t_4))
    for  i in u_4:
        v_4.append(sorted(i))


    s_3=[]
    l_3c=[]
    s_4=[]
    l_4c=[]


    for i in v_3:
        for j in f_3_sets:
            if i==j:
                s_3.append(i)

    for i in v_4:
        for j in f_4_sets:
            if i==j:
                s_4.append(i)



    for i in s_3:
        for j in range(3):
            l_3c.append(i[j])


    for i in s_4:
        for j in range(4):
            l_4c.append(i[j])


    if len(s_4)>=1:
        c4_c = s_4[0]
        for i in range(len(c4_c)):
            screen.blit(pygame.image.load('Image/'+c4_c[i]+'.gif'),(1250 + 50*i,y_u))
            screen.blit(pygame.image.load('Image/back111.gif'),(1250 + 50*i,y_u))

        for j in range(4):
            if s_4[0][j] in sample_c:
                sample_c.remove(s_4[0][j])



    if len(s_3)>=1:
        c3_1_c = s_3[0]
        for i in range(len(c3_1_c)):
            screen.blit(pygame.image.load('Image/'+c3_1_c[i]+'.gif'),(500 + 50*i,y_u))
            screen.blit(pygame.image.load('Image/back111.gif'),(500 + 50*i,y_u))
        for j in range(3):
            if s_3[0][j] in sample_c:
                sample_c.remove(s_3[0][j])



    if len(s_3)>=2 and len(set(l_3c[0:6]))==6:
        c3_2_c = s_3[1]
        for i in range(len(c3_2_c)):
            screen.blit(pygame.image.load('Image/'+c3_2_c[i]+'.gif'),(750 + 50*i,y_u))
            screen.blit(pygame.image.load('Image/back111.gif'),(750 + 50*i,y_u))
        for j in range(3):
            if s_3[1][j] in sample_c:
                sample_c.remove(s_3[1][j])



    if len(s_3)>=3 and len(set(l_3c[0:9]))==9:
        c3_3_c = s_3[2]
        for i in range(len(c3_3_c)):
            screen.blit(pygame.image.load('Image/'+c3_3_c[i]+'.gif'),(1000 + 50*i,y_u))
            screen.blit(pygame.image.load('Image/back111.gif'),(1000 + 50*i,y_u))
        for j in range(3):
            if s_3[2][j] in sample_c:
                sample_c.remove(s_3[2][j])


    
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            
            for i in range(len(sample_p)):
                
                if (xc + 25* i) < mx < (xc + 25* (i+1)) and 500<my<650 and z==1 :
                    y+=1
                    z-=1
                    n=sample_p.pop(i)
                    deck_dis.append(n)

            
            if 650<mx<730 and 300<my<425 and z==0:
                y+=1
                z+=1
                p = deck_dis.pop()
                sample_p.append(p)


            if 400<mx<480 and 300<my<425 and z==0:
                y+=1
                z+=1
                q=deck.pop()
                sample_p.append(q)


            if 900<mx<1100 and 325<my<385 and z!=1:
                if len(c3_1_p)<3 or len(c3_2_p)<3 or len(c3_3_p)<3 or len(c4_p)<4 or sorted(c3_1_p) or sorted(c3_2_p) or sorted(c3_3_p) not in f_3_sets or sorted(c4_p) not in f_4_sets :
                   game_lost=True


            if 900<mx<1100 and 325<my<385 and sy==0 and z!=1:
                if sorted(c3_1_p) and sorted(c3_2_p) and sorted(c3_3_p) in f_3_sets and sorted(c4_p) in f_4_sets:
                   game_won=True

       

        if event.type==KEYDOWN and event.key ==K_KP1:
            for i in range(len(sample_p)):
                if (xc + 25* i) < mx < (xc + 25* (i+1)) and 500<my<650:
                    r=sample_p.pop(i)
                    c3_1_p.append(r)


        if event.type==KEYDOWN and event.key ==K_KP2:
            for i in range(len(sample_p)):
                if (xc + 25* i) < mx < (xc + 25* (i+1)) and 500<my<650:
                    r=sample_p.pop(i)
                    c3_2_p.append(r)



        if event.type==KEYDOWN and event.key ==K_KP3:
            for i in range(len(sample_p)):
                if (xc + 25* i) < mx < (xc + 25* (i+1)) and 500<my<650:
                    r=sample_p.pop(i)
                    c3_3_p.append(r)


        if event.type==KEYDOWN and event.key ==K_KP4:
            for i in range(len(sample_p)):
                if (xc + 25* i) < mx < (xc + 25* (i+1)) and 500<my<650:
                    r=sample_p.pop(i)
                    c4_p.append(r)
            

        if event.type==KEYDOWN and event.key ==ord('r'):

            for i in range(len(c3_1_p)):
                if (500 + 50* i) < mx < (500 + 50* (i+1)) and 500<my<650:
                    r=c3_1_p.pop(i)
                    sample_p.append(r)


            for i in range(len(c3_2_p)):
                if (750 + 50* i) < mx < (750 + 50* (i+1)) and 500<my<650:
                    r=c3_2_p.pop(i)
                    sample_p.append(r)


            for i in range(len(c3_3_p)):
                if (1000 + 50* i) < mx < (1000 + 50* (i+1)) and 500<my<650:
                    r=c3_3_p.pop(i)
                    sample_p.append(r)


            for i in range(len(c4_p)):
                if (1250 + 50* i) < mx < (1250 + 50* (i+1)) and 500<my<650:
                    r=c4_p.pop(i)
                    sample_p.append(r)
        

        if event.type==KEYDOWN and event.key ==ord('q'):
            play = False


        if event.type == pygame.QUIT:
            play = False


    disp()
    pygame.display.update()