import asyncio
import random
stand_list_file = open('standnames.txt', 'r')
stand_list = stand_list_file.readline()
stand_name_list = stand_list.split(',')
stand_stat_type = ['Power', 'Speed', 'Range', 'Durability', 'Precision', 'Potential']

#this will write a ".txt" document that stores names for stands. Do this first before anything else.
def write_stand_list():
    stand_list_write = open('standnames.txt', 'w')
    return stand_list_write

def stand_name():
    name = ""
    while name == "":
        name = stand_name_list[random.randint(0, len(stand_name_list)-1)]
        if name == "":
            return
        else:
            return name
def send_stand_stat(stat):
    letter = ["A", "B", "C", "D", "E"]
    letter_grade = letter[random.randint(0, 4)]
    return "{0}: {1}" .format(stand_stat_type[stat], letter_grade)
def random_stand():
    return '***{6}*** \n  {0} \n  {1} \n  {2} \n  {3} \n  {4} \n  {5}'.format(send_stand_stat(0), send_stand_stat(1),send_stand_stat(2),send_stand_stat(3),send_stand_stat(4),send_stand_stat(5),stand_name())
def stand_exist(stand_name):
    if stand_name_list.count(stand_name) == 0:
        return False
    elif stand_name_list.count(stand_name) >= 1:
        return True
def remove_stand(stand_name):
    if stand_exist(stand_name) == True:
        stand_name_list.remove(stand_name)
        stand_list_overwrite = open('standnames.txt', 'w')
        stand_list_overwrite
        for item in stand_name_list:
            stand_list_overwrite.write("%s," % item)
    else:
        return
def add_stand(stand_name):
    if stand_exist(stand_name) == False:
            with open("standnames.txt", "a") as myfile:
                myfile.write(',')
                myfile.write(name)
    else:
        return
