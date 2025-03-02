import os
import pygame

from .background import slow_bg_obj
# from .helps import helps
from constants import WIDTH,\
    controlImage,\
    helpsImage,\
    CANVAS, \
    soundList, \
    framespersec, \
    FPS, \
    FONT_PATH

class AudioControls:
    def __init__(self, soundList):
        self.soundList = soundList
        self.volume = 100
        self.muted = False
        self.prev_volume = -1
        # volume icons
        self.VOL_ICON = pygame.image.load(
            os.path.join('assets', 'graphics', 'audio.png'))
        self.MUTE_ICON = pygame.image.load(
            os.path.join('assets', 'graphics', 'mute.png'))

        pygame.mixer.music.set_volume(self.volume / 100)
        for soundItem in self.soundList:
            soundItem.set_volume(self.volume / 100)

    def set_volume(self, level):
        if level == 0:
            self.muted = True
        if self.muted and level > 0:
            self.muted = False
            self.prev_volume = 50  # if you unmute at zero vol, defaults to 50
        self.volume = level
        pygame.mixer.music.set_volume(level / 100)
        for soundItem in soundList:
            soundItem.set_volume(level / 100)

    def dec_volume(self, amt):
        amt = max(0, self.volume - amt)
        self.set_volume(amt)

    def inc_volume(self, amt):
        amt = min(100, self.volume + amt)
        self.set_volume(amt)

    def toggle_mute(self): # 볼룸 껏다 킴
        if self.muted:
            self.set_volume(self.prev_volume)
            self.muted = False
        else:
            self.prev_volume = self.volume
            self.muted = True
            self.set_volume(0)

    def display_volume(self, CANVAS):
        background_width = slow_bg_obj.rectBGimg.width
        screen_rect = CANVAS.get_rect()
        center_x = screen_rect.centerx
        starting_x = center_x - background_width//2

        control_font = pygame.font.Font(
            os.path.join(FONT_PATH, "neue.ttf"), 30)
        if self.muted:
            CANVAS.blit(self.MUTE_ICON, (starting_x + 20, 695))
            vol_lbl_text = " --"
        else:
            CANVAS.blit(self.VOL_ICON, (starting_x + 20, 695))
            vol_lbl_text = str(self.volume).rjust(3, " ")

        vol_label = control_font.render(vol_lbl_text, 1, (255, 255, 255))
        CANVAS.blit(vol_label, (starting_x + 70, 695))

    def play_music(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)


audio_cfg = AudioControls(soundList)


class DisplayControls:
    def toggle_full_screen(self):
        screen = pygame.display.get_surface()
        if (screen.get_flags() & pygame.FULLSCREEN):
            pygame.display.set_mode((750, 750))
        else:
            info = pygame.display.Info()
            pygame.display.set_mode(
                (info.current_w, info.current_h), pygame.FULLSCREEN)


display_cfg = DisplayControls


def settings():
    run = True

    control_title_font = pygame.font.Font(
        os.path.join(FONT_PATH, 'edit_undo.ttf'), 50)
    control_font = pygame.font.Font(os.path.join(FONT_PATH, 'neue.ttf'), 36)
    keys_font = pygame.font.Font(os.path.join(FONT_PATH, 'neue.ttf'), 30)


    while run:
        slow_bg_obj.update()
        slow_bg_obj.render(CANVAS)

        window_width = CANVAS.get_width()
        background_width = slow_bg_obj.rectBGimg.width
        screen_rect = CANVAS.get_rect()
        center_x = screen_rect.centerx
        starting_x = center_x - background_width//2



        screen_rect = CANVAS.get_rect()
        center_x = screen_rect.centerx
        starting_x = center_x - background_width//2
        ending_x = center_x + background_width//2

        helps_label = control_font.render('[h]', 1, (255, 255, 255))
        CANVAS.blit(helps_label, (ending_x - 67, 30))
        CANVAS.blit(helpsImage, (ending_x - 130, 25))




        control_title_label = control_title_font.render(
            'Settings', 1, (0, 0, 209))
        CANVAS.blit(control_title_label, (window_width//2 -
                    control_title_label.get_width()//2 - 30, 130))
        CANVAS.blit(controlImage, (window_width//2 +
                    control_title_label.get_width()//2 - 10, 120))

        helps_label = control_font.render('Help (How to play)', 1, (0, 225, 0))
        CANVAS.blit(helps_label, (starting_x + 125, 270))   #215
        helps_key_label = keys_font.render('press [h]', 1, (240, 0, 0))
        CANVAS.blit(helps_key_label, (starting_x + 470, 270))

        Sdown_label = control_font.render('Speed down', 1, (0, 225, 0))
        CANVAS.blit(Sdown_label, (starting_x + 125, 325))   #270
        Sdown_key_label = keys_font.render('[<]', 1, (240, 0, 0))
        CANVAS.blit(Sdown_key_label, (starting_x + 470, 325))

        Sup_label = control_font.render('Speed up', 1, (0, 225, 0))
        CANVAS.blit(Sup_label, (starting_x + 125, 380))     #325
        Sup_key_label = keys_font.render('[>]', 1, (240, 0, 0))
        CANVAS.blit(Sup_key_label, (starting_x + 470, 380))

        # down_label = control_font.render('Move Down', 1, (0, 225, 0))
        # CANVAS.blit(down_label, (starting_x + 125, 380))
        # down_key_label = keys_font.render('[down] or [s]', 1, (240, 0, 0))
        # CANVAS.blit(down_key_label, (starting_x + 470, 380))
        #
        # up_label = control_font.render('Move Up', 1, (0, 225, 0))
        # CANVAS.blit(up_label, (starting_x + 125, 435))
        # up_key_label = keys_font.render('[up] or [w]', 1, (240, 0, 0))
        # CANVAS.blit(up_key_label, (starting_x + 470, 435))

        mute_label = control_font.render('Mute Audio', 1, (0, 225, 0))
        CANVAS.blit(mute_label, (starting_x + 125, 435))
        mute_key_label = keys_font.render('[m]', 1, (240, 0, 0))
        CANVAS.blit(mute_key_label, (starting_x + 470, 435))

        sfx_label = control_font.render('Volume Up/Down', 1, (0, 225, 0))
        CANVAS.blit(sfx_label, (starting_x + 125, 490))
        sfx_key_label = keys_font.render('[+]/[-]', 1, (240, 0, 0))
        CANVAS.blit(sfx_key_label, (starting_x + 470, 490))

        sfx_label = control_font.render('Toggle Full Screen', 1, (0, 225, 0))
        CANVAS.blit(sfx_label, (starting_x + 125, 545))
        sfx_key_label = keys_font.render('[f]', 1, (240, 0, 0))
        CANVAS.blit(sfx_key_label, (starting_x + 470, 545))

        escape_label = control_font.render('Return back to home', 1, (0, 225, 0))
        CANVAS.blit(escape_label, (starting_x + 125, 600))
        escape_key_label = keys_font.render('[backspace]', 1, (240, 0, 0))
        CANVAS.blit(escape_key_label, (starting_x + 470, 600))

        control_title_label = control_font.render(
            '[Backspace]', 1, (255, 255, 255))
        CANVAS.blit(control_title_label, (starting_x + 30, 30))

        audio_cfg.display_volume(CANVAS)

        pygame.display.update()
        framespersec.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_m: 
                    audio_cfg.toggle_mute() # m => 소리
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    display_cfg.toggle_full_screen()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_h]:
            from .helps import helps
            helps()

        if keys[pygame.K_BACKSPACE]:
            run = False
