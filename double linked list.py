class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.nexts = None

head = None        

choice = 1
while choice:
    x = int(input("Enter a number: "))
    newnode = Node(x)
    if head is None:
        head = temp = newnode
    else:
        temp.nexts = newnode
        newnode.prev = temp
        temp = newnode
    
    choice = int(input("Do you want to continue? (0/1): "))   
    
    
def insert_at_beginning():
    global head
    initial_value = int(input("Enter the value to insert at beginning: "))
    newnode = Node(initial_value)
    newnode.nexts = head
    if head is not None:
        head.prev = newnode
    head = newnode

def insert_at_end():
    global head
    end_value = int(input("Enter the value to insert at end: "))
    newnode = Node(end_value)
    
    if head is None:  
        head = newnode
        return
    
    temp = head
    while temp.nexts is not None:
        temp = temp.nexts
    temp.nexts = newnode
    newnode.prev = temp

def insert_at_position():
    global head
    pos_value = int(input("Enter a value that to be inserted: "))
    pos = int(input("Enter the position: "))
    newnode = Node(pos_value)

    if pos == 0:  
        insert_at_beginning()
        return

    temp = head
    i = 0
    while i < pos - 1 and temp is not None:
        temp = temp.nexts
        i += 1

    if temp is None:   
        print("Position out of bounds.")
        return

    newnode.nexts = temp.nexts
    newnode.prev = temp
    if temp.nexts is not None:
        temp.nexts.prev = newnode
    temp.nexts = newnode

def delete_at_beginning():
    global head
    if head is not None:  
        head = head.nexts
        if head is not None:
            head.prev = None

def delete_at_end():
    global head
    if head is None:  
        return
    
    if head.nexts is None:  
        head = None
        return

    temp = head
    while temp.nexts is not None:
        temp = temp.nexts
    temp.prev.nexts = None 

def delete_at_position():
    global head
    pos = int(input("Enter a position to be deleted: "))
    
    if pos == 0:
        delete_at_beginning()
        return

    temp = head
    i = 0
    while i < pos and temp is not None:
        temp = temp.nexts
        i += 1

    if temp is None: 
        print("Position out of bounds.")
        return

    if temp.prev is not None:
        temp.prev.nexts = temp.nexts
    if temp.nexts is not None:
        temp.nexts.prev = temp.prev

def display():
    global head
    temp = head
    while temp is not None:  
        print("Values:", temp.data)
        temp = temp.nexts

def reverse():
    global head
    temp = None
    current = head

    while current is not None:
        temp = current.prev
        current.prev = current.nexts
        current.nexts = temp
        current = current.prev  

    if temp is not None:  
        head = temp.prev  

def main():
    while True:
        print("1 for insert at beginning\n2 for insert at end\n3 for insert at particular position\n"
              "4 for delete at beginning\n5 for delete at end\n6 for delete at position\n"
              "7 for reverse a linked list\n8 for display\n0 for exit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            insert_at_beginning()
        elif choice == 2:
            insert_at_end()
        elif choice == 3:
            insert_at_position()
        elif choice == 4:
            delete_at_beginning()
        elif choice == 5:
            delete_at_end()
        elif choice == 6:
            delete_at_position()
        elif choice == 7:
            reverse()
        elif choice == 8:
            display()
        elif choice == 0:
            break
        else:
            print("Invalid option, please try again.")    

if __name__ == "__main__":
    main()
