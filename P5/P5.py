import random

class Node(object):
    def __init__(self, key, level):
        self.key = key
        self.forward = [None]*(level+1)

class SkipList(object):
    def __init__(self, max_lvl, P):
        self.MAXLVL = max_lvl
        self.P = P
        self.header = self.createNode(self.MAXLVL, -1)
        self.level = 0

    def createNode(self, lvl, key):
        n = Node(key, lvl)
        return n

    def randomLevel(self):
        lvl = 0
        while random.random()<self.P and lvl<self.MAXLVL:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None]*(self.MAXLVL+1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
            
        current = current.forward[0]
        
        if current == None or current.key != key:
            rlevel = self.randomLevel()
            if rlevel > self.level:
                for i in range(self.level+1, rlevel+1):
                    update[i] = self.header
                self.level = rlevel

            n = self.createNode(rlevel, key)

            for i in range(rlevel+1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n
    
    def search(self, key): 
        current = self.header
        counter = 0
        flag = False
        for i in range(self.level, -1, -1):
            while(current.forward[i] and current.forward[i].key < key):
                current = current.forward[i]
                counter += 1
            if (current.forward[i] and current.forward[i].key == key):
                counter += 1
                flag = True
                print(counter)
                break

        if not flag:
            print(-1)
    
    def delete(self, key):

        update = [None]*(self.MAXLVL+1)
        current = self.header
        for i in range(self.level, -1, -1):
            while(current.forward[i] and current.forward[i].key < key):
                current = current.forward[i]
            update[i] = current
            
        current = current.forward[0]
        
        if current != None and current.key == key:
            for i in range(self.level+1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while(self.level>0 and self.header.forward[self.level] == None):
                self.level -= 1

    def getlayers(self):
        print(self.MAXLVL)
    
    def printLayer(self,object):
        lvl = object
        head = self.header
        node = head.forward[lvl]
        while(node != None):
            print(node.key, end=" ")
            node = node.forward[lvl]
        print("")
        

#main
lst = SkipList(3, 0.6)
lst.insert(4)
lst.insert(99)
lst.insert(177)
lst.insert(0)
lst.insert(75)
lst.insert(369)
lst.insert(7)
lst.insert(1005)
lst.insert(750)
lst.insert(19)
lst.printLayer(3)
lst.printLayer(2)
lst.printLayer(1)
lst.printLayer(0)
lst.getlayers()
lst.search(1005)
lst.search(55)
lst.delete(99)
lst.printLayer(0)
