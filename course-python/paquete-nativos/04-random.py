import random
import string


lista_1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista_2 = [1, 2, 3, 4, 5, 6, 7, 8]

random.shuffle(lista_1)

print(
    random.random(),
    random.randint(1, 10),
    print(lista_1),
    random.choice(lista_2),
    random.choices(lista_2, k=3)
)

# string aleatorios
char = string.ascii_letters

digitos = string.digits


select = "".join(random.choices(char + digitos, k=10))
print(select)
