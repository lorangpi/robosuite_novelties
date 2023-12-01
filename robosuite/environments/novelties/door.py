import numpy as np
from robosuite.environments.manipulation.pick_place import PickPlaceCan

class Door(PickPlaceCan):
    """
    Door novelty: an unlocked door is placed in between the pick and drop areas.
    """

    def __init__(self, **kwargs):
        super().__init__(door_pos=(-0.05, 0.4, 0.1, -np.pi/2), plate_pos=(-0.4, -0.225, 0.1), door_locked=False, novelty="Door", **kwargs)

