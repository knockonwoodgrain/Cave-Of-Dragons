import json
from os import error
import random
import time
import sys
print(""" _______  _______           _______    _______  _______    ______   _______  _______  _______  _______  _        _______ 
(  ____ \\(  ___  )|\\     /|(  ____ \\  (  ___  )(  ____ \\  (  __  \\ (  ____ )(  ___  )(  ____ \\(  ___  )( (    /|(  ____ \\
| (    \\/| (   ) || )   ( || (    \\/  | (   ) || (    \\/  | (  \\  )| (    )|| (   ) || (    \\/| (   ) ||  \\  ( || (    \\/
| |      | (___) || |   | || (__      | |   | || (__      | |   ) || (____)|| (___) || |      | |   | ||   \\ | || (_____ 
| |      |  ___  |( (   ) )|  __)     | |   | ||  __)     | |   | ||     __)|  ___  || | ____ | |   | || (\\ \\) |(_____  )
| |      | (   ) | \\ \\_/ / | (        | |   | || (        | |   ) || (\\ (   | (   ) || | \\_  )| |   | || | \\   |      ) |
| (____/\\| )   ( |  \\   /  | (____/\\  | (___) || )        | (__/  )| ) \\ \\__| )   ( || (___) || (___) || )  \\  |/\\____) |
(_______/|/     \\|   \\_/   (_______/  (_______)|/         (______/ |/   \\__/|/     \\|(_______)(_______)|/    )_)\\_______)""")

