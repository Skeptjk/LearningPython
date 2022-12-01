import pygame as py
import math as m
from random import randint as rn
from Model import *

py.font.init()
py.mixer.init()
py.mixer.set_num_channels(64)

smallfont = py.font.Font("slkscre.ttf",8)

font = py.font.Font("slkscre.ttf",16)
mfont = py.font.Font("slkscre.ttf",24)

bigfont = py.font.Font("slkscre.ttf",48)
biggerfont = py.font.Font("slkscre.ttf",32)






actual_screen = py.display.set_mode((1280,640))
screen = py.Surface((1280,640))
py.display.set_caption("Battle")


def create_particles(x,y,size,vx,vy,timer,col):
    radius = size/2
    p = [x,y,vx,vy,timer,py.Surface((size,size)),radius]
    p[5].blit(doShiny(radius,col),(0,0),special_flags=py.BLEND_RGB_ADD)
    p[5].set_colorkey((0,0,0))
    particles.append(p)

class Button():
    def __init__(self,x,y,img,use):
        self.x, self.y = x, y
        self.img = img
        self.use = use
        py.draw.rect(self.img,(5,5,5),(0,0,64,64),5)

    def draw(self):
        screen.blit(self.img, (self.x-32,self.y-32))

    def clicked(self):
        if collision(self.x,self.y,64,64,mox,moy) and click:
            self.use()
            return 1
        return 0


class Pawn():
    def __init__(self,x,y,col):
        self.x, self.y = x, y
        self.target = 0
        self.vx, self.vy = 0, 0 
        self.speed = 1

        self.flip = 0
        self.frame_rate = 4
        self.frame_timer = 0
        self.frame = 0
        self.running = 0

        self.attack_speed = 1
        self.attack_timer = rn(1,int(120/self.attack_speed/4))*4

        

        
        
        self.col = col
        self.hp_bar = py.Surface((66,16))
        py.draw.rect(self.hp_bar,(5,5,5),(0,0,66,10),2)
        num_bars = int(self.max_hp/20)
        for i in range(num_bars):
            py.draw.line(self.hp_bar,(5,5,5),(i/num_bars*64,0),(i/num_bars*64,9),1)

        self.hp_bar.set_colorkey((0,0,0))
        #Flipping blue units so they face reds before the battle starts
        if self.col == "Blue": 
            self.flip = 1
        if self.col == "Red":
            self.enemy_team = teams["Blue"]
        else:
            self.enemy_team = teams["Red"]

    def frame_count(self):
        self.frame_timer += 1
        if self.frame_timer > game_fps/self.frame_rate:
            self.frame += 1
            if self.frame > len(self.anim)-1:
                self.frame = 0
            self.frame_timer = 0

    def draw(self):
        screen.blit(py.transform.flip(self.img,self.flip,0), (self.x-32,self.y-32))

    def get_target(self):
        least_far = 1000
        self.target = 0
        for unit in self.enemy_team:
            dist = dis(self.x,self.y,unit.x,unit.y)
            if dist < least_far:
                least_far = dist
                self.target = unit

    def move(self):
        if self.target != 0:
            t = self.target
            ag = m.atan2(t.y-self.y, t.x -self.x)
            self.vx = self.speed * m.cos(ag)
            self.vy = self.speed * m.sin(ag)
            self.running = 1
        else:
            self.vx = 0
            self.vy = 0
            self.running = 0

        self.x += self.vx
        self.y += self.vy
    def attack(self):
        pass
    
    def die(self):
        if self.hp <= 0:
            teams[self.col].remove(self)
    
    def draw_hp_bar(self):
        py.draw.rect(screen,(255,0,0),(self.x-32+2, self.y-32+2,self.hp/self.max_hp*64,6))
        screen.blit(self.hp_bar,(self.x-32, self.y-32))

