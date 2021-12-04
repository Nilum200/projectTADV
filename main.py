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
            # If no valid options are found, count is reset in the while loop to prevent it from accessing wrong index.
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
        id_00 = IntroScene([], 1, 'Script_Intro.txt')
        # Protagonist Awakens.
        id_01 = StandardScene(['Get Weapon', 'Back Window'], [2, 3], 'Script_Protagonist_Awakens.txt')
        # Get Weapon.
        id_02 = GainItemScene(['Find Family', 'Town Guard'], [8, 4], 'Script_Get_Weapon.txt', ['sword', 'axe'])
        # Out the Window.
        id_03 = GainItemScene(['Town Guard', 'Escape Town'], [4, 5], 'Script_Out_The_Window.txt', ['lockpicks'])
        # Find the Town Guard.
        id_04 = StandardScene(['Escape Town', 'Find Family'], [5, 8], 'Script_Town_Guard.txt')
        # Escape Town.
        id_05 = StandardScene(['Help Sister', 'Leave Sister'], [6, 7], 'Script_Escape_Town.txt')
        # Save sister.
        id_06 = EndingChallengeScene('Script_Escape_Town.txt', 'sword', 'End_Messenger.txt', 'End_Marauder.txt')
        # Leave sister.
        id_07 = EndingNoChallengeScene(script='End_Survivors_Guilt.txt')
        # Search for Family/Discover the Enemy.
        id_08 = StandardScene(['Follow Them', 'Ambush Them'], [9, 10], 'Script_Search_Family.txt')
        # Follow them.
        id_09 = StandardScene(['Go Help', 'Keep Following'], [11, 14], 'Script_Follow.txt')
        # Ambush them.
        id_10 = AmbushScene(['Continue Story', ''], [11], 'Script_Ambush.txt', 'End_Marauder.txt')
        # The Wildfire.
        id_11 = StandardScene(['Save Gun', 'Save Sally'], [12, 13], 'Script_Wildfire.txt')
        # Save the Gun/Going on your own.
        id_12 = GainItemScene(['Continue Story', ''], [14], 'Script_Get_Gun.txt', ['gun'])
        # Save Sally/Regroup with the Squad.
        id_13 = GainItemScene(['Continue Story', ''], [14], 'Script_Sally_Squad.txt', ['sally squad'])
        # The Butcher's Shop.
        id_14 = ButcherScene([], [], 'Script_Butcher.txt')
        # The Back Way.
        id_15 = StandardScene(['Rescue Parents', 'Assassinate Leader'], [16, 17], 'Script_Back_Way.txt')
        # Rescue Parents.
        id_16 = EndingNoChallengeScene('Script_Rescue_Parents.txt')
        # Assassinate the Leader.
        id_17 = EndingChallengeScene('Script_Assassinate_Leader.txt', 'gun', 'End_Equalizer.txt', 'End_Naive.txt')
        # Confrontation.
        id_18 = StandardScene(['Duel', 'Negotiate'], [19, 20], 'Script_Confrontation.txt')
        # Duel to the Death.
        id_19 = EndingChallengeScene('Script_Duel.txt', 'axe', 'End_Sacrifice.txt', 'End_Really.txt')
        # Negotiate
        id_20 = StandardScene(['Surrender Town', 'Join', 'Demand Surrender'], [21, 22, 23], 'Script_Negotiate.txt')
        # Surrender Town, Spare Family
        id_21 = EndingNoChallengeScene('End_Surrender_Town.txt')
        # We'll Join You
        id_22 = EndingNoChallengeScene('End_Join.txt')
        # Surrender or Die
        id_23 = SoDScene('End_Hero.txt', 'End_Last_Standing.txt')
        # Break-In and Surprise Attack.
        id_24 = StandardScene(['Rush Leader', 'Overwhelm Them'], [25, 26], 'Script_Break_In.txt')
        # Go for the Leader.
        id_25 = EndingChallengeScene('Script_Go_Leader.txt', 'gun', 'End_Equalizer.txt', 'End_Naive.txt')
        # Overwhelm Them.
        id_26 = EndingChallengeScene('Script_Overwhelm.txt', 'sally squad', 'End_Rush.txt', 'End_Alone.txt')

        # Contain all instantiated scenes in a list that can be called with the scene_id.
        id_list = [id_00, id_01, id_02, id_03, id_04, id_05, id_06, id_07, id_08, id_09, id_10, id_11, id_12, id_13, id_14, id_15, id_16, id_17, id_18, id_19, id_20, id_21, id_22, id_23, id_24, id_25, id_26]
        next_scene = id_list[scene_id]
        next_scene.scene_reader(player1)


