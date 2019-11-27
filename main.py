from converter import CFGfromFile, CFGtoCNF, printGrammar
from cykparser import CYKParser
import sys
import re

mkey = {"if" : "a", "elif" : "b", "else" : "c", "for" : "d", "in" : "e", "while" : "f", "continue" : "g", "pass" : "h", "break" : "i", "class" : "j", "def" : "k", "return" : "l", "as" : "m", "import" : "n", "from" : "o", "raise" : "p", "and" : "q", "or" : "r", "not" : "s", "is" : "t", "True" : "u", "False" : "v", "None" : "w", "with" : "A"}

def preprocessInput(inp):
    global key

    match = []
    newInp = ""
    while inp:
        x = re.search("[A-Za-z_][A-Za-z0-9_]*", inp)
        if x != None:
            newInp += inp[:x.span()[0]]
            if x.group() not in mkey:
                newInp += "x"
            else:
                newInp += mkey[x.group()]
            inp = inp[x.span()[1]:]
        else:
            newInp += inp
            inp = ""

    newInp = re.sub("[0-9]+[A-Za-z_]+", "R", newInp)
    newInp = re.sub("[0-9]+", "y", newInp)
    newInp = re.sub("#.*", "", newInp)
    mltstr = re.findall(r'([\'\"])\1\1(.*?)\1{3}', newInp, re.DOTALL)
    for i in range(len(mltstr)):
        multi = mltstr[i][0]*3 + mltstr[i][1] + mltstr[i][0]*3
        newInp = newInp.replace(multi, "z")

    str = re.findall(r'([\'\"])(.*?)\1{1}', newInp, re.DOTALL)
    for i in range(len(str)):
        one = str[i][0] + str[i][1] + str[i][0]
        newInp = newInp.replace(one, "z")

    newInp = newInp.replace(" ", "")
    newInp = re.sub("[xyz]{1}:[xyz]{1},", "", newInp)
    return (newInp + '\n')

def highlightNameError(inp):
    normal = "\033[1;37;40m"
    red = "\033[1;37;41m"
    newInp = ""
    while inp:
        x = re.search("[0-9]+[A-Za-z_]+", inp)
        if x != None:
            newInp += inp[:x.span()[0]] + red + x.group() + normal
            inp = inp[x.span()[1]:]
        else:
            newInp += inp
            inp = ""
    return (newInp + '\n')

def fileReader(path):
    with open(path, "r") as f:
        content = f.read()
    return content

def banner():
    print("                  ___       _   _                     ")
    print("                 / _ \_   _| |_| |__   ___  _ __      ")
    print("                / /_)/ | | | __| '_ \ / _ \| '_ \     ")
    print("               / ___/| |_| | |_| | | | (_) | | | |    ")
    print("               \/     \__, |\__|_| |_|\___/|_| |_|    ")
    print("               ___    |___/             _ _           ")
    print("              / __\___  _ __ ___  _ __ (_) | ___ _ __ ")
    print("             / /  / _ \| '_ ` _ \| '_ \| | |/ _ \ '__|")
    print("            / /__| (_) | | | | | | |_) | | |  __/ |   ")
    print("            \____/\___/|_| |_| |_| .__/|_|_|\___|_|   ")
    print("                                 |_|   version 4.05   \n\n")

if __name__ == "__main__":
    # Get CNF
    banner()
    CFG = CFGfromFile("grammar.txt")
    CNF = CFGtoCNF(CFG)

    for i in range(3, 0, -1):
        print(i)

    # Input
    inp = fileReader(sys.argv[1])
    inpHighlighted = highlightNameError(inp)
    source = inp

    # Preprocess
    inp = preprocessInput(inp)

    #Waiting message
    print("Compiling " + str(sys.argv[1]) + "...\n")
    # Check
<<<<<<< HEAD
    print(source)

    print("Waiting for your verdict...\n")


    print()
    print(inp)
    if (len(inp) == 0):
        print("Accepted")
        exit(0)

    # Parse
    CYKParser(inp, CNF, source)
=======
    print("========================= SOURCE CODE =========================\n")
    print(inpHighlighted)
    print("=========================== VERDICT ===========================\n")
    if (len(inp) == 0):
        print("Accepted")
        print("\n===============================================================")
        exit(0)

    # Parse
    CYKParser(inp, CNF)
    print("\n===============================================================")
>>>>>>> 2ec44da07504d105fe747afd5ad5ec86113f7669
