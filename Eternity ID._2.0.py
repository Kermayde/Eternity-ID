import random
import tkinter as tk
from threading import Timer
from tkinter import *
from tkinter import ttk
import sys
#----------- librarys---------

#----------- librarys ends----
#import pygame
#from pygame.locals import *
from PIL import Image, ImageTk

#------- Variables echidis --------
def all_variables():
    global HPcharacter, HPenemy, vuelta, message, coins, smallpoti, poti, bigpoti, smallelixir, elixir, bigelixir, \
        itemguardian, itemdamage, itemdouble, itemarmor, xp, thrustlv, falchionlv, burnlv, counterlv, thunderlv, \
        extenuarlv, freezelv, etherlv, mana, HPmax, HPenemymax, c, p1, r1, enemylv, edamage, damagecharacter, eut, \
        halfdamage, mcounter, burndamage, burnturn
    HPcharacter = 15
    HPenemy = 20
    vuelta = 0
    message = 1
    coins = 200
    smallpoti = 0
    poti = 0
    bigpoti = 0
    smallelixir = 0
    elixir = 0
    bigelixir = 0
    itemguardian = 0
    itemdamage = 0
    itemdouble = 0
    itemarmor = 0
    xp = 25
    thrustlv = 1
    falchionlv = 0
    burnlv = 0
    counterlv = 0
    thunderlv = 1
    extenuarlv = 0
    freezelv = 0
    etherlv = 0
    mana = 10
    HPmax = 1
    HPenemymax = 20
    #c = 0
    p1=1
    r1=1
    enemylv = 0
    edamage = 5
    damagecharacter = 15
    eut = 0
    halfdamage = 1
    mcounter = .1
    burndamage = 1
    burnturn = 0
all_variables()
#------- Variables echidis ends ------

#----- color/info barr --------
def barrr():
    hpprogressbar["maximum"] = HPmax
    hpprogressbar["value"] = HPcharacter
    xpprogressbar["maximum"] = HPenemymax
    xpprogressbar["value"] = HPenemy
    manaprogressbar["maximum"] = 10
    manaprogressbar["value"] = mana
#-------- color/info barr----------


# ----- light button -------
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = "dark slate gray"

    def on_leave(self, e):
        self['background'] = self.defaultBackground
#----------- lihgt button ends ----------

def RBGAImage(path):
    return Image.open(path).convert("RGBA")

def raise_frame(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)
f7 = Frame(root)
f8 = Frame(root)
f9 = Frame(root)

for frame in (f1, f2, f3, f4, f5, f6, f7, f8, f9):
    frame.grid(row=0, column=0, sticky='news')

 #---------------------------------game code start---------------------
def set_lv_name_enemy():
    labellvenemy = Label(f4, text=("Lv:", enemylv, ename), bg="white", font=("Copperplate Gothic Bold", 10), fg="gray15")
    labellvenemy.place(relx=0.85, rely=0.05, anchor=CENTER)

def nextbattle_action():
    global HPcharacter
    global vuelta, eut
    eut = 0
    enemy_stats()
    HPcharacter = HPmax
    all_mana()
    barrr()
    turn_on()
    select_map()
    select_enemy()
    character_image()
    backname.config(state=DISABLED)
    set_lv_name_enemy()
    enemy_image()
    raise_frame(f4)
def reset_stats():
    global HPcharacter, r1, p1
    HPcharacter = HPmax
    more_mana()
    r1 = 1
    labelroundinfo.config(text=("-+-+-", "Round", r1, "-+-+-"))
    p1 = p1 + 1
    labelpisoinfo.config(text=("-+-+-", "Piso", p1, "-+-+-"))
def have_skill():
    if c == 1:
        if thrustlv <= 0:
            buttonthrustb.config(state=DISABLED)
        if falchionlv <= 0:
            buttonfalchionb.config(state=DISABLED)
        if counterlv <= 0:
            buttoncounterb.config(state=DISABLED)
        if burnlv <= 0:
            buttonburnb.config(state=DISABLED)
    elif c == 2:
        if thunderlv <= 0:
            buttonthunderb.config(state=DISABLED)
        if extenuarlv <= 0:
            buttonextenuarb.config(state=DISABLED)
        if freezelv <= 0:
            buttonfreezeb.config(state=DISABLED)
        if etherlv <= 0:
            buttonetherb.config(state=DISABLED)
    else:
        labelerrorinfo.config(text="error in have skill")
        raise_frame(f7)
def have_item():
    if itemarmor >= 1:
        buttonarmor70b.config(state=NORMAL)
    else:
        buttonarmor70b.config(state=DISABLED)
    if itemdouble >= 1:
        buttondouble70b.config(state=NORMAL)
    else:
        buttondouble70b.config(state=DISABLED)
    if itemguardian >= 1:
        buttonguardian70b.config(state=NORMAL)
    else:
        buttonguardian70b.config(state=DISABLED)
    if itemdamage >= 1:
        buttondamage70b.config(state=NORMAL)
    else:
        buttondamage70b.config(state=DISABLED)
    #---
    if smallpoti >= 1:
        buttonsmallpoti70b.config(state=NORMAL)
    else:
        buttonsmallpoti70b.config(state=DISABLED)
    if poti >= 1:
        buttonpoti70b.config(state=NORMAL)
    else:
        buttonpoti70b.config(state=DISABLED)
    if bigpoti >= 1:
        buttonbigpoti70b.config(state=NORMAL)
    else:
        buttonbigpoti70b.config(state=DISABLED)
    #---
    if smallelixir >= 1:
        buttonsmallelixir70b.config(state=NORMAL)
    else:
        buttonsmallelixir70b.config(state=DISABLED)
    if elixir >= 1:
        buttonelixir70b.config(state=NORMAL)
    else:
        buttonelixir70b.config(state=DISABLED)
    if bigelixir >= 1:
        buttonbigelixir70b.config(state=NORMAL)
    else:
        buttonbigelixir70b.config(state=DISABLED)
def have_mana_off():
    global buttonthrustb, buttonfalchionb, buttonburnb, buttoncounterb, buttonthunderb, buttonextenuarb, \
        buttonfreezeb, buttonetherb, mana
    if c == 1:
        if mana <= 1:
            buttonthrustb.config(state=DISABLED)
            buttonfalchionb.config(state=DISABLED)
            buttoncounterb.config(state=DISABLED)
            buttonburnb.config(state=DISABLED)
        elif mana <= 2:
            buttonfalchionb.config(state=DISABLED)
            buttonburnb.config(state=DISABLED)
            buttoncounterb.config(state=DISABLED)
        elif mana <= 3:
            buttonburnb.config(state=DISABLED)
            buttoncounterb.config(state=DISABLED)
        elif mana <= 5:
            buttoncounterb.config(state=DISABLED)
        else:
            print("ok")
            barrr()
    elif c == 2:
        if mana <= 1:
            buttonthunderb.config(state=DISABLED)
            buttonextenuarb.config(state=DISABLED)
            buttonfreezeb.config(state=DISABLED)
            buttonetherb.config(state=DISABLED)
        elif mana <= 2:
            buttonextenuarb.config(state=DISABLED)
            buttonfreezeb.config(state=DISABLED)
            buttonetherb.config(state=DISABLED)
        elif mana <= 3:
            buttonfreezeb.config(state=DISABLED)
            buttonetherb.config(state=DISABLED)
        elif mana <= 5:
            buttonetherb.config(state=DISABLED)
        else:
            print("ok")

def have_mana_on():
    global buttonthrustb, buttonfalchionb, buttonburnb, buttoncounterb, buttonthunderb, buttonextenuarb, \
        buttonfreezeb, buttonetherb, mana
    if c == 1:
        if mana >= 2:
            buttonthrustb.config(state=NORMAL)
        elif mana >= 3:
            buttonfalchionb.config(state=NORMAL)
            buttonthrustb.config(state=NORMAL)
        elif mana >= 4:
            buttonburnb.config(state=NORMAL)
            buttonthrustb.config(state=NORMAL)
            buttonfalchionb.config(state=NORMAL)
        elif mana >= 6:
            buttoncounterb.config(state=NORMAL)
            buttonthrustb.config(state=NORMAL)
            buttonfalchionb.config(state=NORMAL)
            buttonburnb.config(state=NORMAL)
        else:
            print("ok")
            barrr()
    elif c == 2:
        if mana >= 2:
            buttonthunderb.config(state=NORMAL)
        elif mana >= 3:
            buttonextenuarb.config(state=NORMAL)
            buttonthunderb.config(state=NORMAL)
        elif mana >= 4:
            buttonfreezeb.config(state=NORMAL)
            buttonthunderb.config(state=NORMAL)
            buttonextenuarb.config(state=NORMAL)
        elif mana >= 6:
            buttonetherb.config(state=NORMAL)
            buttonthunderb.config(state=NORMAL)
            buttonextenuarb.config(state=NORMAL)
            buttonfreezeb.config(state=NORMAL)
        else:
            print("ok")
