import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import * 

DUCK_IMG = { DEFAULT_TYPE: DUCKING, HEAD_TYPE: DUCKING}
JUMP_IMG = { DEFAULT_TYPE: JUMPING, HEAD_TYPE: JUMPING_HEAD}
RUN_IMG = { DEFAULT_TYPE: RUNNING, HEAD_TYPE: RUNNING_HEAD}

class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True 
        self.dino_jump = False
        self.jump_vel = JUMP_VEL
        self.dino_duck = False
        self.time = 0
        self.animacao = 0
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0    

    def update(self, user_input):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump() 
        elif self.dino_duck:
            self.duck()        
        
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False 
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True 
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False     

        if self.step_index >= 9:
            self.step_index = 0     

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.time += 1
        if self.time == 10:
            self.animacao += 1
            self.time = 0
        self.image = RUN_IMG[self.type][self.animacao]
        self.dino_rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        if self.animacao == 3:
            self.animacao = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.image = pygame.transform.scale(self.image, (200, 200))
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL


    def duck(self):
        self.time += 1
        if self.time == 10:
            self.animacao += 1
            self.time = 0
        self.image = DUCK_IMG[self.type][self.animacao]
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = 290
        self.step_index += 1
        self.dino_duck = False
        if self.animacao == 3:
            self.animacao = 0


