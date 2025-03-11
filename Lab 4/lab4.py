import os
import time

def write_bits(f, bits, bit_length):
    """Записує біти у файл з вирівнюванням по байтах."""
    while len(bits) % 8 != 0:
        bits += '0'
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        byte_array.append(int(byte, 2))
    f.write(bytes(byte_array))


def lzw_compress(input_file, output_file, max_bits=12, reset_dict=True):
    # Ініціалізація словника
    dict_size = 256
    dictionary = {bytes([i]): i for i in range(dict_size)}
    
    w = b''
    compressed = []
    bit_buffer = ''
    
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        # Запис заголовка: 1 байт для max_bits та reset_dict
        header = bytes([max_bits, reset_dict])
        f_out.write(header)
        
        while True:
            c = f_in.read(1)
            if not c:
                break
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                compressed.append(dictionary[w])
                # Додавання нової фрази до словника
                if dict_size < (1 << max_bits):
                    dictionary[wc] = dict_size
                    dict_size += 1
                else:
                    if reset_dict:
                        dictionary = {bytes([i]): i for i in range(256)}
                        dict_size = 256
                w = c
        
        if w:
            compressed.append(dictionary[w])
        
        # Конвертація індексів у бітовий рядок
        bit_buffer = "".join([bin(code)[2:].zfill(max_bits) for code in compressed])
        
        # Запис бітів у файл
        write_bits(f_out, bit_buffer, len(bit_buffer))

def lzw_decompress(input_file, output_file):
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        # Читання заголовка
        header = f_in.read(2)
        max_bits = header[0]
        reset_dict = bool(header[1])
        
        # Ініціалізація словника
        dict_size = 256
        dictionary = {i: bytes([i]) for i in range(dict_size)}
        
        # Читання бітового потоку
        bit_data = "".join([bin(byte)[2:].zfill(8) for byte in f_in.read()])
        
        # Обробка бітів
        codes = []
        for i in range(0, len(bit_data), max_bits):
            code_bits = bit_data[i:i+max_bits]
            if not code_bits:
                continue
            codes.append(int(code_bits, 2))
        
        # Декодування
        w = bytes([codes.pop(0)])
        f_out.write(w)
        
        for k in codes:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[0:1]
            else:
                raise ValueError(f'Невірний код: {k}')
            
            f_out.write(entry)
            
            # Оновлення словника
            if dict_size < (1 << max_bits):
                dictionary[dict_size] = w + entry[0:1]
                dict_size += 1
            elif reset_dict:
                dictionary = {i: bytes([i]) for i in range(256)}
                dict_size = 256
            
            w = entry


# Стискання
# 1
start_time = time.time()
lzw_compress("INPUT/маленький володар перснів.docx", "COMPRESSED/compressed_маленький володар перснів.lzw")
print(time.time() - start_time)

start_time = time.time()
lzw_decompress("COMPRESSED/compressed_маленький володар перснів.lzw", "DECOMPRESSED/decompressed_маленький володар перснів.docx")
print(time.time() - start_time)

# 2
start_time = time.time()
lzw_compress("INPUT/pngegg.png", "COMPRESSED/compressed_pngegg.lzw")
print(time.time() - start_time)

start_time = time.time()
lzw_decompress("COMPRESSED/compressed_pngegg.lzw", "DECOMPRESSED/decompressed_pngegg.png")
print(time.time() - start_time)

# 3
start_time = time.time()
lzw_compress("INPUT/task03.pdf", "COMPRESSED/compressed_task03.lzw")
print(time.time() - start_time)

start_time = time.time()
lzw_decompress("COMPRESSED/compressed_task03.lzw", "DECOMPRESSED/decompressed_task03.pdf")
print(time.time() - start_time)

# 4
start_time = time.time()
lzw_compress("INPUT/test2.exe", "COMPRESSED/compressed_test2.lzw")
print(time.time() - start_time)

start_time = time.time()
lzw_decompress("COMPRESSED/compressed_test2.lzw", "DECOMPRESSED/decompressed_test2.exe")
print(time.time() - start_time)

# 5
start_time = time.time()
lzw_compress("INPUT/повноцінний Володар перснів.txt", "COMPRESSED/compressed_повноцінний Володар перснів.lzw")
print(time.time() - start_time)

start_time = time.time()
lzw_decompress("COMPRESSED/compressed_повноцінний Володар перснів.lzw", "DECOMPRESSED/decompressed_повноцінний Володар перснів.txt")
print(time.time() - start_time)