class   C:
    def __init__(self,size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize,setSize,delSize)

c = C()
print(c.size)
print(c.x)
c.x=18
print(c.x)
del c.x
print(c.x)
