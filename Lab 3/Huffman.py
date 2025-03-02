from huffman_tree import *
import time


def huffman_dict_to_bits(huffman_codes):
    bitstream = []
    current_byte = 0
    bit_count = 0

    for symbol, code in huffman_codes.items():
        bitstream.append(bin(symbol)[2:].zfill(8))
        
        code_length = len(code)
        bitstream.append(bin(code_length)[2:].zfill(8))
        
        for bit in code:
            current_byte = (current_byte << 1) | int(bit)
            bit_count += 1
            if bit_count == 8:
                bitstream.append(bin(current_byte)[2:].zfill(8))
                current_byte = 0
                bit_count = 0
        
        if bit_count > 0:
            current_byte <<= (8 - bit_count)
            bitstream.append(bin(current_byte)[2:].zfill(8))
            current_byte = 0
            bit_count = 0

    return bitstream


def bits_to_huffman_dict(bitstream):
    huffman_codes = {}
    bitstream = bitstream
    bit_position = 0

    while bit_position < len(bitstream):
        symbol = bitstream[bit_position]
        bit_position += 1
        
        code_length = bitstream[bit_position]
        bit_position += 1
        
        code = ""
        bits_remaining = code_length
        while bits_remaining > 0:
            current_byte = bitstream[bit_position]
            bit_position += 1
            for i in range(7, -1, -1):
                if bits_remaining == 0:
                    break
                bit = (current_byte >> i) & 1
                code += str(bit)
                bits_remaining -= 1
        
        huffman_codes[symbol] = code

    return huffman_codes



def encode(input_file_name, output_file_name):
    with open(input_file_name, "rb") as f:
        data = f.read()

    table = dict()
    
    # Підрахунок символів
    for el in data:
        if el in table:
            table[int(el)] += 1
        else:
            table[int(el)] = 1

    symbols, counts = [], []
    # Створення окремих списків для символів 
    # та для скільки кожен символ зустрічається
    for (s, c) in table.items():
        symbols.append(s)
        counts.append(c)

    # Генерування дерева Хаффмана та словник
    node = build_huffman_tree(symbols, counts)
    HCode = generate_huffman_codes(node)

    # Кодування словника Хаффмана
    encoded_hcode = huffman_dict_to_bits(HCode)
    lehc = len(encoded_hcode)
    lehc_bin = bin(lehc)[2:].zfill(13)
    # print(lehc)

    # Кодування основної частини файлу
    encoded_parts = []
    for b in data:
        encoded_parts.append(HCode[b])
    encoded_file = "".join(encoded_parts)
    print(f"Encoded main part in bits: {len(encoded_file)}\nEncoded main part in bytes: {len(encoded_file)//8}")

    # Чорна магія із з'єднанням усього разом
    # Якої кількості бітів не вистачає щоб закрити байт
    fill_gap_zero = (8 - len(encoded_file) % 8) % 8
    # print(fill_gap_zero)
    # 3 біти на кількість бітів що не вистачило для закриття байту
    # наступні 13 кількість наступних байтів, що виділенно на словник Хаффмана
    # сама таблиця Хаффмана та основна частина
    ef_str = "".join([bin(fill_gap_zero)[2:].zfill(3), lehc_bin, "".join(encoded_hcode), encoded_file, "0"*fill_gap_zero])
    efs_list = [int(ef_str[i:i+8], 2) for i in range(0, len(ef_str), 8)]
    encoded_file_bytes = bytes(efs_list)

    # Запис усього "добра" у файл
    with open(output_file_name, "wb") as f:
        f.write(encoded_file_bytes)
    


