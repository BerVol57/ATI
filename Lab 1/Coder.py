BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
PADDING_CHAR = '='
COMMENT_CHAR = '-'

def base64_encode(data):
    encoded = []
    for i in range(0, len(data), 3):
        chunk = data[i:i+3]
        if len(chunk) == 3:
            a, b, c = chunk 
            encoded.append(BASE64_ALPHABET[(a >> 2)])
            encoded.append(BASE64_ALPHABET[((a & 3) << 4) ^ (b >> 4)])
            encoded.append(BASE64_ALPHABET[((b & 15) << 2) ^ (c >> 6)])
            encoded.append(BASE64_ALPHABET[c & 63])
        else:
            if len(chunk) == 2:
                a, b = chunk
                encoded.append(BASE64_ALPHABET[(a >> 2)])
                encoded.append(BASE64_ALPHABET[((a & 3) << 4) ^ (b >> 4)])
                encoded.append(BASE64_ALPHABET[(b & 15) << 2])
                encoded.append(PADDING_CHAR)
            else:
                a = chunk[0]
                encoded.append(BASE64_ALPHABET[a >> 2])
                encoded.append(BASE64_ALPHABET[(a & 3) << 4])
                encoded.append(PADDING_CHAR)
                encoded.append(PADDING_CHAR)
    return ''.join(encoded)

def encode_file(input_file, output_file=None):
    if output_file is None:
        output_file = input_file + '.base64'
    
    with open(input_file, 'rb') as f:
        data = f.read()
    
    encoded_data = base64_encode(data)
    
    with open(output_file, 'w') as f:
        for i in range(0, len(encoded_data), 76):
            f.write(encoded_data[i:i+76] + '\n')
    
    print(f"File encoded and saved as {output_file}")

# Приклад використання
encode_file('pngegg.png')