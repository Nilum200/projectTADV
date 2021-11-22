# reminder: Don't make everything static methods--wanders away from OOP.
# to-do: A "help" function for players would be nice--to check inventory, current HP, et cetera...
# to-do: Win/Loss conditions to break out of the StoryBeats loop.
# to-do: An inventory check function that allows me to check/retrieve an item for if/else narrative branches.
# to-do: Put win/loss scenes into their own category with their own triggers... maybe... hmm...
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


# These classes contain the various scenes throughout the story.
# lol these will probably be hundreds of lines.
# off we go then. Get in, loser!
# Choice: Save or help sister.
class EscapeScene:
    def escape_scene(self, player_loader):
        print("{name} attempts get out of town--anywhere is safer than here.".format(name=player_loader.name))
        print("With a little luck, no danger would come for {him}.".format(him=player_loader.gender[2]))
        print("Unfortunately, the same could not be said of {his} sister.".format(his=player_loader.gender[3]))
        print("She was pinned by a beastly marauder against a fence post!")
        print("It was possible to rescue her. All {he} had to do was try.".format(he=player_loader.gender[0]))
        print("On the other hand, the marauder was bigger than {he} was, and {he} might die in the attempt.".format(he=player_loader.gender[0]))
        print("Would {name} try to save {his} sister, or abandon her?".format(name=player_loader.name, his=player_loader.gender[3]))
        print("Valid choices: save | flee")
        choice = InputMethods.choose(['save', 'flee'])
        ScenePicker.scene_picker(choice, player_loader)


# Player searches for their family.
class FamilyScene:
    def family_scene(self, player_loader):
        print("This scene is incomplete. Turn back!")


# Player abandons their sister and gets a sad ending.
class FleeScene:
    def flee_scene(self, player_loader):
        print("{name} decides that survival is what matters most and leaves {his} sister behind.".format(name=player_loader.name, his=player_loader.gender[3]))
        print("Riding out alone, there isn't much left to do but to realize that everyone {he} knew was now doomed.".format(he=player_loader.gender[0]))
        print("What was the point of surviving if everyone you knew was dead?")
        print("END: SURVIVOR'S GUILT")


# Choice: Escape town or search for family.
class GuardsScene:
    def guards_scene(self, player_loader):
        print("Luckily, {name} didn't live far from the town guard headquarters.".format(name=player_loader.name))
        print("Traveling through town was nonetheless distressing--a few were still scrambling for safety, while others lay dead or dying upon the ground.")
        print("Thankfully, the town guard captain--Johnny Swordfish--was still there to greet {him}.".format(him=player_loader.gender[2]))
        print("'We need your help searching for survivors--you could start with your family', he said.")
        print("'On the other hand--if you're not feeling up to potential confrontations with marauders--I need to send someone to warn the King that these monsters have come for us.'")
        print("'I'll leave you to decide which is best.'")
        print("Valid choices: family | escape")
        choice = InputMethods.choose(['family', 'escape'])
        ScenePicker.scene_picker(choice, player_loader)


# Choice: Get a weapon or go out the back window.
class IntroScene:
    def intro_scene(self, player_loader):
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
        ScenePicker.scene_picker(choice, player_loader)


# Attempt to save sister--if have sword/axe: Good end. Without: Bad end.
class SaveScene:
    def save_scene(self, player_loader):
        print("{name} charges the maleficent marauder!".format(name=player_loader.name))
        # player_loader.inventory.append('sword')
        has_weapon = False
        for i in player_loader.inventory:
            # Odd error: If I set "if" to search for sword OR axe, and BOTH are true, it prints twice.
            if i == 'sword' or i == 'axe':
                print("Quick thinking with one of {his} family weapons allows {him} to overcome the marauder and save {his} sister!".format(his=player_loader.gender[3], him=player_loader.gender[2]))
                print("Thankful to be alive, {his} sister explains that she was sent by Sir Johnny Swordfish to alert the King of the marauder threat.".format(his=player_loader.gender[3]))
                print("Together, they would alert the rest of the kingdom to the danger.")
                print("Losing everything else they once knew was a high price to pay--but at least they had each other...")
                print("END: HEROIC MESSENGER")
                has_weapon = True
                break
        if has_weapon == False:
            print("Against all reason, {he} threw himself at the marauder!".format(he=player_loader.gender[0]))
            print("Unfortunate, then, that the marauder had greater size and--y'know--weapons.")
            print("The last thing {name} sees is the shocked look on {his} sister's face as {he} is impaled by the marauder's blade.".format(name=player_loader.name, his=player_loader.gender[3], he=player_loader.gender[0]))
            print("Maybe think about using some weapons in your next life?")
            print("END: KILLED BY MARAUDER.")


