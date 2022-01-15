class Node : 
    def __init__(self, data, next) :
        self.data = data
        self.next = next
    
class LinkedList :
    def __init__(self) :
        self.no = 0
        self.head = None
        self.current = None
    
    def __len__(self) :
        return self.no
    
    def search(self, data) :
        count = 0
        ptr = self.head
        
        while ptr != None :
            if ptr.data == data :
                self.current = ptr
                return count
            count += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data) :
        return self.search(data) >= 0
    
    def add_first(self, data) :
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1
    
    def add_last(self, data) :
        if self.head is None :
            self.add_first(data)
        else :
            ptr = self.head
            while ptr.next != None :
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)    
            self.no += 1
    
    def remove_first(self) :
        if self.head != None :
            self.head = self.current = self.head.next
        self.no += 1
    
    def remove_last(self) :
        if self.head != None :
            if self.head.next != None :
                self.remove_first()
            else :
                ptr = self.head
                pre = self.head
                
                while ptr.next != None :
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1
    
    def remove(self, p) :
        if self.head != None :
            if p == self.head :
                self.remove_first
        
    
        