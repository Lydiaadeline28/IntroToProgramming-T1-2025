 # narrow path events
#mushroom options
def small_cottage():
    print("YOU SURVIVE: the people in the cottage give you a map and help you get home")
def inn_food():
    print("YOU SURVIVE: the people in the people in the inn give you dinner and a map to help you get home ")
def haunted_building():
    print("ENDING: the monsters attack you")
def troll_tavern():
    print("ENDING: the trolls eat you for dinner")
def mushroom():  
    # player picks between 4 different buildings
    print(" you safely continue on without being affected, you see 4 different buildings you can go to.")
    print (" a small cottage with the lights on")
    print("an inn with the smells of food")
    print("a scary dark seemingly haunted building ")
    print(" a tavern of trolls")
    choice = input("> ")
    if choice == "1":
        small_cottage()
    elif choice == "2":
        inn_food()
    elif choice == "3":
       haunted_building()
    elif choice == "4":
        troll_tavern()
    else:
        print("Invalid choice. Try again.")

#apple gifts options
def west():
    print("YOU SURVIVE: you return home")
def east():
    print("ENDING: you wander into the cursed forest where the monsters eat you")
def north():
    print("ENDING: you wander up into the witch of the west's backyard, she turns you into a frog and you hop around for eternity")
def south():
    print("ENDING: you wander up and into the evil queens dungeon where you are imprisoned for life.")

#underground path options
def apple_gift():
    #player must remember where their house is
    print("The underground people accept the apple and you ask them for help, they lead you through the ground and ask where your house is, there are 4 directions around you which do you choose? The underground people cannot follow you above ground and you wont be able to turn back.")
    choice = input("> ")
    if choice == "1":
        west()
    elif choice == "2":
        east()
    elif choice == "3":
       north()
    elif choice == "4":
        south()
    else:
        print("Invalid choice. Try again.")
def sword_gift():
    print("YOU SURVIVE:the underground people really appreciate this gift and help you back home")
def nothing_gift():
    print("ENDING:The underground people become suspisous of you and abandon you in the unescapable underground cave for life")
def fight_underground():
    print("ENDING:the underground people beat you extremley easily and feed you to their underground dragon")
# chicken options
def underground_path():
    #player chooses what to do with the underground people
    print("You see some underground people who are wary of you, they might help you get back home.")
    print("1: Gift them a sword")
    print("2.Fight them")
    print("3. Gift them An apple")
    print("4.dont give them anything. and attempt to move around their homes")
    choice = input("> ")
    if choice == "1":
        sword_gift()
    elif choice == "2":
        fight_underground()
    elif choice == "3":
       apple_gift()
    elif choice == "4":
        nothing_gift()
    else:
        print("Invalid choice. Try again.")
# forest path options
def mango():
    print("YOU SURVIVE: you get a map to go home and a mango tree")
def orange():
    print("YOU SURVIVE: you get unlimited oranges for life and you are teleported back home")
def kiwi():
    print("YOU SURVIVE: you get turned green permanently but the wizard helps you get home")
def dragonfruit():
    print("ENDING: you are cursed to guard the forests dragon fruit forever.")
def forest_path():
    print("you get lost and realize your going in circles, A wizard approaches you and says 4 magic fruit will help or harm you, you agree since you dont have any hope")
    print("1: A mango ")
    print("2. An orange ")
    print("3. A kiwi")
    print("4. A dragonfruit ")
    choice = input("> ")
    if choice == "1":
        mango()
    elif choice == "2":
        orange()
    elif choice == "3":
       kiwi()
    elif choice == "4":
        dragonfruit()
    else:
        print("Invalid choice. Try again.")
def creature_path():
    print("ENDING: a troll eats you")
def dark_path():
    print("ENDING: the monsters eat you")
