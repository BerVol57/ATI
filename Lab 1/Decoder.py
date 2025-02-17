BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
PADDING_CHAR = '='
COMMENT_CHAR = '-'

def base64_decode(encoded_data):
    decoded = bytearray()
    for i in range(0, len(encoded_data), 4):
        chunk = encoded_data[i:i+4]
        if len(chunk) == 4:
            a = BASE64_ALPHABET.find(chunk[0])
            b = BASE64_ALPHABET.find(chunk[1])
            c = BASE64_ALPHABET.find(chunk[2])
            d = BASE64_ALPHABET.find(chunk[3])
            
            if a == -1 or b == -1 or (c == -1 and chunk[2] != PADDING_CHAR) or (d == -1 and chunk[3] != PADDING_CHAR):
                raise ValueError("Invalid character in input")
            
            decoded.append((a << 2) ^ (b >> 4))
            if chunk[2] != PADDING_CHAR:
                decoded.append(((b & 15) << 4) ^ (c >> 2))
            
            if chunk[3] != PADDING_CHAR:
                decoded.append(((c & 3) << 6) ^ d)

    return bytes(decoded)

def decode_file(input_file, output_file=None):
    if output_file is None:
        if input("Автоматично назвати файл [нажміть ENTER]:") == "":
            if input_file.endswith('.base64'):
                output_file = input_file[:-7]
            else:
                output_file = input_file + '.decoded'
        else:
            print("Згоду на автоматичну назву не надано...")
            return
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    update_lines = []
    for line in lines:
        if line.startswith(COMMENT_CHAR):
            continue
        else:
            update_lines.append(line)
    
    lines = update_lines

    encoded_data = []
    for line_num, line in enumerate(lines, start=1):
        line = line.strip()
        if len(line) != 76 and line_num != len(lines):
            raise ValueError(f"Рядок {line_num}: Некоректна довжина рядку ({len(line)})")
        for i in range(len(line)):
            if line[i] not in BASE64_ALPHABET + PADDING_CHAR:
                raise ValueError(f"Рядок {line_num}, символ {i+1}: Некоректний вхідний символ ({line[i]})")
            if PADDING_CHAR in line:
                padding_index = line.find(PADDING_CHAR)
                if padding_index != len(line) - 1 and padding_index != len(line) - 2:
                    raise ValueError(f"Рядок {line_num}: Неправильне використання паддінгу")

        encoded_data.append(line)
    
    encoded_data = ''.join(encoded_data)
    
    try:
        decoded_data = base64_decode(encoded_data)
    except ValueError as e:
        print(f"Помилка декодування: {e}")
        return
    
    with open(output_file, 'wb') as f:
        f.write(decoded_data)
    
    print(f"Файл декодовано та збережено як {output_file}")

# Приклад використання
decode_file('pngegg.png.base64')