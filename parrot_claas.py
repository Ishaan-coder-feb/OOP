class parrot:
    species="budgie"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("The species of the parrot is ",self.species,"it's name is ",self.name,"and it is",self.age,"years old.")
obj=parrot("mohit",7)
