import pygame

class Sound:
    def __init__(self, file_path, channel):
        self.file_path = file_path
        self.channel = channel

    def play(self):
        self.channel.play(pygame.mixer.Sound(self.file_path))

class Box:
    def __init__(self, note, key, position):
        self.note = note
        self.key = key
        self.position = position
        self.activation_time = 0
        self.activated_this_iteration = False
        
        self.width = None
        self.height = None
        self.default_color = None
        self.active_color = None
        self.color = None
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.height))

    def activate(self):
        self.color = self.active_color
        self.activation_time = pygame.time.get_ticks()
        self.activated_this_iteration = True
        
    def update_color(self):
        elapsed_time = pygame.time.get_ticks() - self.activation_time
        if elapsed_time > 100:
            self.color = self.default_color
        
class WhiteBox(Box):
    def __init__(self, note, key, position):
        super().__init__(note, key, position)
        self.width = 100
        self.height = 200
        self.default_color = (255, 255, 255)
        self.active_color = (224, 224, 224)
        self.color = self.default_color

class BlackBox(Box):
    def __init__(self, note, key, position):
        super().__init__(note, key, position)
        self.width = 70
        self.height = 110
        self.default_color = (0, 0, 0)
        self.active_color = (64, 64, 64)
        self.color = self.default_color          
            
class PianoController:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((940, 300))
        pygame.display.set_caption("CS 110 FINAL EXAM")

        self.channels = [pygame.mixer.Channel(i) for i in range(8)]
        
        self.white_sounds = [
            Sound("notes/(W1)_noteC_letterA.mp3", self.channels[0]),
            Sound("notes/(W2)_noteD_letterS.mp3", self.channels[1]),
            Sound("notes/(W3)_noteE_letterD.mp3", self.channels[2]),
            Sound("notes/(W4)_noteF_letterF.mp3", self.channels[3]),
            Sound("notes/(W5)_noteG_letterG.mp3", self.channels[4]),
            Sound("notes/(W6)_noteA_letterH.mp3", self.channels[5]),
            Sound("notes/(W7)_noteB_letterJ.mp3", self.channels[6]),
            Sound("notes/(W8)_noteC_letterK.mp3", self.channels[7]),
        ]

        self.white_boxes = [
            WhiteBox(self.white_sounds[0], pygame.K_a, (30, 50)),
            WhiteBox(self.white_sounds[1], pygame.K_s, (142, 50)),
            WhiteBox(self.white_sounds[2], pygame.K_d, (254, 50)),
            WhiteBox(self.white_sounds[3], pygame.K_f, (366, 50)),
            WhiteBox(self.white_sounds[4], pygame.K_g, (478, 50)),
            WhiteBox(self.white_sounds[5], pygame.K_h, (590, 50)),
            WhiteBox(self.white_sounds[6], pygame.K_j, (702, 50)),
            WhiteBox(self.white_sounds[7], pygame.K_k, (814, 50)),
        ]

        self.channels = [pygame.mixer.Channel(i) for i in range(5)]
        
        self.black_sounds = [
            Sound("notes/(B1)_noteC#_letterW.mp3", self.channels[0]),
            Sound("notes/(B2)_noteD#_letterE.mp3", self.channels[1]),
            Sound("notes/(B3)_noteF#_letterT.mp3", self.channels[2]),
            Sound("notes/(B4)_noteG#_letterY.mp3", self.channels[3]),
            Sound("notes/(B5)_noteA#_letterU.mp3", self.channels[4]),
        ]

        self.black_boxes = [
            BlackBox(self.black_sounds[0], pygame.K_w, (106, 50)),
            BlackBox(self.black_sounds[1], pygame.K_e, (215, 50)),
            BlackBox(self.black_sounds[2], pygame.K_t, (435, 50)),
            BlackBox(self.black_sounds[3], pygame.K_y, (550, 50)),
            BlackBox(self.black_sounds[4], pygame.K_u, (660, 50)),
        ]
            
    def handle_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                for box in self.white_boxes:
                    if event.key == box.key:
                        box.note.play()
                        box.activate()
                        return
                for box in self.black_boxes:
                    if event.key == box.key:
                        box.note.play()
                        box.activate()
                        return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                for box in self.black_boxes:
                    if box.position[0] < event.pos[0] < box.position[0] + box.width and \
                       box.position[1] < event.pos[1] < box.position[1] + box.height:
                        if not box.activated_this_iteration:
                            box.note.play()
                            box.activate()
                            return
                for box in self.white_boxes:
                    if box.position[0] < event.pos[0] < box.position[0] + box.width and \
                       box.position[1] < event.pos[1] < box.position[1] + box.height:
                        if not box.activated_this_iteration:
                            box.note.play()
                            box.activate()
                            return
                
                for box in self.white_boxes + self.black_boxes:
                    box.activated_this_iteration = False

    def update_gui(self):
        self.screen.fill((153, 204, 255))

        for box in self.white_boxes:
            box.update_color()
            box.draw(self.screen)
        for box in self.black_boxes:
            box.update_color()
            box.draw(self.screen)

        pygame.display.flip()

def main():
    piano = PianoController()

    while True:
        piano.handle_user_input()
        piano.update_gui()

if __name__ == '__main__':
    main()