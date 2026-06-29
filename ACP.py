class intro_robot:
    def __init__(self,name,model,colour,material):
        self.name=name
        self.model=model
        self.colour=colour
        self.material=material
        print("Hi,I am a robot, my name is", self.name ," and my model is ",self.model,",I am",self.colour ,
      "colour and the material I am made out of is ",self.material)
obj=intro_robot("Agni","fire 18","Green","Alumunium")
