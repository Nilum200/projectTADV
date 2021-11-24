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
# Single Path: Wildfire. If player lacks sword, they die. If they have sword, they sacrifice it to continue.
class AmbushScene:
    def ambush_scene(self, player_loader):
        print("Scene incomplete.")


# Ending: If player has gun, they kill the leader. If player does not, leader kills/captures them.
class AssassinateScene:
    def assassinate_scene(self, player_loader):
        print("Scene incomplete.")


# Choice: The Back Way, Confrontation, Break-In & Surprise.
# See if you can make it so "The Back Way" only appears if someone has the prerequisite item: lockpicks.
class ButcherScene:
    def butcher_scene(self, player_loader):
        choice_options = []
        print("Arriving at the butcher's shop, {name} contemplates {his} options...".format(name=player_loader.name, his=player_loader.gender[3]))
        if 'lockpicks' in player_loader.inventory:
            choice_options.append('infiltrate')
            print("Using lockpicks, {he} could silently infiltrate through the back door.".format(he=player_loader.gender[0]))
        if 'axe' in player_loader.inventory:
            choice_options.append('surprise')
            print("Using {his} mother's axe, {he} could break his way through the front door and attempt a surprise attack.".format(his=player_loader.gender[3], he=player_loader.gender[0]))
        if 'sally_squad' in player_loader.inventory:
            choice_options.append('confront')
            print("With Sally and her squad behind {him}, {name} could attempt a direct confrontation.".format(him=player_loader.gender[2], name=player_loader.name))
        # This is janky and would be better resolved with a check to see if the player has multiple options.
        # For the moment, though, the emphasis is simply on making a complete prototype. Refinement can come later.
        print("Regardless, {name} would have to make a decision about this final confrontation.".format(name=player_loader.name))
        print("So, which will it be?")
        choice_options_string = " | ".join(choice_options)
        print("Valid choices: " + choice_options_string)
        choice = InputMethods.choose(choice_options)
        ScenePicker.scene_picker(choice, player_loader)


# Choice: Duel or Negotiate.
class ConfrontScene:
    def confront_scene(self, player_loader):
        print("Scene unfinished.")


# Player dies without a weapon. Player sacrifices themselves to kill the leader if they have a sword or axe.
class DuelScene:
    def duel_scene(self, player_loader):
        print("Scene isn't done yet.")


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


# Save protagonist's family and other prisoners, but lose the town/become refugees.
# I may need a better name for this--family isn't super clear.
class FamilyScene:
    def family_scene(self, player_loader):
        print("Placeholder for the scene. Imagine your happy place.")


# Choice: Save Sally or save the Town's Pistol.
class FireScene():
    def fire_scene(self, player_loader):
        print("Incomplete scene. Egads!")


# Player abandons their sister and gets a sad ending.
class FleeScene:
    def flee_scene(self, player_loader):
        print("{name} decides that survival is what matters most and leaves {his} sister behind.".format(name=player_loader.name, his=player_loader.gender[3]))
        print("Riding out alone, there isn't much left to do but to realize that everyone {he} knew was now doomed.".format(he=player_loader.gender[0]))
        print("What was the point of surviving if everyone you knew was dead?")
        print("END: SURVIVOR'S GUILT")


# Choice: Listen to the cries for help or continue straight to the butcher's shop.
class FollowScene:
    def follow_scene(self, player_loader):
        print("Following the brute wasn't difficult, as they never bothered to look back.")
        print("They were heading toward the old butcher's shop--was that where the bandits were gathering their loot?")
        print("Cries for help echo throughout the area, most too far to even consider helping.")
        print("One piercing shriek, however, reaches {name}'s ears.".format(name=player_loader.name))
        print("It came from a nearby burning structure.")
        print("The marauder appears to be ignoring it, continuing to drag the body to its final destination instead.")
        print("Would {name} listen to the cry for help, or carry on following in silence?".format(name=player_loader.name))
        print("Valid choices: fire | butcher")
        choice = InputMethods.choose(['fire', 'butcher'])
        ScenePicker.scene_picker(choice, player_loader)


# Choice: Escape town or search for family.
class GuardsScene:
    def guards_scene(self, player_loader):
        print("Luckily, {name} didn't live far from the town guard headquarters.".format(name=player_loader.name))
        print("Traveling through town was nonetheless distressing--a few were still scrambling for safety, while others lay dead or dying upon the ground.")
        print("Thankfully, the town guard captain--Johnny Swordfish--was still there to greet {him}.".format(him=player_loader.gender[2]))
        print("'We need your help searching for survivors--you could start with your family', he said.")
        print("'On the other hand--if you're not feeling up to potential confrontations with marauders--I need to send someone to warn the King that these monsters have come for us.'")
        print("'I'll leave you to decide which is best.'")
        print("Valid choices: search | escape")
        choice = InputMethods.choose(['search', 'escape'])
        ScenePicker.scene_picker(choice, player_loader)


# Player takes gun instead of saving Sally; player goes it alone to the butcher's shop.
class GunScene:
    def gun_scene(self, player_loader):
        print("This gun isn't complete. Go get a gun elsewhere.")
        player_loader.inventory.append('gun')


# Use lockpicks to sneak into the place all subtle-like.
class InfiltrateScene:
    def infiltrate_scene(self, player_loader):
        print("Not finished yet.")


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


# Player opts to join the marauders.
class JoinScene:
    def join_scene(self, player_loader):
        print("Evil isn't ready to accept you yet--scene not done.")


