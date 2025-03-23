# BWT
def bwt_transform(data):
    """Перетворення Барроуза-Вілера (BWT)"""
    rotations = [data[i:] + data[:i] for i in range(len(data))]
    rotations.sort()
    index = rotations.index(data)
    transformed = bytes([rotation[-1] for rotation in rotations])
    return transformed, index

#
with open('test.txt', 'rb') as f:
    test = f.read()

with open('test_bwt.txt', 'wb') as f:
    bwt_data, idx = bwt_transform(test)
    f.write(bwt_data)
    f.write(bytes([idx]))

with open('test_bwt.txt', 'rb') as f:
    test = f.read()
#

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

#
with open('test_ibwt.txt', 'wb') as f:
    ibwt_data = ibwt_transform(test[:-1], test[-1])
    f.write(ibwt_data)
#


# MTF
def mtf_transform(data):
    """MTF-перетворення"""
    alphabet = list(range(256))
    result = []
    for byte in data:
        # print(byte)
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
    # print(transformed)
    for idx in transformed:
        # print(idx)
        byte = alphabet[idx]
        result.append(byte)
        # Оновлюємо алфавіт
        del alphabet[idx]
        alphabet.insert(0, byte)
    return bytes(result)