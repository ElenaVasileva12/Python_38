# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию,
#  Вы должны реализовать функционал для изменения и удаления данных

import os
filename = "tell.txt"

def load_tel():
    if os.path.isfile(filename):
        with open(filename, encoding="UTF-8") as f:
            r = f.readlines()
            s = []
            for line in r:
                s.append(line.split())
        return s
    s = []
    return s

def input_tel(s):
    first_name = input("Введите имя: ")
    patronimic = input("Введите отчество: ")
    last_name = input("Введите фамилию: ")
    tel = input("Введите телефон: ")
    with open(filename, "a", encoding="UTF-8") as f:
        f.write(f"{last_name} {first_name} {patronimic} {tel} \n")
    s.append([last_name, first_name, patronimic, tel])
    return s

def search_tel(s, object): #Поиск данных
    for line in s:
        if object in line or object.capitalize() in line:
            return " ".join(line)
    return "Записи не найдено"

def write_tell(s, old_name,new_name): #Изменение данных (в одну строку)
    new_line=[' '.join(line).replace(old_name,new_name) if old_name in line else ' '.join(line) for line in s]
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(f"{new_line} \n")
       
    return new_line

def delete_tell(s, old_name): #Удаление данных (в одну строку)
    new_line=[' '.join(line).replace(old_name,'') if old_name in line else ' '.join(line) for line in s]
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(f"{new_line} \n")
    return new_line
 
def show_tell(s):
    for line in s:
        print(" ".join(line))


if __name__ == "__main__":
    s = load_tel()
    while True:
        action = input("1 - Добавить данные \n2 - Искать данные \n3 - Посмотреть \n4 - Изменить \n5 - Удалить \n6 - Выход:\n")
        if action == "1":
            s = input_tel(s)
        elif action == "2":
            search_name = input("Ищите! ")
            print(search_tel(s, search_name))
        elif action == "3":
            show_tell(s)
        elif action == "4":
            old_name=input("Ищем! ")
            new_name=input("На что меняем? ")
            print(write_tell(s,old_name,new_name))
        elif action == "5":
            old_name=input("Запишите то что нужно удалить:  ")
            print(delete_tell(s,old_name))
        elif action == "6":
            print("Good bye!")
            break
        else:
            print("Подумай!!!")