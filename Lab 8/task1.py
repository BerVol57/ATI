from functools import cmp_to_key

def bwt(input_name, output_name, test_mode=False):
    if test_mode:
        text = input_name
    else:
        with open(input_name, 'r') as f:
            text = f.read().strip()
    
    n = len(text)
    if n == 0:
        return "" if test_mode else None
    
    # Визначаємо функцію порівняння двох обертань за їхніми символами
    def compare_rotations(i, j):
        for k in range(n):
            # Порівнюємо символи обертань для індексів i та j
            ci = text[(i + k) % n]
            cj = text[(j + k) % n]
            if ci < cj:
                return -1
            elif ci > cj:
                return 1
        return 0  # якщо обертання ідентичні
    
    # Сортуємо індекси, використовуючи функцію порівняння
    sorted_indices = sorted(range(n), key=cmp_to_key(compare_rotations))
    
    # Формуємо BWT з символів, що стоять перед відсортованими індексами
    bwt_result = ''.join(text[(i - 1) % n] for i in sorted_indices)
    
    if test_mode:
        return bwt_result
    else:
        with open(output_name, 'w') as f:
            f.write(bwt_result)