def turn_off():
    global buttonthrustb, buttonfalchionb, buttonburnb, buttoncounterb, buttonthunderb, buttonextenuarb, \
        buttonfreezeb, buttonetherb, mana
    buttonsmallpoti70b.config(state=DISABLED)
    buttonpoti70b.config(state=DISABLED)
    buttonbigpoti70b.config(state=DISABLED)
    buttonsmallelixir70b.config(state=DISABLED)
    buttonelixir70b.config(state=DISABLED)
    buttonbigelixir70b.config(state=DISABLED)
    buttondamage70b.config(state=DISABLED)
    buttonguardian70b.config(state=DISABLED)
    buttondouble70b.config(state=DISABLED)
    buttonarmor70b.config(state=DISABLED)
    if c == 1:
        buttonthrustb.config(state=DISABLED)
        buttonfalchionb.config(state=DISABLED)
        buttonburnb.config(state=DISABLED)
        buttoncounterb.config(state=DISABLED)
    elif c == 2:
        buttonthunderb.config(state=DISABLED)
        buttonextenuarb.config(state=DISABLED)
        buttonfreezeb.config(state=DISABLED)
        buttonetherb.config(state=DISABLED)
    else:
        labelerrorinfo.config(text="error in turn off")
        raise_frame(f7)
def turn_on():
    global buttonthrustb, buttonfalchionb, buttonburnb, buttoncounterb, buttonthunderb, buttonextenuarb, \
        buttonfreezeb, buttonetherb, mana
    buttonsmallpoti70b.config(state=NORMAL)
    buttonpoti70b.config(state=NORMAL)
    buttonbigpoti70b.config(state=NORMAL)
    buttonsmallelixir70b.config(state=NORMAL)
    buttonelixir70b.config(state=NORMAL)
    buttonbigelixir70b.config(state=NORMAL)
    buttondamage70b.config(state=NORMAL)
    buttonguardian70b.config(state=NORMAL)
    buttondouble70b.config(state=NORMAL)
    buttonarmor70b.config(state=NORMAL)
    if c == 1:
        buttonthrustb.config(state=NORMAL)
        buttonfalchionb.config(state=NORMAL)
        buttonburnb.config(state=NORMAL)
        buttoncounterb.config(state=NORMAL)
        have_mana_off()
        have_mana_on()
        have_item()
        have_skill()
    elif c == 2:
        buttonthunderb.config(state=NORMAL)
        buttonextenuarb.config(state=NORMAL)
        buttonfreezeb.config(state=NORMAL)
        buttonetherb.config(state=NORMAL)
        have_mana_off()
        have_mana_on()
        have_item()
        have_skill()
    else:
        labelerrorinfo.config(text="error in turn on")
        raise_frame(f7)

#---------- enemy stats ---------------

def enemy_stats():
    global enemylv, edamage, HPenemy, HPenemymax
    elv = random.randint(1, 5)
    enemylv = enemylv + elv
    ed = round(elv * 3)
    edamage = edamage + ed
    eh = round(elv * 5)
    HPenemy = HPenemymax
    HPenemy = HPenemy + eh
    HPenemymax = HPenemymax + eh
def enemy_action():
    global enemylv, edamage, eHP, eut, takedamage
    eulty = random.randint(1, 5)
    if eulty == 1:
        eut = 1
        porsen = round(edamage * .5)
        maxd = round(edamage * 1.1)
        takedamage = random.randint(porsen, maxd)
        print(enemylv)
    else:
        eut = 0
        takedamage = random.randint(0, edamage)
        print("gg")

#--------------------------------------

#-------------
def combat_message():
    global labelcombat, messageb
    labelcombat = Label(f4, text=messageb, bg="gray15", font=("Copperplate Gothic Bold", 12), fg="white")
    labelcombat.place(relx=0.5, rely=0.4, anchor=CENTER)

def combat_coins_message():
    global labelcoincombat, messagecoinb, coins
    labelcoincombat = Label(f4, text="+3 coins", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="gold")
    labelcoincombat.place(relx=0.55, rely=0.63, anchor=CENTER)
    coins = coins + 3
    labelcoincombat.config(fg="gray15")
    f4.after(200, lambda: labelcoincombat.config(fg="gold4"))
    f4.after(400, lambda: labelcoincombat.config(fg="gold3"))
    f4.after(600, lambda: labelcoincombat.config(fg="gold2"))
    f4.after(8000, lambda: labelcoincombat.config(fg="gold"))
    f4.after(1200, lambda: labelcoincombat.config(fg="gold2"))
    f4.after(1400, lambda: labelcoincombat.config(fg="gold3"))
    f4.after(1600, lambda: labelcoincombat.config(fg="gold4"))
    f4.after(1800, lambda: labelcoincombat.config(fg="gray15"))
    f4.after(2000, lambda: labelcoincombat.place_forget())
    f4.after(2000, lambda: labelcoins.config(text=coins))
    f4.after(2000, lambda: labelcoinsb.config(text=coins))

def burn_damage():
    global burnturn, HPenemy
    HPenemy = HPenemy - burndamage
    burnturn = burnturn - 1

def enemy_attack_inbattle():
    global ut, burnturn, burndamage
    if HPenemy <= 0:
        if HPcharacter == HPmax:
            f4.after(2000, lambda: labelcombat.config(text=" Perfect! \n YOU WON ", bg="gray15",
                     activebackground='firebrick4', fg="gold2", font=("Copperplate Gothic Bold", 25)))
            f4.after(6000, lambda: labelcombat.place_forget())
            f4.after(6000, lambda: turn_on())
            f4.after(6000, lambda: raise_frame(f5))
            f4.after(6000, lambda: reset_stats())
        else:
            f4.after(2000, lambda: labelcombat.config(text=" YOU WON ", bg="gray15",
                                                      activebackground='firebrick4', fg="blue violet",
                                                      font=("Copperplate Gothic Bold", 25)))
            f4.after(6000, lambda: labelcombat.place_forget())
            f4.after(6000, lambda: turn_on())
            f4.after(6000, lambda: raise_frame(f5))
            f4.after(6000, lambda: reset_stats())
    else:
        if takedamage <= 0:
            f4.after(2000, lambda: labelcombat.config(text="The enemy missed the attack"))
            f4.after(2000, lambda: character_image())
            f4.after(4000, lambda: labelcombat.place_forget())
            f4.after(4000, lambda: turn_on())
            f4.after(4000, lambda: more_mana())
            f4.after(4000, lambda: barrr())
            ut = ut - 1
            f4.after(4000, lambda: character_image())
        else:
            f4.after(2000, lambda: labelcombat.config(text="The enemy is attaking..."))
            f4.after(4000, lambda: labelcombat.config(text=("The", "enemy's", "attack", "is:", takedamage)))
            f4.after(4200, lambda: barrr())
            f4.after(4200, lambda: character_image())
            if ut == 2:
                ut = ut - 1
                f4.after(8000, lambda: labelcombat.config(text=("you", "reflected", "the", "attack")))
                ut = ut - 1
            else:
                take_hurt()
                f4.after(6000, lambda: labelcombat.config(text=("Your", "HP", "is:", HPcharacter)))
                f4.after(6000, lambda: character_image())
                f4.after(6000, lambda: more_mana())
                f4.after(6000, lambda: barrr())
                f4.after(6100, lambda: life_die())
        if burnturn >= 1:
            f4.after(8000, lambda: burn_damage())
            f4.after(9000, lambda: labelcombat.config(text=("The", "Enemy", "is", "burning:", "-", burndamage)))
            f4.after(9000, lambda: barrr())
            f4.after(9000, lambda: enemy_image())
        else:
            print("gg")

#---------Button actions---------

def more_mana():
    global mana
    if mana >= 8:
        mana = 10
    else:
        mana = mana + 3
def all_mana():
    global mana
    mana = 10
def take_hurt():
    global HPcharacter
    HPcharacter = HPcharacter - takedamage
def life_die():
    global exitgameButton, buttonrestart
    if HPcharacter <= 0:
        f4.after(2000, lambda: labelcombat.config(text=" GAME OVER ", bg="gray15", fg="firebrick4",
                                                   font=("Copperplate Gothic Bold", 25)))
        f4.after(6000, lambda: labelcombat.place_forget())
        f9.after(2000, lambda: labelend.config(text=" GAME OVER ", bg="gray15", fg="firebrick4",
                                                  font=("Copperplate Gothic Bold", 25)))
        buttonrestart = HoverButton(f9, text=" Exit Game ", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 18), command=sys.exit)
        buttonrestart.place(relx=0.65, rely=0.7, anchor=CENTER)
        exitgameButton = HoverButton(f9, text="Play Again", bg="gray15", activebackground='firebrick4', fg="white",
                                 font=("Copperplate Gothic Bold", 18), command=play_again)
        exitgameButton.place(relx=0.35, rely=0.7, anchor=CENTER)
        f4.after(6000, lambda: raise_frame(f9))
    else:
        f4.after(2000, lambda: labelcombat.place_forget())
        f4.after(2000, lambda: turn_on())
