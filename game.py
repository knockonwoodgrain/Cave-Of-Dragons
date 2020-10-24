import json

print("""
 ██████  █████  ██    ██ ███████      ██████  ███████     ██████  ██████   █████   ██████   ██████  ███    ██ ███████ 
██      ██   ██ ██    ██ ██          ██    ██ ██          ██   ██ ██   ██ ██   ██ ██       ██    ██ ████   ██ ██      
██      ███████ ██    ██ █████       ██    ██ █████       ██   ██ ██████  ███████ ██   ███ ██    ██ ██ ██  ██ ███████ 
██      ██   ██  ██  ██  ██          ██    ██ ██          ██   ██ ██   ██ ██   ██ ██    ██ ██    ██ ██  ██ ██      ██ 
 ██████ ██   ██   ████   ███████      ██████  ██          ██████  ██   ██ ██   ██  ██████   ██████  ██   ████ ███████ 
""")

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
    def __init__(
     self,
     health: int = 100,
     Stones: int = 0,
     Smokes: int = 0,
     Place: str = "Entrance",
     Screw: bool = False,
     Key: bool = False,
     RedKey: bool = False,
     GreenKey: bool = False,
     Firester: bool = False,
     Gryphon: bool = False,
     WoodenSword: bool = False,
     GoldenSword: bool = False) -> None:
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
        self.Firester = Firester
        self.GryphonKill = Gryphon
        self.WoodenSword = WoodenSword
        self.Place = Place
        self.GoldenSword = GoldenSword

    def Checkpointsave(self):
        checkpoint = open("checkpoint.json", "w")
        newfile = {
            "stones": 0,
            "screw": False,
            "smokes": 0,
            "key": False,
            "rkey": False,
            "gkey": False,
            "firester": False,
            "place" : "entrance",
            "wsword" : False,
            "gryphonkill" : False
        }
        try:
            newfile["stones"] = self.Stones
            newfile["screw"] = self.Screw
            newfile["smokes"] = self.Smokes
            newfile["key"] = self.Key
            newfile["rkey"] = self.RKey
            newfile["gkey"] = self.GKey
            newfile["firester"] = self.Firester
            newfile["place"] = self.Place
            newfile["wsword"] = self.WoodenSword
            newfile["gryphonkill"] = self.GryphonKill
        except KeyError:
            print("I tried man")
        checkpointjson = json.dumps(newfile)
        checkpoint.write(checkpointjson)
        checkpoint.close()
        ask = input("Do you want to quit?\n>")
        if ask.lower() in ("yes", "y"):
            print("quitting game, continue your quest later")
            exit()
        elif ask.lower() in ("no","n"):
            print("ok go back to the place where you were")
            if self.Place == "Entrance":
                self.Entrance()
            elif self.Place == "FireMonsterRoom":
                self.FireMonsterRoom()
            elif self.Place == "WoodenChestRoom" :
                self.WoodenChestRoom()
            elif self.Place == "Gryphon" :
                self.Gryphon()
            elif self.Place == "GuardRoom" :
                self.GuardRoom()
            elif self.Place == "GoldRoom" :
                self.GoldRoom()
            elif self.Place == "GrenadeRoom" :
                self.GrenadeRoom()

    def CheckpointLoad(self):
        savefile = input(
            "Do you want to load latest save file or start from new?\n1)Load save file-------1\n2)Start new "
            "game-------2\n>")
        if savefile == "1":
            print("loading save file")
            try:
                checkpoint = open("checkpoint.json", "r")
            except FileNotFoundError:
                print("Save file not found, making new file, please don't edit it")
                checkpoint1 = open("checkpoint.json", "w")
                newfile = {
                    "stones": 0,
                    "screw": False,
                    "smokes": 0,
                    "key": False,
                    "rkey": False,
                    "gkey": False,
                    "firester": False,
                    "wsword": False,
                    "gryphonkill" : False
                }
                checkpoint1json = json.dumps(newfile)
                checkpoint1.write(checkpoint1json)
                checkpoint1.close()
                checkpoint = open("checkpoint.json", "r")
            data = checkpoint.read()
            dictt = json.loads(data)
            try:
                self.Stones = dictt["stones"]
                self.Screw = dictt["screw"]
                self.Smokes = dictt["smokes"]
                self.Key = dictt["key"]
                self.RKey = dictt["rkey"]
                self.GKey = dictt["gkey"]
                self.Firester = dictt["firester"]
                self.WoodenSword = dictt["wsword"]
                self.GryphonKill = dictt["gryphonkill"]
                if dictt["place"] == "Entrance" :
                    self.Entrance()
                elif dictt["place"] == "FireMonsterRoom" :
                    self.FireMonsterRoom()
                elif dictt["place"] == "WoodenChestRoom" :
                    self.WoodenChestRoom()
                elif dictt["place"] == "Gryphon" :
                    self.Gryphon()
                elif dictt["place"] == "GuardRoom" :
                    self.GuardRoom()
                elif dictt["place"] == "GoldRoom" :
                    self.GoldRoom()
                elif dictt["place"] == "GrenadeRoom" :
                    self.GrenadeRoom()
            except KeyError:
                print("Little Boy tried to hack :D")

        elif savefile == "2":
            while True:
                ask = input("Do you really wanna do that all your progress will be lost\n>")
                if ask.lower() in ("yes","y"):
                    self.Entrance()
                elif ask.lower() in ("no","n"):
                    print("ok then start the game again")
                    input("")
                    break
                else:
                    print("that isn't yes or no, so put it again")
                    continue

    def Decode(self, x):
        if not x:
            print("you have to put something")
            self.Verb = " "
            self.Obj = " "
            self.Obj2 = " "
        elif x:
            words = x.split(" ")
            if 'to' in words:
                words.remove('to')
            elif 'towards' in words:
                words.remove('towards')
            elif len(words) >= 2:
                self.Verb = words[0]
                self.Obj = words[1]
                if len(words) >= 3:
                    self.Obj2 = words[2]
            elif len(words) == 1:
                self.Verb = words[0]
            else:
                print("I cant really decode that, please write one to three words")

    def damage(self, dmg: int = 5) -> None:
        self.health -= dmg

    def GrenadeRoom(self) -> None:
        print('Grenade Room')
        print(
            'You have entered the Grenade room it has a lot of \ngrenades lots of them sprawled on the floor boxes '
            '\nfull of them but you don\'t have the knowledge to \nuse then you can only use the \nsmoke grenades '
            'there are five of them in front of you')
        self.Place = "GrenadeRoom"
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() in ("take", "t") and self.Obj == "smokes" or self.Obj == "grenades":
                print('You have taken the smoke grenades, you can use them to skip fighting from monsters of you don\'t want to')
                self.Smokes = 5
            elif self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map":
                print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory":
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements":
                self.Achievements()
            elif self.Verb == " " and self.Obj == " " and self.Obj2 == " ":
                continue
            else:
                self.UnidentifiedInput()

    def Gryphon(self) -> None:
        print('Gryphon Room')
        self.Place = "Gryphon"
        if self.Screw:
            print(
                '' + 'The room has broken down now, the enchanted sword takes you to the gold room, you cannot access '
                     'this room')
            self.GoldRoom()  # !NOTE:imp: [TO Make as Method]
        elif  not self.Screw:
            print('you have entered the gryphon room\nHere there is a gryphon\ndo you want to fight him?')
            while True:
                x = input(">")
                self.Decode(x)
                if self.Verb.lower() in ("no", "n"):
                    if self.GryphonKill:
                        print("Doesn't matter he is already dead, the cave smells of his ruins")
                    elif not self.GryphonKill:
                        print("you have chosen not to fight him, what a dumbass, dude you have to fight him aight")
                elif self.Verb.lower() in ("yes", "y"):
                    if self.GryphonKill:
                        print("Doesn't matter he is already dead, the cave smells of his ruins")
                    elif not self.GryphonKill:
                        if self.WoodenSword:
                            print("Okay you fought him and won")
                            print("Now you have the screw which opens the screwchest in wooden  chest room")
                            self.Screw = True
                            self.GryphonKill = True
                        elif not self.WoodenSword:
                            print("you don't have the golden sword so you lost and died")
                elif self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map":
                    print(Map)
                elif self.Verb.lower() == "quit" or self.Obj.lower() == "quit":
                    self.Checkpointsave()
                elif self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory":
                    self.Inventory()
                elif self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements":
                    self.Achievements()
                elif (self.Verb.lower() == "go" and self.Obj.lower() in ("west", "w")) or (self.Verb.lower() == "west"):
                    self.GoldRoom()
                elif (self.Verb.lower() == "go" and self.Obj.lower() in ("south", "s")) or (self.Verb.lower() == "south"):
                    print("there is a wall here") 
                elif self.Verb.lower() in ("go", "north") and self.Obj.lower() in ("north", "n"):
                    print("there is a wall here")   
                elif (self.Verb.lower() == "go" and self.Obj.lower() in ("east", "e")) or (self.Verb.lower() == "east"): 
                    print("there is a wall here")
                elif self.Verb == " " and self.Obj == " " and self.Obj2 == " ":
                    continue
                else:
                    self.UnidentifiedInput()

    def GoldRoom(self):
        print('GoldRoom')
        print(
            'You have entered the gold room\nevery thing is made of gold\non a podium an enchanted wooden sword '
            'floats\nclaim the sword')
        self.Place = "GoldRoom"
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() in ("take", "t", "claim") and self.Obj.lower() == "sword":
                if not self.WoodenSword:
                    print('You now have the sword')
                    self.WoodenSword = True
                elif self.WoodenSword:
                    print("You already have the sword")
            elif self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map":
                    print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory":
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements":
                self.Achievements()
            elif self.Verb.lower() in ("go", "g") and self.Obj.lower() in ("s", "south"):
                if self.GKey == True:
                    self.WoodenChestRoom()
                elif self.GKey == False:
                    print('you don\'t have the green key card\nit is in the guardroom')
            elif self.Verb.lower() in ("go", "g") and self.Obj.lower() in ("e", "east"): 
                if self.GKey == True:
                    self.Gryphon() 
                elif self.GKey == False:
                    print('you don\'t have the green key card\nit is in the guardroom')   
            elif self.Verb.lower() in ("go", "g") and self.Obj.lower() in ("n", "north"):
                print(self.GKey)
                if self.GKey == True:
                    self.GrenadeRoom() 
                elif self.GKey == False:
                    print('you don\'t have the green key card\nit is in the guardroom')
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("west", "w")) or (self.Verb.lower() == "west"):
                print("there is a wall here")
            elif self.Verb == " " and self.Obj == " " and self.Obj2 == " ":
                continue
            else :
                self.UnidentifiedInput()

    def GuardRoom(self):
        print('Guard Room')
        print(
            'There is a big guard dragon in front of you\nyou do not have the power to defeat him\nyou can distract '
            'him with \'throwing\' stones\nhe sits on a desk it has a drawer\nthe drawer has the red and green key '
            'card')
        self.Place = "GuardRoom"
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() in ("throw", "use") and self.Obj.lower() in "stones":
                if self.RKey == True and self.GKey == True:
                    print("You already have the keys dumbass")
                elif self.RKey == False and self.GKey == False:
                    if self.Stones == 5:
                        print("so you want to distract the guard?")
                        x = input(">")
                        self.Decode(x)
                        if self.Verb.lower() in ('y', "yes"):
                            print('The guard is now distracted\ngo to the drawer')
                            x = input(">")
                            self.Decode(x)
                            if self.Verb.lower() in ("go", "drawer") and self.Obj.lower() in ("to", "drawer") and self.Obj2 == "drawer":
                                print(
                                    'you have reached the drawer \nit consists of a red and green key card\nyou take '
                                    'them')
                                self.RKey = True
                                self.GKey = True
                            else:
                                print('you cannot do that probably, or you phrased it wrong, now distract him again')
                        elif self.Verb.lower() in ("no", "n"):
                            print(
                                'you cannot defeat him, now he \nhas come back near the drawer \nyou will have to '
                                'throw the stone again')
                    elif not self.Stones:
                        print('you don\'t have the stones\ngo to the entrance to get the stones')
            elif self.Verb.lower() in ("go", "g") and self.Obj.lower() in ("west", "w"):
                self.WoodenChestRoom()  # NOTE make this a method
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("south", "s")) or (self.Verb.lower() == "south"):
                print("there is a wall here")
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("north", "n")) or (self.Verb.lower() == "north"):
                print("there is a wall here")
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("east", "e")) or (self.Verb.lower() == "east"):
                print("there is a wall here")
            elif self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map":
                print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory":
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements":
                self.Achievements()
            elif self.Verb == " " and self.Obj == " " and self.Obj2 == " ":
                continue
            else:
                self.UnidentifiedInput()

    def WoodenChestRoom(self):
        print('Wooden Chest Room')
        print(
            'you have entered the Wooden Chest Room\nthere are a lot of chests there which are locked shut\nthere is '
            'one chest known as screwchest which\ncan be opened, there is a scroll on the screwchest\nthere is a door '
            'in the east which says guard room\nand a gold door in the north')
        self.Place = "WoodenChestRoom"
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() in ("take", "scroll") and self.Obj.lower() == "scroll":
                print('you have the scroll, if you want to read it then put read scroll')
            elif self.Verb.lower() in ("read", "r") and self.Obj.lower() == "scroll":
                print(
                    'the scroll says the following:\nAdventurer find the gryphon kill him and get the tools \nit '
                    'posseses one of them can open the screwchest\nYou keep the scroll back')
            elif self.Verb.lower() in ("open", "o") and self.Obj.lower() == "screwchest":
                if self.Screw:
                    print('It has a golden sword \nyou have now taken the golden sword')
                    self.GoldenSword = True
                elif not self.Screw:
                    print('First get the screwdriver, which the gryphon has')
            elif self.Verb.lower() in ("go", "east") and self.Obj.lower() == "east":
                self.GuardRoom()  # NOTE use this as a method
            elif self.Verb.lower() in ("go", "north") and self.Obj.lower() in ("north", "n"):
                if self.RKey:
                    self.GoldRoom()
                elif not self.RKey:
                    print('You need a red key card')
            elif self.Verb.lower() in ("go", "south") and self.Obj.lower() in ("south", "s"):
                self.Entrance()
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("west", "w")) or (self.Verb.lower() == "west"):
                print("there is a wall here")
            elif self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map":
                print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory":
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements":
                self.Achievements()
            elif self.Verb == " " and self.Obj == " " and self.Obj2 == " ":
                continue
            else:
                self.UnidentifiedInput()

    def FireMonsterRoom(self):
        print('Fire Monster Room:')
        print(
            'you have entered the "firester" room where the great firester is\nhe has a secret, if you hit him with '
            'your hands you can easily\ndefeat him')
        self.Place =  "FireMonsterRoom"
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() in ("kill", "hit") and self.Obj.lower() in ("firester", "him"):
                if not self.Firester:
                    print('you defeated the fire monster, it leaves a key , take it to open the chest in entrance')
                    self.Firester = True
                x = input(">")
                self.Decode(x)
                if self.Verb.lower() in ("take", "t") and self.Obj.lower() in "key":
                    if self.Key:
                        print("You already have the key")
                    elif not self.Key:
                        print('key taken')
                    self.Key = True
            elif self.Verb.lower() in ("go", "north") and self.Obj.lower() in ("north", "n"):
                print('there is a wall here')
            elif self.Verb.lower() in ("go", "south") and self.Obj.lower() in ("south", "s"):
                print('there is a wall here')
            elif self.Verb.lower() in ("go", "east") and self.Obj.lower() in ("east", "e"):
                print('there is a wall here')
            elif self.Verb.lower() in ("go", "west") and self.Obj.lower() in ("west", "w"):
                self.Entrance()
            elif self.Verb.lower() in ("show", "map") and self.Obj.lower() in "map":
                print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "show") and self.Obj.lower() in "inventory":
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "show") and self.Obj.lower() in "achievements":
                self.Achievements()
            elif self.Verb == " " and self.Obj == " " and self.Obj2 == " ":
                continue
            elif self.Firester:
                print("He is already dead")
                self.Firester = True
                break
            else:
                self.UnidentifiedInput()

    def Entrance(self):
        print("If you want, Put map and the map will appear")
        print('The Entrance:')
        print(
            'you have entered the entrance of a mighty cave \nyou see a chest on the floor \nsome stones and an empty '
            'bookshelf\nthere are doors in the east and in the north')
        self.Place = "Entrance"
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() in "take" and self.Obj.lower() in "stones":
                if self.Stones == 5:
                    print('you already have the stones')
                elif self.Stones == 0:
                    self.Stones = 5
                    print("stones taken")
            elif self.Verb.lower() in "open" and self.Obj.lower() in "chest":
                if not self.Key:
                    print('cannot open chest, fire monster has the key')
                elif self.Key:
                    print('Chest consists of a iron knife , you take the knife')
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("north", "n")) or (self.Verb.lower() in "north"):
                self.WoodenChestRoom()
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("east", "e")) or (self.Verb.lower() in "east"):
                self.FireMonsterRoom()
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("west", "w")) or (self.Verb.lower() in "west"):
                print("there is a wall here")
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("south", "s")) or (self.Verb.lower() in "south"):
                print("there is a wall here")
            elif self.Verb.lower() == "show" and self.Obj.lower() == "map":
                print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "show", "inv") and self.Obj.lower() == "inventory":
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "show", "ach") and self.Obj.lower() == "achievements":
                self.Achievements()    
            elif self.Verb == " " and self.Obj == " " and self.Obj2 == " ":
                continue    
            else:
                self.UnidentifiedInput()
    def Inventory(self):
        if self.Stones == 5:
            print("5 stones")
        if self.Screw:
            print("Screw")
        if self.Smokes == 5:
            print("5 smokes")
        if self.Key:
            print("key")
        if self.RKey:
            print("Red Key")
        if self.GKey:
            print("Green Key")
        if self.WoodenSword:
            print("Wooden sword")
    
    def Achievements(self):
        if self.GryphonKill:
            print("Its a lion!, it's an eagle!, it's Gryphon!:\nKill Gryphon")
        if self.Firester:
            print("Extinguished:\nKill Firester")
        if self.GKey:
            print("Who throw the stone?:\nDistract guard")
    
    def UnidentifiedInput(self):
        if self.Verb.lower() == "nice" and self.Obj.lower() in ("man", "dude", "bitch", "dude","man", "girl", "boi", "bro", "one") or (self.Verb.lower() == "lmao"):
            print("yeah very nice")
            print("niceeeee" + self.Obj.lower())
        elif self.Verb.lower() == "lmao":
            print("lmao nice")
        elif self.Verb.lower() == "yea" and self.Obj.lower() == "boi":
            print("yea boii")
        elif self.Verb.lower() in ("ok","hmm","k","ya","yes","oof","ew","no","yeah","aight","alright","hmmm","hmmm","never"):
            print("whatev idc")
        elif self.Verb.lower() in ("idc","idk"):
            print("you should")
        elif self.Verb.lower() in ("what", "wut", "what?", "wht?", "?"):
            print("idk dude figure it out,(dude is unisex)")
        elif self.Verb.lower() in ("fuck","hate","you","suck","are","dumb","donkey","bitch","motherfucker","whore","dick","cunt","pussy", "dumbass") and self.Obj.lower() in ("you","fuck","suck","are","dumb","donkey","bitch","motherfucker","whore","dick","cunt","pussy", "dumbass"):
            print("stop being offensive")
            i = 100
            while i >= 1:
                print("game crash motherfucker")
                i -= 1
                print("haahahahaahahaha")
        elif self.Verb.lower() in ("go", "g") and self.Obj.lower() not in ('east','west','north', 'south'):
            print("damn check your spellings")
        elif self.Verb.lower() == "pewdiepie":
            print("how's it goin bros my name is PewDiePie")
        elif self.Verb.lower() == "pls":
            print("i am not dank enough")
        elif self.Verb.lower() == "lmao" and self.Verb.lower() == "ded":
            print("(outro music plays)")
        elif self.Verb.lower() == ("wassup","whadup","sup","yo","hey", "hi", "hello", "yea"):
            if self.Obj.lower() == ("bitch", "dude","man", "girl", "boi", "bro"):
                print("yo")
        elif self.Verb == " " and self.Obj == " " and self.Obj2 == " ":
            print("ok")
        else:
            print(self.Verb + "?")
            if self.Place == "GrenadeRoom":
                print("put take smokes")
            elif self.Place == "Gryphon":
                print("do ou wanna fight him or not??")

if __name__ == "__main__": 
  starts = Player()
  starts.CheckpointLoad()
