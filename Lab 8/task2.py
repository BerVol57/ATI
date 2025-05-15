def inverse_bwt(bwt):
        """Обернене BWT з використанням First Occurrence та Rank"""
        # Відсортована перша колонка (F)
        F = sorted(bwt)
        len_bwt = len(bwt)
        
        # 1. Обчислюємо First Occurrence для кожного символу в F
        first_occurrence = {}
        for i, char in enumerate(F):
            if char not in first_occurrence:
                first_occurrence[char] = i
        
        # 2. Обчислюємо префіксні суми (Rank) для кожного символу в BWT
        chars = ["$", "A", "C", "G", "T"]
        rank = {c: [0] * (len_bwt + 1) for c in chars}
        
        for i in range(len_bwt):
            current_char = bwt[i]
            for c in chars:
                rank[c][i+1] = rank[c][i]
            rank[current_char][i+1] += 1
        
        # 3. Відновлюємо оригінальний рядок
        original = []
        current_row = F.index('$')
        for _ in range(len_bwt):
            char = bwt[current_row]
            original.append(char)
            current_row = first_occurrence[char] + rank[char][current_row]
        
        original = original[::-1]
        original.pop(0)
        return ''.join(original) + "$"


def ibwt(input_name, output_name, test_mode=False):
    if test_mode:
        bwt_str = input_name
    else:
        with open(input_name, 'r') as f:
            bwt_str = f.read().strip()
    
    original_str = inverse_bwt(bwt_str)

    if test_mode:
        return original_str
    else:
        with open(output_name, 'w') as f:
            f.write(original_str)