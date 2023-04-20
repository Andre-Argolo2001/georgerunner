from dino_runner.utils.constants import HEAD, HEAD_TYPE, SHIELD_TYPE, SHIELD
from dino_runner.components.powerups.power_up import PowerUp


class Shield(PowerUp):
    def __init__(self):
        self.image = HEAD
        self.type = HEAD_TYPE
        super().__init__(self.image, self.type)
        