# The WeaponScene class is missing choice & scene-picker invocations.
# Don't forget them when you start building this path out.
# Choice: Search for family or go to the town guard.
class WeaponScene:
    # Placeholder for the weapon scene. Brave hero, aren't you?
    def weapon_scene(self, player_loader):
        print("Though it takes some amount of searching, {name} finds {his} father's sword and mother's axe.".format(name=player_loader.name, his=player_loader.gender[3]))
        # PyCharm IDE **hates** this for some reason and is convinced it will spit out errors.
        # Yet it works... hmm... will it cause me future problems, or is the IDE imperfect?
        player_loader.inventory.append('sword')
        player_loader.inventory.append('axe')
        print("Armed up, {name} heads out the door into town.".format(name=player_loader.name))
        print("Now, should {he} search for {his} family, or head toward the town guard headquarters?".format(he=player_loader.gender[0], his=player_loader.gender[3]))
        print("Valid choices: family | guards")
        choice = InputMethods.choose(['family', 'guards'])
        ScenePicker.scene_picker(choice, player_loader)


# Choice: Escape town or go to the town guard.
class WindowScene:
    # Placeholder for the window scene. Run Forest, Run!
    def window_scene(self, player_loader):
        print("{name} opts to slip out the back window of {his} sister's room.".format(name=player_loader.name, his=player_loader.gender[3]))
        print("While on the way out, {name} stumbles across {his} lockpicks.".format(name=player_loader.name, his=player_loader.gender[3]))
        # Error: his life? more like {his} life amirite
        print("It never seemed to matter how many times {his} parents tried to throw them away, they would always manage to find their way back into his life.".format(his=player_loader.gender[3]))
        print("No matter. They might come in handy...")
        player_loader.inventory.append('lockpicks')
        print("ACQUIRED: LOCKPICKS")
        print("Once out the back window, {name} contemplates {his} next move...".format(name=player_loader.name, his=player_loader.gender[3]))
        print("{name} could attempt to skip town--after all, {name} isn't much of a fighter...".format(name=player_loader.name))
        print("On the other hand, {he} could try to make it to the town guard and see what could be done.".format(he=player_loader.gender[0]))
        print("Valid choices: escape | guards")
        choice = InputMethods.choose(['escape', 'guards'])
        ScenePicker.scene_picker(choice, player_loader)


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


# This class is responsible for selecting/transitioning between scenes.
class ScenePicker(object):
    @staticmethod
    # This is cursed, but it works. All hail Cthulhu.
    def scene_picker(verifier, player_loader):
        if verifier == 'escape_scene':
            active_scene = EscapeScene()
            active_scene.escape_scene(player_loader)
        elif verifier == 'family_scene':
            active_scene = FamilyScene()
            active_scene.family_scene(player_loader)
        elif verifier == 'flee_scene':
            active_scene = FleeScene()
            active_scene.flee_scene(player_loader)
        elif verifier == 'guards_scene':
            active_scene = GuardsScene()
            active_scene.guards_scene(player_loader)
        elif verifier == 'intro_scene':
            active_scene = IntroScene()
            active_scene.intro_scene(player_loader)
        elif verifier == 'save_scene':
            active_scene = SaveScene()
            active_scene.save_scene(player_loader)
        elif verifier == 'weapon_scene':
            active_scene = WeaponScene()
            active_scene.weapon_scene(player_loader)
        elif verifier == 'window_scene':
            active_scene = WindowScene()
            active_scene.window_scene(player_loader)
        else:
            # Ideally, this should never print. Ever. If it somehow does, then I know something is profoundly busted.
            print("Nilum, something broke here: " + str(verifier) + ".")


# Where things go until they're better organized. A test space, for testing... IN SPACE!

player = PC()
player.pc_intro()
# This is a flat line. I should think of how to replace this at some point, but it works--for now.
first_choice = 'intro_scene'
# first_scene = IntroScene()

ScenePicker.scene_picker(first_choice, player)

# Little by little, day by day, I carry on...
