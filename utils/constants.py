import pygame
import os

# Global Constants
TITLE = "George run"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
X_POS_BG = 0 
Y_POS_BG = 380
GAME_SPEED = 20
TIME = 0

X_POS = 80
Y_POS = 280

Y_POS_DUCK = 340

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino/dead0.png"))
pygame.transform.scale(ICON, (200, 200))
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/andando0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/andando1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/andando2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/andando3.png")),
]

RUNNING_HEAD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/ativado0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/ativado1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/ativado2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/ativado3.png")),
]
RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/andando1.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_HEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/ativado1.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/abaixado0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/abaixado1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/abaixado2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/abaixado3.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
HEAD = pygame.image.load(os.path.join(IMG_DIR, 'Other/cabeca_dinosauro.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

JUMP_VEL = 8.5

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HEAD_TYPE = "cabeca"