class Rifleman(Pawn):
    def __init__(self,x,y,col):
        global sound_count

        self.img_set = img_dicts[col]["Rifleman"]
        self.idle, self.aim, self.anim = self.img_set
        self.aiming = 0
        self.max_hp = 100
        self.hp = self.max_hp
        Pawn.__init__(self,x,y,col)
        self.inaccuracy = 3 #%
        self.sound_channel = sound_count%10
        sound_count += 1

    def draw(self):
        if self.running:
            self.img = self.anim[self.frame]
        elif self.aiming:
            self.img = self.aim
        else: 
            self.img =  self.idle
        screen.blit(py.transform.flip(self.img,self.flip,0), (self.x-32,self.y-32))
        
        self.draw_hp_bar()

        '''txt = font.render(str(self.sound_channel),True,(0,0,0))
        screen.blit(txt,(self.x,self.y-40))'''
    def move(self):

        self.aiming = 0
        self.running = 0
        if self.target != 0:
            t = self.target
            dist = dis(t.x,t.y,self.x,self.y)
            if dist > 500:
                self.running = 1
                ag = m.atan2(t.y-self.y, t.x -self.x)
                self.vx = self.speed * m.cos(ag)
                self.vy = self.speed * m.sin(ag)

                if self.vx > 0:
                    self.flip = 0
                else:
                    self.flip = 1
            else:
                self.vx, self.vy = 0, 0 
                self.aiming = 1
                ag = m.atan2(t.y-self.y, t.x -self.x)
                self.flip = int(limit(sign(-m.cos(ag))+1,1))
        else:
            self.vx, self.vy = 0, 0 

        self.x += self.vx
        self.y += self.vy

    def attack(self):
        if self.aiming:
            self.attack_timer += 1
            if self.attack_timer > 120/self.attack_speed:
                self.attack_timer = rn(0,30) #Do not do this in high attack speed entities

                t = self.target
                ag = m.atan2(t.y-self.y, t.x -self.x)+rn(-self.inaccuracy,self.inaccuracy)*m.pi*2/200
                bullet = [self.x, self.y, m.cos(ag) * 8, m.sin(ag) * 8, self.col,10]
                bullets.append(bullet)

                if not py.mixer.Channel(self.sound_channel).get_busy():
                        py.mixer.Channel(self.sound_channel).play(shot)
                for i in range(10):
                    vx = rn(10,30)/10*m.cos(ag+rn(-30,30)/100)
                    vy = rn(10,30)/10*m.sin(ag+rn(-30,30)/100)
                    given_color = multiply_color(color(rn(100,250)),0.7)
                    size = rn(2,20)
                    create_particles(self.x,self.y,size,vx,vy,rn(10,80)/(size/10),given_color)

class Soldier(Pawn):
    def __init__(self,x,y,col):
        self.img_set = img_dicts[col]["Soldier"]
        self.idle, self.anim = self.img_set
        self.img = self.idle

        self.max_hp = 120
        self.hp = self.max_hp
        Pawn.__init__(self,x,y,col)
        self.frame_rate = 8

    def draw(self):
        if self.target != 0:
            t = self.target
            ag = m.atan2(t.y-self.y, t.x -self.x)
            self.flip = int(limit(sign(-m.cos(ag))+1,1))

        if self.running:
            self.img = self.anim[self.frame]
        
        else: 
            self.img =  self.idle

        screen.blit(py.transform.flip(self.img,self.flip,0), (self.x-32,self.y-32))
        self.draw_hp_bar()


    def move(self):
        if self.target != 0 and dis(self.x,self.y,self.target.x,self.target.y) > 40:
            t = self.target
            ag = m.atan2(t.y-self.y, t.x -self.x)
            
            self.vx = self.speed * m.cos(ag)
            self.vy = self.speed * m.sin(ag)
            self.running = 1
        else:
            self.vx = 0
            self.vy = 0
            self.running = 0

        self.x += self.vx
        self.y += self.vy

    def attack(self):
        if self.target != 0:
            self.attack_timer += 1
            if self.attack_timer > 120/self.attack_speed:
                self.attack_timer = 0

                t = self.target
                ag = m.atan2(t.y-self.y, t.x -self.x)
                blow = [self.x, self.y, m.cos(ag) * 3, m.sin(ag) * 3, self.col, 0, 40]
                blows.append(blow)
        
