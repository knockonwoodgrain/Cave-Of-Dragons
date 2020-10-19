from json.decoder import JSONDecodeError
from os import error
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
    def __init__(self, health: int = 100, Stones: int = 0, Smokes: int = 0, Screw: bool = False, Key: bool = False, RedKey: bool = False, GreenKey: bool = False, Firester: bool = False) -> None:
        self.health = health
        self.Stones = Stones
        self.Smokes = Smokes
        self.Screw = Screw
        self.Key = Key
        self.RKey = RedKey
        self.GKey = GreenKey
        self.x  = ""
        self.Verb = ""
        self.Obj2  = ""
        self.Obj  = ""
        self.Firester = Firester
    
    def Checkpointsave(self):
        checkpoint = open("checkpoint.json", "w")
        newfile = {
            "stones" : 0,
            "screw" : False,
            "smokes" : 0,
            "key" : False,
            "rkey" : False,
            "gkey" : False,
            "firester" : False
        }
        try :
            newfile["stones"] = self.Stones
            newfile["screw"] = self.Screw
            newfile["smokes"] = self.Smokes
            newfile["key"] = self.Key
            newfile["rkey"] = self.RKey
            newfile["gkey"] = self.Gkey
            newfile["firester"] =self.Firester
        except KeyError :
            print("I tried man")
        print(self.Key)
        checkpointjson = json.dumps(newfile)
        checkpoint.write(checkpointjson)
        checkpoint.close()

    def CheckpointLoad(self):
        savefile = input("Do you want to load latest save file or start from new?\n1)Load save file-------1\n2)Start new game-------2\n>")
        if savefile == "1" :
            print("loading save file")
            try :
                checkpoint = open("checkpoint.json", "r")
            except FileNotFoundError :
                print("Save file not found, making new file, please don't edit it")
                checkpoint1 = open("checkpoint.json", "w")
                newfile = {
                    "stones" : 0,
                    "screw" : False,
                    "smokes" : 0,
                    "key" : False,
                    "rkey" : False,
                    "gkey" : False,
                    "firester" : False
                }
                checkpoint1json = json.dumps(newfile)
                checkpoint1.write(checkpoint1json)
                checkpoint1.close()
                checkpoint = open("checkpoint.json", "r")
            data = checkpoint.read()
            dict = json.loads(data)
            print(dict)
            try:
                self.Stones = dict["stones"]
                self.Screw = dict["screw"]
                self.Smokes = dict["smokes"]
                self.Key = dict["key"]
                self.RKey = dict["rkey"]
                self.Gkey = dict["gkey"]
                self.Firester = dict["firester"]
            except KeyError:
              print("Little Boy tried to hack :D")
            self.Entrance()
            
        elif savefile == "2" :
            print("starting new game")
            self.Entrance()

    def Decode(self,x):
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
        if self.Verb.lower() in ("take" , "t") and self.Obj in "smokes" or self.Obj in "grenades":
            print('You have taken the smoke grenades you can use them to skip fighting from monsters of you dont want to')
        elif self.Verb.loewr() in ("show" , "map") and self.Obj.lower() in "map":
                print(Map)
        elif self.Verb.lower() in ("quit"):
                self.Checkpointsave()
        else :
            print('I don\'t know what you typed but it\'s not take smokes, so anyway you take them\nnow you have five smokes you can use them to skip fight\'s')

    def Gryphon(self) -> None:
        print('\033[1m' + 'Gryphon Room')
        if self.Screw:
            print('\033[0m' + 'you have entered the gryphon room\nHere there is a gryphon\ndo you want to fight him?')
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() in ("no" , "n"):
                print("you have chosen not to fight him, what a dumbass, dude you have to fighthim aight")
            elif self.Verb.lower() in ("yes" , "y"):
                print("Okay you fought him and won, because you have the sword, right?")
            elif self.Verb.lower() in ("show" , "map") and self.Obj.lower() in "map":
                print(Map)
            elif self.Verb.lower() in ("quit"):
                self.Checkpointsave()
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
            if self.Verb.lower() in ("take", "t") and self.Obj.lower() in "sword":
                print('you now have the sword')
            elif self.Verb.lower() in ("go", "g"):
                if self.GKey:
                    if self.Verb.lower() in ("s", "south"):
                        self.WoodenChestRoom()
                    elif self.Verb.lower() in ("e", "east"):
                        self.Gryphon() # NOTE:imp:make this a method
                        print("Still in development")
                    elif self.Verb.lower() in ("n", "north"):
                        self.GrenadeRoom() #NOTE:imp:make this a method
                        print("Still in development")
                    elif self.Verb.lower() in ("show", "map") and self.Obj.lower() in "map":
                        print(Map)
                    elif self.Verb.lower() in ("quit"):
                        self.Checkpointsave()
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
            if self.Verb.lower() in ("throw" , "use") and self.Obj.lower() in "stones":
                if self.RKey == True and self.GKey == True :
                    print("You already have the keys dumbass")
                elif self.RKey == False and self.GKey == False :
                    if self.Stones == 5:
                        print("so you want to distract the guard?")
                        x = input(">")
                        self.Decode(x)
                        if self.Verb.lower() in ('y', "yes"):
                            print('The guard is now distracted\ngo to the drawer')
                            x = input(">")
                            self.Decode(x)
                            if self.Verb.lower() in ("go", "drawer") and self.Obj.lower() in ("to", "drawer") and self.Obj2 in "drawer":
                                print('you have reached the drawer \nit consists of a red and green key card\nyou take them')
                                self.RKey = True
                                self.Gkey = True
                            else:
                                print('you cannot do that now distract him again')
                        elif self.Verb.lower() in ("no", "n"):
                            print('you cannot defeat him, now he \nhas come back near the drawer \nyou will have to throw the stone again')
                    elif not self.Stones:
                        print('you dont have the stones\ngo to the entrance to get the stones')
            elif self.Verb.lower() in ("go", "g") and self.Obj.lower() in ("west" , "w"):
                self.WoodenChestRoom()#NOTE make this a method
                print("still in development")
            elif self.Verb.lower() in ("show", "map") and self.Obj.lower() in "map":
                print(Map)
            elif self.Verb.lower() in ("quit"):
                self.Checkpointsave()
            else :
                print('you cannot do that')

    def WoodenChestRoom(self):
        print('\033[1m' + 'Wooden Chest Room')
        print('\033[0m' + 'you have entered the Wooden Chest Room\nthere are a lot of chests there which are locked shut\nthere is one chest known as screwchest which\ncan be opened, there is a scroll on the screwchest\nthere is a door in the east which says guard room\nand a gold door in the north')
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() in ("take", "scroll") and self.Obj.lower() in "scroll":
                print('you have the scroll, if you want to read it then put read scroll')
            elif self.Verb.lower() in ("read", "r") and self.Obj.lower() in "scroll":
                print('the scroll says the following:\nAdventurer find the gryphon kill him and get the tools \nit posseses one of them can open the screwchest\nYou keep the scroll back')
            elif self.Verb.lower() in ("open", "o") and self.Obj.lower() in "screwchest":
                if self.Screw:
                    print('It has a golden sword \nyou have now taken the golden sword')
                elif not self.Screw:
                    print('First get the screwdriver, which the gryphon has')
            elif self.Verb.lower() in ("go", "east") and self.Obj.lower() in "east":
                self.GuardRoom()#NOTE use this as a method
                print("Still in development")
            elif self.Verb.lower() in ("go", "north") and self.Obj.lower() in ("north", "n"):
                if not self.RKey:
                    self.GoldRoom()
                elif self.RKey:
                    print('You need a red key card')
            elif self.Verb.lower() in ("go", "south") and self.Obj.lower() in ("south", "s"):
                self.Entrance()
            elif self.Verb.lower() in ("show", "map") and self.Obj.lower() in "map":
                print(Map)
            elif self.Verb.lower() in "quit":
                self.Checkpointsave()
            else :
                print('My Dumb code cannot understand what you mean to say so please reframe it')


    def FireMonsterRoom(self):
        print('\033[1m' + 'Fire Monster Room:')
        print('\033[0m' + 'you have entered the "firester" room where the great firester is\nhe has a secret, if you hit him with your hands you can easyly\ndefeat him')
        while True :
            x = input(">")
            self.Decode(x)       
            if self.Verb.lower() in ("kill", "hit") and self.Obj.lower() in ("firester", "him"):
                    if not self.Firester:
                        print('you defeated the fire monster, it leaves a key , take it to open the chest in entrance')
                        self.Firester = True
                    x = input(">")
                    self.Decode(x)
                    if self.Verb.lower() in ("take" , "t") and self.Obj.lower() in "key":
                        if self.Key == True :
                            print("You already have the key")
                        elif self.Key == False :
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
            elif self.Verb.lower() in ("quit"):
                self.Checkpointsave()
            elif self.Firester:
                print("He is already dead")
                self.Firester = True
                break
            else :
                print('You cannot do that')

    def Entrance(self):
        print("\033[1m" + "If you want, Put map and the map will appear")
        print('\033[1m' + 'The Entrance:' + '\033[0m')
        print('you have entered the entrance of a mighty cave \nyou see a chest on the floor \nsome stones and an empty bookshelf\nthere are doors in the east and in the north')
        while True:
            x = input(">")
            self.Decode(x)
            if self.Verb.lower() in "take" and self.Obj.lower() in "stones":
                if self.Stones == 5 :
                    print('you already have the stones')
                elif self.Stones == 0 :
                    self.Stones = 5
                    print("stones taken")
            elif self.Verb.lower() in "open" and self.Obj.lower() in "chest":
                if not self.Key:
                    print('cannot open chest, fire monster has the key')
                elif self.Key:
                    print('Chest consists of a iron knife , you take the knife')
            elif (self.Verb.lower() in "go" and self.Obj.lower() in ("north","n")) or (self.Verb.lower() in "north"):
                self.WoodenChestRoom()
            elif (self.Verb.lower() in "go" and self.Obj.lower() in ("east","e")) or (self.Verb.lower() in "east"):
                self.FireMonsterRoom()
            elif (self.Verb.lower() in "show" and self.Obj.lower() in "map"):
                print(Map)
            elif self.Verb.lower() in ("quit"):
                self.Checkpointsave()
            else :
                print('My Dumb Code Cannot Understand What You Wrote So LMAO')
starts = Player(100, 0,  0, False, False, False, False)
starts.CheckpointLoad()