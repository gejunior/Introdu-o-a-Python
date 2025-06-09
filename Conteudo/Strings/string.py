curso = "pYtHon"
print(curso.upper())
# >>> PYTHON
print(curso.lower())
# >>> python
print(curso.title())
# >>> Python

#Eliminando espaços
curso = "           Python  "
print(curso.strip())
# >>> "Python"

print(curso.lstrip())#elimina da esquerda
# >>> "Python  "
print(curso.rstrip())#elimina da direita
# >>> "         Python"

#junção e centralização
curso = "Python"

print(curso.center(10, "#"))
# >>> ##Python##
print(".".join(curso))
# >>> "P.y.t.h.o.n"

menu = "Python"
print("####" + menu + "####")
print(menu.center(14, "#"))
print("-".join(menu))

for letra in menu:
    print(letra, end = " - ")
print()