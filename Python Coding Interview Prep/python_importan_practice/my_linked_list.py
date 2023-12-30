# A simple Python program to introduce a linked list 

# Node class 
class Node: 

    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 


# Linked List class contains a Node object 
class LinkedList: 

    # Function to initialize head 
    def __init__(self): 
        self.head = None

    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        lst = []
        while (temp): 
            lst.append(temp.data) 
            temp = temp.next
        print([l for l in lst])

    # This function is in LinkedList class 
    # Function to insert a new node at the beginning 
    def push(self, new_data): 

        # 1 & 2: Allocate the Node & 
        #    Put in the data 
        new_node = Node(new_data) 
            
        # 3. Make next of new Node as head 
        new_node.next = self.head 
            
        # 4. Move the head to point to new Node 
        self.head = new_node 


    # This function is in LinkedList class. 
    # Inserts a new node after the given prev_node. This method is 
    # defined inside LinkedList class shown above */ 
    def insertAfter(self, prev_node, new_data): 

        # 1. check if the given prev_node exists 
        if prev_node is None: 
            print("The given previous node must inLinkedList.")
            return

        # 2. Create new node & 
        # 3. Put in the data 
        new_node = Node(new_data) 

        # 4. Make next of new Node as next of prev_node 
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node 
        prev_node.next = new_node


    # This function is defined in Linked List class 
    # Appends a new node at the end. This method is 
    # defined inside LinkedList class shown above */ 
    def append(self, new_data): 

        # 1. Create a new node 
        # 2. Put in the data 
        # 3. Set next as None 
        new_node = Node(new_data) 

        # 4. If the Linked List is empty, then make the 
        # new node as head 
        if self.head is None: 
            self.head = new_node 
            return

        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next

        # 6. Change the next of last node 
        last.next = new_node 


    def mth_to_start(self, key):
        # Store head node 
        temp = self.head 
        i = 0

        while(temp is not None): 
            if temp and i == key: 
                break
            temp = temp.next
            i += 1

        # if key was not present in linked list 
        if(temp == None): 
            return "NIL"
        
        return temp.data


    def mth_to_last(self, key):
        # initialize variables
        previous = None         # `previous` initially points to None
        current = self.head     # `current` points at the first element
        following = current.next    # `following` points at the second element
        count = 1

        # go till the last element of the list
        while current:
            current.next = previous # reverse the link
            previous = current      # move `previous` one step ahead
            current = following         # move `current` one step ahead
            if following:               # if this was not the last element
                following = following.next    # move `following` one step ahead
                count += 1

        self.head = previous
        return self.mth_to_start(key)



# Given a reference to the head of a list and a key, 
# delete the first occurence of key in linked list 
def deleteNode(self, key): 
     
    # Store head node 
    temp = self.head 

    # If head node itself holds the key to be deleted 
    if (temp is not None): 
        if (temp.data == key): 
            self.head = temp.next
            temp = None
            return

    # Search for the key to be deleted, keep track of the 
    # previous node as we need to change 'prev.next' 
    while(temp is not None): 
        if temp.data == key: 
            break
        prev = temp 
        temp = temp.next

    # if key was not present in linked list 
    if(temp == None): 
        return

    # Unlink the node from linked list 
    prev.next = temp.next

    temp = None


    def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def prettyPrintLinkedList(node):
    import sys
    while node and node.next:
        sys.stdout.write(str(node.val) + "->")
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")

def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            node = stringToListNode(line)
            prettyPrintLinkedList(node)
        except StopIteration:
            break


# Code execution starts here 
if __name__=='__main__': 

    # Start with the empty list 
    llist = LinkedList() 

    print("adding 1 -> 2 -> 3")
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 

    ''' 
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 

    llist.head   second          third 
        |            |               | 
        |            |               | 
    +----+------+    +----+------+   +----+------+ 
    | 1 | None |     | 2 | None |    | 3 | None | 
    +----+------+    +----+------+   +----+------+ 
    '''

    llist.head.next = second; # Link first node with second 

    ''' 
    Now next of first Node refers to second. So they 
    both are linked. 

    llist.head   second          third 
        |            |               | 
        |            |               | 
    +----+------+    +----+------+   +----+------+ 
    | 1 | o-------->| 2 | null |     | 3 | null | 
    +----+------+    +----+------+   +----+------+ 
    '''

    second.next = third; # Link second node with the third node 

    ''' 
    Now next of second Node refers to third. So all three 
    nodes are linked. 

    llist.head   second          third 
        |            |               | 
        |            |               | 
    +----+------+    +----+------+   +----+------+ 
    | 1 | o-------->| 2 | o-------->| 3 | null | 
    +----+------+    +----+------+   +----+------+ 
    '''

    # Insert 6.  So linked list becomes 6->None 
    llist.append(6) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    llist.push(7); 
  
    # Insert 9 at the beginning. So linked list becomes 9->7->6->None 
    llist.push(9); 
  
    # Insert 4 at the end. So linked list becomes 9->7->6->4->None 
    llist.append(4) 
  
    # Insert 8, after 7. So linked list becomes 9 -> 7-> 8-> 6-> 4-> None 
    llist.insertAfter(llist.head.next, 8) 
  
    print ('Created linked list is:'), 
    llist.printList() 

    key = 2
    result = llist.mth_to_start(key)
    print(f"From first data of the index {key} is {result}")
    result = llist.mth_to_last(key)
    print(f"from last data of the index {key} is {result}")

    main()