class Pistol(Pawn):
    def __init__(self,x,y,col):
        global sound_count 

        self.img_set = img_dicts[col]["Pistol"]
        self.idle, self.aim, self.saber = self.img_set
        self.anim = self.aim
        self.has_shot = 0

        self.max_hp = 80
        self.hp = self.max_hp
        Pawn.__init__(self,x,y,col)
        self.inaccuracy = 6 #%    

        self.sound_channel = sound_count%10
        sound_count += 1

        self.speed = 1.6
          
    def draw(self):
        if self.running:
            if self.has_shot:
                self.img = self.saber[self.frame]
            else:
                self.img = self.aim[self.frame]

        else: 
            self.img =  self.idle

        screen.blit(py.transform.flip(self.img,self.flip,0), (self.x-32,self.y-32))
        self.draw_hp_bar()

    def move(self):

        self.running = 0
        if self.target != 0:
            t = self.target
            dist = dis(t.x,t.y,self.x,self.y)
            if self.has_shot:
                if dist > 50:
                    self.running = 1
                    ag = m.atan2(t.y-self.y, t.x -self.x)
                    self.vx = self.speed * m.cos(ag)
                    self.vy = self.speed * m.sin(ag)

                    if self.vx > 0:
                        self.flip = 0
                    else:
                        self.flip = 1
                else:
                    self.vx, self.vy = 0, 0 
                    
                    ag = m.atan2(t.y-self.y, t.x -self.x)
                    self.flip = int(limit(sign(-m.cos(ag))+1,1))
            else:
                if dist > 180:
                    self.running = 1
                    ag = m.atan2(t.y-self.y, t.x -self.x)
                    self.vx = self.speed * m.cos(ag)
                    self.vy = self.speed * m.sin(ag)

                    if self.vx > 0:
                        self.flip = 0
                    else:
                        self.flip = 1
                else:
                    self.vx, self.vy = 0, 0 
                    ag = m.atan2(t.y-self.y, t.x -self.x)
                    self.flip = int(limit(sign(-m.cos(ag))+1,1))
        else:
            self.vx, self.vy = 0, 0 

        self.x += self.vx
        self.y += self.vy

    def attack(self):
        if self.target != 0:

            if self.has_shot:
                self.attack_timer += 1
                if self.attack_timer > 120/self.attack_speed:
                    self.attack_timer = 0

                    t = self.target
                    ag = m.atan2(t.y-self.y, t.x -self.x)
                    blow = [self.x, self.y, m.cos(ag) * 3, m.sin(ag) * 3, self.col, 0, 30]
                    blows.append(blow)
            elif self.running == 0:
                self.attack_timer += 1
                if self.attack_timer > 120/self.attack_speed:
                    self.attack_timer = rn(0,30) #Do not do this in high attack speed entities

                    t = self.target
                    ag = m.atan2(t.y-self.y, t.x -self.x)+rn(-self.inaccuracy,self.inaccuracy)*m.pi*2/200
                    bullet = [self.x, self.y, m.cos(ag) * 8, m.sin(ag) * 8, self.col,30]
                    bullets.append(bullet)

                    if not py.mixer.Channel(self.sound_channel).get_busy():
                        py.mixer.Channel(self.sound_channel).play(shot)

                    for i in range(10):
                        vx = rn(10,30)/10*m.cos(ag+rn(-30,30)/100)
                        vy = rn(10,30)/10*m.sin(ag+rn(-30,30)/100)
                        given_color = multiply_color(color(rn(100,250)),0.7)
                        size = rn(2,20)
                        create_particles(self.x,self.y,size,vx,vy,rn(10,80)/(size/10),given_color)
                    self.has_shot = 1
                    self.anim = self.saber
                    self.idle = self.saber[0]


