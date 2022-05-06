from random import choice, randint

class Bunny():
    value = "bunny rabbit"
    sexes = ["male", "female"]
    colours = ["white", "brown", "black", "spotted"]
    names = ["billy","mandy","tom","matt","bill","bob","steven"]

    def __init__(self, sex, colour, age, name, vampire):
        self.sex = choice(Bunny.sexes)
        self.colour = choice(Bunny.colours)
        self.age = 0
        self.name = choice(Bunny.names)

        chance = randint(0,100)
        if chance < 2:
            self.vampire = True
        else:
            self.vampire = False

    def kill_bunny(self):
        if self.age > 10 and self.vampire==False:
            print("I died")
        elif self.age > 50 and self.vampire==True:
            print("A vampire bunny has died!")

bunny1 = Bunny("sex","colour","age","name","vampire")
bunny2 = Bunny("sex","colour","age","name","vampire")
bunny3 = Bunny("sex","colour","age","name","vampire")
bunny4 = Bunny("sex","colour","age","name","vampire")
bunny5 = Bunny("sex","colour","age","name","vampire")

initial_bunnies = [bunny1,bunny2,bunny3,bunny4,bunny5]
initial_bunnies.sort(key=lambda x: x.age, reverse=True)

for bunny in initial_bunnies:
    print(vars(bunny))
#If male aged 2+ exists, for each female aged 2+, create new bunny
#filter male bunnies via list comprehension
#new bunny should have same color as mother

print("")
mature_males = [bunny for bunny in initial_bunnies if bunny.sex == "male" and bunny.age >=2 and bunny.vampire==False]
mature_females = [bunny for bunny in initial_bunnies if bunny.sex == "females" and bunny.age >=2 and bunny.vampire==False]
for male in mature_males:
    for female in mature_females:
        new_bunny = Bunny("sex",female.colour,"age","name","vampire")
        print(f"{new_bunny.name} was born!")

#if bunny older than 10, they die (via class method)

#If a radioactive mutant vampire bunny is born, 
#each turn it will change one normal bunny into a radioactive vampire bunny.
#Check for existence of vampire bunnies

vampires = [bunny for bunny in initial_bunnies if bunny.vampire==True]
normals = [bunny for bunny in initial_bunnies if bunny.vampire==False]

if vampires:
    for vampire in vampires:
        victim = choice(normals)
        victim.vampire = True

if len(initial_bunnies)==0:
    print("Program has finished")

if len(initial_bunnies)>1000:
    sacrifices = choice(initial_bunnies, k=500)
    initial_bunnies.remove(sacrifices)


#End Turn
#Age += 1