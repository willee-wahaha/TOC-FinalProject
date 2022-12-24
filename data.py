import random

names = ["aaa", "bbb", "ccc"]
pics = ["FR9W2eDXoAAMv-j", "E2RdeZHWQAYqeND", "ExXH73KXAAIGcvq"]

char_name = 0
char_pics = 0

def reset():
    char_name = 0
    char_pics = 0

    filename = 'savedata.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics))

    filename = 'data.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics))

def save():
    filename = 'data.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
                i += 1
            else:
                char_pics = int(lines)

    filename = 'savedata.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics))

def load():
    filename = 'savedata.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
                i += 1
            else:
                char_pics = int(lines)

    filename = 'data.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics))

def create():
    char_name = random.randint(0, len(names) - 1)
    char_pics = random.randint(0, len(pics) - 1)
    
    filename = 'data.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics))

def get_name():
    filename = 'data.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
                i += 1
            else:
                char_pics = int(lines)
    return names[char_name]

def get_photo():
    filename = 'data.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
                i += 1
            else:
                char_pics = int(lines)

    return pics[char_pics]

