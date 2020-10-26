def fullenergy(m = int(input("введите значение")),h = int(input("введите значение")),v = int(input("введите значение"))):
    value = ((m*v**2)/2) + (m*9.81*h)
    return value

print(fullenergy())