def play_again():
    all_variables()
    raise_frame(f1)
    buttonrestart.place_forget()
    exitgameButton.place_forget()
    have_item()
    have_skill()

def thrust_action():
    global HPcharacter, HPenemy, mana, messageb, r1
    global ut, eut
    ut = ut - 1
    character_image()
    turn_off()
    mana = mana - 2
    r1 = r1 + 1
    f4.after(10000, lambda: labelroundinfo.config(text=("-+-+-", "Round", r1, "-+-+-")))
    barrr()
    have_mana_off()
    enemy_action()
    givedamage = random.randint(0, damagecharacter)
    HPenemy = HPenemy - givedamage
    messageb = "You use Thrust"
    combat_message()
    if givedamage <= 0:
        f4.after(2000, lambda: labelcombat.config(text="You failed the attack"))
    else:
        f4.after(2000, lambda: labelcombat.config(text=("your", "attack", "was:", givedamage)))
        f4.after(4000, lambda: labelcombat.config(text=("The", "enemy's", "HP", "is:", HPenemy)))
        f4.after(4000, lambda: barrr())
    f4.after(4000, lambda: enemy_image())
    f4.after(4000, lambda: enemy_attack_inbattle())
    f4.after(6000, lambda: combat_coins_message())

def falchion_action():
    global HPcharacter, HPenemy, mana, messageb, r1
    global ut, eut
    ut = ut - 1
    character_image()
    turn_off()
    mana = mana - 4
    r1 = r1 + 1
    f4.after(10000, lambda: labelroundinfo.config(text=("-+-+-", "Round", r1, "-+-+-")))
    barrr()
    have_mana_off()
    enemy_action()
    givedamage = random.randint(0, halfdamage)
    givedamage2 = random.randint(0, halfdamage)
    givedamage3 = random.randint(0, halfdamage)
    HPenemy = HPenemy - givedamage
    HPenemy = HPenemy - givedamage2
    HPenemy = HPenemy - givedamage3
    messageb = "You use Falchion"
    combat_message()
    if givedamage <= 0:
        f4.after(2000, lambda: labelcombat.config(text="You failed the attack"))
    else:
        f4.after(2000, lambda: labelcombat.config(text=("your", "first", "attack", "was:", givedamage)))
    if givedamage2 <= 0:
        f4.after(4000, lambda: labelcombat.config(text="You failed the attack"))
    else:
        f4.after(4000, lambda: labelcombat.config(text=("your", "second", "attack", "was:", givedamage2)))
    if givedamage3 <= 0:
        f4.after(6000, lambda: labelcombat.config(text="You failed the attack"))
    else:
        f4.after(6000, lambda: labelcombat.config(text=("your", "third", "attack", "was:", givedamage3)))
    f4.after(8000, lambda: labelcombat.config(text=("The", "enemy's", "HP", "is:", HPenemy)))
    f4.after(8000, lambda: barrr())
    f4.after(8000, lambda: enemy_image())
    f4.after(8000, lambda: enemy_attack_inbattle())
    f4.after(8000, lambda: combat_coins_message())

def burn_action():
    global HPcharacter, HPenemy, mana, messageb, r1, burnturn
    global ut, eut
    ut = ut - 1
    burnturn = 3
    character_image()
    turn_off()
    mana = mana - 4
    r1 = r1 + 1
    f4.after(10000, lambda: labelroundinfo.config(text=("-+-+-", "Round", r1, "-+-+-")))
    barrr()
    have_mana_off()
    enemy_action()
    #givedamage = random.randint(0, damagecharacter)
    #HPenemy = HPenemy - givedamage
    messageb = "You use Burn"
    combat_message()
    f4.after(4000, lambda: barrr())
    f4.after(4000, lambda: enemy_image())
    f4.after(4000, lambda: enemy_attack_inbattle())
    f4.after(6000, lambda: combat_coins_message())


def counter_action():
    global HPcharacter, HPenemy, mana, messageb, r1
    global ut, eut
    ut = ut = 2
    character_image()
    turn_off()
    mana = mana - 6
    r1 = r1 + 1
    f4.after(10000, lambda: labelroundinfo.config(text=("-+-+-", "Round", r1, "-+-+-")))
    barrr()
    have_mana_off()
    enemy_action()
    givedamage = random.randint(0, damagecharacter)
    HPenemy = HPenemy - givedamage
    messageb = "You use Counter"
    combat_message()
    f4.after(2000, lambda: enemy_image())
    f4.after(2000, lambda: enemy_attack_inbattle())
    f4.after(2000, lambda: combat_coins_message())
    counterdamage = round(takedamage * mcounter)
    HPenemy = HPenemy - counterdamage
    f4.after(12000, lambda: labelcombat.config(text=("your", "attack", "was:", counterdamage)))
    f4.after(14000, lambda: labelcombat.config(text=("The", "enemy's", "HP", "is:", HPenemy)))
    f4.after(14000, lambda: more_mana())
    f4.after(14000, lambda: character_image())
    f4.after(14000, lambda: barrr())
    f4.after(14100, lambda: life_die())

def smallpotion_action():
    global HPcharacter
    global vuelta
    global ut
    ut = ut - 1
    if tiket.get() == 1:
        HPcharacter = random.randint(0, 15)
        vuelta = vuelta + 1
        character_image()
    elif tiket.get() == 2:
        HPcharacter = random.randint(0, 15)
        vuelta = vuelta + 1
        character_image()
    else:
        labelerrorinfo.config(text="error in smallpotion action")
        raise_frame(f7)

def ultimate_action():
    global HPcharacter
    global vuelta
    global ut
    if tiket.get() == 1:
        ut = 1
        HPcharacter = random.randint(0, 15)
        vuelta = vuelta + 1
        character_image()
    elif tiket.get() == 2:
        ut = 2
        HPcharacter = random.randint(0, 15)
        vuelta = vuelta + 1
        character_image()
    else:
        labelerrorinfo.config(text="error in ******")
        raise_frame(f7)
ut = 0
#-----------Kermany Buttons---------
def thunder_action():
    global HPcharacter, HPenemy, mana, messageb, r1, coins
    global ut, eut
    ut = ut - 1
    r1 = r1 + 1
    f4.after(10000, lambda: labelroundinfo.config(text=("-+-+-", "Round", r1, "-+-+-")))
    turn_off()
    mana = mana - 2
    barrr()
    have_mana_off()
    enemy_action()
    givedamage = random.randint(0, damagecharacter)
    HPenemy = HPenemy - givedamage
    messageb = "You use Thunder"
    combat_message()
    if givedamage <= 0:
        f4.after(2000, lambda: labelcombat.config(text="You failed the attack"))
    else:
        f4.after(2000, lambda: labelcombat.config(text=("your", "attack", "was:", givedamage)))
        f4.after(4000, lambda: labelcombat.config(text=("The", "enemy's", "HP", "is:", HPenemy)))
        f4.after(4000, lambda: barrr())
    f4.after(4000, lambda: enemy_image())
    f4.after(4000, lambda: enemy_attack_inbattle())
    f4.after(6000, lambda: combat_coins_message())

#---------Button actions ends-------




def character_image():
    global character
    global critical
    life = round(HPmax * .4)
    if ut <= 0:
        if tiket.get() == 1:
            if HPcharacter >= life:
                character = RBGAImage("characters/chrom 50%.png")
                critical = RBGAImage("characters/critical0.png")
                image_battle()
            else:
                character = RBGAImage("characters/chrom_hurt 50%.png")
                critical = RBGAImage("characters/critical.png")
                image_battle()
        elif tiket.get() == 2:
            if HPcharacter >= life:
                character = RBGAImage("characters/kermany 50%.png")
                critical = RBGAImage("characters/critical0.png")
                image_battle()
            else:
                character = RBGAImage("characters/kermany_hurt 50%.png")
                critical = RBGAImage("characters/critical.png")
                image_battle()
        else:
            labelerrorinfo.config(text="error in character image\nwithout ultimate")
            raise_frame(f7)
    else:
        if tiket.get() == 1:
                character = RBGAImage("characters/chrom_ulty 50%.png")
                image_battle()
        elif tiket.get() == 2:
                character = RBGAImage("characters/kermany_ulty 50%.png")
                image_battle()
        else:
            labelerrorinfo.config(text="error in character image\nwith ultimate")
            raise_frame(f7)

