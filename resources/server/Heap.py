class MinHeap:
    def __init__(self):
        self.prices = []
        self.actualSize = 0 #Necessary due to lazy deletion process fcr sliding window

    def heapifyUp(self, index):
        while index > 0:
            #heapifies up until either the price is in a valid position, or the price is the root of the heap
            if self.prices[index] >= self.prices[(index-1)//2]:
                break
            self.prices[index], self.prices[(index-1)//2] = self.prices[(index-1)//2], self.prices[index]
            index = (index-1)//2

    def heapPush(self, price):
        self.prices.append(price)
        self.heapifyUp(len(self.prices) - 1)
        self.actualSize += 1

    def heapifyDown(self, index):
        while index < len(self.prices)//2:
            if self.prices[index] > self.prices[(index+1)*2 - 1]:
                if len(self.prices) > (index+1)*2 and self.prices[(index+1)*2] < self.prices[(index+1)*2 - 1]:
                    self.prices[index], self.prices[(index+1)*2] = self.prices[(index+1)*2], self.prices[index]
                    index = (index+1)*2
                else:
                    self.prices[index], self.prices[(index+1)*2-1] = self.prices[(index+1)*2 - 1], self.prices[index]
                    index = (index+1)*2 - 1
            elif len(self.prices) > (index+1)*2 and self.prices[index] > self.prices[(index+1)*2]:
                self.prices[index], self.prices[(index+1)*2] = self.prices[(index+1)*2], self.prices[index]
                index = (index+1)*2
            else:
                break

    def heapTop(self):
         return self.prices[0]

    def popHelper(self):
        #This method just pops without reducing the size, mainly used for when I need to lazy delete elements in SlidingMedian.py
        top = self.heapTop()
        self.prices[0], self.prices[-1] = self.prices[-1], self.prices[0]
        self.prices.pop()
        self.heapifyDown(0)
        return top

    def heapPop(self):
        if not self.prices:
            return None
        top = self.popHelper()
        self.actualSize -= 1
        return top

    def __len__(self):
        # overloading length operator to return the effective length of the heap (not including elements pending deletion
        return self.actualSize

    def totalSize(self):
        return len(self.prices)

class MaxHeap(MinHeap):
    def __init__(self):
        super().__init__()

    def heapPush(self, price):
        super().heapPush(-price)

    def heapTop(self):
        return -super().heapTop()

    def heapPop(self):
        return -super().heapPop()