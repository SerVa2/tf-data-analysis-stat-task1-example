import pandas as pd
import numpy as np


chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    acceleration = -(np.log(1 - np.mean(x)/29))/10
    return acceleration
    
