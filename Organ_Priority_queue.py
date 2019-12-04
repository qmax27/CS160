class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        if not self.isEmpty() or current != None:  # in order to make this a stack we would have to make it so the item is only removed if it equals the head so we would have the boolean statement check if the head equals the item removed
            while not found:
                if current.getData() == item:  # to make unordered list queue
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            if previous == None:  # What happens when the list is empty in this function?
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            return "List is empty"  #


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


    def fuldel(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval


    def delMin(self, i):
        retval = self.heapList[1]
        i.add(retval)
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def binarySearchHelper(self, item, start, end):
        if abs(end - start) <= 1:
            return False
        midpoint = (start + end) // 2
        if self.heapList[midpoint] == item:
            return True, midpoint
        if item < self.heapList[midpoint]:
            return self.binarySearchHelper(item, start, midpoint)
        return self.binarySearchHelper(item, midpoint, end)

    def transfer(self, i, l):
        d_p = self.binarySearchHelper(i, 0, self.currentSize)
        if d_p[0] == True:
            l.add(i)
            self.heapList[d_p[1]] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop(d_p[1])
            self.percDown(d_p[1])
        else:
            print('Patient not currently awaiting organ')





organslist = BinHeap()
organslist.insert(3)
organslist.insert(2)
organslist.insert(7)
organslist.insert(8)
organslist.insert(9)
organslist.transfer(7)




