import random

names = ["Amelia",
"Benjamin",
"Charlotte",
"David",
"Emily",
"Finn",
"Grace",
"Henry",
"Isabella",
"Jack",
"Lily",
"Max",
"Olivia",
"Percy",
"Quinn",
"Ruby",
"Samuel",
"Tess",
"Umberto",
"Violet",
"Wyatt",
"Zoe",
]
pics = ["FR9W2eDXoAAMv-j", "E2RdeZHWQAYqeND", "ExXH73KXAAIGcvq"]
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

char_name = 0
char_pics = 0
char_level = 1

m_name = ""
m_level = -1

def reset():
    char_name = 0
    char_pics = 0
    char_level = -1

    m_name = "0"
    m_level = -1

    filename = 'savedata.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics) + "\n")
        f.writelines(str(char_level))

    filename = 'data.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics) + "\n")
        f.writelines(str(char_level))

    filename = 'savemonster.txt'
    with open(filename, 'w') as f:
        f.writelines(str(m_name) + "\n")
        f.writelines(str(m_level))

    filename = 'monster.txt'
    with open(filename, 'w') as f:
        f.writelines(str(m_name) + "\n")
        f.writelines(str(m_level))

def save():
    filename = 'data.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
            elif(i == 1):
                char_pics = int(lines)
            else:
                char_level = int(lines)

            i += 1

    filename = 'monster.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                m_name = str(lines)
                index = m_name.rfind("\n")
                if index != -1:
                    m_name = m_name[:index]
            else:
                m_level = int(lines)

            i += 1

    filename = 'savedata.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics) + "\n")
        f.writelines(str(char_level))

    filename = 'savemonster.txt'
    with open(filename, 'w') as f:
        f.writelines(str(m_name) + "\n")
        f.writelines(str(m_level))

def load():
    filename = 'savedata.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
            elif(i == 1):
                char_pics = int(lines)
            else:
                char_level = int(lines)

            i += 1

    filename = 'savemonster.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                m_name = str(lines)
                index = m_name.rfind("\n")
                if index != -1:
                    m_name = m_name[:index]
            else:
                m_level = int(lines)

            i += 1

    filename = 'data.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics) + "\n")
        f.writelines(str(char_level))

    filename = 'monster.txt'
    with open(filename, 'w') as f:
        f.writelines(str(m_name) + "\n")
        f.writelines(str(m_level))

def create():
    char_name = random.randint(0, len(names) - 1)
    char_pics = random.randint(0, len(pics) - 1)
    char_level = 1

    filename = 'data.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics) + "\n")
        f.writelines(str(char_level))

def new_monster():

    filename = 'data.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
            elif(i == 1):
                char_pics = int(lines)
            else:
                char_level = int(lines)

            i += 1

    m_name = ""

    l = random.randint(5, 20)
    for i in range(l):
        m_name = m_name + chars[random.randint(0, len(chars) - 1)]
    
    low = int(char_level / 5)
    if(low <= 0): 
        low = 1
    m_level = random.randint(low, char_level * 5)

    filename = 'monster.txt'
    with open(filename, 'w') as f:
        f.writelines(str(m_name) + "\n")
        f.writelines(str(m_level))

def get_name():
    filename = 'data.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
            elif(i == 1):
                char_pics = int(lines)
            else:
                char_level = int(lines)

            i += 1
    
    return names[char_name]

def get_photo():
    filename = 'data.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
            elif(i == 1):
                char_pics = int(lines)
            else:
                char_level = int(lines)

            i += 1

    return pics[char_pics]

def get_level():
    filename = 'data.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
            elif(i == 1):
                char_pics = int(lines)
            else:
                char_level = int(lines)

            i += 1

    return char_level

def get_monster_name():
    filename = 'monster.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                m_name = str(lines)
                index = m_name.rfind("\n")
                if index != -1:
                    m_name = m_name[:index]
            else:
                m_level = int(lines)

            i += 1

    return m_name

def get_monster_level():
    filename = 'monster.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                m_name = str(lines)
                index = m_name.rfind("\n")
                if index != -1:
                    m_name = m_name[:index]
            else:
                m_level = int(lines)

            i += 1

    return m_level

def fight_with_monster():
    filename = 'data.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                char_name = int(lines)
            elif(i == 1):
                char_pics = int(lines)
            else:
                char_level = int(lines)

            i += 1
    
    filename = 'monster.txt'
    with open(filename) as f:
        i = 0
        for lines in f.readlines():
            if(i == 0):
                m_name = str(lines)
                index = m_name.rfind("\n")
                if index != -1:
                    m_name = m_name[:index]
            else:
                m_level = int(lines)

            i += 1

    total = m_level + char_level
    gate = int((m_level * 100) / total)
    result = random.randint(0, 100)
    if(result >= gate):
        char_level += m_level

        m_name = "0"
        m_level = -1
        result = 1
    else:
        char_name = 0
        char_pics = 0
        char_level = -1

        m_name = "0"
        m_level = -1
        result = 0

    filename = 'data.txt'
    with open(filename, 'w') as f:
        f.writelines(str(char_name) + "\n")
        f.writelines(str(char_pics) + "\n")
        f.writelines(str(char_level))

    filename = 'monster.txt'
    with open(filename, 'w') as f:
        f.writelines(str(m_name) + "\n")
        f.writelines(str(m_level))

    return result
    

