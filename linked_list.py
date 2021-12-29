class node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None 


class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        new_node = node(data)
        cur = self.head 
        while cur.next != None:
            cur = cur.next 
        cur.next = new_node

    def length(self):
        cur = self.head 
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next 

        return total 

    def display(self):
        elems = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elems.append(curr_node.data)

        print(elems)

    def get(self, index):
        if index >= self.length():
            return -1
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1

    def delete(self, index):
        if index >= self.length():
            return -1
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx ==  index:
                last_node.next = cur_node.next
                return 
            cur_idx +=1


my_linkedlist = linked_list()
my_linkedlist.display()
my_linkedlist.append(3)
my_linkedlist.append(4)
my_linkedlist.display()
print(my_linkedlist.get(1))
my_linkedlist.append(5)
my_linkedlist.append(7)
my_linkedlist.display()
my_linkedlist.delete(0)
my_linkedlist.display()