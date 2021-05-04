from random import randint
import pygame
pygame.mixer.init()
Fond = pygame.mixer.music.load("theme5.mid")
Jou=(0)
print("[-----Bienvenue-----]")
print(" _?_")
print("/O O\\")
print("\_-_/")
Rec=int(input("Voulez vous commencez à jouez ? Oui=1 Non=2"))
while Rec<1 or Rec>2 :
    Print("[-----Erreur-----]")
    print(" ___")
    print("/è é\\")
    print("\_n_/")
    print("Il faut mettre 1 ou 2!")
    Rec=int(input("Voulez vous commencez à jouez ? Oui=1 Non=2"))
if Rec==1 :
    Jou=(1)
while Rec==1:
    """Lecture de la musique"""
    pygame.mixer.music.play(1)
    """Définition statistique du personnage"""
    SanMax=(10)
    San=(10)
    Att=(3)
    Def=(2)
    Xp=(0)
    XpNec=(5)
    Niv=(1)
    Van=(0)
    while San>=0:
        """Création statistique de l'ennemi"""
        print ("[-----Nouvel adversaire-----]")
        if Xp==XpNec-1 :
            print(" A_A")
            print("/è é\\")
            print("\\v-v/")
            print(" \_/")
            print("Un boss apparait.")
            SanEnn=SanMax
            AttEnn=Att
            DefEnn=Def
        if Van==0 :
            print(" A_A")
            print("/è é\\")
            print("\\v-v/")
            print(" \_/")
            print("Un ennemi apparait.")
            SanEnn=(randint(SanMax-5,SanMax-2))
            AttEnn=(randint(Att-1,Att))
            DefEnn=(randint(Def-1,Def))
        if not Van==0 and not Xp==XpNec-1 :
            print(" A_A")
            print("/è é\\")
            print("\\v-v/")
            print(" \_/")
            print("Un autre ennemi apparait.")
            SanEnn=(randint(SanMax-5,SanMax-2))
            AttEnn=(randint(Att-1,Att))
            DefEnn=(randint(Def-1,Def))
        print("Santé ennemi:",SanEnn)
        print("Attaque ennemi:",AttEnn)
        print("Défense ennemi:",DefEnn)
        while (SanEnn>0):
            """Situation"""
            print("[-----Tour suivant-----]")
            print("Situation:")
            print("Santé joueur:",San)
            print("Santé ennemi:",SanEnn)
            """Demande d'action"""
            Cho=int(input("Attaquer=1 Reposer=2"))
            """Action aléatoire de l'ennemi"""
            while Cho<1 or Cho>2 :
                Print("[-----Erreur-----]")
                print(" ___")
                print("/è é\\")
                print("\_n_/")
                print("Il faut mettre 1 ou 2!")
                Cho=int(input("Attaquer=1 Reposer=2"))
            if Xp==XpNec-1:
                ChoEnn=(randint(1,2))
            if not Xp==XpNec-1:
                ChoEnn=(randint(1,3))
            if ChoEnn==3:
                print(" A_A")
                print("/O O\\")
                print("\___/")
                print(" \_/")
                print("L'ennemi passe son tour")
            """Soin joueur"""
            if Cho==2:
                San=San+(Def)
                print(" ___   z")
                print("/U U\ z")
                print("\_o_/z")
                if San>=SanMax:
                    San=(SanMax)
                    print("Vous êtes en pleine forme")
                else:
                    print("Vous récupérer",(Def), "point de vie")
            """Attaque ennemi"""
            if ChoEnn==1:
                San=San-(AttEnn)
                print(" A_A")
                print("/è é\\")
                print("\\V-V/")
                print(" A_A")
                print(" \_/")
                print("L'ennemi attaque, vous perdez",AttEnn, "point de vie")
            """Attaque joueur"""
            if Cho==1:
                print(" ___    /")
                print("/è é\ \/")
                print("\_n_/-O\\")
                """Defense ennemi"""
                if ChoEnn==2:
                    SanEnn=SanEnn-(Att-Def)
                    print("--A_A")
                    print("-/o o\\")
                    print("-\\ U /")
                    print("--\_/")
                    print("L'ennemi se défend, vous lui infligez",(Att-DefEnn), "de dégat")
                else:
                    SanEnn=SanEnn-(Att)
                    print("Vous infligez",Att, "de dégat")
        """Attribution d'expérience"""
        Xp=(Xp+1)
        print(" +1XP")
        print("/O O\\")
        print("\_U_/")
        print("Vous gagnez 1 point d'expérience.")
        print(Xp,"/",XpNec)
        """Passage de niveau"""
        if Xp==XpNec:
            SanMax=(SanMax+5*Niv)
            Att=(Att+(Niv*2))
            Def=(Def+(Niv*2))
            Xp=(0)
            XpNec=(XpNec*2)
            Niv=(Niv+1)
            print("[-----Level up-----]")
            print(" +1N")
            print("/n n\\")
            print("\_U_/")
            print("Vous gagnez un niveau, vous êtes niveau",Niv)
            print("Santé maximal joueur:",SanMax)
            print("Attaque joueur:",Att)
            print("Soin joueur:",Def)
        """Augmentation du score"""
        Van=(Van+1)
        print("L'ennemi est éliminé.")
        print(" A_A")
        print("/X X\\")
        print("\ _ /")
        print(" \_/")
    else:
        """Bilan de la partie"""
        pygame.mixer.music.stop()
        print("[-----Game over-----]")
        print(" ___")
        print("/X X\\")
        print("\_n_/")
        if Van==0:
            print("Vous n'avez vaincu aucun ennemi.")
        if Van==1:
            print("Vous avez êtes tué après avoir vaincu",Van,"ennemi.")
        if Van>1:
            print("Vous avez êtes tué après avoir vaincu",Van,"ennemis et atteint le niveau",Niv,".")
        """Demande pour rejouer"""
        print("[-----Retry-----]")
        Rec=int(input("Voulez vous recommencez ? Oui=1 Non=2"))
        while Rec<1 or Rec>2 :
            print("[-----Erreur-----]")
            print("Il faut mettre 1 ou 2!")
            Rec=int(input("Voulez vous recommencez ? Oui=1 Non=2"))
"""Fin du programme"""
if Jou==1 :
    print("[-----Crédit-----]")
    print("Programmeur : D. Roquain")
    print("Merci d'avoir joué.")
    print(" ___   A_A")
    print("/U O\ /n n\\")
    print("\_U_/ \\v-v/")
    print("       \_/")
if Jou==0 :
    print(" ___")
    print("/U U\\")
    print("\_n_/")
    print("Dommage pour toi.")