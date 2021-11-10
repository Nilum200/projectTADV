# Establish a Player Class here. It should take: HP, Inventory, Gender, Name.
class PC:
    def __init__(self, name='StandardMcDefault', gender='neutral'):
        self.name = name
        self.gender = gender

    def gender_picker(self):
        if self.gender == 'male':
            self.gender = ['himself', 'him', 'his']
        elif self.gender == 'female':
            self.gender = ['herself', 'her', 'hers']
        elif self.gender == 'neutral':
            self.gender = ['themself', 'them', 'theirs']

    female = ['herself', 'her', 'hers']
    neutral = ['themself', 'them', 'theirs']


# Establish methods for input on Name/Gender here. Don't forget that gender has multiple pronouns! Himself, him, his.
print("Hello and welcome to TADV! To play, type in a corresponding option when they appear.")
player = PC()
temp_name = input('Enter your name:')
temp_gender = input('Are you...\n 1) Male \n 2) Female \n 3) Neutral\n Option:')
player.name = temp_name
player.gender = temp_gender.lower()
player.gender_picker()
print(player.name)
print("Your pronouns are: " + str(player.gender) + ".")

# Establish an intro here. Eg: "{Name} finds {himself/herself} in danger..."
