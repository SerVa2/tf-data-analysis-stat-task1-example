import pandas as pd
import numpy as np


chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    error = np.random.uniform(-29, np.exp(1), size=n) # сгенерировать ошибку измерения
    v = x + error # скорость с учетом ошибки
    a = np.diff(v) / 10 # расчет ускорения
    return np.mean(a) # точечная оценка коэффициента ускорения