Map = """
    +---------+                                       __ 
    |Grenade  |======================================== \\
    |Room     |                                       | |
    +---------+                                       | |
        | |                                           | |
    +---------+       +-------------------+   +-------------------+
    |Gold Room|=======|           Room    |   |___________?       |
    +---------+       |           Of      |   |                   |
        | |           +---------+ Gryphon |   |                   |
    +---------+                 |         |   +-------------------+
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
    hunger: int = 10,
    height: int = 5.9,
    gender: str = "neutral",
    quirk: str = "neutral",
    age: int = 0,
    goldcoins: int = 0,
    expertise: str = "neutral",
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
    GoldenSword: bool = False,
    Start:bool = False,
    Goblin: str = "neutral",
    newfile: dict = {
            "actone" :{
                "stones": 0,
                "screw": False,
                "smokes": 0,
                "key": False,
                "rkey": False,
                "gkey": False,
                "firester": False,
                "wsword" : False,
                "gryphonkill" : False,
                "goldensword": False
                },
            "acttwo":{
                "start" : False,
                "goblin": "neutral"
            },
            "money": {
                "goldcoins": 0
            },
            "place" : "Entrance",
            "selfcharacter":{
                "name": "steve",
                "height": 5.9,
                "hunger": 10,
                "gender": "neutral",
                "quirk" : "neutral",
                "age" : 0,
                "expertise": "neutral"
            }
        }) -> None:
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
        self.fourth = ""
        self.fifth = ""
        self.Firester = Firester
        self.GryphonKill = Gryphon
        self.WoodenSword = WoodenSword
        self.Place = Place
        self.GoldenSword = GoldenSword
        self.Start = Start
        self.Goblin = Goblin
        self.newfile = newfile
        self.hunger = hunger
        self.height = height
        self.gender = gender
        self.quirk = quirk
        self.expertise = expertise
        self.age = age
        self.goldcoins = goldcoins
    
    def Checkpointsave(self):
        checkpoint = open("checkpoint.json", "w")
        try:
            self.newfile["actone"]["stones"] = self.Stones
            self.newfile["actone"]["screw"] = self.Screw
            self.newfile["actone"]["smokes"] = self.Smokes
            self.newfile["actone"]["key"] = self.Key
            self.newfile["actone"]["rkey"] = self.RKey
            self.newfile["actone"]["gkey"] = self.GKey
            self.newfile["actone"]["firester"] = self.Firester
            self.newfile["place"] = self.Place
            self.newfile["actone"]["wsword"] = self.WoodenSword
            self.newfile["actone"]["gryphonkill"] = self.GryphonKill
            self.newfile["actone"]["goldensword"] = self.GoldenSword
            self.newfile["acttwo"]["start"] = self.Start
            self.newfile["acttwo"]["goblin"] = self.Goblin
            self.newfile["selfcharacter"]["hunger"] = self.hunger
            self.newfile["selfcharacter"]["height"] = self.height
            self.newfile["selfcharacter"]["gender"] = self.gender
            self.newfile["selfcharacter"]["quirk"] = self.quirk
            self.newfile["selfcharacter"]["expertise"] = self.expertise
            self.newfile["selfcharacter"]["age"] = self.age
            self.newfile["money"]["goldcoins"] = self.goldcoins
        except KeyError:
            print("I guess there is something wrong with my code")
            input()
        checkpointjson = json.dumps(self.newfile, indent = 4)
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
            elif self.Place == "Marketplace":
                self.Marketplace()
        

    def CheckpointLoad(self):
        while True:
            savefile = input("Do you want to load latest save file or start from new?\n1)Load save file-------1\n2)Start new game-------2\n>")
            if savefile == "1":
                print("loading save file")
                try:
                    checkpoint = open("checkpoint.json", "r")
                except FileNotFoundError:
                    print("Save file not found, making new file, please don't edit it")
                    checkpoint1 = open("checkpoint.json", "w")
                    checkpoint1json = json.dumps(self.newfile, indent = 4)
                    checkpoint1.write(checkpoint1json)
                    checkpoint1.close()
                    checkpoint = open("checkpoint.json", "r")
                data = checkpoint.read()
                dictt = json.loads(data)
                try:
                    self.Stones = dictt["actone"]["stones"]
                    self.Screw = dictt["actone"]["screw"]
                    self.Smokes = dictt["actone"]["smokes"]
                    self.Key = dictt["actone"]["key"]
                    self.RKey = dictt["actone"]["rkey"]
                    self.GKey = dictt["actone"]["gkey"]
                    self.Firester = dictt["actone"]["firester"]
                    self.WoodenSword = dictt["actone"]["wsword"]
                    self.GryphonKill = dictt["actone"]["gryphonkill"]
                    self.GoldenSword = dictt["actone"]["goldensword"]
                    self.Start = dictt["acttwo"]["start"]
                    self.Goblin = dictt["acttwo"]["goblin"]
                    self.hunger = dictt["selfcharacter"]["hunger"]
                    self.height = dictt["selfcharacter"]["height"] 
                    self.gender = dictt["selfcharacter"]["gender"]
                    self.quirk = dictt["selfcharacter"]["quirk"]
                    self.expertise = dictt["selfcharacter"]["expertise"]
                    self.age = dictt["selfcharacter"]["age"]
                    self.goldcoins = dictt["money"]["goldcoins"]
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
                    elif dictt["place"] == "Marketplace":
                        self.Marketplace()
                except KeyError:
                    print("looks like the save file is corrupt\nfixing file")
                    self.RemoveProgress()
                    self.Loading("actone")
                    self.CheckpointLoad()
                break

            elif savefile == "2":
                while True:
                    ask = input("Do you really wanna do that all your progress will be lost\n>")
                    if ask.lower() in ("yes","y"):
                        self.RemoveProgress()
                        self.Entrance()
                    elif ask.lower() in ("no","n"):
                        print("ok then start the game again")
                        input("")
                        break
                    else:
                        print("that isn't yes or no, so put it again")
                        continue
                break
            else:
                print("put 1 or 2 you nincompoop")
                continue
    
    def RemoveProgress(self):
        checkpoint1 = open("checkpoint.json", "w")
        checkpoint1json = json.dumps(self.newfile, indent = 4)
        checkpoint1.write(checkpoint1json)
        checkpoint1.close()     
                
    def Decode(self, x):
        if not x:
            print("you have to put something")
            self.Verb = " "
            self.Obj = " "
            self.Obj2 = " "
        elif x:
            words = x.split(" ")
            if len(words) >= 1:
                self.Verb = words[0]
                self.Obj = ""
                if len(words) >= 2:
                    self.Obj = words[1]
                    if len(words) >= 3:
                        self.Obj2 = words[2]
                        if len(words) == 4:
                            self.fourth = words[3]
                            if len(words) == 5:
                                self.fifth = words[4]
            elif len(words) == 1:
                self.Verb = words[0]
            else:
                print("I cant really decode that, please write one to three words")

    def damage(self, dmg: int = 5) -> None:
        self.health -= dmg
    
    def eat(self, hun: int = 1) -> None:
        self.hunger += hun
    
    def losehun(self, hun: int = 1) -> None:
        self.hunger -= hun

    def addgold(self, mon: int = 5) -> None:
        self.goldcoins += mon

    def removegold(self, mon: int = 5) -> None:
        self.goldcoins -= mon

    def Marketplace(self):
        if self.Start == False:
            print(" _____          _          __    ___  _____ _____      __  \n"
                    "|  ___|        | |        / _|  / _ \\/  __ \\_   _|    /  |\n" 
                    "| |__ _ __   __| |   ___ | |_  / /_\\ \\ /  \\/ | |______`| |\n" 
                    "|  __| '_ \\ / _` |  / _ \\|  _| |  _  | |     | |______|| |\n" 
                    "| |__| | | | (_| | | (_) | |   | | | | \\__/\\ | |      _| |_\n"
                    "\\____/_| |_|\\__,_|  \\___/|_|   \\_| |_/\\____/ \\_/      \\___/")        
            print("you keep going through a small tunnel, \nyou don't know where it leads,")
            input()
            print("\ryou have no knowledge of your previous life, \nyou just remember waking up in the entrance of the cave,")
            input()
            print("\rthe tunnels smell of methane, after travelling for 8 hours\nyou start hearing voices you keep going faster")
            input()
            print("\ryou reach the marketplace,\nan underground subway turned into a place to trade,\na humanlike creature approaches you")
            input("press enter to continue")
            self.Loading("actone")
            print("it is a goblin, goblins love gold, \nthey are very greedy and cunning,\nhe says,'ooh, a human; what have you got?'\nthen he starts checking what you have")
            while True:
                x = input("what do you do?\n>")
                self.Decode(x)
                if self.Verb.lower() in ("resist", "stop") and self.Obj.lower() in ("goblin", "him") or (self.Verb.lower() in ("resist", "stop")):
                    print("you resisted him and he stopped checking")
                elif self.Verb.lower() in ("challenge", "hit", "duel") and self.Obj.lower() in ("goblin", "him") or (self.Verb.lower() in ("challenge", "him")):
                    print("you chellenge him to a duel")
                elif self.Verb.lower() in ("throw", "toss"):
                    x = input("what?\n>")
                    self.Decode(x)
                    if self.Verb.lower() in ("stones", "stone", "a") or (self.Verb.lower() in ("stones", "stone", "a", "some") and self.Obj.lower() in ("stones", "stone", "a")):
                        print("you threw stones at him\nhe gave you a dirty look and said, 'you will regret this'\nthen he went away")
                        self.Goblin = "worse"
                    elif self.Verb.lower() in ("smokes", "grenades", "a", "smoke") or (self.Verb.lower() in ("smokes", "smoke", "a") and self.Obj.lower() in ("smokes", "smoke", "a", "grenade")):
                        print("you throw a smoke at him and run away into the crowd")
                        self.Goblin = "bad"
                elif self.Verb.lower() in ("throw", "toss"):
                    if self.Obj.lower() in ("stones", "stone", "a") or (self.Obj.lower() in ("stones", "stone", "a", "some") and self.Obj2.lower() in ("stones", "stone", "a")):
                        print("you threw stones at him\nhe gave you a dirty look and said, 'you will regret this'\nthen he went away")
                        self.Goblin = "worse"
                    elif self.Obj.lower() in ("smokes", "grenades", "a", "smoke") or (self.Obj.lower() in ("smokes", "smoke", "a") and self.Obj2.lower() in ("smokes", "smoke", "a", "grenade")):
                        print("you throw a smoke at him and run away into the crowd")
                        self.Goblin = "bad"
                elif self.Verb.lower() == "" or (self.Verb.lower() == "let" and self.Obj.lower() in ("him", "it", "the") and self.Obj2.lower("check") ):
                    print("you let him check and he says\n,'ooh you have a lot of valuable stuff hehe,\ngive me the wooden sword and i'll give you 25 gold coins'")
                    while True:
                        x = input("do you wanna trade the sword?\n>")
                        self.Decode(x)
                        if self.Verb.lower() in ("yes","y"):
                            self.addgold(25)
                            self.WoodenSword = False
                            print("you traded your wooden sword 25 gold")
                            print("you realise that you are very hungry\nyou can get food for the price\ngo on deeper, explore(put explore)")
                            break
                        elif self.Verb.lower() in ("no", "n"):
                            print("you have no money, you might get hungry \nlater on are you sure you want this?")
                            break
                        else:
                            print("invalid input put yes or no")
                            continue
                elif self.Verb.lower() == "explore":
                    self.Start = True
                    print("you walk away from the goblin and start to explore the place")
                    print("here you meet a man like you he looks at you and asks your name,\n'I am the great knight sent to destroy the evil creatures of the cave', \nhe closely looks at your armor and says,'you are from the kingdom what are you doing here?'\nyou say that you have forgot who you are\nand want to go to the kingdom to find your true identity")
                    time.sleep(5)
                    print("the man takes you with him to a food stall after you tell him that you are hungry\nyou people eat food, you ask questions to him(write name,weight,job status, relation etc to know more about him)")
                    x = input(">")
                    self.Decode(x)
                    if self.Verb.lower() == "name":
                        print("his name is Jim Smith")
                    elif self.Verb.lower() == "height":
                        print("his hright is 6 feet 9 inches nice")
                    elif self.Verb.lower() == "weight":
                        print("his weight is 69 kg nice")
                    elif self.Verb.lower() == "status":
                        print("he is a good looking fair knight, he is calm and composed")
                        print("you have introduced yourself to the marketplace, now that is done, you leave the knight you can go to him if you want")
                        self.Start = True

                elif (self.Verb.lower() == "go" and self.Obj.lower() in ("south", "s")) or (self.Verb.lower() == "south"):
                    print("Still in development")
                elif (self.Verb.lower() == "go" and self.Obj.lower() in ("east", "e")) or (self.Verb.lower() == "east"):
                    print("do you really wanna go there, its a long way back, you will get hungry and lose a bit of health")
                    while True:
                        x = input(">")
                        self.Decode(x)
                        if self.Verb.lower() in ("yes","y"):
                            print("really nigga?")
                            self.GrenadeRoom()
                            break
                        elif self.Verb.lower() in ("no", "n"):
                            print("you have no money")
                            break
                        else:
                            print("invalid input pur yes or no")
                            continue
                
                else:
                    self.UnidentifiedInput()
            
                

    def countdown(self,t): 
        while t: 
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        
        print('Fire in the hole!!') 

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
            if self.Verb.lower() in ("take", "t") and self.Obj.lower() == "smokes" or self.Obj.lower() == "grenades":
                print('You have taken the smoke grenades, you can use them to skip fighting from monsters of you don\'t want to')
                self.Smokes = 5
            elif self.Verb.lower() in ("show", "map") or (self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map"):
                print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "inv") or (self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory"):
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "ach") or (self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements"):
                self.Achievements()
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("south", "s")) or (self.Verb.lower() == "south"):
                self.GoldRoom()
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("east", "e")) or (self.Verb.lower() == "east"):
                self.Marketplace()
            elif self.Verb == " " and self.Obj == " " and self.Obj2 == " ":
                continue
            else:
                self.UnidentifiedInput()

    def Gryphon(self) -> None:
        print('Gryphon Room')
        self.Place = "Gryphon"
        if self.Screw:
            print(
                '' + 'The room has broken down now, the enchanted sword takes you to the gold room,you cannot access '
                     'this room')
            self.GoldRoom()  # !NOTE:imp: [TO Make as Method]
        elif  not self.Screw:
            print('you have entered the gryphon room\nHere there is a gryphon\ndo you want to fight him?\nalternatively you can also use smokes by typing use smokes')
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
                            print("you have two choices, an easy level fight, and a medium level fight\nEasy----1\nMedium--2")
                            while True:
                                ans = input(">")
                                if ans == "1":
                                    print("Easy")
                                    self.EzyPeazyFight()
                                    break
                                elif ans == "2":
                                    self.MediumFight()
                                    break
                                else :
                                    print("put only 1 or 2 you nimbus")
                            print("Now you have the screw which opens the screwchest in wooden  chest room")
                            self.Screw = True
                            self.GryphonKill = True
                        elif not self.WoodenSword:
                            print("you don't have the golden sword so you lost and died")
                elif self.Verb.lower() == "use" and self.Obj.lower() in ("smokes, grenades"):
                    print("okay you skipped fighting him and go the screw, but remember that he might cause a problem later on")
                    self.Screw = True 
                elif self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map":
                    print(Map)
                elif self.Verb.lower() == "quit" or self.Obj.lower() == "quit":
                    self.Checkpointsave()
                elif self.Verb.lower() in ("inventory", "inv") or (self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory"):
                    self.Inventory()
                elif self.Verb.lower() in ("achievements", "ach") or (self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements"):
                    self.Achievements()
                elif (self.Verb.lower() == "go" and self.Obj.lower() in ("west", "w")) or (self.Verb.lower() == "west"):
                    self.GoldRoom()
                elif (self.Verb.lower() == "go" and self.Obj.lower() in ("south", "s")) or (self.Verb.lower() == "south"):
                    print("there is a wall here") 
                elif self.Verb.lower() in ("go", "north") and self.Obj.lower() in ("north", "n") or (self.Verb.lower() == "north"):
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
            elif self.Verb.lower() in ("show", "map") or (self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map"):
                    print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "inv") or (self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory"):
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "ach") or (self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements"):
                self.Achievements()
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("south", "s")) or (self.Verb.lower() == "south"):
                if self.GKey == True:
                    self.WoodenChestRoom()
                elif self.GKey == False:
                    print('you don\'t have the green key card\nit is in the guardroom')
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("east", "e")) or (self.Verb.lower() == "east"): 
                if self.GKey == True:
                    self.Gryphon() 
                elif self.GKey == False:
                    print('you don\'t have the green key card\nit is in the guardroom')   
            elif self.Verb.lower() in ("go", "north") and self.Obj.lower() in ("north", "n") or (self.Verb.lower() == "north"):
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
                            if self.Verb.lower() in ("go", "drawer") or (self.Verb.lower() in ("go", "drawer") and self.Obj.lower() in ("to", "drawer")):
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
            elif self.Verb.lower() in ("show", "map") or (self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map"):
                print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "inv") or (self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory"):
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "ach") or (self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements"):
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
            elif self.Verb.lower() in ("open", "o") and self.Obj.lower() in ("screwchest", "chest"):
                if self.Screw:
                    print('It has a golden sword \nyou have now taken the golden sword')
                    self.GoldenSword = True
                elif not self.Screw:
                    print('First get the screwdriver, which the gryphon has')
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("east", "e")) or (self.Verb.lower() == "east"):
                self.GuardRoom()  # NOTE use this as a method
            elif self.Verb.lower() in ("go", "north") and self.Obj.lower() in ("north", "n") or (self.Verb.lower() == "north"):
                if self.RKey:
                    self.GoldRoom()
                elif not self.RKey:
                    print('You need a red key card')
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("south", "s")) or (self.Verb.lower() == "south"):
                self.Entrance()
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("west", "w")) or (self.Verb.lower() == "west"):
                print("there is a wall here")
            elif self.Verb.lower() in ("show", "map") or (self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map"):
                print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "inv") or (self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory"):
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "ach") or (self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements"):
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
                elif self.Firester:
                    print("He is already dead")
                    self.Firester = True
                x = input(">")
                self.Decode(x)
                if self.Verb.lower() in ("take", "t") and self.Obj.lower() in "key":
                    if self.Key:
                        print("You already have the key")
                    elif not self.Key:
                        print('key taken')
                    self.Key = True
            elif self.Verb.lower() in ("go", "north") and self.Obj.lower() in ("north", "n") or (self.Verb.lower() == "north"):
                print('there is a wall here')
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("south", "s")) or (self.Verb.lower() == "south"):
                print('there is a wall here')
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("east", "e")) or (self.Verb.lower() == "east"):
                print('there is a wall here')
            elif (self.Verb.lower() == "go" and self.Obj.lower() in ("west", "w")) or (self.Verb.lower() == "west"):
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
            elif self.Verb.lower() in ("show", "map") or (self.Verb.lower() in ("show", "map") and self.Obj.lower() == "map"):
                print(Map)
            elif self.Verb.lower() == "quit":
                self.Checkpointsave()
            elif self.Verb.lower() in ("inventory", "inv") or (self.Verb.lower() in ("inventory", "show") and self.Obj.lower() == "inventory"):
                self.Inventory()
            elif self.Verb.lower() in ("achievements", "ach") or (self.Verb.lower() in ("achievements", "show") and self.Obj.lower() == "achievements"):
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
        if self.Verb.lower() == "nice" and self.Obj.lower() in ("man", "dude", "bitch", "dude","man", "girl", "boi", "bro", "one") or (self.Verb.lower() == "nice"):
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
        elif self.Verb.lower() in ("fuck","hate","you","suck","are","dumb","donkey","bitch","motherfucker","whore","dick","cunt","pussy", "dumbass") and self.Obj.lower() in ("you","fuck","suck","are","dumb","donkey","bitch","motherfucker","whore","dick","cunt","pussy", "dumbass") or (self.Verb.lower() in ("fuck","hate","you","suck","are","dumb","donkey","bitch","motherfucker","whore","dick","cunt","pussy", "dumbass")):
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
            try:
                print(self.Verb + " " + self.Obj + "?")
            except error:
                print(self.Obj)
            if self.Place == "GrenadeRoom":
                print("put take smokes")
            elif self.Place == "Gryphon":
                print("do ou wanna fight him or not??")
    
    def EzyPeazyFight(self):
        print("this is rock, paper, scissors, lizard, spock\nthis will decide if you win or lose")
        print("Scissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock\n(and as it always has) \nRock crushes Scissors")
        print("if you lose five times you lose the game man\nRock------r\nPaper-----p\nScissors--sc\nLizard----l\nSpock-----sp")
        i = 0
        t = 0
        while i <= 5 or t <= 5:
            answer = random.randint(1,5)
            inputs = input(">")
            if inputs.lower() == "r":
                self.Loading("fight")
                if answer == 1:
                    print("that's a tie, but you win")
                    i += 1
                elif answer == 2:
                    print("paper, you lose")
                    t += 1
                elif answer == 3:
                    print("scissors, you win")
                    i += 1
                elif answer == 4:
                    print("lizard, you win")
                    i += 1
                elif answer == 5:
                    print("spock, you lose")
                    t += 1
            elif inputs.lower() == "p":
                self.Loading("fight")
                if answer == 1:
                    print("rock, you win")
                    i += 1
                elif answer == 2:
                    print("paper, you tie, you win")
                    i += 1
                elif answer == 3:
                    print("scissors, you lose")
                    t += 1
                elif answer == 4:
                    print("lizard, you lose")
                    t += 1
                elif answer == 5:
                    print("spock, you win")
                    i += 1
            elif inputs.lower() == "sc":
                self.Loading("fight")
                if answer == 1:
                    print("rock, you lose")
                    t += 1
                elif answer == 2:
                    print("paper, you win")
                    i += 1
                elif answer == 3:
                    print("scissors, you tie, you win")
                    i += 1
                elif answer == 4:
                    print("lizard, you win")
                    i += 1
                elif answer == 5:
                    print("spock, you lose")
                    t += 1
            elif inputs.lower() == "l":
                self.Loading("fight")
                if answer == 1:
                    print("rock, you lose")
                    t += 1
                elif answer == 2:
                    print("paper, you win")
                    i += 1
                elif answer == 3:
                    print("scissors, you lose")
                    t += 1
                elif answer == 4:
                    print("lizard, you tie, you win")
                    i += 1
                elif answer == 5:
                    print("spock, you win")
                    i += 1
            elif inputs.lower() == "sp":
                self.Loading("fight")
                if answer == 1:
                    print("rock, you win")
                    i += 1
                elif answer == 2:
                    print("paper, you lose")
                    t += 1
                elif answer == 3:
                    print("scissors, you win")
                    i += 1
                elif answer == 4:
                    print("lizard, you lose")
                    t += 1
                elif answer == 5:
                    print("spock, it's only logical, not really you still get a point")
                    i += 1
            elif inputs.lower() == "score":
                print("your score:" + str(i))
                print("opponents score:" + str(t))
            elif inputs.lower() in ("yes","y"):
                print("okay fight again")
                i == 0
                t == 0
            else :
                print("put r,p,sc,l or sp not anything else")
            if i >= 5:
                print("you win")
                break
            elif t >= 5:
                print("you lose, 10 health reduced, fight again?")
                self.damage(10)
                break
        if self.health == 0:
            print("lmao ded\nall your progress will be lost\ngame closing in 7 seconds")
            self.RemoveProgress()
            time.sleep(7)
            exit()

    def Loading(self, var):
        if var == "fight":
            i = 0
            while i != 5:
                time.sleep(0.06)
                sys.stdout.write("\r\\")
                time.sleep(0.06)
                sys.stdout.write("\r|")
                time.sleep(0.06)
                sys.stdout.write("\r/")
                time.sleep(0.06)
                sys.stdout.write("\r-")
                i += 1
        elif var == "actone":
            i = 0
            while i != 5:
                time.sleep(0.06)
                sys.stdout.write("\rloading:\\")
                time.sleep(0.06)
                sys.stdout.write("\rloading:|")
                time.sleep(0.06)
                sys.stdout.write("\rloading:/")
                time.sleep(0.06)
                sys.stdout.write("\rloading:-")
                i += 1
        
    def MediumFight(self):
        print("you have chosen to fight in medium mode, this one does not depend on your luck.")
        print("first you have to unscramble these words, if you want a hint then put 'hint', but you will lose 25 health\nETRONIVNMNE\n")
        if self.Place == "Gryphon":
            while self.health != 0:
                answers = input(">")
                if answers.lower() == "environment":
                    print("yes you are right, on to the next one")
                    break
                elif answers != "environment" and answers != "hint":
                    print("that is the wrong answer, you might need a hint")
                elif answers.lower() == "hint":
                    print("its related to the nature")
                    print("it surrounds us")
                    self.damage(25)
                    continue
            print("next word you need to unscramble is\nPERCSOICMO")
            while self.health != 0:
                answers1 = input(">")
                if answers1.lower() == "microscope":
                    print("yes you are right, on to the next one")
                    break
                elif answers1.lower() != "microcsope" and answers1 != "hint":
                    print("you might want a hint, cuz that was wrong")
                    continue
                elif answers1.lower() == "hint":
                    print("its easy if I give you a hint, but here you go\nit is used in biology")
                    self.damage(25)
                    continue
            print("the next word is.....\nEMEERTRUAPT")
            while self.health != 0:
                answers2 = input(">")
                if answers2.lower() == "temperature":
                    print("yes you are right, on to the next one")
                    break
                elif answers2.lower() != "temperature" and answers2 != "hint":
                    print("you might want a hint, cuz that was wrong")
                    continue
                elif answers2.lower() == "hint":
                    print("it's related to heat")
                    self.damage(25)
                    continue
            print("it's a thicc boi\nATEPLHEN")
            while self.health != 0:
                answers3 = input(">")
                if answers3.lower() == "elephant":
                    print("yes you are right, on to the next one")
                    break
                elif answers3.lower() != "elephant" and answers3 != "hint":
                    print("you might want a hint, cuz that was wrong")
                    continue
                elif answers3.lower() == "hint":
                    print("it's an animal")
                    self.damage(25)
                    continue
        if self.health == 0:
            print("lmao ded, all your progress will lost")
            print("lmao ded\nall your progress will be lost\ngame closing in 7 seconds")
            self.RemoveProgress()
            time.sleep(7)
            exit()
        elif self.health != 0:
            print("you survived the fight dude nice one")

    
if __name__ == "__main__": 
  starts = Player()
  starts.CheckpointLoad()