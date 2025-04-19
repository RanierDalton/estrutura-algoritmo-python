class Node:
    def __init__(self, data):
        self.data = data
        # referencia para próximo nós
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        # passando as referencias dos nós até o último nó
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return
    
    def length(self):
        
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def to_list(self):
        result = []
        current_node = self.head
        # pra cada nó, adiciona o valor na ista
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def get(self, index):
        if index < 0 or index >= self.length():
            return None
        # percorre a lista até o nó desejado
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data if current_node else None
    
    # exercícios desafios:
    def search(self, value):
        current_node = self.head
        
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False
    
    def remove_at_start(self):
        self.head = self.head.next

    def remove_at_end(self):
        current_node = self.head
        prev_node = None
        while current_node:
            prev_node = current_node
            current_node = current_node.next

            if current_node.next is None:
                prev_node.next = None

    def insert_at_start(self, value):
        current_node = Node(value)
        next_node = self.head
        current_node.next = next_node
        self.head = current_node

    def insert_at_end(self, value):
        last_node = Node(value)
        prev_node = self.head
        while prev_node:       
            prev_node = prev_node.next
            if prev_node.next == None:
                prev_node.next = last_node
                return 
            
    def remove_element_by_value(self, value):
        prev_node = None
        later_node = self.head.next
        current_node = self.head

        if current_node.data == value:
            self.head = later_node
            return 
        
        while current_node:
            prev_node = current_node
            current_node = later_node
            later_node = later_node.next

            if current_node.data == value:
                prev_node.next = later_node
                return

    def insert_at_index(self,value,index):
        if index < 0 or index >= self.length():
            return False
        
        new_node = Node(value)
        prev_node = None
        current_node = self.head

        for _ in range(index):
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = new_node
        new_node.next = current_node


# Testes
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    print("Lista original:")
    ll.display()
    
    print("Comprimento da lista:", ll.length())
    
    print("Lista como array:", ll.to_list())
    
    ll.reverse()
    
    print("Lista invertida:")
    ll.display()