from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder

class QueueEmptyException(Exception):
    pass
class OrderQueue:
    def __init__(self):
        self.orderQueue = [0]
        self.currentSize = 0
    def percUp(self, i):
        while i // 2 > 0:
          if self.orderQueue[i].getTime() < self.orderQueue[i // 2].getTime():
             tmp = self.orderQueue[i // 2]
             self.orderQueue[i // 2] = self.orderQueue[i]
             self.orderQueue[i] = tmp
          i = i // 2

    def addOrder(self, order):
      self.orderQueue.append(order)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.orderQueue[i].getTime() > self.orderQueue[mc].getTime():
              tmp = self.orderQueue[i]
              self.orderQueue[i] = self.orderQueue[mc]
              self.orderQueue[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.orderQueue[i*2] < self.orderQueue[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def processNextOrder(self):
      if self.currentSize == 0:
          raise QueueEmptyException
      ready_order = self.orderQueue[1]
      self.orderQueue[1] = self.orderQueue[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.orderQueue.pop()
      self.percDown(1)
      return ready_order.getOrderDescription()

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.orderQueue = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

