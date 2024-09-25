import numpy as np

def GenerateBasicFormation():

    formation = [
        np.array([-13, 0]),    # Goalkeeper
        np.array([-10, 6]),  # Left Defender
        np.array([-10, 2]),   # Center Back Left
        np.array([-10, -2]),    # Center Back Right
        np.array([-10, -6]),   # Right Defender
        np.array([1, 5]),    # Left Midfielder
        np.array([1, 0]),    # Center Midfielder Left
        np.array([1, -5]),     # Center Midfielder Right
        np.array([8, 0]),     # Right Midfielder
        np.array([9, 1]),    # Forward Left
        np.array([12, 0])      # Forward Right
    ]

    return formation