class Mage(Pawn):
    def __init__(self, x, y, col):
        global sound_count

        self.img_set = img_dicts[col]["Mage"]
        self.idle, self.aim, self.anim = self.img_set
        self.aiming = 0

        self.max_hp = 200
        self.hp = self.max_hp
        Pawn.__init__(self,x,y,col)
        self.inaccuracy = 3 #%
        self.sound_channel = 0#10+sound_count%53
        self.attack_speed = 0.4
        self.speed = 0.4

    def draw(self):
        if self.running:
            self.img = self.anim[self.frame]
        elif self.aiming:
            self.img = self.aim[self.frame]
        else: 
            self.img =  self.idle
        screen.blit(py.transform.flip(self.img,self.flip,0), (self.x-32,self.y-32))
        self.draw_hp_bar()

    def move(self):

        self.running = 0
        self.aiming = 0
        if self.target != 0:
            t = self.target
            dist = dis(t.x,t.y,self.x,self.y)
            if dist > 300:
                self.running = 1
                ag = m.atan2(t.y-self.y, t.x -self.x)
                self.vx = self.speed * m.cos(ag)
                self.vy = self.speed * m.sin(ag)

                if self.vx > 0:
                    self.flip = 0
                else:
                    self.flip = 1
            else:
                self.aiming = 1
                self.vx, self.vy = 0, 0 
                ag = m.atan2(t.y-self.y, t.x -self.x)
                self.flip = int(limit(sign(-m.cos(ag))+1,1))
        else:
            self.vx, self.vy = 0, 0 

        self.x += self.vx
        self.y += self.vy
    def attack(self):
        if self.aiming and self.target != 0:
            self.attack_timer += 1
            if self.attack_timer > 120/self.attack_speed:
                self.attack_timer = 0

                t = self.target
                ag = m.atan2(t.y-self.y, t.x -self.x)+rn(-self.inaccuracy,self.inaccuracy)*m.pi*2/200
                ball = [self.x, self.y, m.cos(ag) * 8, m.sin(ag) * 8, self.col,80]
                fireballs.append(ball)

                py.mixer.Channel(self.sound_channel).play(fire)
                

def collide_pawns(p1,p2):
    if collision(p1.x,p1.y,48,48,p2.x,p2.y):
        p1.x += sign(p1.x-p2.x)
        p1.y += sign(p1.y-p2.y)

        p2.x -= sign(p1.x-p2.x)
        p2.y -= sign(p1.y-p2.y)

red_team = []
blue_team = []

player_turn = "Red"

def red_turn():
    global player_turn
    player_turn = "Red"
def blue_turn():
    global player_turn
    player_turn = "Blue"



red_button = Button(1180,40,upload("red_moustache1",64,64),red_turn)
blue_button = Button(1244,40,upload("blue_moustache1",64,64),blue_turn)

teams = {"Red": red_team, "Blue": blue_team}

red_riflemen = [upload("red_moustache1",64,64),upload("red_moustache_aim",64,64),
                [upload("red_moustache1",64,64),upload("red_moustache2",64,64)]]
blue_riflemen = [upload("blue_moustache1",64,64),upload("blue_moustache_aim",64,64),
                [upload("blue_moustache1",64,64),upload("blue_moustache2",64,64)]]

red_soldier = [upload("red_infantry1",64,64),
                [upload("red_infantry1",64,64),upload("red_infantry2",64,64),
                upload("red_infantry3",64,64),upload("red_infantry4",64,64),
                upload("red_infantry5",64,64),upload("red_infantry6",64,64),
                upload("red_infantry7",64,64),upload("red_infantry8",64,64)]]
blue_soldier = [upload("blue_infantry1",64,64),
                [upload("blue_infantry1",64,64),upload("blue_infantry2",64,64),
                upload("blue_infantry3",64,64),upload("blue_infantry4",64,64),
                upload("blue_infantry5",64,64),upload("blue_infantry6",64,64),
                upload("blue_infantry7",64,64),upload("blue_infantry8",64,64)]]

red_beard = [upload("red_beard1",64,64),
                [upload("red_beard1",64,64),upload("red_beard2",64,64)],
                [upload("red_beard_saber1",64,64),upload("red_beard_saber2",64,64)]]

blue_beard = [upload("blue_beard1",64,64),
                [upload("blue_beard1",64,64),upload("blue_beard2",64,64)],
                [upload("blue_beard_saber1",64,64),upload("blue_beard_saber2",64,64)]]

