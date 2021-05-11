class MyDict(dict):

    def my_get(self,key):
        if self.get(key) == None:
            return 0
        else:
            return self.get(key)


dct = {1: 'q', 2: 'e', 3: 't'}
mydict = MyDict(dct)
print(mydict.my_get(6))