def chicken():
    #pick between 4 paths to get home
    print("you safely make it for now.. you must now try to make it out of the forest, you see 4 paths before you.")
    print("1: A path shrouded in darkness")
    print("2. a path filled with trees and lush flora ")
    print("3. a path with faint sounds of creatures")
    print("4. a path underground")
    choice = input("> ")
    if choice == "1":
        forest_path()
    elif choice == "2":
        dark_path()
    elif choice == "3":
       creature_path()
    elif choice == "4":
        underground_path()
    else:
        print("Invalid choice. Try again.")


def glowing_fairy():
    print("YOU SURVIVE: The fairy helps you get to your house by using magic")
def piano():
    print("YOU SURVIVE, you get it correct and the lion helps you get home")
def book():
    print("ENDING: the lion eats you")
def house():
    print("ENDING: the lion leaves you in the unescapeable forest ")
def bottle():
    print("ENDING: The lion leaves you stranded")
def talking_lion():
    print("The talking lion will help you get back home if you solve his riddle, What has keys but cant open locks?.")
    print("1.A piano")
    print("2.A book")
    print("3.A house")
    print("4.A bottle")
    choice = input("> ")
    if choice == "1":
        piano()
    elif choice == "2":
        book()
    elif choice == "3":
       house()
    elif choice == "4":
        bottle()
    else:
        print("Invalid choice. Try again.")
def talking_snake():
    print("ENDING: the snake turns out to be evil and betrays you, leading you to an unescapable forest")


def underground_cave():
    print("YOU SURVIVE:He finds his gold, the dragon flies you to your house")
def in_volcano():
    print("ENDING:His gold was not found,the dragon drops you in the volcano")
def in_palace():
    print("ENDING: His gold was not found, he leaves you with the evil queen who turns you into a frog.")
def on_island():
    print("ENDING: His gold was not found, he drops you in the ocean")
def dragon():
    print("the dragon will help you if you can tell him where is gold is, what do you say?")
    print("1.A cave in the ground")
    print("2.Inside a volcano")
    print("3.Inside a palace")
    print("4.On an island")
    choice = input("> ")
    if choice == "1":
        underground_cave()
    elif choice == "2":
        in_volcano()
    elif choice == "3":
       in_palace()
    elif choice == "4":
        on_island()
    else:
        print("Invalid choice. Try again.")
def stream():
    #player chooses a creature to help them
    print("your thirst is quenched, you must now try to make it out of the forest, you see 4 diffrent creatures that will either help or harm you.")
    print("1.A glowing fairy")
    print("2.A talking lion")
    print("3.A talking snake")
    print("4.A dragon")
    choice = input("> ")
    if choice == "1":
        glowing_fairy()
    elif choice == "2":
        talking_lion()
    elif choice == "3":
       talking_snake()
    elif choice == "4":
        dragon()
    else:
        print("Invalid choice. Try again.")
def pwd_1():
    print("CORRECT,You survive: the monster lets you go and you leave,behind the inn you see your home. you survive.")
def pwd_2():
    print("WRONG: you get disentragrated by the monster")
def pwd_3():
    print("WRONG: you get disentragrated by the monster")
def pwd_4():
    print("WRONG: you get disentragrated by the monster")
def haunted_inn():
    #player picks a password to avoid demise
    print(" there is a monster who will only spare you if you guess the answer right. which answer do you say?")
    print("1: 14124")
    print("2. password")
    print("3. watermelon")
    print("4.piggy09122020")
    choice = input("> ")
    if choice == "1":
        pwd_1()
    elif choice == "2":
        pwd_2()
    elif choice == "3":
       pwd_3()
    elif choice == "4":
        pwd_4()
    else:
        print("Invalid choice. Try again.")
def pie_inn():
    print("YOU SURVIVE: you eat pie and the people in the inn help you get back home")
def candy_inn():
    print("ENDING: A witch pushes you into her oven and eats you")
def ogre_inn():
    print("YOU SURVIVE: you eat some gruel and the ogres help you get home.")
