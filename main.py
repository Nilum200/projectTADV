# Establish a Player Class here. It should take: HP, Inventory, Gender, Name.
class PC:
    def __init__(self, name='StandardMcDefault', gender='neutral', hit_points=3, inventory=[]):
        self.name = name
        self.gender = gender
        self.hit_points = hit_points
        self.inventory = inventory

    # The system that currently controls how gender is stored in the gender table.
    # If no valid option is presented: It will loop until a valid option is presented.
    def gender_picker(self):
        valid = False
        while not valid:
            sex = input('Enter your gender: Male, Female, or Neutral: ')
            if sex.lower() == 'male':
                self.gender = ['he', 'himself', 'him', 'his']
                valid = True
            elif sex.lower() == 'female':
                self.gender = ['she', 'herself', 'her', 'hers']
                valid = True
            elif sex.lower() == 'neutral':
                self.gender = ['they', 'themself', 'them', 'theirs']
                valid = True
            else:
                print("Hmm... Let's try that again, shall we?")

    # This may belong better in another class, but for now, it stays in here.
    def inventory_checker(self, item):
        for i in self.inventory:
            if item.lower() == i:
                return True
        return False

    # Triggering this causes the PC to name their character and give them pronouns.
    def pc_intro(self):
        print("Hello and welcome to TADV! To play, type in a corresponding option when they appear.")
        self.name = input("Enter your name: ")
        self.gender_picker()
        # I may remove this line later--for now it's useful for bug testing, in case something explodes name/gender.
        print("Your name is {name} and your gender pronouns are {gender}.".format(name=self.name, gender=self.gender))


# Where things go until they're better organized. A test space, for testing... IN SPACE!

# Establish an intro here. Eg: "{Name} finds {himself/herself} in danger..."
player = PC()
player.pc_intro()

# This is a lot to just vomit into python. I should really consider how best to design this so it isn't tons of lines.
print("----------")
print("{name} is a commoner, living in a small, idyllic village in a grand fantasy kingdom.".format(name=player.name))
print("In recent times, people have been speaking of monsters who seek to assail the kingdom at large...")
print("... but such must be mere fairy tales, right?")
print("----------")
print("{name} awakens to the scent of smoke and the sounds of screaming.".format(name=player.name))
print("The town must be under attack!")
print("{he} knows that somewhere in the house, his parents kept a weapon for self defense...".format(he=player.name))
print("... but {he} would have to spend time trying to find it.".format(he=player.gender[0]))
print("Alternatively, {he} could try to slip out the back window.".format(he=player.gender[0]))
print("What to do...")
print("1) Weapon \n 2) Window")
Protagonist_Awakens = input("Select: ")
print("You have chosen: " + Protagonist_Awakens)
