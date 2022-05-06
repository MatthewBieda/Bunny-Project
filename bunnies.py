from random import choice, randint, sample

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

    def increment_age(self):
        self.age += 1

bunny1 = Bunny("sex","colour","age","name","vampire")
bunny2 = Bunny("sex","colour","age","name","vampire")
bunny3 = Bunny("sex","colour","age","name","vampire")
bunny4 = Bunny("sex","colour","age","name","vampire")
bunny5 = Bunny("sex","colour","age","name","vampire")

initial_bunnies = [bunny1,bunny2,bunny3,bunny4,bunny5]
initial_bunnies.sort(key=lambda x: x.age, reverse=True)

Bunnies_exist = True

while Bunnies_exist:

    for bunny in initial_bunnies:
        print(vars(bunny))
    #If male aged 2+ exists, for each female aged 2+, create new bunny
    #filter male bunnies via list comprehension
    #new bunny should have same color as mother

    print("")

    mature_males = [bunny for bunny in initial_bunnies if bunny.sex == "male" and bunny.age >=2 and bunny.vampire==False]
    mature_females = [bunny for bunny in initial_bunnies if bunny.sex == "female" and bunny.age >=2 and bunny.vampire==False]

    for male in mature_males:
        for female in mature_females:
            new_bunny = Bunny("sex",female.colour,"age","name","vampire")
            print(f"{new_bunny.name} was born!")
            initial_bunnies.append(new_bunny)

    #if bunny older than 10, they die (via class method)
    old_bunnies = [bunny for bunny in initial_bunnies if bunny.age > 10 and bunny.vampire==False]
    old_vampire_bunnies = [bunny for bunny in initial_bunnies if bunny.age > 50 and bunny.vampire==True]

    for bunny in old_bunnies:
        print(f"{bunny.name} has died")
        initial_bunnies.remove(bunny)
        
    for vamp_bunny in old_vampire_bunnies:
        print(f"Vampire {vamp_bunny.name} has died")
        initial_bunnies.remove(vamp_bunny)
        

    #If a radioactive mutant vampire bunny is born, 
    #each turn it will change one normal bunny into a radioactive vampire bunny.
    #Check for existence of vampire bunnies

    vampires = [bunny for bunny in initial_bunnies if bunny.vampire==True]
    normals = [bunny for bunny in initial_bunnies if bunny.vampire==False]

    if vampires and len(normals):
        for vampire in vampires:
            victim = choice(normals)
            victim.vampire = True

    if len(initial_bunnies)==0:
        print("Extinction")
        Bunnies_exist=False

    if len(initial_bunnies)>1000:
        sacrifices = sample(initial_bunnies, 500)
        for sacrificial_bunny in sacrifices:
            initial_bunnies.remove(sacrificial_bunny)

    #END OF TURN
    #INCREMENT AGE

    for bunny in initial_bunnies:
        bunny.increment_age()

