import numpy as np


# The passes happen according to the number sequence 1 -> 2 -> 3 -> 4 .... 11 -> Goal
def GenerateBasicFormation(current_playmode, world_playmodes):
    formation = [
        np.array([-13, 0]),  # Goalkeeper               p1
        np.array([-9, -2]),  #                          p2
        np.array([-4, -2]),  #                          p3
        np.array([-6, 2]),  #                          p4
        np.array([-2, 4]),  #                          p5
        np.array([3, 3]),  #                          p6
        np.array([-0.5, 0]),  #                          p7
        np.array([3, -4]),  #                          p8
        np.array([7, -3]),  #                          p9
        np.array([9, 2]),  #                          p10
        np.array([12, -1]),  #                          p11
    ]
    if current_playmode == world_playmodes.M_OUR_CORNER_KICK:
        return [
            np.array([-13, 0]),
            np.array([5, -5]),
            np.array([5, 0]),
            np.array([5, 5]),
            np.array([-5, 0]),
            np.array([-10, -5]),
            np.array([-10, 0]),
            np.array([-10, 5]),
            np.array([-13, -7]),
            np.array([-14, -5]),
            np.array([-13, -7]),
        ]
    if current_playmode == world_playmodes.M_OUR_FREE_KICK:
        return [
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
        ]
    if current_playmode == world_playmodes.M_OUR_GOAL_KICK:
        return [
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
        ]
    if current_playmode == world_playmodes.M_OUR_KICK_OFF:
        return [
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
            np.array([-13, 0]),
        ]

    return formation
