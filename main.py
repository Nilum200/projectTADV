# Version 2: Back to the ramparts we charge!
# The purpose of this class is to take a list of choices and return a scene ID, which is then fed into ScenePicker.
# to-do: Rebuild the scenes within the new structure of code. Rely as much as possible on automation.
# to-do: Watch it explode. Laugh. Drink. Try again.
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
        id_01_intro_scene = BaseScene([], [], 'Base_Script.txt')
        # Add scene 2 here.
        # Add scene 3 here.
        # Et cetera...
        # Contain all instantiated scenes in a list that can be called with the scene_id.
        id_list = [id_01_intro_scene]
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
                self.gender = ['she', 'her', 'hers', 'herself']
                valid_choice = True
            elif answer.lower() == 'neutral':
                self.gender = ['they', 'them', 'theirs', 'themself']
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
        else:
            print("If this prints, there weren't enough valid choices presented. Oops.")


# WiP. Ignore.
class ChildScene(BaseScene):
    def __init__(self, choices, scene_id_list, script):
        super().__init__(choices, scene_id_list, script)


player1 = PlayerLoader('StandardMcDefault', ['he', 'him', 'his', 'himself'], [])
player1.character_gen()
ScenePicker.scene_picker(0)
