# Version 2: Back to the ramparts we charge!
# The purpose of this class is to take a list of choices and return a scene ID, which is then fed into ScenePicker.
# to-do: Clean up the two ending classes to no longer request *choice* and *scene_id* information.
# to-do: Rename/reorganize scripts in shared folder to follow a scheme: script_name; end_name; and so on...
class Choose(object):
    @staticmethod
    def choose(choice_list, scene_list):
        valid = False
        while not valid:
            # "Count" is my cheeky way of creating a variable for scene_list.
            # Scene_list contains valid ID's for use in scene_picker. See scene_picker to understand.
            count = -1
            answer = input('Choose: ')
            # For loop to check answer against valid options.
            for index in choice_list:
                count += 1
                if index.lower() == answer.lower():
                    valid = True
                    print("Executing Path: " + answer + ".")
                    # Return scene_id for ScenePicker.
                    return scene_list[count]
            # Prevent input from exploding if invalid input is given.
            if not valid:
                print("Invalid entry, please try again.")


# Takes a valid scene ID from Choose and opens the scene based on ID.
# No more infinite if/else loops. One set of ID's shuffled into a list which are then called one by one as appropriate.
class ScenePicker(object):
    @staticmethod
    def scene_picker(scene_id):
        # IntroScene which serves as a trigger to get the ball rolling.
        id_00 = IntroScene([], 1, 'Intro_Script.txt')
        # Protagonist Awakens.
        id_01 = StandardScene(['Get Weapon', 'Back Window'], [2, 3], 'Protagonist_Awakens_Script.txt')
        # Get Weapon.
        id_02 = GainItemScene([], [], 'Placeholder_Script.txt', ['sword', 'axe'])
        # Out the Window.
        id_03 = GainItemScene(['Town Guard', 'Escape Town'], [4, 5], 'Out The Window.txt', ['lockpicks'])
        # Find the Town Guard.
        id_04 = StandardScene([], [], 'Placeholder_Script.txt')
        # Escape Town.
        id_05 = StandardScene(['Help Sister', 'Leave Sister'], [6, 7], 'Escape_Town_Script.txt')
        # Attempt to save sister.
        id_06 = EndingChallengeScene([], [], 'Escape_Town_Script.txt', 'sword', 'End_Messenger.txt', 'End_Marauder.txt')
        # Leave sister.
        id_07 = EndingNoChallengeScene([], [], 'End_Survivors_Guilt.txt')

        # Contain all instantiated scenes in a list that can be called with the scene_id.
        id_list = [id_00, id_01, id_02, id_03, id_04, id_05, id_06, id_07]
        next_scene = id_list[scene_id]
        next_scene.scene_reader(player1)


# A simple player class with a character generator method inside.
class PlayerLoader:
    def __init__(self, name, gender, inventory):
        self.name = name
        self.gender = gender
        self.inventory = inventory

    def character_gen(self):
        print("What would you like to name the protagonist of this story?")
        self.name = input("Name: ")
        print("What is the protagonist's gender?")
        valid_choice = False
        while not valid_choice:
            answer = input("1) Male 2) Female 3) Neutral\nGender: ")
            if answer.lower() == 'male':
                self.gender = ['he', 'him', 'his', 'himself']
                valid_choice = True
            elif answer.lower() == 'female':
                self.gender = ['she', 'her', 'her', 'herself']
                valid_choice = True
            elif answer.lower() == 'neutral':
                self.gender = ['they', 'them', 'their', 'themself']
                valid_choice = True
            else:
                print("Hmm... something went wrong. Did you type male, female, or neutral? Let's try that again.")


# The base scene from which all other scenes are derived. All hail the parent.
class BaseScene:
    def __init__(self, choices, scene_id_list, script):
        self.choices = choices
        self.scene_id_list = scene_id_list
        self.script = script

    def scene_reader(self, player):
        text = open(self.script)
        text_open = text.read()
        print(text_open.format(name=player.name, he=player.gender[0], him=player.gender[1], his=player.gender[2], himself=player.gender[3]))
        text.close()
        self.scene_operator(player)

    def scene_operator(self, player):
        if len(self.choices) > 1:
            scene = Choose.choose(self.choices, self.scene_id_list)
            ScenePicker.scene_picker(scene)
        else:
            print("--END OF VALID CHOICES--")


# Assuming I don't have to perform any overrides, this is the default class to call for instantiating a scene.
# Classes are like sets of instructions...
class StandardScene(BaseScene):
    def __init__(self, choices, scene_id_list, script):
        super().__init__(choices, scene_id_list, script)

    def scene_reader(self, player):
        super().scene_reader(player)

    def scene_operator(self, player):
        super().scene_operator(player)


# Like standard scene, but adds item(s) to a player's inventory.
class GainItemScene(BaseScene):
    def __init__(self, choices, scene_id_list, script, items):
        super().__init__(choices, scene_id_list, script)
        self.items = items

    def scene_reader(self, player):
        for entry in self.items:
            player.inventory.append(entry)
            print("{name} has acquired: ".format(name=player.name) + str(entry))
        super().scene_reader(player)

    def scene_operator(self, player):
        super().scene_operator(player)


# Endings with an inventory check challenge.
class EndingChallengeScene(BaseScene):
    def __init__(self, choices, scene_id_list, script, inv_check, good_end, bad_end):
        super().__init__(choices, scene_id_list, script)
        self.inv_check = inv_check
        self.good_end = good_end
        self.bad_end = bad_end

    def scene_reader(self, player):
        super().scene_reader(player)

    def scene_operator(self, player):
        good_end = False
        for item in player.inventory:
            if item == self.inv_check:
                good_end = True
                text = open(self.good_end)
                text_open = text.read()
                print(text_open.format(name=player.name, he=player.gender[0], him=player.gender[1], his=player.gender[2], himself=player.gender[3]))
                text.close()
        if not good_end:
            text = open(self.bad_end)
            text_open = text.read()
            print(text_open.format(name=player.name, he=player.gender[0], him=player.gender[1], his=player.gender[2], himself=player.gender[3]))
            text.close()


# Endings without a challenge check.
# More complex endings/branches will require specific child scenes, but hey--step in the right direction.
class EndingNoChallengeScene(BaseScene):
    def __init__(self, choices, scene_id_list, script):
        super().__init__(choices, scene_id_list, script)

    def scene_reader(self, player):
        super().scene_reader(player)

    def scene_operator(self, player):
        pass


# These are all specific children classes for scenes that don't fit the above moulds.
class IntroScene(BaseScene):
    def __init__(self, choices, scene_id_list, script):
        super().__init__(choices, scene_id_list, script)

    def scene_reader(self, player):
        super().scene_reader(player)

    def scene_operator(self, player):
        ScenePicker.scene_picker(self.scene_id_list)


# Instantiate player class into an object and generate their name/gender to replace default variable contents.
player1 = PlayerLoader('StandardMcDefault', ['he', 'him', 'his', 'himself'], [])
player1.character_gen()
# Start trigger.
ScenePicker.scene_picker(0)
