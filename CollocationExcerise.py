from random import choice
from os import system
from time import sleep
from datetime import date, datetime

def ask(numberList,inputPhrase,internalCycle):
    NoT = int(input("Numero domande => "))
    NoC = 0
    LoW = []
    for x in range(NoT):
        print(x+1,"/",NoT)
        randomKey = choice(list(listAll[numberList].keys()))
        randomA = choice(listAll[numberList][randomKey])

        if numberList == 0:
            print("....",randomA)
        else:
            print(randomA,"....")

        res = input(inputPhrase).lower().replace("\n","")
        while res.replace(" ","") == "":
            res = input(inputPhrase).lower().replace("\n","")

        if internalCycle == False:
            res = res.replace(" ", "")

        for word in res.split(" "):
            if word not in list(listAll[numberList].keys()) or randomA not in listAll[numberList][word]:
                LoW.append(randomA)
                print("SBAGLIATO! ")
                print("La risposta giusta era '" + randomKey + "'")
                break
        else:
            NoC += 1
            print("GIUSTO!")

        sleep(1)
        system("clear")

    print("RISPOSTE GIUSTE => ", NoC)
    print("DOMANDE SBAGLIATE => " , LoW)
    print("Hai totalizzato : ", float(100*NoC/NoT))

    file_object = open('log.txt', 'a')
    file_object.write(str(datetime.now()) + "\n")
    file_object.write("MODALITA' " +  str(numberList) + "\n") 
    file_object.write("RISPOSTE GIUSTE => "+ str(NoC) + "/"+ str(NoT) + "\n")
    file_object.write("DOMANDE SBAGLIATE => " + str(LoW) + "\n")
    file_object.write("Hai totalizzato : "+ str(float(100*NoC/NoT))+ "\n")
    file_object.write("\n")
    file_object.close()
    
    sleep(5)

