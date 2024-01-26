"""DRM Encryption."""

input = "UEQBJPJCBUDGBNKCAHXCVERXUCVK"

def split(x: str) -> list[str]:
    new_list = []
    first = ""
    second = ""
    number = len(x) // 2
    for i in range(0, number):
       first += x[i]
    for i in range(number, len(x)):
        second += x[i]
    new_list.append(first)
    new_list.append(second)
    return new_list


def num_value(x: list[str]) -> list[int]:
    new_list = []
    first_value = 0
    second_value = 0
    for i in x:
        if i == x[0]:
            for y in range(0, len(i)):
                first_value += ord(i[y]) - 65
        else:
            for y in range(0, len(i)):
                second_value += ord(i[y]) - 65
    new_list.append(first_value)
    new_list.append(second_value)
    return new_list
             

def wrap_around(x: list[str], y: list[int]) -> list[str]:
    new_list = []
    integer = 0
    for a in x:
        place = ""
        i = y[integer]
        for b in range(0, len(a)):
            z = ord(a[b]) - 65 + i
            while z > 25:
                z -= 26
            z = chr(z + 65)
            place += z
        new_list.append(place)
        integer += 1

    return new_list


def combine(x: list[str]) -> str:
    str_stor = ""
    first_list = x[0]
    second_list = x[1]
    for i in range(0, len(x[0])):
        y = (ord(first_list[i]) - 65) + (ord(second_list[i]) - 65)
        while y > 25:
            y -= 26
        y = chr(y + 65)
        str_stor += y
    return str_stor



encryption = split(input)
encryption_num = num_value(encryption)
encrypted = (wrap_around(encryption, encryption_num))
final = (combine(encrypted))
print(final)

