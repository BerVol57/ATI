import random

## Задача №1

# Один шаблон - очікується лінійне дерево
input_task1_test1 = """1
AGTCCG"""
expectet_output_t1t1 = """0->1:A
1->2:G
2->3:T
3->4:C
4->5:C
5->6:G"""

# Шаблони з різними початковими символами
input_task1_test2 = """4
AGTCCG
GGTCCG
TGTCCG
CGTCCG"""
expectet_output_t1t2 = """0->1:A
1->2:G
2->3:T
3->4:C
4->5:C
5->6:G
0->7:G
7->8:G
8->9:T
9->10:C
10->11:C
11->12:G
0->13:T
13->14:G
14->15:T
15->16:C
16->17:C
17->18:G
0->19:C
19->20:G
20->21:T
21->22:C
22->23:C
23->24:G"""

# Шаблони з довгими спільними префіксами
input_task1_test3 = """4
AGTCCG
AGTTG
AGCGGTGG
AGTCGGGCT"""
expectet_output_t1t3 = """0->1:A
1->2:G
2->3:T
3->4:C
4->5:C
5->6:G
4->7:G
7->8:G
8->9:G
9->10:C
10->11:T
3->12:T
12->13:G
2->14:C
14->15:G
15->16:G
16->17:T
17->18:G
18->19:G"""

# Шаблони різної довжини
input_task1_test4 = """2
A
GTCCG"""
expectet_output_t1t4 = """0->1:A
0->2:G
2->3:T
3->4:C
4->5:C
5->6:G"""

# Шаблони, що є префіксами інших
# (за умовою не можна, але перевіримо чи алгоритм не зависає)
input_task1_test5 = """6
A
AG
AGT
AGTC
AGTCC
AGTCCG"""
expectet_output_t1t5 = """0->1:A
1->2:G
2->3:T
3->4:C
4->5:C
5->6:G"""

# Максимальна кількість шаблонів та 
# максимальна довжина шаблонів (100, 100)
alphabet = ["A", "T", "G", "C"]
input_task1_test6 = "100\n"

input_task1_test6 += "".join(["".join(random.choices(alphabet, k=100)) + "\n" for _ in range(100)])

## Задача №2

# Порожній набір шаблонів
input_task2_test1 = """AGCTCGC
0"""
expectet_output_t2t1 = """"""

# Текст без входженнь жодного з шаблонів
input_task2_test2 = """AAAAAAAAAA
3
GTC
CTG
TGC"""
expectet_output_t2t2 = """"""

# Перевірка правильності індексу 0
input_task2_test3 = """AAAA
1
A"""
expectet_output_t2t3 = """0 1 2 3"""

# Один шаблон, що зустрічається в кінці тексту
input_task2_test4 = """GGGGGA
1
A"""
expectet_output_t2t4 = """5"""

# Один шаблон, який зустрічається кілька разів
input_task2_test5 = """AGAGAGA
1
AGA"""
expectet_output_t2t5 = """0 2 4"""

# Кілька шаблонів, що перекриваються в тексті
input_task2_test6 = """CACACA
2
ACA
CAC"""
expectet_output_t2t6 = """0 1 2 3"""

# Максимальна довжина тексту, 
# максимальна кількість та довжина шаблонів
# штучно вставили один з шаблонів на 9800 місце
pref = "".join(random.choices(alphabet, k=100))
input_task2_test7 = "".join(random.choices(alphabet, k=9_800))
input_task2_test7 += pref + "".join(random.choices(alphabet, k=100)) + "\n5000\n"

input_task2_test7 += "".join(["".join(random.choices(alphabet, k=100)) + "\n" for _ in range(5_000 - 1)])
input_task2_test7 += pref

expectet_output_t2t7 = """9800"""