class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqsum(self):
        self.sum= self.x**2+self.y**2+self.z**2
        return self.sum
sqsum_obj=point(1,3,5)
print(sqsum_obj.sqsum())
