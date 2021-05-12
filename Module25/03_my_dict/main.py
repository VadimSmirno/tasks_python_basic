class MyDict(dict):

    def get(self,key,default=0):
        return super().get(key,default)



dct = {1: 'q', 2: 'e', 3: 't'}
mydict = MyDict(dct)
print(mydict.get(5))
print(mydict.get(1))

