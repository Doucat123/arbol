from cola import Cola
import linecache


def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split

class NodeTree():

    def __init__(self, value, other_values=None):
        self.value = value
        self.other_values = other_values
        self.left = None
        self.right = None
        self.height = 0

class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_values=None):

        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)
        __inorden(self.root)

    def inorden_derrotas(self,key):
        def __inorden_derrotas(root,key):
            if root is not None:
                __inorden_derrotas(root.left,key)
                if root.other_values['Derrotado'] == key:
                    print (root.value)
                __inorden_derrotas(root.right,key)
        __inorden_derrotas(self.root,key)

    def inorden_criaturas(self):
        def __inorden_criaturas(root):
            if root is not None:
                __inorden_criaturas(root.left)
                if root.other_values['Derrotado'] is not None:
                    print(root.value,' fue derrotado por ',root.other_values['Derrotado'])
                else:
                    print(root.value)
                __inorden_criaturas(root.right)
        __inorden_criaturas(self.root)

    def inorden_mostrar_capturados(self,key):
        def __inorden_mostrar_capturados(root,key):
            if root is not None:
                __inorden_mostrar_capturados(root.left,key)
                if root.other_values['Capturada'] == key:
                    print(root.value)
                __inorden_mostrar_capturados(root.right,key)
        __inorden_mostrar_capturados(self.root,key)

    def inorden_ranking(self, ranking):
        def __inorden_ranking(root, ranking):
            if root is not None:
                __inorden_ranking(root.left, ranking)
                if root.other_values['Derrotado'] is not None:
                    if root.other_values['Derrotado'] not in ranking:
                        ranking[root.other_values['Derrotado']] = 1
                    else:
                        ranking[root.other_values['Derrotado']] += 1
                __inorden_ranking(root.right, ranking)
        __inorden_ranking(self.root, ranking)

    def inorden_rank(self, file_name,rank):
        def __inorden_rank(root, file_name,rank):
            if root is not None:
                __inorden_rank(root.left, file_name,rank)
                value = get_value_from_file(file_name, root.other_values)
                if rank in value[1].split('/'):
                    print(root.value, value[0].split('/'))
                __inorden_rank(root.right, file_name,rank)

    def inorden_especie(self, file_name,species):
        def __inorden_especie(root, file_name,species):
            if root is not None:
                __inorden_especie(root.left, file_name,species)
                value = get_value_from_file(file_name, root.other_values)
                if species in value[2].split('/'):
                    print(root.value, value[0].split('/'))
                __inorden_especie(root.right, file_name,species)
        __inorden_especie(self.root, file_name,species)

    def inorden_master(self, file_name):
        def __inorden_master(root, file_name):
            if root is not None:
                __inorden_master(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                if not '-' in value[3].split('/'):
                    print(root.value, value[0].split('/'))
                __inorden_master(root.right, file_name)
        __inorden_master(self.root, file_name)

    def inorden_carcter(self, file_name,caracter):
        def __inorden_carcter(root, file_name,caracter):
            if root is not None:
                __inorden_carcter(root.left, file_name,caracter)
                value = get_value_from_file(file_name, root.other_values)
                if caracter in value[0]:
                    print(root.value, value[0])
                __inorden_carcter(root.right, file_name,caracter)
        __inorden_carcter(self.root, file_name,caracter)

    def inorden_add_field(self, key, value=None):
        def __inorden_add_field(root, key, value):
            if root is not None:
                __inorden_add_field(root.left, key, value)
                root.other_values[key] = value
                __inorden_add_field(root.right, key, value)
        __inorden_add_field(self.root,key,value)

    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)

        __inorden_file(self.root, file_name)

    def inorden_file_lightsaber(self, file_name, lightsaber_color):
        def __inorden_file_lightsaber(root, file_name, lightsaber_color):
            if root is not None:
                __inorden_file_lightsaber(root.left, file_name, lightsaber_color)
                value = get_value_from_file(file_name, root.other_values)
                if lightsaber_color in value[4].split('/'):
                    print(root.value, value[4].split('/'))
                __inorden_file_lightsaber(root.right, file_name, lightsaber_color)

        __inorden_file_lightsaber(self.root, file_name, lightsaber_color)

    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)

        __inorden_s_v(self.root, is_hero)

    def inorden_start_with(self, cadena):
        def __inorden_start_with(root, cadena):
            if root is not None:
                __inorden_start_with(root.left, cadena)
                if root.other_values is True and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena)
        __inorden_start_with(self.root,cadena)

    def inorden_start_with_jedi(self, cadena):
        def __inorden_start_with_jedi(root, cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with_jedi(root.right, cadena)
        __inorden_start_with_jedi(self.root, cadena)

    def inorden_modificar_capturada(self, list, key, value):
        def __inorden_add_field(root, list, key, value):
            if root is not None:
                __inorden_add_field(root.left, list, key, value)
                if root.value in list:
                    root.other_values[key] = value
                __inorden_add_field(root.right, list, key, value)
        __inorden_add_field(self.root, list, key, value)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)
        __postorden(self.root)

    def postorden_hero(self):
        def __postorden_hero(root):
            if root is not None:
                __postorden_hero(root.right)
                if root.other_values is True:
                    print(root.value)
                __postorden_hero(root.left)

        __postorden_hero(self.root)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value, root.height)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)

    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
        return __search(self.root, key)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count
        return __contar(self.root, value)
    
    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count
        return __contar_heroes(self.root)

    def contar_nodos(self):
        def __contar_nodos(root):
            count = 0
            if root is not None:
                count = 1
                count += __contar_nodos(root.left)
                count += __contar_nodos(root.right)
            return count
        return __contar_nodos(self.root)

    def dividir_heroes(self,arbol1,arbol2):
        def __dividir_heroes(root,arbol1,arbol2):
            if root is not None:
                __dividir_heroes(root.right,arbol1,arbol2)
                if root.other_values==True:
                    arbol1.insert_node(root.value)
                elif root.other_values==False:
                    arbol2.insert_node(root.value)
                __dividir_heroes(root.left,arbol1,arbol2)
        __dividir_heroes(self.root,arbol1,arbol2)
