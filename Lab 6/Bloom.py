from numba import njit
from Hpoly import *
import numpy as np


@njit
def bloom_add(T: np.ndarray, keys: np.ndarray, data: np.ndarray):
    """Додати елемент до фільтра Блума"""
    for k in keys:
        idx = H_poly(k, data)
        T[idx] = True

@njit
def bloom_contains(T: np.ndarray, keys: np.ndarray, data: np.ndarray) -> bool:
    """Перевірити наявність елемента у фільтрі"""
    for k in keys:
        if not T[H_poly(k, data)]:
            return False
    return True