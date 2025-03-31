from numba import njit
import numpy as np

N = 1 << 16

@njit
def H_poly(k: int, data: np.ndarray) -> int:
    """Поліноміальна геш-функція"""
    result = 1
    for i in range(0, len(data), 2):
        x_i = data[i] + (data[i+1] << 8)
        result = (result * k + x_i) % N
    return result

@njit
def preprocess_data(s_chars: np.ndarray) -> np.ndarray:
    """Попередня обробка рядка"""
    length = len(s_chars)
    if length % 2 != 0:
        padded = np.zeros(length + 1, dtype=np.uint8)
        padded[:length] = s_chars
        return padded
    return s_chars