red_mage = [upload("red_mage1",64,64),
            [upload("red_mage_aim1",64,64),upload("red_mage_aim2",64,64)],
            [upload("red_mage1",64,64),upload("red_mage2",64,64)]]

blue_mage = [upload("blue_mage1",64,64),
            [upload("blue_mage_aim1",64,64),upload("blue_mage_aim2",64,64)],
            [upload("blue_mage1",64,64),upload("blue_mage2",64,64)]]

red_img_dict = {"Rifleman": red_riflemen, "Soldier": red_soldier, "Pistol": red_beard, "Mage": red_mage}
blue_img_dict = {"Rifleman": blue_riflemen,  "Soldier": blue_soldier, "Pistol": blue_beard, "Mage": blue_mage}

img_dicts = {"Red": red_img_dict, "Blue": blue_img_dict}


brushes = ["Rifleman", "Soldier", "Pistol","Mage"]
brush = "Rifleman"

class_dict = {"Rifleman": Rifleman, "Soldier": Soldier, "Pistol": Pistol, "Mage": Mage}
 
def update_buttons():
    red_button.img = red_img_dict[brush][0].copy()
    py.draw.rect(red_button.img,(5,5,5),(0,0,64,64),5)

    blue_button.img = blue_img_dict[brush][0].copy()
    py.draw.rect(blue_button.img,(5,5,5),(0,0,64,64),5)

bullets = []
bullet = py.Surface((8,8))
py.draw.circle(bullet,(5,5,5),(4,4),2)

shot = py.mixer.Sound("rifle_shot.wav")
shot.set_volume(0.3)
fire = py.mixer.Sound("fire_sound2.wav")


sound_count = 0

blows = []
blow_imgs = [upload("blow1",64,64),upload("blow2",64,64),upload("blow3",64,64),
            upload("blow4",64,64),upload("blow5",64,64)]

fireballs = []

particles = []

def get_y(obj):
    return obj.y

ready = 1

game_fps = 120

