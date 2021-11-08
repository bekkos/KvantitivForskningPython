import os
import re

path = input("Define root folder path: ")
top_files = os.listdir(path)

results = []
brukere = []

class Result():
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2
        self.frames = self.f2 - self.f1
        self.seconds = self.frames / 30

class Bruker():
    def __init__(self, id):
        self.scenarios = []
        self.id = id

for x in top_files:
    files = os.listdir(path + x)
    files.sort(key=int)
    print(files)
    bruker = Bruker(x)
    for i in files:
        index_files = os.listdir(path + x + "/" + i)
        for a in index_files:
            frame_files = os.listdir(path + x + "/" +  i + "/")
            numbers = []
            for a in frame_files:
                n = re.findall(r'\d+', a)
                if len(n) > 0:
                    numbers.append(n[0]) 
            n = Result(int(numbers[0]), int(numbers[1]))
        bruker.scenarios.append(n)
    brukere.append(bruker)

output = ""

for b in brukere:
    print("---- Ny bruker ----")
    output += "----" + b.id + "---- \n"
    itr = 1
    for s in b.scenarios:
        output += "-- Scenario " + str(itr) + " --\n"
        output += "Frames: " + str(s.frames) + "\n" 
        output += "Seconds: " + str(s.seconds) + "\n"
        itr += 1


f = open("./results.txt" , "w+")
f.write(output)
f.close()