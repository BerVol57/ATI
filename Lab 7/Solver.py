from PrefixTrie import *


def solve_task1(input_file: str, output_file: str = "", 
                read_from_file = True, write2file = True):
    
    try:
        if read_from_file:
            with open(input_file, 'r') as f:
                n = int(f.readline())
                patterns = [f.readline().strip() for _ in range(n)]
        else:
            data = input_file.split()
            
            if data[0].isdigit():
                n = int(data[0])
                patterns = data[1:]
            else:
                print("Їжачок розлючений... Видали цю нісенітницю!")
                return
            
        trie = Trie()
        for pattern in patterns:
            trie.insert(pattern)

        adjacency_list = trie.get_adjacency_list()

        if write2file:
            with open(output_file, 'w') as f_out:
                for start, end, char in adjacency_list:
                    f_out.write(f"{start}->{end}:{char}\n")
        else:
            return "\n".join([f"{edge[0]}->{edge[1]}:{edge[2]}" 
                              for edge in adjacency_list])

    except Exception as e:
        print(f"Помилка: {e}")
        return None


def solve_task2(input_file: str, output_file: str = "", 
                read_from_file = True, write2file = True):

    try:
        if read_from_file:
            with open(input_file, 'r') as f:
                text = f.readline().strip()
                n = int(f.readline())
                patterns = [f.readline().strip() for _ in range(n)]
        else:
            data = input_file.split()
            text = data[0]
            if data[1].isdigit():
                n = int(data[1])
                patterns = data[2:]
            else:
                if write2file:
                    with open(output_file, "W") as f:
                        f.write()
                return
    
        trie = Trie()
        for pattern in patterns:
            trie.insert(pattern)


        occurrences = []
        for i in range(len(text)):
            current_node = trie.root
            for j in range(i, len(text)):
                char = text[j]
                if char in current_node.children:
                    current_node = current_node.children[char]
                    if current_node.is_end_of_word:
                        occurrences.append(i)
                        break
                else:
                    break

        # occurrences.sort()
        
        if write2file:
            with open(output_file, 'w') as f_out:
                if occurrences:
                    f_out.write(" ".join(map(str, occurrences)))
                else:
                    pass # Write an empty file as per the example
        else:
            return " ".join(map(str, occurrences))

    except Exception as e:
        print(f"Помилка: {e}")
        return None