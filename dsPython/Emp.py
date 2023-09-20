class Person:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display(self):
        print("{} {} {}".format(self.id, self.name,self.sal))
