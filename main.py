class Queue:
    def __init__(self,l):
        self.queue=[]
        self.limit=l
        self.front=None
        self.rear=None
    def isFull(self):
        if self.rear==self.limit-1:
            return True
        else:
            return False
    def isEmpty(self):
        if self.front==None:
            return True
        else:
            return False
    def enqueue(self,ele):
        if self.isFull():
            print("Maximum limit reached")
        else:
            if self.front==None and self.rear==None:
                self.front=self.rear=0
            else:
                self.rear=self.rear+1
        self.queue.append(ele)
    def dequeue(self):
        if self.isEmpty():
            print("No more elements")
        else:
            return(self.queue.pop(0))
