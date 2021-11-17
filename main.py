# reminder: Don't make everything static methods--wanders away from OOP.
# to-do: A "help" function for players would be nice--to check inventory, current HP, et cetera...
# to-do: Win/Loss conditions to break out of the StoryBeats loop.
# to-do: An inventory check function that allows me to check/retrieve an item for if/else narrative branches.
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
                self.gender = ['she', 'herself', 'her', 'her']
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


# Class contains story beats, each contained in a function.
# Ideally, I can get it working such that it automates the process of going from one beat to the next...
# ... until win/loss conditions are encountered.
class StoryBeats:
    @staticmethod
    def intro_scene(player_loader):
        # Consider: Could a for loop replace each instance of {name}, {his}, {him} with appropriate gender pronouns?
        # Might be my next little project here...
        print("{name} is a commoner, living in a small, idyllic village.".format(name=player_loader.name))
        print("Your objective is to help {him} survive.".format(him=player_loader.gender[2]))
        print("Have fun...")
        print("----------")
        print("{name} awakens to the scent of smoke and sounds of screaming!".format(name=player_loader.name))
        # Fix the capitalization thing later OR reframe the narration so I never have to deal with it.
        print("{he} knows that {his} father keeps a weapon in the house, but he isn't sure where...".format(he=player_loader.gender[0], his=player_loader.gender[3]))
        print("Alternatively, {he} could try sneaking out the back window into the garden.".format(he=player_loader.gender[0]))
        print("What does {name} decide to do?".format(name=player_loader.name))
        # I should find a way to handle this with a little more grace at some point.
        print("Valid choices: weapon | window")
        # and now StoryBeats picks scenes inside itself until a win or loss condition is triggered. Fabulous.
        choice = InputMethods.choose(['weapon', 'window'])
        InputMethods.scene_picker(choice, player_loader)

    # Placeholder for the weapon scene. Brave hero, aren't you?
    def weapon_scene(player_loader):
        print("Though it takes some amount of searching, you find your father's sword and mother's axe.")
        # PyCharm IDE **hates** this for some reason and is convinced it will spit out errors.
        # Yet it works... hmm... will it cause me future problems, or is the IDE imperfect?
        player_loader.inventory.append('sword')
        player_loader.inventory.append('axe')
        print("Weapon path test: Success.")
        print("Did the inventory update?")
        print(player_loader.inventory)

    # Placeholder for the window scene. Run Forest, Run!
    def window_scene(player_loader):
        print("This is the window scene placeholder. If we got here, mission successful.")


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
                    scene_picker = answer.lower() + "_scene"
                    # This return statement feeds input into the scene picker.
                    # I fully realize this could permit a non-linear story. I'll think about it...
                    return scene_picker
            if not valid:
                print("Invalid entry, please try again.")

    # Scene picker checks the string input of a previous decision and then races off to fetch a scene.
    def scene_picker(verifier, player_loader):
        if verifier == 'intro_scene':
            StoryBeats.intro_scene(player_loader)
        elif verifier == 'weapon_scene':
            StoryBeats.weapon_scene(player_loader)
        elif verifier == 'window_scene':
            StoryBeats.window_scene(player_loader)
        else:
            # Ideally, this should never print. Ever. If it somehow does, then I know something is profoundly busted.
            # Naturally, I managed to trigger it once--and it helped me.
            print("Nilum, something broke here: " + str(verifier) + ".")


# Where things go until they're better organized. A test space, for testing... IN SPACE!

player = PC()
player.pc_intro()
# This is a flat line. I should think of how to replace this at some point, but it works--for now.
first_choice = 'intro_scene'
InputMethods.scene_picker(first_choice, player)

# I'm getting smarter every day. Delightful!