def select_enemy():
    global foe, foe1, ehurt, eulty, ename
    foe1 = random.choice(("a", "b", "c", "d", "e", "f", "g"))
    if foe1 == "a":
        ename = "Dead Knight"
        foe = RBGAImage("characters/dead knight/Death_Knight 50%.png")
        ehurt = RBGAImage("characters/dead knight/Death_Knight_hurt 50%.png")
        eulty = RBGAImage("characters/dead knight/Death_Knight_ulty 50%.png")
    elif foe1 == "b":
        ename = "Robin"
        foe = RBGAImage("characters/robin/robin 50%.png")
        ehurt = RBGAImage("characters/robin/robin_hurt 50%.png")
        eulty = RBGAImage("characters/robin/robin_ulty 50%.png")
    elif foe1 == "c":
        ename = "Rey Criko"
        foe = RBGAImage("characters/rey criko/rey_criko 50%.png")
        ehurt = RBGAImage("characters/rey criko/rey_criko_hurt 50%.png")
        eulty = RBGAImage("characters/rey criko/rey_criko_ulty 50%.png")
    elif foe1 == "d":
        ename = "Corrin"
        foe = RBGAImage("characters/corrin/Corrin 50%.png")
        ehurt = RBGAImage("characters/corrin/Corrin_hurt 50%.png")
        eulty = RBGAImage("characters/corrin/Corrin_ulty 50%.png")
    elif foe1 == "e":
        ename = "Freyja"
        foe = RBGAImage("characters/freyja/Freyja 50%.png")
        ehurt = RBGAImage("characters/freyja/Freyja_hurt 50%.png")
        eulty = RBGAImage("characters/freyja/Freyja_ulty 50%.png")
    elif foe1 == "f":
        ename = "Idunn"
        foe = RBGAImage("characters/idunn/Idunn 50%.png")
        ehurt = RBGAImage("characters/idunn/Idunn_hurt 50%.png")
        eulty = RBGAImage("characters/idunn/Idunn_ulty 50%.png")
    elif foe1 == "g":
        ename = "Azura"
        foe = RBGAImage("characters/azura/Azura 50%.png")
        ehurt = RBGAImage("characters/azura/Azura_hurt 50%.png")
        eulty = RBGAImage("characters/azura/Azura_ulty 50%.png")
    else:
        labelerrorinfo.config(text="error in select enemy")
        raise_frame(f7)
    enemy_image()

def enemy_image():
    global enemy
    global critical2
    elife = round(HPenemymax * .4)
    if eut <= 0:
        if HPenemy >= elife:
            enemy = foe
            critical2 = RBGAImage("characters/critical0.png")
            image_battle()
        else:
            enemy = ehurt
            critical2 = RBGAImage("characters/criticalEnemy.png")
            image_battle()
    else:
        enemy = eulty
        image_battle()
#----------------------------------game code ends-----------------------

root.title("Eternity ID")
root.geometry("750x495")


#------- Menu (f1)----------
f1.config(bg="gray1")
background = PhotoImage(file = "interface/menu.png")
Label(f1, image = background, bd=0).pack()
playButton = HoverButton(f1,text="Play", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 20), command=lambda:raise_frame(f2))
playButton.place(x=235,y=350)
exitButton = HoverButton(f1, text=" Exit ", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 20), command=sys.exit)
exitButton.place(x=410,y=350)
creditsButton = HoverButton(f1, text="Credits", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 15), command=lambda:raise_frame(f8))
creditsButton.place(x=600,y=420)
#---------- Menu (f1) ends------------
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='cyan4')
s.configure("blue.Horizontal.TProgressbar", foreground='red', background='brown4')


#------ Character pass---------
def chrome_c():
    global tiket
    global s, c
    global labelthrustinfo, labelfalchioninfo, labelburninfo, labelcounterinfo
    global HPcharacter, HPmax, damagecharacter
    global buttonthrustb, buttonfalchionb, buttonburnb, buttoncounterb, buttonthunderb, buttonextenuarb, \
        buttonfreezeb, buttonetherb, halfdamage
    tiket.set(1)
    character_image()
    damagecharacter = 15
    halfdamage = round(damagecharacter * .5)
    raise_frame(f3)
    c = 1
    s.configure("mana.Horizontal.TProgressbar", foreground='red', background='gold3')
    HPcharacter = 20
    HPmax = 20
    #---------- buttons-----
    buttonthrustm = HoverButton(f5, text="  Thrust  \nXP: 1", bg="gray15", activebackground='firebrick4',
                                fg="white", font=("Copperplate Gothic Bold", 11), command=buy_thrust)
    buttonthrustm.place(x=225, y=290)
    buttonfalchionm = HoverButton(f5, text="Falchion \nXP: 1", bg="gray15",
                                    activebackground='firebrick4', fg="white",font=("Copperplate Gothic Bold", 11), command=buy_falchion)
    buttonfalchionm.place(x=430, y=290)
    buttonburnm = HoverButton(f5, text="    Burn    \nXP: 1", bg="gray15", activebackground='firebrick4',
                                fg="white", font=("Copperplate Gothic Bold", 11), command=buy_burn)
    buttonburnm.place(x=225, y=340)
    buttoncounterm = HoverButton(f5, text=" Counter \nXP: 3", bg="gray15", activebackground='firebrick4',
                                fg="white", font=("Copperplate Gothic Bold", 11), command=buy_counter)
    buttoncounterm.place(x=430, y=340)
    # ----------- buttons battle-----
    buttonthrustb = HoverButton(f4, text="  Thrust  ", bg="gray15", activebackground='firebrick4',
                                fg="white", font=("Copperplate Gothic Bold", 13), command=thrust_action)
    buttonthrustb.place(x=50, y=400)
    buttonfalchionb = HoverButton(f4, text="Falchion ", bg="gray15",
                                  activebackground='firebrick4', fg="white", font=("Copperplate Gothic Bold", 13),
                                  command=falchion_action)
    buttonfalchionb.place(x=200, y=400)
    buttonburnb = HoverButton(f4, text="    Burn    ", bg="gray15", activebackground='firebrick4',
                              fg="white", font=("Copperplate Gothic Bold", 13), command=burn_action)
    buttonburnb.place(x=50, y=450)
    buttoncounterb = HoverButton(f4, text=" Counter ", bg="gray15", activebackground='firebrick4',
                                 fg="white", font=("Copperplate Gothic Bold", 13), command=counter_action)
    buttoncounterb.place(x=200, y=450)
    #---------- info lv-------
    labelthrustinfo = Label(f5, text=("Thrust", "Lv:", thrustlv), bg="gray15", activebackground='firebrick4',
                                fg="white", font=("Copperplate Gothic Bold", 10))
    labelthrustinfo.place(x=15, y=440)
    labelfalchioninfo = Label(f5, text=("Falchion", "Lv:", falchionlv), bg="gray15",
                                  activebackground='firebrick4', fg="white", font=("Copperplate Gothic Bold", 10))
    labelfalchioninfo.place(x=15, y=470)
    labelburninfo = Label(f5, text=("Burn", "Lv:", burnlv), bg="gray15", activebackground='firebrick4',
                              fg="white", font=("Copperplate Gothic Bold", 10))
    labelburninfo.place(x=150, y=440)
    labelcounterinfo = Label(f5, text=("Counter", "Lv:", counterlv), bg="gray15", activebackground='firebrick4',
                                 fg="white", font=("Copperplate Gothic Bold", 10))
    labelcounterinfo.place(x=150, y=470)

labelthrustinfo = 1
labelfalchioninfo = 1
labelburninfo = 1
labelcounterinfo = 1