# A simple player class with a character generator method inside.
class PlayerLoader:
    def __init__(self, name, gender, inventory):
        self.name = name
        self.gender = gender
        self.inventory = inventory

    # Now generates a name and a gender in a single method.
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
        # Used to specify a list of choices for *Choose* class/method. This is what the player sees.
        self.choices = choices
        # Used to specify a list of ID's in tandem with choices. Like a map...
        self.scene_id_list = scene_id_list
        # Calling a text file to be read as the script.
        self.script = script

    # Opens, reads, formats, and then closes the text file associated with scene before continuing to scene_operator.
    def scene_reader(self, player):
        text = open(self.script)
        text_open = text.read()
        print(text_open.format(name=player.name, he=player.gender[0], him=player.gender[1], his=player.gender[2], himself=player.gender[3]))
        text.close()
        self.scene_operator(player)

    # Checks if there are sufficient valid options to continue.
    # If true: Feed choices & scene_id_list into choose method; feed return value into ScenePicker.
    # If false: Print a debug line that informs me I'm missing an argument somewhere.
    def scene_operator(self, player):
        if len(self.choices) > 0:
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
# choices & scene_id_list are irrelevant, so they get default arguments of empty strings.
class EndingChallengeScene(BaseScene):
    def __init__(self, script, inv_check, good_end, bad_end, choices='', scene_id_list=''):
        super().__init__(choices, scene_id_list, script)
        self.inv_check = inv_check
        self.good_end = good_end
        self.bad_end = bad_end

    def scene_reader(self, player):
        super().scene_reader(player)

    # Currently limited to checking against a single item in the form of a string.
    # I could make it more complex and have it check against a table of valid answers...
    # ... but the program doesn't require this to function. It seems bad form to unnecessarily complicate things.
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


# Endings without a challenge check. They just read the script and then ignore scene_operator.
class EndingNoChallengeScene(BaseScene):
    def __init__(self, script, choices='', scene_id_list='',):
        super().__init__(choices, scene_id_list, script)

    def scene_reader(self, player):
        super().scene_reader(player)

    def scene_operator(self, player):
        pass


# More complex endings/branches will require specific child scenes, but hey--step in the right direction.
# These are all specific children classes for scenes that don't fit the above moulds.
class IntroScene(BaseScene):
    def __init__(self, choices, scene_id_list, script):
        super().__init__(choices, scene_id_list, script)

    def scene_reader(self, player):
        super().scene_reader(player)

    def scene_operator(self, player):
        ScenePicker.scene_picker(self.scene_id_list)


class AmbushScene(BaseScene):
    def __init__(self, choices, scene_id_list, script, fail_script):
        super().__init__(choices, scene_id_list, script)
        self.fail_script = fail_script

    def scene_reader(self, player):
        continue_story = False
        for item in player.inventory:
            if item == 'sword':
                continue_story = True
                text = open(self.script)
                text = text.read()
                # Reminder: Player loses sword here. Be sure to tell them that in the script to avoid confusion.
                print(text.format(name=player.name, he=player.gender[0], him=player.gender[1], his=player.gender[2], himself=player.gender[3]))
                player.inventory.remove('sword')
                self.scene_operator(player)
        if not continue_story:
            text = open(self.fail_script)
            text = text.read()
            print(text.format(name=player.name, he=player.gender[0], him=player.gender[1], his=player.gender[2], himself=player.gender[3]))

    def scene_operator(self, player):
        super().scene_operator(player)


class ButcherScene(BaseScene):
    def __init__(self, choices, scene_id_list, script):
        super().__init__(choices, scene_id_list, script)

    def scene_reader(self, player):
        text = open(self.script)
        text = text.read()
        # Be sure the script is written such as to go: "And the options available are..."
        print(text.format(name=player.name, he=player.gender[0], him=player.gender[1], his=player.gender[2], himself=player.gender[3]))
        for item in player.inventory:
            if item == 'lockpicks':
                print("A set of lockpicks could be used to get in the back door discretely.")
                self.choices.append('back door')
                self.scene_id_list.append(15)
            if item == 'sally squad':
                print("Sally's gang have the numbers for a direct confrontation.")
                self.choices.append('confront marauders')
                self.scene_id_list.append(18)
            if item == 'axe':
                print("A quick-footed break-in with mother's axe might grant the advantage of total surprise.")
                self.choices.append('break in')
                self.scene_id_list.append(24)
        print("Valid Choices: ", self.choices)
        self.scene_operator(player)

    def scene_operator(self, player):
        super().scene_operator(player)


class SoDScene(BaseScene):
    def __init__(self, good_end, bad_end, script='', choices='', scene_id_list=''):
        super().__init__(script, choices, scene_id_list)
        self.bad_end = bad_end
        self.good_end = good_end

    def scene_reader(self, player):
        good_end = False
        # I wonder if this is more efficient than for loops... theoretically it should be.
        if 'sword' in player.inventory and 'axe' in player.inventory:
            good_end = True
            text = open(self.good_end)
            text = text.read()
            print(text.format(name=player.name, he=player.gender[0], him=player.gender[1], his=player.gender[2], himself=player.gender[3]))
        if not good_end:
            text = open(self.bad_end)
            text = text.read()
            print(text.format(name=player.name, he=player.gender[0], him=player.gender[1], his=player.gender[2], himself=player.gender[3]))


# Instantiate player class into an object and generate their name/gender to replace default variable contents.
player1 = PlayerLoader('StandardMcDefault', ['he', 'him', 'his', 'himself'], [])
player1.character_gen()
# Start trigger.
ScenePicker.scene_picker(0)
