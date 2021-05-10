class MyDict(dict):

    def my_get(self,key,dct):
        self.get(key)
        if not key in dct:
            return 0
        else:
            return dct[key]


dct = {1:'q',2:'e', 3:'t'}
mydict = MyDict()
print(mydict.my_get(5,dct))