def kermany_c():
    global tiket
    global s, c
    global labelthunderinfo, labelextenuarinfo, labelfreezeinfo, labeletherinfo
    global HPcharacter, HPmax, damagecharacter
    global buttonthrustb, buttonfalchionb, buttonburnb, buttoncounterb, buttonthunderb, buttonextenuarb, \
        buttonfreezeb, buttonetherb
    HPcharacter = 15
    HPmax = 15
    tiket.set(2)
    c = 2
    damagecharacter = 20
    print(tiket.get())
    character_image()
    s.configure("mana.Horizontal.TProgressbar", foreground='red', background='purple')
    raise_frame(f3)
    # ---------- buttons-----
    buttonthunderm = HoverButton(f5, text="Thunder \nXP: 1", bg="gray15", activebackground='firebrick4',
                                fg="white", font=("Copperplate Gothic Bold", 11), command=buy_thunder)
    buttonthunderm.place(x=225, y=290)
    buttonextenuarm = HoverButton(f5, text="Extenuar\nXP: 1", bg="gray15",
                                  activebackground='firebrick4', fg="white", font=("Copperplate Gothic Bold", 11),
                                  command=buy_extenuar)
    buttonextenuarm.place(x=430, y=290)
    buttonfreezem = HoverButton(f5, text=" Freeze   \nXP: 1", bg="gray15", activebackground='firebrick4',
                              fg="white", font=("Copperplate Gothic Bold", 11), command=buy_freeze)
    buttonfreezem.place(x=225, y=340)
    buttonetherm = HoverButton(f5, text="   Ether    \nXP: 3", bg="gray15", activebackground='firebrick4',
                                 fg="white", font=("Copperplate Gothic Bold", 11), command=buy_ether)
    buttonetherm.place(x=430, y=340)
    #----------- buttons battle-----
    buttonthunderb = HoverButton(f4, text="Thunder ", bg="gray15", activebackground='firebrick4',
                                 fg="white", font=("Copperplate Gothic Bold", 13), command=thunder_action)
    buttonthunderb.place(x=50, y=400)
    buttonextenuarb = HoverButton(f4, text="Extenuar", bg="gray15",
                                  activebackground='firebrick4', fg="white", font=("Copperplate Gothic Bold", 13),
                                  command=buy_extenuar)
    buttonextenuarb.place(x=200, y=400)
    buttonfreezeb = HoverButton(f4, text=" Freeze   ", bg="gray15", activebackground='firebrick4',
                                fg="white", font=("Copperplate Gothic Bold", 13), command=buy_freeze)
    buttonfreezeb.place(x=50, y=450)
    buttonetherb = HoverButton(f4, text="    Ether    ", bg="gray15", activebackground='firebrick4',
                               fg="white", font=("Copperplate Gothic Bold", 13), command=buy_ether)
    buttonetherb.place(x=200, y=450)
    # ---------- info lv-------
    labelthunderinfo = Label(f5, text=("Thunder", "Lv:", thunderlv), bg="gray15", activebackground='firebrick4',
                            fg="white", font=("Copperplate Gothic Bold", 10))
    labelthunderinfo.place(x=15, y=440)
    labelextenuarinfo = Label(f5, text=("Extenuar", "Lv:", extenuarlv), bg="gray15",
                              activebackground='firebrick4', fg="white", font=("Copperplate Gothic Bold", 10))
    labelextenuarinfo.place(x=15, y=470)
    labelfreezeinfo = Label(f5, text=("Burn", "Lv:", freezelv), bg="gray15", activebackground='firebrick4',
                          fg="white", font=("Copperplate Gothic Bold", 10))
    labelfreezeinfo.place(x=150, y=440)
    labeletherinfo = Label(f5, text=("Ether", "Lv:", etherlv), bg="gray15", activebackground='firebrick4',
                             fg="white", font=("Copperplate Gothic Bold", 10))
    labeletherinfo.place(x=150, y=470)
labelthunderinfo = 1
labelextenuarinfo = 1
labelfreezeinfo = 1
labeletherinfo = 1

#-------Character pass ends --------

#-------Selection C (f2)---------
tiket = IntVar()
background1 = PhotoImage(file = "interface\select.png")
Label(f2, image = background1, bd=0).pack()
cbutton = HoverButton(f2, text=" Knight ", bg="gray15", activebackground='firebrick4', fg="white",
                      font=("Copperplate Gothic Bold", 20), command=chrome_c)
cbutton.place(x=215,y=350)
kbutton = HoverButton(f2, text="Magician", bg="gray15", activebackground='firebrick4',
                      fg="white", font=("Copperplate Gothic Bold", 20), command=kermany_c)
kbutton.place(x=390,y=350)
backButton = HoverButton(f2, text="  Back  ", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 20), command=lambda:raise_frame(f1))
backButton.place(x=305,y=420)
nextButton = HoverButton(f2, text="  Next  ", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 20), command=lambda:raise_frame(f3))
nextButton.pack()

#--------Selection C (f2) ends--------

#---------Set Name (f3)----------
background3 = PhotoImage(file = "interface/sname.png")
Label(f3, image = background3, bd=0).pack()
back2Button = HoverButton(f3, text="  Back  ", bg="gray15", activebackground='firebrick4', fg="white",
                          font=("Copperplate Gothic Bold", 20), command=lambda:raise_frame(f2))
back2Button.place(x=305,y=420)
 #      ---text name----
textbox = Entry(f3, font=("Copperplate Gothic Bold", 19))
textbox.place(x=177, y=160)
textbox.insert(END, "")
def player_name():
    playername = textbox.get()
    global question
    question = Label(f3, text="Confirm?", bg="gray15", font=("Copperplate Gothic Bold", 12), fg="white", bd=0)
    question.place(x=335, y=200)
    global buttonyes
    buttonyes = HoverButton(f3, text="Yes", bg="gray15", activebackground='firebrick4', fg="white",
                            font=("Copperplate Gothic Bold", 12), command=lambda:raise_frame(f5))
    buttonyes.place(x=300,y=240)
    global buttonno
    buttonno = HoverButton(f3, text="No", bg="gray15", activebackground='firebrick4', fg="white",
                              font=("Copperplate Gothic Bold", 12), command=button_no)
    buttonno.place(x=400, y=240)
    name.config(text=playername)
    buttonacept.config(state=DISABLED)
    textbox.config(state=DISABLED)
def button_no():
    textbox.config(state=NORMAL)
    buttonacept.config(state=NORMAL)
    question.place_forget()
    buttonyes.place_forget()
    buttonno.place_forget()
 #     -text name ends-----
buttonacept = HoverButton(f3, text="  Accept  ", bg="gray15", activebackground='firebrick4', fg="white",
                          font=("Copperplate Gothic Bold", 12), command=player_name)
buttonacept.place(x=470,y=160)
Button(f3, text='What is your name adventurous?', bg="gray15", fg="white", state=DISABLED, activebackground="red",
       font=("Copperplate Gothic Bold", 15), command=lambda:raise_frame(f1)).place(x=177,y=80)
#----------- set name (f3) ends--------


#Label(f4, text='FRAME 4').pack()
def select_map():
    global map, backgroundmap
    map = random.choice(("maps/map1.png","maps/map2.png","maps/map3.png","maps/map4.png","maps/map5.png",
                         "maps/map6.png","maps/map7.png","maps/map8.png","maps/map9.png","maps/map10.png",
                         "maps/map11.png","maps/map12.png","maps/map13.png","maps/map14.png","maps/map15.png",
                         "maps/map16.png","maps/map17.png","maps/map18.png","maps/map19.png","maps/map20.png",
                         "maps/map21.png","maps/map22.png","maps/map23.png","maps/map24.png","maps/map25.png",
                         "maps/map26.png","maps/map27.png","maps/map28.png","maps/map29.png","maps/map30.png",
                         "maps/map31.png","maps/map32.png","maps/map33.png"))
    backgroundmap = RBGAImage(map)


select_map()
backgroundmap = RBGAImage(map)
battlefield = RBGAImage(map)
enemy = RBGAImage("characters/Lif 50%.png")
critical2 = RBGAImage("characters/critical0.png")

#**********Store***********
def buy_smallpotions():
    global smallpoti
    global coins
    global message
    if coins >= 5:
        smallpoti = smallpoti + 1
        coins = coins - 5
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelsmallpotiinfo.config(text=("Small_potion:", smallpoti))
        message = "+1 Small Potion"
        message_temp()
    else:
        message="insufficient coins"
        message_temp()
def buy_potions():
    global poti
    global coins
    global message
    if coins >= 10:
        poti = poti + 1
        coins = coins - 10
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelpotiinfo.config(text=("Potion:", poti))
        message = "+1 Potion"
        message_temp()
    else:
        message="insufficient coins"
        message_temp()
def buy_bigpotions():
    global bigpoti
    global coins
    global message
    if coins >= 10:
        bigpoti = bigpoti + 1
        coins = coins - 10
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelbigpotiinfo.config(text=("Big_potion:", bigpoti))
        message = "+1 Big Potion"
        message_temp()
    else:
        message="insufficient coins"
        message_temp()
def buy_smallelixir():
    global smallelixir
    global coins
    global message
    if coins >= 5:
        smallelixir = smallelixir + 1
        coins = coins - 5
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelsmallelixirinfo.config(text=("Small_elixir:", smallelixir))
        message = "+1 Small Elixir"
        message_temp()
    else:
        message="insufficient coins"
        message_temp()
def buy_elixir():
    global elixir
    global coins
    global message
    if coins >= 10:
        elixir = elixir + 1
        coins = coins - 10
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelelixirinfo.config(text=("Elixir:", elixir))
        message = "+1 Elixir"
        message_temp()
    else:
        message="insufficient coins"
        message_temp()
def buy_bigelixir():
    global bigelixir
    global coins
    global message
    if coins >= 40:
        bigelixir = bigelixir + 1
        coins = coins - 10
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelbigelixirinfo.config(text=("Big_elixir:", bigelixir))
        message = "+1 Big Elixir"
        message_temp()
    else:
        message="You are very poor"
        message_temp()
def buy_itemdamage():
    global itemdamage
    global coins
    global message
    if coins >= 40:
        itemdamage = itemdamage + 1
        coins = coins - 40
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labeldamageinfo.config(text=("True_Damage:", itemdamage))
        message = "+1 True Damage"
        message_temp()
    else:
        message="insufficient coins"
        message_temp()