listAll = [
    {
        "do":
        [
            "the accounts",
            "business",
            "a crossword",
            "a course in Spanish",
            "damage",
            "a deal",
            "a degree",
            "the dishes",
            "your duty",
            "an exam",
            "exercise",
            "an experiment",
            "the food for a party",
            "French at school",
            "good",
            "your hair",
            "'Hamlet'",
            "your homework",
            "an impression",
            "your job",
            "judo",
            "lunch",
            "60 miles per hour",
            "an operation",
            "Paris",
            "research",
            "the shopping",
            "a sketch",
            "a test",
            "a tour",
            "a translation",
            "the washing",
            "some work",
            "the laundry"
        ],
        "make":
        [
            "an appointment",
            "an argument for sth",
            "an attempt",
            "the bed",
            "a cake",
            "a cake gor sth",
            "changes",
            "a choice",
            "a connection",
            "a contribution",
            "a decision",
            "dinner",
            "an effort",
            "a face",
            "a film/movie",
            "friends",
            "a guess",
            "an impact",
            "an impression",
            "a mark",
            "a mess",
            "money",
            "a noise",
            "a note/notes",
            "a mistake",
            "peace",
            "a photocopy",
            "your point",
            "progress",
            "a promise",
            "a sketch",
            "a speech",
            "a statement",
            "a suggestion",
            "a trip",
            "your will"
        ],
        "have":
        [
            "an accident",
            "an argument",
            "a bath/shower",
            "a break",
            "breakfast",
            "cancer",
            "a chance",
            "a chat",
            "a cold",
            "difficulty",
            "a drink",
            "a feeling",
            "fun",
            "a guess",
            "a heart attack",
            "a holiday/vacation",
            "an idea",
            "an impact",
            "an interest",
            "a look",
            "a meeting",
            "a party",
            "a plan",
            "a nap",
            "an operation",
            "an opportunity",
            "patiance",
            "problems",
            "a schock",
            "a snack",
            "a swim",
            "time",
            "trouble"
        ],
        "take":
        [
            "action",
            "a bath/shower",
            "a bite",
            "a break",
            "the bus",
            "a call",
            "a chance",
            "a class",
            "control",
            "a course in Spanish",
            "a decision",
            "a deep breath",
            "a dislike to sb",
            "an exam",
            "French at school",
            "a guess",
            "a holiday/vacation",
            "an interest in sth",
            "an interest",
            "the lead",
            "a look",
            "medicine",
            "a nap",
            "notes",
            "notice",
            "a photo/picture",
            "a pill",
            "a risk",
            "a sip",
            "size 14",
            "a swim",
            "sb's temperature",
            "a walk",
            "an x-ray"
        ],
        "give":
        [
            "advice to sb",
            "sb an answer",
            "birth",
            "sb a chance",
            "a chance",
            "sb a choice",
            "a choice",
            "credit to sb",
            "a cry of pain",
            "an example",
            "sb an headache",
            "sb help",
            "sb an hug",
            "sb an idea",
            "the impression that..",
            "instruction",
            "an insight into sth",
            "sb a kiss",
            "sb a lecture",
            "sb a lesson",
            "sb a lift/ride",
            "your opinion",
            "sb an order",
            "a party",
            "a performance",
            "sth a polish",
            "sb a present",
            "priority to sth",
            "sth a pull",
            "sb a push",
            "sb a shock",
            "a sigh",
            "a smile",
            "a speech",
            "some thousht to sth",
            "sb time",
            "a welcome to sb"
        ]
    },
    {
        "to":
        [
            "agree",
            "arrange",
            "can't afford",
            "decide",
            "learn",
            "manage",
            "offer",
            "prefer",
            "refuse",
            "seem",
            "tend",
            "afford",
            "appear",
            "ask",
            "beg",
            "care",
            "claim",
            "consent",
            "demand",
            "expect",
            "deserve",
            "fail",
            "hesitate",
            "hope",
            "offer",
            "plan",
            "prepare",
            "pretend",
            "promise",
            "refuse",
            "seem",
            "struggle",
            "swear",
            "threaten",
            "volunteer",
            "wait",
            "want",
            "wish"
        ],
        "objectto":
        [
            "advise",
            "allow",
            "cause",
            "enable",
            "encourage",
            "expect",
            "force",
            "warn"
        ],
        "objectinf":
        [
            "make",
            "let"
        ],
        "ing":
        [
            "admit",
            "avoid",
            "can't help",
            "can't stand",
            "enjoy",
            "fancy",
            "imagine",
            "keep",
            "miss",
            "practise",
            "spend time",
            "waste time",
            "stop",
            "advise",
            "anticipate",
            "appreciate",
            "complete",
            "consider",
            "delay",
            "deny",
            "discuss",
            "dislike",
            "finish",
            "mention",
            "mind",
            "postpone",
            "practise",
            "quit",
            "recall",
            "recollect",
            "recommend",
            "resent",
            "resist",
            "risk",
            "suggest",
            "tolerate",
            "understand"
        ],
        "ing/to":
        [
            "begin",
            "continue",
            "hate",
            "intend",
            "like",
            "love",
            "prefer",
            "start",
            "forget",
            "regret",
            "remember",
            "mean",
            "need",
            "try"
            
        ]
    },
    {
        "to": [
            "adapt",
            "add",
            "agree to",
            "apologize",
            "belong",
            "consent",
            "devote",
            "happen",
            "lead",
            "listen",
            "object",
            "react",
            "refer",
            "reply",
            "speak",
            "talk",
            "turn"
        ],
        "for": [
            "admire",
            "apologize",
            "apply",
            "ask",
            "blame for",
            "care",
            "excuse",
            "head",
            "long",
            "pay",
            "pray",
            "prepare",
            "scold",
            "search",
            "vote",
            "wait",
            "wish",
            "work"
        ],
        "from": [
            "abstain",
            "borrow",
            "escape",
            "graduate",
            "hide",
            "infer",
            "prevent",
            "prohibit",
            "protect",
            "recover",
            "rescue",
            "resign",
            "retire",
            "save",
            "separate",
            "stem",
            "suffer"
        ],
        "at": [
            "aim",
            "arrive",
            "glance",
            "guess",
            "hint",
            "laugh",
            "look",
            "marvel",
            "peer",
            "point",
            "smile",
            "stare",
            "wink"
        ],
        "on": [
            "agree on",
            "base",
            "be",
            "blame on",
            "comment",
            "concentrate",
            "congratulate",
            "count",
            "depend",
            "elaborate",
            "impose",
            "insist",
            "play",
            "pride",
            "rely",
            "work"
        ],
        "up": ["bring", "grow"],
        "about": [
            "argue su qualcosa",
            "ask su qualcosa",
            "boast",
            "concern",
            "decide",
            "dream",
            "forget",
            "know",
            "protest",
            "think",
            "worry"
        ],
        "with": [
            "acquaint",
            "agree with",
            "associate",
            "charge (accusare)",
            "clutter",
            "coinncide",
            "collide",
            "compare",
            "comply",
            "confront",
            "confuse (confondere)",
            "cover",
            "cram",
            "deal",
            "discuss con",
            "help",
            "tamper"
        ],
        "in": [
            "absorb",
            "be engrossed",
            "believe",
            "confide con",
            "implicate",
            "involve",
            "participate",
            "result",
            "specialize",
            "succeed",
            "trust in"
        ]
    }
]

while True:
    system("clear")

    a = 0
    while a <= 0 or a > 4:
        system("clear")
        print("Scegli la modalità : \n 1) DO,MAKE,HAVE,TAKE,GIVE \n 2) TO,ING... \n 3) TO, ABOUT, WITH.... \n 4) VEDI LOGS \n 5) ESCI")
        try:
            a = int(input(" => "))
        except:
            continue

    system("clear")

    if a == 1:
        ask(0,"(do,make,have,take,give) => ",True)
    elif a == 2:    
        ask(1,"(to,object to,object inf,ing,ing/to) => ",False)
    elif a == 3:    
        ask(2,"(to, for, from, at, up, on, about, with, in) => ",True)
    elif a == 4:
        file = open('log.txt',mode='r')
        print(file.read())
        file.close()
        input("")
    elif a == 5:
        quit()
