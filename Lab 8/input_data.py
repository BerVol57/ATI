import random
## Задача №1
# Мінімальн довжина 
task1_input1 = "$"
task1_output1 = "$"

# Усі символи однакові
task1_input2 = "A"*1000 + "$"
task1_output2 = task1_input2

# Максимальна довжина, не повинно вибивати
alphabet = ["A", "G", "C", "T"]
task1_input3 = "".join(random.choices(alphabet, k=10**3)) + "$"

# Унікальні циклічні зсуви
task1_input4 = "CAGATA$"
task1_output4 = "ATCG$AA"


## Задача №2
# Мінімальна довжина
task2_input1 = "$"
task2_output1 = "$"

# BWT з повтореннями символів
task2_input2 = "AC$A"
task2_output2 = "ACA$"

# Максимальна довжина
task2_input3 = random.choices(alphabet, k=1_000_001)
task2_input3[random.randint(0, 1_000_000)] = "$"
task2_input3 = "".join(task2_input3)

# Складні BWT з багатьма символами
task2_input4 = task1_output4
task2_output4 = task1_input4


## Задача №3
# Шабло довший за текст
task3_input1 = "CA\nAGTA"
task3_output1 = 0

# Шаблон відсутній у тексті
task3_input2 = "AGTA\nCAT"      #хе-хе кіт :)
task3_output2 = 0

# Декілька входжень шаблону
task3_input3 = "ACACGACTA\nAC"
task3_output3 = 3

# Шаблон на межі текстів (початок\кінець)
task3_input4 = "TAGACAT\nT"
task3_output4 = 2