def buy_itemdouble():
    global itemdouble
    global coins
    global message
    if coins >= 40:
        itemdouble = itemdouble + 1
        coins = coins - 40
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labeldoubleinfo.config(text=("Double_Attack:", itemdouble))
        message = "+1 Double Attack"
        message_temp()
    else:
        message="insufficient coins"
        message_temp()
def buy_itemarmor():
    global itemarmor
    global coins
    global message
    if coins >= 40:
        itemarmor = itemarmor + 1
        coins = coins - 40
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelarmorinfo.config(text=("Stony_Armor:", itemarmor))
        message = "+1 Stony Armor"
        message_temp()
    else:
        message="insufficient coins"
        message_temp()
def buy_itemguardian():
    global itemguardian
    global coins
    global message
    if coins >= 40:
        itemguardian = itemguardian + 1
        coins = coins - 40
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelguardianinfo.config(text=("Guardian_Angel:", itemguardian))
        message = "+1 Guardian Angel"
        message_temp()
    else:
        message="insufficient coins"
        message_temp()
#-------------------
def buy_thrust():
    global thrustlv
    global xp
    global message
    if xp >= 1:
        thrustlv = thrustlv + 1
        xp = xp - 1
        labelxp.config(text=xp)
        labelxpin.config(text=xp)
        labelxpb.config(text=xp)
        labelthrustinfo.config(text=("Thrust", "Lv:", thrustlv))
        message = "+1Lv Thrust"
        message_temp()
    else:
        message = "insufficient XP"
        message_temp()
def buy_falchion():
    global falchionlv
    global xp
    global message
    if xp >= 1:
        falchionlv = falchionlv + 1
        xp = xp - 1
        labelxp.config(text=xp)
        labelxpin.config(text=xp)
        labelxpb.config(text=xp)
        labelfalchioninfo.config(text=("Falchion", "Lv:", falchionlv))
        message = "+1Lv Falchion"
        message_temp()
    else:
        message = "insufficient XP"
        message_temp()
def buy_burn():
    global burnlv
    global xp
    global message
    if xp >= 1:
        burnlv = burnlv + 1
        xp = xp - 1
        labelxp.config(text=xp)
        labelxpin.config(text=xp)
        labelxpb.config(text=xp)
        labelburninfo.config(text=("Burn", "Lv:", burnlv))
        message = "+1Lv Burn"
        message_temp()
    else:
        message = "insufficient XP"
        message_temp()
def buy_counter():
    global counterlv
    global xp
    global message
    if xp >= 3:
        counterlv = counterlv + 1
        xp = xp - 3
        labelxp.config(text=xp)
        labelxpin.config(text=xp)
        labelxpb.config(text=xp)
        labelcounterinfo.config(text=("Counter", "Lv:", counterlv))
        message = "+1Lv Counter"
        message_temp()
    else:
        message = "insufficient XP"
        message_temp()
#----
def buy_thunder():
    global thunderlv
    global xp
    global message
    if xp >= 1:
        thunderlv = thunderlv + 1
        xp = xp - 1
        labelxp.config(text=xp)
        labelxpin.config(text=xp)
        labelxpb.config(text=xp)
        labelthunderinfo.config(text=("Thunder", "Lv:", thunderlv))
        message = "+1Lv Thunder"
        message_temp()
    else:
        message = "insufficient XP"
        message_temp()
def buy_freeze():
    global freezelv
    global xp
    global message
    if xp >= 1:
        freezelv = freezelv + 1
        xp = xp - 1
        labelxp.config(text=xp)
        labelxpin.config(text=xp)
        labelxpb.config(text=xp)
        labelfreezeinfo.config(text=("Freeze", "Lv:", freezelv))
        message = "+1Lv Freeze"
        message_temp()
    else:
        message = "insufficient XP"
        message_temp()
def buy_extenuar():
    global extenuarlv
    global xp
    global message
    if xp >= 1:
        extenuarlv = extenuarlv + 1
        xp = xp - 1
        labelxp.config(text=xp)
        labelxpin.config(text=xp)
        labelxpb.config(text=xp)
        labelextenuarinfo.config(text=("Extenuar", "Lv:", extenuarlv))
        message = "+1Lv Extenuar"
        message_temp()
    else:
        message = "insufficient XP"
        message_temp()
def buy_ether():
    global etherlv
    global xp
    global message
    if xp >= 1:
        etherlv = etherlv + 1
        xp = xp - 1
        labelxp.config(text=xp)
        labelxpin.config(text=xp)
        labelxpb.config(text=xp)
        labeletherinfo.config(text=("Ether", "Lv:", etherlv))
        message = "+1Lv Ether"
        message_temp()
    else:
        message = "insufficient XP"
        message_temp()
def buy_hp():
    global HPcharacter
    global xp
    global message
    if xp >= 1:
        HPcharacter = HPcharacter + 5
        xp = xp - 1
        labelxp.config(text=xp)
        labelxpin.config(text=xp)
        labelxpb.config(text=xp)
        labelhpinfo.config(text=("HP:", HPcharacter))
        message = "+5 HP"
        message_temp()
    else:
        message = "insufficient XP"
        message_temp()
#-----------------------------------------
#-------------------- inventory sell ------------------------
def buy_smallpotions_s():
    global smallpoti
    global coins
    global message
    if smallpoti >= 1:
        smallpoti = smallpoti - 1
        coins = coins + 3
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelsmallpotiinfo.config(text=("Small_potion:", smallpoti))
        message = "-1 Small Potion, +3 coins"
        message_temp_inventory()
    else:
        message="insufficient Small Potions"
        message_temp_inventory()
def buy_potions_s():
    global poti
    global coins
    global message
    if poti >= 1:
        poti = poti - 1
        coins = coins + 7
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelpotiinfo.config(text=("Potion:", poti))
        message = "-1 Potion, +7 coins"
        message_temp_inventory()
    else:
        message="insufficient Potions"
        message_temp_inventory()
def buy_bigpotions_s():
    global bigpoti
    global coins
    global message
    if bigpoti >= 1:
        bigpoti = bigpoti - 1
        coins = coins + 15
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelbigpotiinfo.config(text=("Big_Potion:", bigpoti))
        message = "-1 Big Potion, +7 coins"
        message_temp_inventory()
    else:
        message="insufficient Big Potions"
        message_temp_inventory()
def buy_smallelixir_s():
    global smallelixir
    global coins
    global message
    if smallelixir >= 1:
        smallelixir = smallelixir - 1
        coins = coins + 3
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelsmallelixirinfo.config(text=("Small_Elixir:", smallelixir))
        message = "-1 Small Elixir, +3 coins"
        message_temp_inventory()
    else:
        message="insufficient Small Elixir"
        message_temp_inventory()
def buy_elixir_s():
    global elixir
    global coins
    global message
    if elixir >= 1:
        elixir = elixir - 1
        coins = coins + 7
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelelixirinfo.config(text=("Elixir:", elixir))
        message = "-1 Elixir, +7 coins"
        message_temp_inventory()
    else:
        message="insufficient Elixir"
        message_temp_inventory()
def buy_bigelixir_s():
    global bigelixir
    global coins
    global message
    if bigelixir >= 1:
        bigelixir = bigelixir - 1
        coins = coins + 15
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelbigelixirinfo.config(text=("Big_Elixir:", bigelixir))
        message = "-1 Big Elixir, +7 coins"
        message_temp_inventory()
    else:
        message="insufficient Big Elixir"
        message_temp_inventory()
#-------------
def buy_damage_s():
    global itemdamage
    global coins
    global message
    if itemdamage >= 1:
        itemdamage = itemdamage - 1
        coins = coins + 40
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labeldamageinfo.config(text=("True_Damage:", itemdamage))
        message = "-1 True Damage, +40 coins"
        message_temp_inventory()
    else:
        message="insufficient True Damage"
        message_temp_inventory()
def buy_double_s():
    global itemdouble
    global coins
    global message
    if itemdouble >= 1:
        itemdouble = itemdouble - 1
        coins = coins + 40
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labeldoubleinfo.config(text=("Double_Attack:", itemdouble))
        message = "-1 Double Attack, +40 coins"
        message_temp_inventory()
    else:
        message="insufficient Double Attack"
        message_temp_inventory()
def buy_guardian_s():
    global itemguardian
    global coins
    global message
    if itemguardian >= 1:
        itemguardian = itemguardian - 1
        coins = coins + 40
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelguardianinfo.config(text=("Guardian_Angel:", itemguardian))
        message = "-1 Guardian Angel, +40 coins"
        message_temp_inventory()
    else:
        message="insufficient Guardian Angel"
        message_temp_inventory()
