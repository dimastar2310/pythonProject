

class MinHeap(object):
     def __init__(self):
      self.list = []

      def add(self, num):
       self.list.append(num)
       self.sort()