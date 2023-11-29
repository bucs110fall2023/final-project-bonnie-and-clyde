from playsound import playsound
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("pookie vibes")

pygame.mixer.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("notes/(1)_noteC_letterA.mp3"))
            if event.key == pygame.K_s:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("notes/(2)_noteD_letterS.mp3"))
            if event.key == pygame.K_d:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("notes/(3)_noteE_letterD.mp3"))
            if event.key == pygame.K_f:
                pygame.mixer.Channel(3).play(pygame.mixer.Sound("notes/(4)_noteF_letterF.mp3"))
            if event.key == pygame.K_g:
                pygame.mixer.Channel(4).play(pygame.mixer.Sound("notes/(5)_noteG_letterG.mp3"))
            if event.key == pygame.K_h:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound("notes/(6)_noteA_letterH.mp3"))
            if event.key == pygame.K_j:
                pygame.mixer.Channel(6).play(pygame.mixer.Sound("notes/(7)_noteB_letterJ.mp3"))
            if event.key == pygame.K_k:
                pygame.mixer.Channel(7).play(pygame.mixer.Sound("notes/(8)_noteC_letterK.mp3"))

    pygame.display.flip()





'''
import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
'''