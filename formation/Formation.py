import numpy as np

def GenerateBasicFormation():

    formation = [
        np.array([-13, 0]),    # Goalkeeper                p1
        np.array([-5, 6]),    # Left Defender              p2
        np.array([-8, 2]),   # Center Back Left            p3
        np.array([-8, -2]),    # Center Back Right         p4
        np.array([-5, -6]),   # Right Defender             p5
        np.array([3, 5]),      # Left Midfielder           p6 
        np.array([1, 0]),      # Center Midfielder Left    p7
        np.array([3, -5]),      # Center Midfielder Right  p8
        np.array([7, 4]),      # Right Midfielder          p9    
        np.array([9, 0]),      # Forward Left              p10
        np.array([7, -4])      # Forward Right             p11
    ]

    return formation