def buy_armor_s():
    global itemarmor
    global coins
    global message
    if itemarmor >= 1:
        itemarmor = itemarmor - 1
        coins = coins + 40
        labelcoins.config(text=coins)
        labelcoinsin.config(text=coins)
        labelcoinsb.config(text=coins)
        labelarmorinfo.config(text=("Stony_Armor:", itemarmor))
        message = "-1 Stony Armor, +40 coins"
        message_temp_inventory()
    else:
        message="insufficient Stony Armor"
        message_temp_inventory()
#-------------------------------------------------------------
def message_temp():
    global message
    temp = Label(f5, text=message, bg="gray15", font=("Copperplate Gothic Bold", 12), fg="white")
    temp.place(x=290, y=405)
    t = Timer(2.0, temp.place_forget)
    t.start()
def message_temp_inventory():
    global message
    temp = Label(f6, text=message, bg="gray15", font=("Copperplate Gothic Bold", 12), fg="white")
    temp.place(x=290, y=405)
    t = Timer(2.0, temp.place_forget)
    t.start()

def image_battle():
    global finalimage
    battlefield.paste(backgroundmap, (0, 0), backgroundmap)
    battlefield.paste(character, (0, 30), character)
    battlefield.paste(enemy, (500, 30), enemy)
    battlefield.paste(critical, (0, 0), critical)
    battlefield.paste(critical2, (0, 0), critical2)
    finalimage = ImageTk.PhotoImage(battlefield)
    final_battle()

finalimage = PhotoImage(file = "others/muestra.png")
label1 = Label(f4, image=finalimage, bd=0)
label1.pack()

def final_battle():
    label1.configure(image=finalimage)



#-------Item images---------
coinsimage = PhotoImage(file= "items/coins.png")
poti1_50 = PhotoImage(file='items/poti50%/potion1 50%.png')
poti2_50 = PhotoImage(file="items/poti50%/potion2 50%.png")
poti3_50 = PhotoImage(file="items/poti50%/potion3 50%.png")
elixir1_50 = PhotoImage(file="items/poti50%/elixir1 50%.png")
elixir2_50 = PhotoImage(file="items/poti50%/elixir2 50%.png")
elixir3_50 = PhotoImage(file="items/poti50%/elixir3 50%.png")
armor_50 = PhotoImage(file="items/armor 50%.png")
guardian_50 = PhotoImage(file="items/guardian 50%.png")
double_50 = PhotoImage(file="items/double 50%.png")
damage_50 = PhotoImage(file="items/damage 50%.png")
xpimage = PhotoImage(file="items/xp.png")
poti1_70 = PhotoImage(file='items/poti70%/potion1 70%.png')
poti2_70 = PhotoImage(file="items/poti70%/potion2 70%.png")
poti3_70 = PhotoImage(file="items/poti70%/potion3 70%.png")
elixir1_70 = PhotoImage(file="items/poti70%/elixir1 70%.png")
elixir2_70 = PhotoImage(file="items/poti70%/elixir2 70%.png")
elixir3_70 = PhotoImage(file="items/poti70%/elixir3 70%.png")
armor_70 = PhotoImage(file="items/armor 70%.png")
guardian_70 = PhotoImage(file="items/guardian 70%.png")
double_70 = PhotoImage(file="items/double 70%.png")
damage_70 = PhotoImage(file="items/damage 70%.png")
#---------------------------

f4.config(bg="gray5")
#      ------background info-----


f4.config(bg="gray1")
name = Label(f4, text="player", bg="white", font=("Copperplate Gothic Bold", 10), fg="gray15")
name.place(relx=0.18, rely=0.05, anchor=CENTER)

labelcoinsb = Label(f4, text=coins, bg="gray15", activebackground='firebrick4', fg="white", image=coinsimage,
                   compound="left", font=("Copperplate Gothic Bold", 15))
labelcoinsb.place(x=370,y=356)
labelxpb = Label(f4, text=xp, bg="gray15", activebackground='firebrick4', fg="white", image=xpimage,
                   compound="left", font=("Copperplate Gothic Bold", 15))
labelxpb.place(x=315,y=356)

#       -----background info ends----
p1=1
r1=1
labelpisoinfo = Label(f4, text=("-+-+-", "Piso", p1, "-+-+-"), bg="gray15",font=("Copperplate Gothic Bold", 15), fg="white")
labelpisoinfo.place(x=300,y=0)
labelroundinfo = Label(f4, text=("-+-+-", "Round", r1, "-+-+-"), bg="gray15",font=("Copperplate Gothic Bold", 20), fg="dark slate gray")
labelroundinfo.place(x=250,y=30)



hpprogressbar = ttk.Progressbar(f4, style="red.Horizontal.TProgressbar")
hpprogressbar.place(x=30, y=362, width=215)
hpprogressbar.step(HPcharacter)

xpprogressbar = ttk.Progressbar(f4, style="blue.Horizontal.TProgressbar")
xpprogressbar.place(x=500, y=362, width=215)
xpprogressbar.step(HPcharacter)

manaprogressbar = ttk.Progressbar(f4, orient=VERTICAL, style="mana.Horizontal.TProgressbar", length=160)
manaprogressbar.place(x=10, y=180)
manaprogressbar.step(HPcharacter)

#borre algo aqui
buttonsmallpoti70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=poti1_70,  command=smallpotion_action)
buttonsmallpoti70b.place(x=550, y=400)
buttonpoti70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=poti2_70, command=smallpotion_action)
buttonpoti70b.place(x=600, y=400)
buttonbigpoti70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=poti3_70, command=smallpotion_action)
buttonbigpoti70b.place(x=650, y=400)
#---
buttonsmallelixir70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=elixir1_70,  command=smallpotion_action)
buttonsmallelixir70b.place(x=550, y=450)
buttonelixir70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=elixir2_70, command=smallpotion_action)
buttonelixir70b.place(x=600, y=450)
buttonbigelixir70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=elixir3_70, command=smallpotion_action)
buttonbigelixir70b.place(x=650, y=450)
#---
buttonguardian70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=guardian_70, command=smallpotion_action)
buttonguardian70b.place(x=500, y=400)
buttondamage70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=damage_70, command=smallpotion_action)
buttondamage70b.place(x=500, y=450)
buttondouble70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=double_70, command=smallpotion_action)
buttondouble70b.place(x=450, y=400)
buttonarmor70b = HoverButton(f4, bg="gray15", activebackground='firebrick4', fg="white",
                          image=armor_70, command=smallpotion_action)
buttonarmor70b.place(x=450, y=450)


buttoninventoryb = HoverButton(f4, text=" I ", bg="gray15", activebackground='firebrick4', fg="white",
                               font=("Copperplate Gothic Bold", 15), command=turn_off)
buttoninventoryb.place(x=705, y=400)

#-------------- Store(f5) ------------------------
f5.config(bg="gray1")
backgroundstore = PhotoImage(file = "interface/store.png")
Label(f5, image = backgroundstore, bd=0).pack()
Label(f5, text=" Store ", bg="gray15", font=("Copperplate Gothic Bold", 30), fg="white").place(x=300, y=5)
nextBattle = HoverButton(f5, text="Next Battle", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 16), command=nextbattle_action)
nextBattle.place(x=575, y=445)
backname = HoverButton(f5, text="Back", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 12), command=lambda:raise_frame(f3))
backname.place(x=15,y=17)
inventory = HoverButton(f5, text="Inventory", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 12), command=lambda:raise_frame(f6))
inventory.place(x=625,y=17)

labelcoins = Label(f5, text=coins, bg="gray15", activebackground='firebrick4', fg="white", image=coinsimage,
                   compound="left", font=("Copperplate Gothic Bold", 15))
labelcoins.place(x=370,y=64)
labelxp = Label(f5, text=xp, bg="gray15", activebackground='firebrick4', fg="white", image=xpimage,
                   compound="left", font=("Copperplate Gothic Bold", 15))
