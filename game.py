Title = """
 _______  _______           _______    _______  _______    ______   _______  _______  _______  _______  _        _______
(  ____ \\(  ___  )|\\     /|(  ____ \\  (  ___  )(  ____ \\  (  __  \\ (  ____ )(  ___  )(  ____ \\(  ___  )( (    /|(  ____ \\
| (    \\/| (   ) || )   ( || (    \\/  | (   ) || (    \\/  | (  \  )| (    )|| (   ) || (    \\/| (   ) ||  \\  ( || (    \\/
| |      | (___) || |   | || (__      | |   | || (__      | |   ) || (____)|| (___) || |      | |   | ||   \\ | || (_____
| |      |  ___  |( (   ) )|  __)     | |   | ||  __)     | |   | ||     __)|  ___  || | ____ | |   | || (\\ \\) |(_____  )
| |      | (   ) | \\ \\_/ / | (        | |   | || (        | |   ) || (\\ (   | (   ) || | \\_  )| |   | || | \\   |      ) |
| (____/\\| )   ( |  \\   /  | (____/\\  | (___) || )        | (__/  )| ) \\ \\__| )   ( || (___) || (___) || )  \\  |/\\____) |
(_______/|/     \\|   \\_/   (_______/  (_______)|/(______/ |/   \\__/|/     \|(_______)(_______)|/    )_)\\_______)"""


Map = """
    +---------+
    |Grenade  |
    |Room     |
    +---------+  
        | |
    +---------+       +-------------------+
    |Gold Room|=======|           Room    |
    +---------+       |           Of      |
        | |           +---------+ Gryphon |
    +---------+                 |         |
    |Wooden   |   +--------+    |         |
    |Chest    |===|Guard   |====|         |
    | Room    |   |Room    |    |         |
    +---------+   +--------+    +---------+
        | |
    +-----------+         +--------------+
    | Entrance  |=========| Fire Monster |
    +-----------+         +--------------+
"""

