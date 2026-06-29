class parrot:
    species="Budgie"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        print("{} sings {}".format(self.name,song))
    def dance(self):
        print("{} dances".format(self.name))
blu=parrot("duson",6)
print(blu.sing("happy"))
print(blu.dance())