def a_branch():
    #player picks an inn
    print("when you pull yourself up you see 4 inns. which do you choose?")
    print("1. an inn made of stone with smell of pie and lights are on")
    print("2. an inn made of candy")
    print ("3. an inn with ogres")
    print("4. a haunted inn")
    choice = input("> ")
    if choice == "1":
        pie_inn()
    elif choice == "2":
        candy_inn()
    elif choice == "3":
       ogre_inn()
    elif choice == "4":
        haunted_inn()
    else:
        print("Invalid choice. Try again.")




def drift_wood():
    print("you wash up in a new place with 4 new paths which do you choose?")
    print("1. an inn made of stone with smell of pie and lights are on")
    print("2. an inn made of candy")
    print ("3. an inn with ogres")
    print("4. a haunted inn")
    choice = input("> ")
    if choice == "1":
        pie_inn()
    elif choice == "2":
        candy_inn()
    elif choice == "3":
       ogre_inn()
    elif choice == "4":
        haunted_inn()
    else:
        print("Invalid choice. Try again.")




def a_rock():
    print("ENDING: your hand slips and you get thrown over the edge of the rapids.")
def random_hand():
    print("YOU SURVIVE: someone pulls you out and you make it back home")
def river():
    print("you get swept in and are carried down the river, what are you going to hold on to before you perish in the rapids? ")
    print("1. a random hand")
    print("2. a branch")
    print ("3. a rock")
    print("4. driftwood")
    choice = input("> ")
    if choice == "1":
        random_hand()
    elif choice == "2":
        a_branch()
    elif choice == "3":
       a_rock()
    elif choice == "4":
        drift_wood()
    else:
        print("Invalid choice. Try again.")




def metal_club():
    print("YOU SURVIVE: past the trees is your house ")
def fire_torch():
    print("ENDING: effective at first but then the fire goes out. does not work at all, troll obliterates you.")
def water_weapon():
    print("ENDING: the troll eats you")
def sword_weapon():
    print("YOU SURVIVE: past the trees is your house ")
def waterfall():
    print(" behind the waterfall you see a a new path, a  troll stands in you way, which weapon do you pick.")
    print("1. metal club")
    print("2. fire torch")
    print ("3. water gun")
    print("4. a sword")
    choice = input("> ")
    if choice == "1":
        metal_club()
    elif choice == "2":
        fire_torch()
    elif choice == "3":
       water_weapon()
    elif choice == "4":
        sword_weapon()
    else:
        print("Invalid choice. Try again.")
def pond():
    print("Ending: You drink the brain eating aboema and die")
def red_berry():
    print("Ending: you get poisoned")
def  old_fish():
    print("you somehow survive eating fish off the floor. You are now thristy, where do you go?")
    print("1.a nearby river")
    print("2. a stream")
    print ("3. a pond")
    print("4. a waterfall")
    choice = input("> ")
    if choice == "1":
        river()
    elif choice == "2":
        stream()
    elif choice == "3":
       pond()
    elif choice == "4":
        waterfall()
    else:
        print("Invalid choice. Try again.")
def narrow_path():
    print(" you go down the path and see 4 different foods")
    print("1. bright red berries")
    print("2. mushrooms")
    print ("3. chicken")
    print("4. a dead old fish")
    choice = input("> ")
    if choice == "1":
        red_berry()
    elif choice == "2":
        mushroom()
    elif choice == "3":
       chicken()
    elif choice == "4":
       old_fish()
    else:
        print("Invalid choice. Try again.")


#Wide path events
#say 12 options
def evil_witch():
	print("Ending: the evil witch turns you into a mouse")
def old_lady():
	print("ENDING The old lady is actually the evil queen and you get imprisoned in her dungeon for life")
def evil_palace():
	print("ending the evil queens gaurds throw you in dungeon")
#small village options
def egg_harbor():
	print( "YOU SURVIVE: You and the wizard make it home safely")
def shell_beach():
	print("ENDING you get taken by the sirens into the ocean")
def taco_shell():
    print("ENDING: The path is through the evil queens taco garden, the gaurds throw you in the dungeon")
def watermelon_way():
    print("ENDING: The water melon way is a dangerous path with strange acidic red water, you accidently fall in.")