def decode(input_file_name, output_file_name= None):
    with open(input_file_name, "rb") as f:
        input_data = f.read()
    
    fgz_lehc = bin(input_data[0])[2:].zfill(8) + bin(input_data[1])[2:].zfill(8)
    fgz = int(fgz_lehc[:3], 2)
    lehc = int(fgz_lehc[3:], 2)
    print(f"lehc: {lehc}")
    # print(f"fgz: {fgz}\nlehc: {lehc}")
    hcode = bits_to_huffman_dict(input_data[2: lehc+2])
    hdecode = {k: v for v, k in hcode.items()}
    
    data = [bin(el)[2:].zfill(8) for el in input_data[lehc+2:]]
    data = "".join(data)
    data = data[:len(data) - fgz]
    
    decoded_data = []
    ccode = ""
    for bit in data:
        ccode += bit
        if ccode in hdecode:
            decoded_data.append(hdecode[ccode])
            ccode = ""
    
    output_data = bytes(decoded_data)
    
    with open(output_file_name, "wb") as f:
        f.write(output_data)
    

print("\nмаленький володар перснів.txt")
start_time = time.time()
encode("Input/маленький володар перснів.txt", "Coded/маленький володар перснів.txt.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/маленький володар перснів.txt.huffman", "Decoded/DECODED маленький володар перснів.txt")
print(f"Decoding time: {time.time() - start_time}")



print("\nповноцінний Володар перснів.txt")
start_time = time.time()
encode("Input/повноцінний Володар перснів.txt", "Coded/повноцінний Володар перснів.txt.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/повноцінний Володар перснів.txt.huffman", "Decoded/DECODED повноцінний Володар перснів.txt")
print(f"Decoding time: {time.time() - start_time}")



print("\ntest1.exe")
start_time = time.time()
encode("Input/test1.exe", "Coded/test1.exe.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/test1.exe.huffman", "Decoded/DECODED test1.exe")
print(f"Decoding time: {time.time() - start_time}")



print("\ntest2.exe")
start_time = time.time()
encode("Input/test2.exe", "Coded/test2.exe.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/test2.exe.huffman", "Decoded/DECODED test2.exe")
print(f"Decoding time: {time.time() - start_time}")



print("\nПсевдо Силабус_Інформаційна безпека.doc")
start_time = time.time()
encode("Input/Псевдо Силабус_Інформаційна безпека.doc", "Coded/Псевдо Силабус_Інформаційна безпека.doc.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/Псевдо Силабус_Інформаційна безпека.doc.huffman", "Decoded/DECODED Псевдо Силабус_Інформаційна безпека.doc")
print(f"Decoding time: {time.time() - start_time}")



print("\nмаленький володар перснів.docx")
start_time = time.time()
encode("Input/маленький володар перснів.docx", "Coded/маленький володар перснів.docx.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/маленький володар перснів.docx.huffman", "Decoded/DECODED маленький володар перснів.docx")
print(f"Decoding time: {time.time() - start_time}")



print("\nмаленький володар перснів.rtf")
start_time = time.time()
encode("Input/маленький володар перснів.rtf", "Coded/маленький володар перснів.rtf.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/маленький володар перснів.rtf.huffman", "Decoded/DECODED маленький володар перснів.rtf")
print(f"Decoding time: {time.time() - start_time}")



print("\nповноцінний Володар перснів.rtf")
start_time = time.time()
encode("Input/повноцінний Володар перснів.rtf", "Coded/повноцінний Володар перснів.rtf.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/повноцінний Володар перснів.rtf.huffman", "Decoded/DECODED повноцінний Володар перснів.rtf")
print(f"Decoding time: {time.time() - start_time}")



print("\ntask03.pdf")
start_time = time.time()
encode("Input/task03.pdf", "Coded/task03.pdf.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/task03.pdf.huffman", "Decoded/DECODED task03.pdf")
print(f"Decoding time: {time.time() - start_time}")



print("\npngegg.png")
start_time = time.time()
encode("Input/pngegg.png", "Coded/pngegg.png.huffman")
print(f"Encoding time: {time.time() - start_time}")

start_time = time.time()
decode("Coded/pngegg.png.huffman", "Decoded/DECODED pngegg.png")
print(f"Decoding time: {time.time() - start_time}")