# 23_ Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas; 
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón; 
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles. 

from BinaryTree import BinaryTree

criaturas_tree = BinaryTree()

lista_criaturas = [
    {'Criatura': 'Ceto', 'Derrotado': None},
    {'Criatura': 'Tifón', 'Derrotado': 'Zeus'},
    {'Criatura': 'Equidna', 'Derrotado': 'Argos Panoptes'},
    {'Criatura': 'Dino', 'Derrotado': None},
    {'Criatura': 'Pefredo', 'Derrotado': None},
    {'Criatura': 'Enio', 'Derrotado': None},
    {'Criatura': 'Escila', 'Derrotado': None},
    {'Criatura': 'Caribdis', 'Derrotado': None},
    {'Criatura': 'Euríale', 'Derrotado': None},
    {'Criatura': 'Esteno', 'Derrotado': None},
    {'Criatura': 'Medusa', 'Derrotado': 'Perseo'},
    {'Criatura': 'Ladón', 'Derrotado': 'Heracles'},
    {'Criatura': 'Águila del Cáucaso', 'Derrotado': None},
    {'Criatura': 'Quimera', 'Derrotado': 'Belerofonte'},
    {'Criatura': 'Hidra de Lerna', 'Derrotado': 'Heracles'},
    {'Criatura': 'León de Nemea', 'Derrotado': 'Heracles'},
    {'Criatura': 'Esfinge', 'Derrotado': 'Edipo'},
    {'Criatura': 'Dragón de la Cólquida', 'Derrotado': None},
    {'Criatura': 'Cerbero', 'Derrotado': None},
    {'Criatura': 'Cerda de Cromión', 'Derrotado': 'Teseo'},
    {'Criatura': 'Ortro', 'Derrotado': 'Heracles'},
    {'Criatura': 'Toro de Creta', 'Derrotado': 'Teseo'},
    {'Criatura': 'Jabalí de Calidón', 'Derrotado': 'Atalanta'},
    {'Criatura': 'Carcinos', 'Derrotado': None},
    {'Criatura': 'Gerión', 'Derrotado': 'Heracles'},
    {'Criatura': 'Láquesis', 'Derrotado': None},
    {'Criatura': 'Átropos', 'Derrotado': None},
    {'Criatura': 'Minotauro de Creta', 'Derrotado': 'Teseo'},
    {'Criatura': 'Harpías', 'Derrotado': None},
    {'Criatura': 'Argos Panoptes', 'Derrotado': 'Hermes'},
    {'Criatura': 'Aves del Estínfalo', 'Derrotado': None},
    {'Criatura': 'Talos', 'Derrotado': 'Medea'},
    {'Criatura': 'Sirenas', 'Derrotado': None},
    {'Criatura': 'Pitón', 'Derrotado': 'Apolo'},
    {'Criatura': 'Cierva de Cerinea', 'Derrotado': None},
    {'Criatura': 'Basilisco', 'Derrotado': None},
    {'Criatura': 'Jabali de Erimanto', 'Derrotado': None},
    {'Criatura': 'Cloto', 'Derrotado': None},
]

for criatura in lista_criaturas:
    criaturas_tree.insert_node(criatura['Criatura'], {'Derrotado': criatura['Derrotado']})

#A
print('A)')
criaturas_tree.inorden_criaturas()
print()

#B
print('B)')
criaturas_tree.inorden_add_field('Descripcion')
criaturas_tree.inorden()
print()

#C
print('C)')
pos=criaturas_tree.search('Talos')
if pos is not None:
    print(f"informacion de Talos:{pos.other_values}")
else:
    print("No se encontro a Talos")
print()

#D
print('D)')
dic_ranking = {}
criaturas_tree.inorden_ranking(dic_ranking)

def order_por(item):
    return item[1]

ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print(ordenados[:3])
print()

#E
print('E)')
print('Criaturas derrotadas por Heracles:')
criaturas_tree.inorden_derrotas('Heracles')
print()

#F
print('F)')
print('Criaturas que no fueron derrotadas:')
criaturas_tree.inorden_derrotas(None)
print()

#G
print('G)')
criaturas_tree.inorden_add_field('Capturada')
criaturas_tree.inorden()
print()

#H
print('H)')
buscados=['Cerbero','Toro de Creta','Cierva de Cerinea','Jabali de Erimanto']

criaturas_tree.inorden_modificar_capturada(buscados,'Capturada','Heracles')
criaturas_tree.inorden()
print()

#I
print('I)')
bus = input('Que desea buscar por coincidencia:')
print(f'Resultados con ({bus}):')
criaturas_tree.search_by_coincidence(bus)
print()

#J
print('J)')
if criaturas_tree.search('Basilisco') is not None:
    criaturas_tree.delete_node('Basilisco')
    print('Basilisco fue eliminado')

if criaturas_tree.search('Sirenas') is not None:
    criaturas_tree.delete_node('Sirenas')
    print('Sirenas fue eliminado')
print()
criaturas_tree.inorden()
print()

#K
print('K)')
criaturas_tree.inorden_modificar_capturada('Aves del Estínfalo','Derrotado','Heracles')
criaturas_tree.inorden()
print()

#L
print('L)')
ser = criaturas_tree.search('Ladón')
if ser is not None:
    otro = ser.other_values
    criaturas_tree.delete_node('Ladón')
    criaturas_tree.insert_node('Dragón Ladón',otro)
    print('Se modifico correctamente "Ladón" por "Dragón Ladón"')
print()

#M
print('M)')
criaturas_tree.by_level()
print()

#N
print('N)')
criaturas_tree.inorden_mostrar_capturados('Heracles')
print()