def small_village():
    print("The villagers give you a map, you and the wizard journey but the final step is only a clue on where to go. All it says is: What has to be broken before you can use it?")
    print ("1. Egg harbor")
    print("2.shell (beach)")
    print("3.taco shell (path)")
    print("4.Watermelon (way)")
    choice = input("> ")
    if choice == "1":
        egg_harbor()
    elif choice == "2":
        shell_beach()
    elif choice == "3":
       taco_shell()
    elif choice == "4":
       watermelon_way ()
    else:
        print("Invalid choice. Try again.")
def troll_home():
    print("ENDING:the trolls attack you and the wizard")
def boat_rapids():
	print("ENDING:you and the wizard crash in the rapids")

def dwarf():
    print("ENDING: The dwarf steals all your stuff and abandons you in the unescapable forest.")

def a_wizard():
    print("The wizard will help you get back home with his magic, but neither of you know where to go exactly, you are faced with 4 options, which do you pick?")
    print("1. By the evil queens palace")
    print("2.through a small forest village")
    print ("3.through the trolls homes")
    print("4.through the rapids by boat")
    choice = input("> ")
    if choice == "1":
        evil_palace()
    elif choice == "2":
        small_village()
    elif choice == "3":
       troll_home()
    elif choice == "4":
       boat_rapids ()
    else:
        print("Invalid choice. Try again.")
#scary path options
def say_12():
    print("CORRECT: the goblin allows you to pass, when you pass the bridge you see 4 people that might help you or harm you.")
    print("1.An evil looking witch")
    print("2.An old lady")
    print ("3.A wizard")
    print("4.Dwarf")
    choice = input("> ")
    if choice == "1":
        evil_witch()
    elif choice == "2":
        old_lady()
    elif choice == "3":
      a_wizard()
    elif choice == "4":
       dwarf ()
    else:
        print("Invalid choice. Try again.")

def say_9():
    print("ENDING: wrong, the goblin feeds you to a dragon")
def say_1():
    print("ENDING: wrong, the goblin drops you into the radioactive water")
def say_2():
    print("ENDING: wrong, the goblin feeds you to a troll")

# wide path options
def viney_path():
    print("ENDING:the flowers release poisounus gas and you get poisouned")
def light_path():
    print("Ending: the light is the flames of a dragon, who incinerates you")
def troll_path():
    print("Ending:the trolls eat you for dinner")
def scary_path():
#goblin riddle
    print("The strange sounds are just the harmless birds, you evade death, you must now cross the bridge. There's a goblin guarding the bridge, he asks you a riddle. Riddle: How many months of the year have 28 days?")
    choice = input("> ")
    print("1.12 months")
    print("2.9 months")
    print ("3.1 month")
    print("4.2 months")
    if choice == "1":
        say_12()
    elif choice == "2":
        say_9()
    elif choice == "3":
       say_1()
    elif choice == "4":
       say_2()
    else:
        print("Invalid choice. Try again.")
def wide_path():
    # the harder level, wide path branch
    print("You have chosen the harder path, one wrong move and you will die, The smell of food is fake, you see many warning signs, when you turn back you dont see the place you began, you have 4 twisted scary paths, which do you choose")
    print("1. a path with vines but nice flowers")
    print("2. a scary path with strange sounds")
    print ("3. a path with light at the end of the path")
    print("4.a path that goes underground, trolls roaming around")
    choice = input("> ")
    if choice == "1":
        viney_path()
    elif choice == "2":
        scary_path()
    elif choice == "3":
       light_path ()
    elif choice == "4":
       troll_path()
    else:
        print("Invalid choice. Try again.")
#start of the game
def start_adventure():
    print("survive the woods: you wake up in the forest, far from your house in the west of the forest, you see 2 paths, which path do you pick?")
    print("1. narrow path with lots of branches")
    print("2. wide clean paved path with the faraway smell of food ")
    choice = input("> ")

    if choice == "1":
        narrow_path()
    elif choice == "2":
       wide_path()
    else:
        print("Invalid choice. Try again.")
start_adventure()  









