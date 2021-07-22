"""IMPLEMENTACIÓN DE LISTAS ENLAZADAS"""

# 1. Crear la clase NODO

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# 2. Crear una clase de lista enlazada
class linked_list:
    def __init__(self):
        self.head = None
        
    # 3. Método para agregar un elemento al final de la lista
    def add_at_end(self,data):
        if self.head == None: #Si esta vacia la lista, agregar un nodo
            self.head = Node(data = data)
            return 
        curr = self.head #Si en la lista hay por lo menos un Nodo, se para en el primer elemento
        while curr.next: #Pregunta si existe un elemento siguiente
            curr = curr.next #Se asigna a current ese elemento siguiente (next)
        curr.next = Node(data=data)

    # 4. Método para agregar un elemento al inicio de la lista
    def add_at_front(self,data):
        self.head = Node(data=data, next=self.head)

    #5. Método para agregar elementos en una posición específica
    def add_at_position(self,data,position):
        curr = self.head
        curr_pos = 0
        if self.head != None:
            while curr.next  and curr_pos != position:
                node_replace = curr
                curr = curr.next
                curr_pos = curr_pos + 1
            node_replace.next = Node (data = data, next = curr)
        else:
            print ("ERROR: La lista no contiene esa cantidad de elementos")

    #6. Método para eliminar nodos cuando encuentre por primera vez ese valor
    def delete_node(self, value):
        curr = self.head
        prev = None
        while curr.next and curr.data != value:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None


    #7. Metodo para imprimir una lista de nodos
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end=" -> ")
            node = node.next
        print("\n")


            

s=linked_list()
s.add_at_end(8)
s.add_at_end(5)
s.add_at_end(3)
s.add_at_end(9)
s.add_at_front(10)
s.add_at_front(1)
s.print_list()
s.add_at_position(20,4)
s.print_list()




