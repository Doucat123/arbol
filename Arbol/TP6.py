# 6. Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de nacimiento, color de sable de luz, 
# ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos tres campos pueden tener más de un valor. 
# Escribir las funciones necesarias para resolver las siguientes consignas:

# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
# b. realizar un barrido inorden del árbol por nombre y ranking;
# c. realizar un barrido por nivel de los árboles por ranking y especie;
# d. mostrar toda la información de Yoda y Luke Skywalker;
# e. mostrar todos los Jedi con ranking “Jedi Master”;
# f. listar todos los Jedi que utilizaron sabe de luz color verde;
# g. listar todos los Jedi cuyos maestros están en el archivo;
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.

from BinaryTree import BinaryTree, get_value_from_file

file_jedi = open('C:\\Users\\axels\\OneDrive\\Documentos\\aprogramas\\python\\Facultad\\Arbol\\jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

#a
nombre_tree = BinaryTree()
especie_tree = BinaryTree()
ranking_tree = BinaryTree()

read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    nombre_tree.insert_node(jedi[0], index+2)
    especie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)

#b
print('B)')
print('Barrido inorden del arbol de nombres')
nombre_tree.inorden()
print()

print('Barrido inorden del arbol de ranking')
ranking_tree.inorden()
print()

#c
print('C)')
print('Barrido por nivel del arbol de ranking')
ranking_tree.by_level()
print()

print('Barrido por nivel del arbol de especie')
especie_tree.by_level()

#d
print('D)')
pos = nombre_tree.search('yoda')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')

pos = nombre_tree.search('luke skywalker')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')
print()

#e
print('E)')
print('Jedis con rango Jedi Master: ')
ranking_tree.inorden_rank('jedis.txt', 'jedi master')
print()

#f
print('F)')
print('Jedis con sable de luz verde:')
nombre_tree.inorden_file_lightsaber('jedis.txt', 'green')
print()

#g
print('G)')
print('Jedis con maestro:')
nombre_tree.inorden_master('jedis.txt')
print()

#h
print('H)')
print('Jedis de la especie Togruta')
especie_tree.inorden_especie('jedis.txt','togruta')
print()

print('Jedis de la especie Cerean')
especie_tree.inorden_especie('jedis.txt','cerean')
print()

#i
print('I)')
print('Jedis donde su nombre empeiza con A:')
nombre_tree.inorden_start_with_jedi('A')
print()

print('Jedis que tienen ( - ) en su nombre')
nombre_tree.inorden_carcter('jedis.txt','-')
print()