class Player:
    def __init__(self, health: int = 100, Stones: int = 0, Smokes: int = 0, Screw: bool = False, Key: bool = False, RedKey: bool = False, GreenKey: bool = False) -> None:
        self.health = health
        self.Stones = Stones
        self.Smokes = Smokes
        self.Screw = Screw
        self.Key = Key
        self.RKey = RedKey
        self.GKey = GreenKey
        self.x = ""
        self.Verb = ""
        self.Obj2 = ""
        self.Obj = ""

    def Decode(self, x):
        words = x.split(" ")
        if 'to' in words :
            words.remove('to')
        elif 'towards' in words :
            words.remove('towards')
        elif len(words) >= 2 :
            self.Verb = words[0]
            self.Obj = words[1]
            if len(words) >= 3 :
                self.Obj2 = words[2]
        elif len(words) == 1:
            self.Verb = words[0]
        else:
            print("I cant really decode that, please write one to three words")

    def damage(self, dmg: int = 5) -> None:
        self.health -= dmg

    def GrenadeRoom(self) -> None:
        print('\033[1m' + 'Grenade Room' + '\033[1m')
        print('You have entered the Grenade room it has a lot of \ngrenades lots of them sprawled on the floor boxes \nfull of them but you don\'t have the knowledge to \nuse then you can only use the \nsmoke grenades there are five of them in front of you')
        x = input(">")
        self.Decode(x)
        if self.Verb.lower() == "take" or self.Verb.lower() == "t" and self.Obj == "smokes" or self.Obj == "grenades":
            print('You have taken the smoke grenades you can use them to skip fighting from monsters of you dont want to')
        elif self.Verb.loewr() == "show" or self.Verb.lower() == "map" and self.Obj.lower() == "map":
                print(Map)
        else :
            print('I don\'t know what you typed but it\'s not take smokes, so anyway you take them\nnow you have five smokes you can use them to skip fight\'s')

    def Gryphon(self) -> None:
        print('\033[1m' + 'Gryphon Room')
        if self.Screw:
            print('\033[0m' + 'you have entered the gryphon room\nHere there is a gryphon\ndo you want to fight him?')
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() == "no" or self.Verb.lower() == "n":
                print("you have chosen not to fight him, what a dumbass, dude you have to fighthim aight")
            elif self.Verb.lower() == "yes" or self.Verb.lower() == "y":
                print("Okay you fought him and won, because you have the sword, right?")
            elif self.Verb.lower() == "show" or self.Verb.lower() == "map" and self.Obj.lower() == "map":
                print(Map)
            else:
                print("My dumb code couldn't really understand the thing you wrote, just write yes or no")
        elif not self.Screw:
            print('\033[0m' + 'The room has broken down now, the enchanted sword takes you to the gold room,you cannot accses this room')
            self.GoldRoom() # !NOTE:imp: [TO Make as Method]

    def GoldRoom(self):
        print('\033[1m' + 'GoldRoom')
        print('\033[0m' + 'You have entered the gold room\nevery thing is made of gold\non a podium an enchanted wooden sword floats\nclaim the sword')
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() == "take" or self.Verb.lower() == "t" and self.Obj.lower() == "sword":
                print('you now have the sword')
            elif self.Verb.lower() == "go" or self.Verb.lower() == "g":
                if self.GKey:
                    if self.Verb.lower() == "s" or self.Verb.lower() == "south":
                        self.WoodenChestRoom()
                    elif self.Verb.lower() == "e" or self.Verb.lower() == "east":
                        self.Gryphon() # NOTE:imp:make this a method
                        print("Still in development")
                    elif self.Verb.lower() == "n" or self.Verb.lower() == "north":
                        self.GrenadeRoom() #NOTE:imp:make this a method
                        print("Still in development")
                    elif self.Verb.lower() == "show" or self.Verb.lower() == "map" and self.Obj.lower() == "map":
                        print(Map)
                    else:
                        print('just put take sword(If you dont have it)\nyou can only go south,east and north')
                elif not self.Gkey:
                    print('you dont have the green key card\nit is in the guardroom')

    def GuardRoom(self):
        print('\033[1m' + 'Guard Room')
        print('\033[0m' + 'There is a big guard dragon in front of you\nyou do not have the power to defeat him\nyou can distract him with \'throwing\' stones\nhe sits on a desk it has a drawer\nthe drawer has the red and green key card')
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() == "throw" or self.Verb.lower() == "use" and self.Obj.lower() == "stones":
                if self.Stones:
                    x = input(">")
                    self.Decode(x)
                    if self.Verb.lower() == 'y' or self.Verb.lower() == "yes":
                        print('The guard is now distracted\ngo to the drawer')
                        x = input(">")
                        self.Decode(x)
                        if self.Verb.lower() == "go" or self.Verb.lower() == "drawer" and self.Obj.lower() == "to" or self.Obj.lower() == "drawer"and self.Obj2 == "drawer":
                            print('you have reached the drawer \nit consists of a red and green key card\nyou take them')
                            self.RKey = True
                            self.Gkey = True
                        else:
                            print('you cannot do that now distract him again')
                    elif self.Verb.lower() == "no" or self.Verb.lower() == "n":
                        print('you cannot defeat him, now he \nhas come back near the drawer \nyou will have to throw the stone again')
                elif not self.Stones:
                    print('you dont have the stones\ngo to the entrance to get the stones')
            elif self.Verb.lower() == "go" and self.Verb.lower() == "g" and self.Obj.lower() == "west" or self.Obj.lower() == "w":
                self.WoodenChestRoom()#NOTE make this a method
                print("still in development")
            elif self.Verb.lower() == "show" or self.Verb.lower() == "map" and self.Obj.lower() == "map":
                print(Map)
            else :
                print('you cannot do that')

    def WoodenChestRoom(self):
        print('\033[1m' + 'Wooden Chest Room')
        print('\033[0m' + 'you have entered the Wooden Chest Room\nthere are a lot of chests there which are locked shut\nthere is one chest known as screwchest which\ncan be opened, there is a scroll on the screwchest\nthere is a door in the east which says guard room\nand a gold door in the north')
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() == "take" or self.Verb.lower() == "scroll" and self.Obj.lower() == "scroll":
                print('you have the scroll, if you want to read it then put read scroll')
            elif self.Verb.lower() == "read" or self.Verb.lower() == "r" and self.Obj.lower() == "scroll":
                print('the scroll says the following:\nAdventurer find the gryphon kill him and get the tools \nit posseses one of them can open the screwchest')
            elif self.Verb.lower() == "open" or self.Verb.lower() == "o" and self.Obj.lower() == "screwchest":
                if not self.Screw:
                    print('you open the chest\n it has a golden sword \nyou have now taken the golden sword')
                elif self.Screw:
                    print('first get the screwdriver, which the gryphon has')
            elif self.Verb.lower() == "go" or self.Verb.lower() == "east" and self.Obj.lower() == "east":
                self.GuardRoom()#NOTE use this as a method
                print("Still in development")
            elif self.Verb.lower() == "go" or self.Verb.lower() == "north" and self.Obj.lower() == "north" or self.Obj.lower() == "n":
                if not self.RKey:
                    self.GoldRoom()
                elif self.RKey:
                    print('You need a red key card')
            elif self.Verb.lower() == "go" or self.Verb.lower() == "south" and self.Obj.lower() == "south" or self.Obj.lower() == "s":
                self.Entrance()
            elif self.Verb.lower() == "show" or self.Verb.lower() == "map" and self.Obj.lower() == "map":
                print(Map)
            else :
                print('My Dumb code cannot understand what you mean to say so please reframe it')


    def FireMonsterRoom(self):
        print('\033[1m' + 'Fire Monster Room:')
        print('\033[0m' + 'you have entered the "firester" room where the great firester is\nhe has a secret, if you hit him with your hands you can easyly\ndefeat him')
        while True :
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() == "kill" or self.Verb.lower() == "hit" and self.Obj.lower() == "him" or self.Obj.lower() == "firester" :
                print('you defeated the fire monster, it leaves a key , take it to open the chest in entrance')
                x = input(">")
                self.Decode(x)
                if self.Verb.lower() == "take" or self.Verb.lower() == "t" and self.Obj.lower() == "key":
                    print('key taken')
                    self.Key = True
            elif self.Verb.lower() == "go" or self.Verb.lower() == "north" and self.Obj.lower() == "north" or self.Obj.lower() == "n":
                print('there is a wall here')
            elif self.Verb.lower() == "go" or self.Verb.lower() == "south" and self.Obj.lower() == "south" or self.Obj.lower() == "s":
                print('there is a wall here')
            elif self.Verb.lower() == "go" or self.Verb.lower() == "east" and self.Obj.lower() == "east" or self.Obj.lower() == "e":
                print('there is a wall here')
            elif self.Verb.lower() == "go" or self.Verb.lower() == "west" and self.Obj.lower() == "west" or self.Obj.lower() == "w":
                self.Entrance()
            elif self.Verb.lower() == "show" or self.Verb.lower() == "map" and self.Obj.lower() == "map":
                print(Map)
            else :
                print('You cannot do that')

    def Entrance(self):
        print(Title)
        print("\033[1m" + "If you want, Put map and the map will appear")
        print('\033[1m' + 'The Entrance:' + '\033[0m')
        print('you have entered the entrance of a mighty cave \nyou see a chest on the floor \nsome stones and an empty bookshelf\nthere are doors in the east and in the north')
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() == "take" or self.Verb.lower() == "t" and self.Obj.lower() == "stones":
                print('stones taken')
            elif self.Verb.lower() == "open" or self.Verb.lower() == "o" and self.Obj.lower() == "chest":
                if self.Key:
                    print('cannot open chest, fire monster has the key')
                elif not self.Key:
                    print('chest opened, it consists of a iron knife , you take the knife')
            elif self.Verb.lower() == "go" or self.Verb.lower() == "north" and self.Obj.lower() == "north" or self.Obj.lower() == "n":
                self.WoodenChestRoom()
            elif self.Verb.lower() == "go" or self.Verb.lower() == "east" and self.Obj.lower() == "east" or self.Obj.lower() == "e":
                self.FireMonsterRoom()
            elif self.Verb.lower() == "show" or self.Verb.lower() == "map" and self.Obj.lower() == "map":
                print(Map)
            else :
                print('My Dumb Code Cannot Understand What You Wrote So LMAO')

starts = Player(100, 0,  0, False, False, False, False)
starts.Entrance()