# If player has a pistol, they shoot the leader dead. Otherwise, they fail. Related to the Surprise/Break-In path.
class LeaderScene:
    def leader_scene(self, player_loader):
        print("Killing leaders is fine, but this scene isn't done yet.")


# Negotiate with the bad guys. Options: Family (Spare them), Join (turn to evil), Surrender (or die!).
class NegotiateScene:
    def negotiate_scene(self, player_loader):
        print("Not done yet.")


# Break-in/Surprise and overwhelm the enemy with numbers, so long as you have sally's squad you win. Otherwise...
class OverwhelmScene:
    def overwhelm_scene(self, player_loader):
        print("Work in progress, come back later.")


# Slip-in and rescue your parents, but, y'know, carefully.
class ParentsScene:
    def parents_scene(self, player_loader):
        print("Rescuing parents takes a while. Scene under construction.")


# Rescue sally instead of the gun. Leads to the Butcher's shop.
class SallyScene:
    def sally_scene(self, player_loader):
        print("Soon enough, young padawan, this scene will be.")


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


# Player searches for their family.
class SearchScene:
    def search_scene(self, player_loader):
        print("{name}'s family was out there somewhere, and {he} had to find them.".format(name=player_loader.name, he=player_loader.gender[0]))
        if 'sword' in player_loader.inventory or 'axe' in player_loader.inventory:
            print("Being armed would provide some measure of comfort, at least.")
        else:
            print("Lacking weapons would make this a more difficult task--unless {he} thought things through carefully...".format(he=player_loader.gender[0]))
        print("While attempting to find any sign of {his} family, {name} spies a single marauder, dragging a body through the streets.".format(his=player_loader.gender[3], name=player_loader.name))
        print("The marauder hasn't noticed {him} yet.".format(him=player_loader.gender[2]))
        print("Perhaps following them might uncover where other survivors are.")
        print("On the other hand, ambushing them was a real possibility, too.")
        print("What should {name} do?".format(name=player_loader.name))
        print("Valid choices: ambush | follow")
        choice = InputMethods.choose(["ambush", "follow"])
        ScenePicker.scene_picker(choice, player_loader)


# Choose to use your axe to take the villains by surprise. Leads to *Leader* and *Overwhelm*.
class SurpriseScene:
    def surprise_scene(self, player_loader):
        print("Surprise! This scene is unfinished.")


# Try to force an enemy to surrender during a confrontation.
class SurrenderScene:
    def surrender_scene(self, player_loader):
        print("The enemy surrenders--not you... when the scene is complete.")


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
        print("Valid choices: search | guards")
        choice = InputMethods.choose(['search', 'guards'])
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
        if verifier == 'ambush_scene':
            active_scene = AmbushScene()
            active_scene.ambush_scene(player_loader)
        if verifier == 'assassinate_scene':
            active_scene = AssassinateScene()
            active_scene.assassinate_scene(player_loader)
        elif verifier == 'butcher_scene':
            active_scene = ButcherScene()
            active_scene.butcher_scene(player_loader)
        elif verifier == 'confront_scene':
            active_scene = ConfrontScene()
            active_scene.confront_scene(player_loader)
        elif verifier == 'duel_scene':
            active_scene = DuelScene()
            active_scene.duel_scene(player_loader)
        elif verifier == 'escape_scene':
            active_scene = EscapeScene()
            active_scene.escape_scene(player_loader)
        elif verifier == 'family_scene':
            active_scene = FamilyScene()
            active_scene.family_scene(player_loader)
        elif verifier == 'fire_scene':
            active_scene = FireScene()
            active_scene.fire_scene(player_loader)
        elif verifier == 'flee_scene':
            active_scene = FleeScene()
            active_scene.flee_scene(player_loader)
        elif verifier == 'follow_scene':
            active_scene = FollowScene()
            active_scene.follow_scene(player_loader)
        elif verifier == 'guards_scene':
            active_scene = GuardsScene()
            active_scene.guards_scene(player_loader)
        elif verifier == 'gun_scene':
            active_scene = GunScene()
            active_scene.gun_scene(player_loader)
        elif verifier == 'infiltrate_scene':
            active_scene = InfiltrateScene()
            active_scene.infiltrate_scene(player_loader)
        elif verifier == 'intro_scene':
            active_scene = IntroScene()
            active_scene.intro_scene(player_loader)
        elif verifier == 'join_scene':
            active_scene = JoinScene()
            active_scene.join_scene(player_loader)
        elif verifier == 'leader_scene':
            active_scene = LeaderScene()
            active_scene.leader_scene(player_loader)
        elif verifier == 'negotiate_scene':
            active_scene = NegotiateScene()
            active_scene.negotiate_scene(player_loader)
        elif verifier == 'overwhelm_scene':
            active_scene = OverwhelmScene()
            active_scene.overwhelm_scene(player_loader)
        elif verifier == 'parents_scene':
            active_scene = ParentsScene()
            active_scene.parents_scene(player_loader)
        elif verifier == 'sally_scene':
            active_scene = SallyScene()
            active_scene.sally_scene(player_loader)
        elif verifier == 'save_scene':
            active_scene = SaveScene()
            active_scene.save_scene(player_loader)
        elif verifier == 'search_scene':
            active_scene = SearchScene()
            active_scene.search_scene(player_loader)
        elif verifier == 'surprise':
            active_scene = SurpriseScene()
            active_scene.surprise_scene(player_loader)
        elif verifier == 'surrender':
            active_scene = SurrenderScene()
            active_scene.surrender_scene(player_loader)
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

# Another burst of energy to reach the top.
