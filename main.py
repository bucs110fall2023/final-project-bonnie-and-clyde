import pygame

class Sound:
    '''
    Represents sound file and its 
    associated pygame mixer channel.
    '''
    
    def __init__(self, file_path, channel):
        '''
        Initializes sound.
        Args:
        - file_path (str): path to sound file.
        - channel: pygame.mixer.Channel used to 
          play multiple sounds.
        '''
        self.file_path = file_path
        self.channel = channel

    def play(self):
        '''
        Plays sound on associated channel. 
        '''
        self.channel.play(pygame.mixer.Sound(self.file_path))
        
class Text:
    '''
    Represents text to be displayed on screen.
    '''
    
    def __init__(self, text, color, position, font_size=24):
        '''
        Initializes text.
        Args:
        - text (str): content of text.
        - color: color of text.
        - position (tuple): screen positioning of text.
        - font_size (int): size of text, set to 24.
        '''
        self.font = pygame.font.SysFont(None, font_size)
        self.text = text
        self.color = color
        self.position = position
        self.render_text()

    def render_text(self):
        '''
        Renders text with specified parameters.
        '''
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(topleft=self.position)

    def draw(self, screen):
        '''
        Displays text with specified parameters on
        specified screen coordinates.
        '''
        screen.blit(self.image, self.rect)
            
class Box:
    '''
    Represents box to be displayed on screen.
    Possesses triggered actions.
    '''
    
    def __init__(self, note, key, position):
        '''
        Initializes box.
        Args:
        - note (sound): sound associated with box.
        - key: key on keyboard associated with box.
        - position (tuple): screen positioning of box.
        '''
        self.note = note
        self.key = key
        self.position = position
        self.activation_time = 0
        self.width = None
        self.height = None
        self.default_color = None
        self.active_color = None
        self.color = None
        
    def draw(self, screen):
        '''
        Displays box with specified parameters on
        specified screen coordinates.
        '''
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.height))

    def activate(self):
        '''
        Activates box.
        '''
        self.color = self.active_color
        self.activation_time = pygame.time.get_ticks()
        
    def update_color(self):
        '''
        Changes color of box for specified time.
        '''
        elapsed_time = pygame.time.get_ticks() - self.activation_time
        if elapsed_time > 100:
            self.color = self.default_color
        
class WhiteBox(Box):
    '''
    Represents white box to be displayed on screen.
    Inherits attributes from Box class.
    '''
    
    def __init__(self, note, key, position, text):
        '''
        Initializes white box.
        Args:
        - note (sound): sound associated with box.
        - key: key on keyboard associated with box.
        - position (tuple): screen positioning of box.
        - text (str): text to be displayed on screen.
        '''
        super().__init__(note, key, position)
        self.width = 100
        self.height = 200
        self.default_color = (255, 255, 255)
        self.active_color = (224, 224, 224)
        self.color = self.default_color
        self.text = text

class BlackBox(Box):
    '''
    Represents black box to be displayed on screen.
    Inherits attributes from Box class.
    '''
    
    def __init__(self, note, key, position, text):
        '''
        Initializes black box.
        Args:
        - note (sound): sound associated with box.
        - key: key on keyboard associated with box.
        - position (tuple): screen positioning of box.
        - text (str): text to be displayed on screen.
        '''
        super().__init__(note, key, position)
        self.width = 70
        self.height = 110
        self.default_color = (0, 0, 0)
        self.active_color = (64, 64, 64)
        self.color = self.default_color
        self.text = text          
            
