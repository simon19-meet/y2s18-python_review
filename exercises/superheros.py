# Write your solutions for 1.5 here!
class Superheroes:
    def __init__(self,name,superpower,strength):
        self.name=name
        self.superpower=superpower
        self.strength=strength

    def PrintDetails(self):
        st="Name: "+self.name+"Superpower: "+self.superpower+"Strength: "+ str(self.strength)
        print(st)
    
    def save_civilian(self,work):
        if self.strength<work:
            print("Super hero is not strong enough :(")
        return self.strength-work

sp=Superheroes("Simon","speed",15)
sp.PrintDetails()
sp.save_civilian(20)

    