# BWT
def bwt_transform(data):
    """Перетворення Барроуза-Вілера (BWT)"""
    rotations = [data[i:] + data[:i] for i in range(len(data))]
    rotations.sort()
    index = rotations.index(data)
    transformed = bytes([rotation[-1] for rotation in rotations])
    return transformed, index


def ibwt_transform(transformed, index):
    """Зворотне перетворення BWT"""
    reversed_word = sorted(transformed)
    table = {}
    for i in range(len(reversed_word)):
        start_indx = transformed.index(reversed_word[i])
        while transformed.index(reversed_word[i], start_indx) in table.values():
            start_indx += 1
        table[i] = transformed.index(reversed_word[i], start_indx)
    res = []
    for _ in range(len(transformed)):
        index = table[index]
        res.append(transformed[index])
    return bytes(res)



# MTF
def mtf_transform(data):
    """MTF-перетворення"""
    alphabet = list(range(256))
    result = []
    for byte in data:
        idx = alphabet.index(byte)
        result.append(idx)
        # Переміщуємо символ на початок
        alphabet.pop(idx)
        alphabet.insert(0, byte)
    return bytes(result)


def imtf_transform(transformed):
    """Зворотне MTF-перетворення"""
    alphabet = list(range(256))
    result = []
    for idx in transformed:
        byte = alphabet[idx]
        result.append(byte)
        # Оновлюємо алфавіт
        del alphabet[idx]
        alphabet.insert(0, byte)
    return bytes(result)