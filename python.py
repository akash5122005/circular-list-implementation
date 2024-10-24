class Queue:
    def __init__(self):
        self.size=1000
        self.queli=[None]*1000
        self.front=None
        self.rear=None

    def isfull(self):
        if self.rear!= None and(self.rear+1)%self.size == self.front:
            return True
        return False
    def isempty(self):
        if self.front is None:
            return True
        return False
    def enque(self,val):
        if self.isfull():
            return
        else:
            if self.front is None:
                self.front  = 0
                self.rear = 0
            elif(self.rear+1)%self.size !=self.front:
                self.rear = (self.rear + 1)%self.size
            self.queli[self.rear]= val
            print(val,"added to the queue")

    def Deque(self):
        if self.isempty()!=True:
            rem = self.queli[self.front]
            if self.front == self.rear:
                self.queli[self.front]=None
                self.front = None
                self.rear = None
            else:
                self.queli[self.front] = None
                self.front+=1
                if self.front == self.size:
                    self.front = self.front%self.size
            return f"{rem} is removed from the queue"
        else:
            print("Queue is Empty")
que = Queue()
for i in range(int(input())):
    li = list(map(str,input().split()))
    if "ENQUEUE" ==li[0]:
        que.enque(' '.join(li[1:]))
    elif "DEQUEUE" == li[0]:
        value = que.Deque()    
        print(value)                                                             
            