class PianoController:
    '''
    Controller.
    Handles user input.
    Updates GUI.
    '''
    def __init__(self):
        '''
        Intializes'''
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((940, 300))
        pygame.display.set_caption("CS 110 FINAL EXAM")

        self.channels = [pygame.mixer.Channel(i) for i in range(8)]
        
        self.white_sounds = [
            Sound("assets/notes/(W1)_noteC_letterA.mp3", self.channels[0]),
            Sound("assets/notes/(W2)_noteD_letterS.mp3", self.channels[1]),
            Sound("assets/notes/(W3)_noteE_letterD.mp3", self.channels[2]),
            Sound("assets/notes/(W4)_noteF_letterF.mp3", self.channels[3]),
            Sound("assets/notes/(W5)_noteG_letterG.mp3", self.channels[4]),
            Sound("assets/notes/(W6)_noteA_letterH.mp3", self.channels[5]),
            Sound("assets/notes/(W7)_noteB_letterJ.mp3", self.channels[6]),
            Sound("assets/notes/(W8)_noteC_letterK.mp3", self.channels[7]),
        ]

        self.white_boxes = [
            WhiteBox(self.white_sounds[0], pygame.K_a, (30, 50), "A"),
            WhiteBox(self.white_sounds[1], pygame.K_s, (142, 50), "S"),
            WhiteBox(self.white_sounds[2], pygame.K_d, (254, 50), "D"),
            WhiteBox(self.white_sounds[3], pygame.K_f, (366, 50), "F"),
            WhiteBox(self.white_sounds[4], pygame.K_g, (478, 50), "G"),
            WhiteBox(self.white_sounds[5], pygame.K_h, (590, 50), "H"),
            WhiteBox(self.white_sounds[6], pygame.K_j, (702, 50), "J"),
            WhiteBox(self.white_sounds[7], pygame.K_k, (814, 50), "K"),
        ]

        self.channels = [pygame.mixer.Channel(i) for i in range(5)]
        
        self.black_sounds = [
            Sound("assets/notes/(B1)_noteC#_letterW.mp3", self.channels[0]),
            Sound("assets/notes/(B2)_noteD#_letterE.mp3", self.channels[1]),
            Sound("assets/notes/(B3)_noteF#_letterT.mp3", self.channels[2]),
            Sound("assets/notes/(B4)_noteG#_letterY.mp3", self.channels[3]),
            Sound("assets/notes/(B5)_noteA#_letterU.mp3", self.channels[4]),
        ]

        self.black_boxes = [
            BlackBox(self.black_sounds[0], pygame.K_w, (106, 50), "W"),
            BlackBox(self.black_sounds[1], pygame.K_e, (215, 50), "E"),
            BlackBox(self.black_sounds[2], pygame.K_t, (435, 50), "T"),
            BlackBox(self.black_sounds[3], pygame.K_y, (550, 50), "Y"),
            BlackBox(self.black_sounds[4], pygame.K_u, (660, 50), "U"),
        ]
        
        self.texts = [
            Text("A", (0, 0, 0), (70, 220)),
            Text("S", (0, 0, 0), (186, 220)),
            Text("D", (0, 0, 0), (298, 220)),
            Text("F", (0, 0, 0), (410, 220)),
            Text("G", (0, 0, 0), (522, 220)),
            Text("H", (0, 0, 0), (634, 220)),
            Text("J", (0, 0, 0), (746, 220)),
            Text("K", (0, 0, 0), (858, 220)),
        
            Text("W", (255, 255, 255), (132, 130)),
            Text("E", (255, 255, 255), (245, 130)),
            Text("T", (255, 255, 255), (467, 130)),
            Text("Y", (255, 255, 255), (579, 130)),
            Text("U", (255, 255, 255), (688, 130)),
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
                
                hit = False
                for box in self.black_boxes:
                    if box.position[0] < event.pos[0] < box.position[0] + box.width and \
                       box.position[1] < event.pos[1] < box.position[1] + box.height:
                            box.note.play()
                            box.activate()
                            hit = True
                            
                if not hit:        
                    for box in self.white_boxes:
                        if box.position[0] < event.pos[0] < box.position[0] + box.width and \
                        box.position[1] < event.pos[1] < box.position[1] + box.height:
                                box.note.play()
                                box.activate()
                                return

    def update_gui(self):
        self.screen.fill((153, 204, 255))

        for box in self.white_boxes:
            box.update_color()
            box.draw(self.screen)
        for box in self.black_boxes:
            box.update_color()
            box.draw(self.screen)
            
        for text in self.texts:
            text.draw(self.screen)

        pygame.display.flip()

def main():
    piano = PianoController()

    while True:
        piano.handle_user_input()
        piano.update_gui()

main()