labelxp.place(x=315,y=64)
#---- store --------
buttonpoti1 = HoverButton(f5, text="Small \nPotions  \n$5 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=poti1_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_smallpotions)
buttonpoti1.place(x=15,y=130)
buttonpoti2 = HoverButton(f5, text="Potions  \n$10 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=poti2_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_potions)
buttonpoti2.place(x=15,y=215)
buttonpoti2 = HoverButton(f5, text="Big \nPotions  \n$10 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=poti3_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_bigpotions)
buttonpoti2.place(x=15,y=300)
buttonelixir1 = HoverButton(f5, text="Small  \nElixir  \n$10 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=elixir1_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_smallelixir)
buttonelixir1.place(x=615,y=130)
buttonelixir2 = HoverButton(f5, text="Elixir  \n$10 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=elixir2_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_elixir)
buttonelixir2.place(x=615,y=215)
buttonelixir3 = HoverButton(f5, text="Big  \nElixir  \n$10 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=elixir3_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_bigelixir)
buttonelixir3.place(x=615,y=300)
buttonarmor = HoverButton(f5, text="Stony \nArmor  \n$50 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=armor_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_itemarmor)
buttonarmor.place(x=235,y=130)
buttonguardian = HoverButton(f5, text="Guardian \nAngel  \n$50 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=guardian_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_itemguardian)
buttonguardian.place(x=390,y=130)
buttondouble = HoverButton(f5, text="Double \nAttack  \n$10 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=double_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_itemdouble)
buttondouble.place(x=235,y=215)
buttondamage = HoverButton(f5, text="True    \nDamage     \n$50 ", bg="gray15", activebackground='firebrick4', fg="white",
                          image=damage_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_itemdamage)
buttondamage.place(x=390,y=215)
buttonhpm = HoverButton(f5, text="   HP   \nXP: 1", bg="gray15", activebackground='firebrick4',
                                 fg="white", font=("Copperplate Gothic Bold", 11), command=buy_hp)
buttonhpm.place(x=341, y=315)
labelhpinfo = Label(f5, text=("HP:", HPcharacter), bg="gray15", activebackground='firebrick4',
                                 fg="white", font=("Copperplate Gothic Bold", 10))
labelhpinfo.place(x=275, y=470)
#--------------------------------------------------

f6.config(bg="gray15")
backgroundinventory = PhotoImage(file = "interface/inventory.png")
Label(f6, image = backgroundinventory, bd=0).pack()

Label(f6, text=("Inventory"), bg="gray15",font=("Copperplate Gothic Bold", 30), fg="white").place(x=269,y=9)
nextBattle = HoverButton(f6, text="Next Battle", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 16), command=lambda:raise_frame(f4))
nextBattle.place(x=293,y=445)
backname = HoverButton(f6, text="Back", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 12), command=lambda:raise_frame(f3))
backname.place(x=15,y=17)
store = HoverButton(f6, text="Store", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 12), command=lambda:raise_frame(f5))
store.place(x=660,y=17)
labelcoinsin = Label(f6, text=coins, bg="gray15", activebackground='firebrick4', fg="white", image=coinsimage,
                   compound="left", font=("Copperplate Gothic Bold", 15))
labelcoinsin.place(x=370,y=64)
labelxpin = Label(f6, text=xp, bg="gray15", activebackground='firebrick4', fg="white", image=xpimage,
                   compound="left", font=("Copperplate Gothic Bold", 15))
labelxpin.place(x=315,y=64)
#------- items inventory------
Label(f6, text="  Potions  ", bg="gray15",font=("Copperplate Gothic Bold", 12), fg="white").place(x=175,y=128)
buttonpoti1 = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=poti1_50, compound="top", font=("Copperplate Gothic Bold", 10), command=buy_smallpotions_s)
buttonpoti1.place(x=190,y=165)
buttonpoti2 = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=poti2_50, compound="top", font=("Copperplate Gothic Bold", 10), command=buy_potions_s)
buttonpoti2.place(x=190,y=230)
buttonpoti3 = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=poti3_50, compound="top", font=("Copperplate Gothic Bold", 10), command=buy_bigpotions_s)
buttonpoti3.place(x=190,y=297)
Label(f6, text="  Elixirs  ", bg="gray15",font=("Copperplate Gothic Bold", 12), fg="white").place(x=495,y=128)
buttonelixir1 = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=elixir1_50, compound="top", font=("Copperplate Gothic Bold", 10), command=buy_smallelixir_s)
buttonelixir1.place(x=505,y=165)
buttonelixir2 = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=elixir2_50, compound="top", font=("Copperplate Gothic Bold", 10), command=buy_elixir_s)
buttonelixir2.place(x=505,y=230)
buttonelixir3 = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=elixir3_50, compound="top", font=("Copperplate Gothic Bold", 10), command=buy_bigelixir_s)
buttonelixir3.place(x=505,y=297)
Label(f6, text="  Items  ", bg="gray15", font=("Copperplate Gothic Bold", 12), fg="white").place(x=345,y=128)
buttonarmor = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=armor_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_armor_s)
buttonarmor.place(x=300,y=185)
buttonguardian = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=guardian_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_guardian_s)
buttonguardian.place(x=300,y=265)
buttondouble = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=double_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_double_s)
buttondouble.place(x=400,y=185)
buttondamage = HoverButton(f6, bg="gray15", activebackground='firebrick4', fg="white",
                          image=damage_50, compound="left", font=("Copperplate Gothic Bold", 10), command=buy_damage_s)
buttondamage.place(x=400,y=265)
#--------------------------------

#---------- info inventory ----------------
labelsmallpotiinfo = Label(f6, text=('Small_Potions:', smallpoti), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labelsmallpotiinfo.place(x=10, y=100)
Label(f6, text="Sell for $3", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=10, y=120)
labelpotiinfo = Label(f6, text=('Potions:', poti), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labelpotiinfo.place(x=10, y=150)
Label(f6, text="Sell for $7", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=10, y=170)
labelbigpotiinfo = Label(f6, text=('Big_Potions:', bigpoti), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labelbigpotiinfo.place(x=10, y=200)
Label(f6, text="Sell for $15", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=10, y=220)
labelsmallelixirinfo = Label(f6, text=('Small_Elixirs:', smallelixir), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labelsmallelixirinfo.place(x=10, y=255)
Label(f6, text="Sell for $3", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=10, y=275)
labelelixirinfo = Label(f6, text=('Elixir:', elixir), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labelelixirinfo.place(x=10, y=305)
Label(f6, text="Sell for $7", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=10, y=325)
labelbigelixirinfo = Label(f6, text=('Big_elixir:', bigelixir), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labelbigelixirinfo.place(x=10, y=355)
Label(f6, text="Sell for $5", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=10, y=375)
#----
labelarmorinfo = Label(f6, text=('Stony_Armor:', bigelixir), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labelarmorinfo.place(x=620, y=150)
Label(f6, text="Sell for $20", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=645, y=170)
labelguardianinfo = Label(f6, text=('Guardian_Angel:', bigelixir), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labelguardianinfo.place(x=597, y=200)
Label(f6, text="Sell for $20", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=645, y=220)
labeldoubleinfo = Label(f6, text=('Double_Attack:', bigelixir), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labeldoubleinfo.place(x=607, y=250)
Label(f6, text="Sell for $20", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=645, y=270)
labeldamageinfo = Label(f6, text=('True_Damage:', bigelixir), bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white")
labeldamageinfo.place(x=620, y=300)
Label(f6, text="Sell for $20", bg="gray15", font=("Copperplate Gothic Bold", 10), fg="white").place(x=645, y=320)
#------------------------------------------------

#-----------------button sell------------------------

#------------ screen error(f7)------------
errorinfo = "error"
def message_error():
    global errorinfo, labelerrorinfo
    labelerrorinfo = Label(f7, text=errorinfo, bg="gray15", font=("Copperplate Gothic Bold", 35), fg="firebrick4")
    labelerrorinfo.place(relx=0.5, rely=0.4, anchor=CENTER)

f7.config(bg="gray15")
exitButton = HoverButton(f7, text=" Exit ", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 20), command=sys.exit)
exitButton.place(x=325,y=400)
message_error()
#------------ screen error ends--------------

#------------ Credits(f8) -------------------
f8.config(bg="gray15")
labeltcreditsinfo = Label(f8, text="Credits", bg="gray15", font=("Copperplate Gothic Bold", 35), fg="blue violet")
labeltcreditsinfo.pack()
labelcreditsinfo = Label(f8, text="+----Director----+\nCarlos Antonio Flores Delgado\n \n+----Programmers----+\n"
                                  "Carlos Antonio Flores Delgado\nJuan Carrillo Francisco Ramirez\n"
                                  "Fernando Sebastian Pamanes Morales\n \n+----Creative Ideas----+\n"
                                  "Carlos Antonio Flores Delgado\nJuan Carrillo Francisco Ramirez\n"
                                  "Fernando Sebastian Pamanes Morales\nAngel Daniel Nuñez Mendoza\n "
                                  "Luis Octavio Najera Agular\n", bg="gray15", font=("Copperplate Gothic Bold", 14), fg="white")
labelcreditsinfo.place(relx=0.5, rely=0.4, anchor=CENTER)
backcButton = HoverButton(f8, text=" Back ", bg="gray15", activebackground='firebrick4', fg="white",
                         font=("Copperplate Gothic Bold", 20), command=sys.exit)
backcButton.place(x=325,y=425)
#------------ credits ends -----------

#----------- win/game over screen --------------
def end_message():
    global labelend, messagee
    labelend = Label(f9, text="Error", bg="gray15", font=("Copperplate Gothic Bold", 12), fg="white")
    labelend.place(relx=0.5, rely=0.4, anchor=CENTER)

f9.config(bg="gray15")
end_message()




""""#----- musuc test-------

pygame.init()
pygame.mixer.music.load("hazbin.mp3")
pygame.mixer.music.play(1)


#------------------------"""

raise_frame(f1)
root.mainloop()
