# ECE4424 Fake News Detection Project
# Topic - Utils
# Authors - Kevin Lizarazu
# Last Modified: 04/17/23

import json
import numpy as np

# Loads configuration contents of JSON structure 
def loadConfig(path: str) -> dict:

    cfg = json.load(open(path, "r"))
    for key, element in cfg.items():
        if isinstance(element, list):
            cfg[key] = np.array(element)
            
    return cfg