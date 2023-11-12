#Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que 
# contemple lo siguiente:

#a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, 
# True y False respectivamente;
#b. listar los villanos ordenados alfabéticamente;
#c. mostrar todos los superhéroes que empiezan con C;
#d. determinar cuántos superhéroes hay en el árbol;
#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
#f. listar los superhéroes ordenados de manera descendente;
#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a 
# los villanos, luego resolver las siguiente tareas:
#I. determinar cuántos nodos tiene cada árbol;
#II. realizar un barrido ordenado alfabéticamente de cada árbol.

from BinaryTree import BinaryTree

arbol=BinaryTree()
arbolHeroe=BinaryTree()
arbolVillano=BinaryTree()

#a
lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': False},
    {'name': 'deadpool', 'heroe': True},
]

for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])

#b
print ('B)')
arbol.inorden_super_or_villano(False)
print()

#c
print ('C)')
arbol.inorden_start_with('C')
print()

#d
print ('D)')
print (f'La cantidad de super heroes es de {arbol.contar_heroes()}')
print()

#e
print ('E)')
modificar=input("Ingrese el heroe que desea modificar:")
pos=arbol.search(modificar)
if pos:
    heroe1=pos.other_values
    arbol.delete_node(modificar)
    nombre=input("Ingrese nuevo nombre:")
    arbol.insert_node(nombre,heroe1)
else:
    print("No se encontro")
    print()
arbol.inorden()
print()

#f
print ('F)')
arbol.postorden()
print()

#g
print ('G)')
arbol.dividir_heroes(arbolHeroe,arbolVillano)


#I
print ('I)')
print (f'La cantidad de heroes es de: {arbolHeroe.contar_nodos()}')
print (f'La cantidad de villanos es de: {arbolVillano.contar_nodos()}')
print()

#II
print ('II)')
print ('Super Heroes:')
arbolHeroe.inorden()
print()
print ('Villanos:')
arbolVillano.inorden()
