import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()
plateforme = pygame.display.set_mode((650,490))
pygame.display.set_caption('premier test')
texte = pygame.font.Font(None,50)

fond = pygame.image.load('fond.webp').convert()
font = texte.render('Mon jeu', True, 'White')

image_ennemi = pygame.image.load('ennemi1.png').convert_alpha()
image_ennemi = pygame.transform.scale(image_ennemi,(64,64))

image_personnage = pygame.image.load('kirby.png').convert_alpha()
image_personnage = pygame.transform.scale(image_personnage,(64,64))

kirby_positionx = 50
kirby_positiony = 375

ennemi_positionx = 550
ennemi_positiony = 385

gravite_joueur = 0

jeu_actif = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if jeu_actif:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and kirby_positiony == 375:
                    gravite_joueur = -20

    plateforme.blit(fond,(0,0))

    if jeu_actif:

        gravite_joueur += 1
        kirby_positiony += gravite_joueur

        if kirby_positiony > 375:
            kirby_positiony = 375
            gravite_joueur = 0

        clavier = pygame.key.get_pressed()

        if clavier[pygame.K_RIGHT]:
            kirby_positionx += 4

        if clavier[pygame.K_LEFT]:
            kirby_positionx -= 4

        ennemi_positionx -= 2

        if ennemi_positionx < -64:
            ennemi_positionx = 650

        kirby_rect = image_personnage.get_rect(topleft=(kirby_positionx, kirby_positiony))
        ennemi_rect = image_ennemi.get_rect(topleft=(ennemi_positionx, ennemi_positiony))

        plateforme.blit(image_personnage, kirby_rect)
        plateforme.blit(image_ennemi, ennemi_rect)
        plateforme.blit(font,(250,30))

        if kirby_rect.colliderect(ennemi_rect):
            jeu_actif = False

    else:
        texte_game_over = texte.render("PERDU", True, "Red")
        plateforme.blit(texte_game_over,(180,220))

    pygame.display.update()
    clock.tick(60)