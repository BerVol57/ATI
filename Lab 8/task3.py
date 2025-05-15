from task1 import bwt as bwt_

def get_bwt(text):
    return bwt_(text, "", True)
    
def bw_matching(text, pattern):
    bwt = get_bwt(text)
    st = sorted(bwt)
    indexs = list(range(len(text)))
    
    table = {}
    for i in range(len(st)):
        start_indx = bwt.index(st[i])
        while bwt.index(st[i], start_indx) in table.values():
            start_indx += 1
        table[i] = bwt.index(st[i], start_indx)
    
    for symb in pattern:
        indexs = [table[i] for i in indexs if bwt[i] == symb]
    return len(indexs)


def matching(input_name, output_name="", test_mode=False):
    if test_mode:
        temp = input_name.split()
        text = temp[0]
        pattern = temp[1]
    else:
        with open(input_name, 'r') as f:
            text = f.readline().strip()
            pattern = f.readline().strip()

        if not text.endswith('$'):
            text += '$'

    count = bw_matching(text, pattern)

    if test_mode:
        return count
    else:
        with open(output_name, 'w') as f:
            f.write(str(count))