frame_count = 0
clock = py.time.Clock()
run = 1
while run:
    screen.fill((80,80,100))

    frame_count += 1
    if frame_count > 39:
        frame_count = 0

    if len(red_team)-1 >= frame_count:
        red_team[frame_count].get_target()
    if len(blue_team)-1 >= frame_count:
        blue_team[frame_count].get_target()

    mox, moy = py.mouse.get_pos()
    for e in py.event.get():
        if e.type == py.QUIT:
            run = 0
        if e.type == py.MOUSEBUTTONDOWN:
            if e.button == 1:
                click = 1
                button_clicked = red_button.clicked()
                if button_clicked == 0:
                    button_clicked = blue_button.clicked()
                if button_clicked == 0:
                    team = teams[player_turn]

                    team.append(class_dict[brush](mox,moy,player_turn))
                print(player_turn)
            if e.button == 4:
                index_ = brushes.index(brush)
                if index_ < len(brushes) - 1:
                    brush = brushes[index_+1]
                else:
                    brush = brushes[0]

                update_buttons()

            if e.button == 5:
                index_ = brushes.index(brush)
                if index_ > 0:
                    brush = brushes[index_-1]
                else:
                    brush = brushes[len(brushes)-1]
                
                update_buttons()
        if e.type == py.KEYDOWN:
            if e.key == py.K_SPACE:
                ready = switch(ready)
            if e.key == py.K_c:
                red_team.clear()
                blue_team.clear()
                
    red_button.draw()
    txt = font.render(str(len(red_team)) + "/40",True,(5,5,5))
    screen.blit(txt,(red_button.x-txt.get_width()/2, red_button.y+40))
    blue_button.draw()
    txt = font.render(str(len(blue_team)) + "/40",True,(5,5,5))
    screen.blit(txt,(blue_button.x-txt.get_width()/2, blue_button.y+40))

    all_pawns = red_team + blue_team
    all_pawns.sort(key= get_y)
    for pawn in all_pawns:
        pawn.draw()
        pawn.frame_count()
        for j in all_pawns:
            collide_pawns(j,pawn)
    
        pawn.die()

    if ready:
        for pawn in all_pawns:
            pawn.move()
            pawn.attack()

        

    blows_remove = []
    for b in blows:
        img = blow_imgs[int(b[5]/4)]
        if sign(b[2]) == 1:
            screen.blit(img,(b[0]-32, b[1]-32))
        else:
            screen.blit(py.transform.flip(img,1,0),(b[0]-32, b[1]-32))
        b[0] += b[2]
        b[1] += b[3]

        b[5] += 1

        if b[4] == "Red":
            for p in blue_team:
                if collision(p.x,p.y,64,64,b[0],b[1]):
                    
                    p.hp -= b[6]
                    b[6] = 0
        if b[4] == "Blue":
            for p in red_team:
                if collision(p.x,p.y,64,64,b[0],b[1]):
                    
                    p.hp -= b[6]
                    b[6] = 0

        if int(b[5]/4) == 5:
            blows_remove.append(b)
    for b in blows_remove:
        if b in blows:
            blows.remove(b)

    fireballs_remove = []
    for b in fireballs:
        for i in range(1):
            given_color = multiply_color(color(rn(100,250)),0.7)
            size = rn(2,20)
            create_particles(b[0],b[1],size,rn(-2,2)/5,rn(-2,2)/5,rn(10,80)/(size/10),given_color)
        b[0] += b[2]
        b[1] += b[3]

        if b[4] == "Red":
            for p in blue_team:
                if collision(p.x,p.y,64,64,b[0],b[1]):
                    fireballs_remove.append(b)
                    
                    for j in blue_team:
                        if dis(j.x,j.y,b[0],b[1]) < 80:
                            j.hp -= b[5]
                    for i in range(10):
                        given_color = multiply_color(color(rn(100,250)),0.7)
                        size = rn(12,32)
                        ag = rn(0,640)/100
                        vx,vy = rn(1,20)/2*m.cos(ag), rn(1,20)/2*m.sin(ag)
                        create_particles(b[0],b[1],size,vx,vy,rn(40,200)/(size/10),given_color)
        if b[4] == "Blue":
            for p in red_team:
                if collision(p.x,p.y,64,64,b[0],b[1]):
                    fireballs_remove.append(b)
                    
                    for j in red_team:
                        if dis(j.x,j.y,b[0],b[1]) < 80:
                            j.hp -= b[5]
                    for i in range(10):
                        given_color = multiply_color(color(rn(100,250)),0.7)
                        size = rn(12,32)
                        ag = rn(0,640)/100
                        vx,vy = rn(1,20)/2*m.cos(ag), rn(1,20)/2*m.sin(ag)
                        create_particles(b[0],b[1],size,vx,vy,rn(40,200)/(size/10),given_color)
        if not collision(b[0],b[1],1280,640,640,320):
            fireballs_remove.append(b)

    for b in fireballs_remove:
        if b in fireballs:
            fireballs.remove(b)

    bullets_remove = []

    for b in bullets:
        screen.blit(bullet,(b[0]-4, b[1]-4))
        b[0] += b[2]
        b[1] += b[3]

        if b[4] == "Red":
            for p in blue_team:
                if collision(p.x,p.y,64,64,b[0],b[1]):
                    bullets_remove.append(b)
                    
                    p.hp -= b[5]
        if b[4] == "Blue":
            for p in red_team:
                if collision(p.x,p.y,64,64,b[0],b[1]):
                    bullets_remove.append(b)
                    
                    p.hp -= b[5]

        if not collision(b[0],b[1],1280,640,640,320):
            bullets_remove.append(b)

    for b in bullets_remove:
        if b in bullets:
            bullets.remove(b)

 
    
    for p in particles:
        screen.blit(p[5],(p[0]-p[6],p[1]-p[6]),special_flags=py.BLEND_RGB_ADD)
        p[0] += p[2]
        p[1] += p[3]

        p[4] -= 1
        if p[4] <= 0:
            particles.remove(p)     

    clock.tick(game_fps)
    py.display.set_caption(str(clock.get_fps()))
    actual_screen.blit(screen,(0,0))

    py.display.update()