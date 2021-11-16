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


# Class hoards story beats, each contained in a function. Ideally I can automate the entire process.
class StoryBeats(object):
    @staticmethod
    # Placeholder for the weapon scene.
    def weapon_scene():
        print("This is a weapon placeholder.")

    # Placeholder for the window scene.
    def window_scene():
        print("This is a window placeholder.")


# The class responsible for handling inputs.
# Pedro is awesome.
class InputMethods(object):
    @staticmethod
    # Give this a clearer name later.
    # Takes input to choose the next scene, which is then put into the scene picker.
    def choose(string_list):
        valid = False
        while not valid:
            answer = input('Choose: ')
            for item in string_list:
                if item.lower() == answer.lower():
                    valid = True
                    print("Test Successful: " + answer + ".")
                    # Eventually: This return statement returns a value fed into StoryBeats.
                    scene_picker = answer.lower() + "_scene"
                    return scene_picker
            if not valid:
                print("Invalid entry, please try again.")

    # Scene picker checks the string input of a previous decision and then races off to fetch a scene.
    def scene_picker(string):
        if string == 'weapon_scene':
            StoryBeats.weapon_scene()
        elif string == 'window_scene':
            StoryBeats.window_scene()
        else:
            print("Hmm...")


first_choice = InputMethods.choose(['weapon', 'window'])
InputMethods.scene_picker(first_choice)

# Where things go until they're better organized. A test space, for testing... IN SPACE!

# Establish an intro here. Eg: "{Name} finds {himself/herself} in danger..."
# player = PC()
# player.pc_intro()

# This is a lot to just vomit into python. I should really consider how best to design this so it isn't tons of lines.

