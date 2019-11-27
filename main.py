from converter import CFGfromFile, CFGtoCNF, printGrammar
from cykparser import CYKParser
import sys
import re

mkey = {"if" : "a", "elif" : "b", "else" : "c", "for" : "d", "in" : "e", "while" : "f", "continue" : "g", "pass" : "h", "break" : "i", "class" : "j", "def" : "k", "return" : "l", "as" : "m", "import" : "n", "from" : "o", "raise" : "p", "and" : "q", "or" : "r", "not" : "s", "is" : "t", "True" : "u", "False" : "v", "None" : "w", "with" : "A"}

# Color code
normal = "\033[1;37;40m"
red = "\033[1;37;41m"

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
        newInp = newInp.replace(multi, "z\n" * mltstr[i][1].count("\n"))

    str = re.findall(r'([\'\"])(.*?)\1{1}', newInp, re.DOTALL)
    for i in range(len(str)):
        one = str[i][0] + str[i][1] + str[i][0]
        newInp = newInp.replace(one, "z")

    newInp = newInp.replace(" ", "")
    newInp = re.sub("[xyz]{1}:[xyz]{1},", "", newInp)
    return (newInp + '\n')

def highlightNameError(inp):
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
    print()
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
    banner()

    # Get CNF
    CFG = CFGfromFile("grammar.txt")
    CNF = CFGtoCNF(CFG)

    # Input
    if (len(sys.argv) < 2):
        inpFilePath = "test.py"
    else:
        inpFilePath = sys.argv[1]

    try:
        inp = fileReader(inpFilePath)
    except Exception as e:
        print(red + "Error:" + str(e) + normal)
        print("Using default path: 'test.py'\n")
        try:
            inpFilePath = "test.py"
            inp = fileReader(inpFilePath)
        except Exception as e:
            print(red + "Error:" + str(e) + normal)
            print("Terminating program...\n")
            exit(0)

    inpHighlighted = highlightNameError(inp)
    source = inp

    # Preprocess
    inp = preprocessInput(inp)

    #Waiting message
    print("Compiling " + str(inpFilePath) + "...\n")
    print("Waiting for your verdict...\n")

    # Check
    print("========================= SOURCE CODE =========================\n")
    for i, line in enumerate(inpHighlighted.split("\n")):
        idx =   f"  {i + 1} | " if len(str(i + 1)) == 1 else\
                f" {i + 1} | " if len(str(i + 1)) == 2 else\
                f"{i + 1} | "
        print(idx + line)
    # print(inpHighlighted.replace("\n", "\n"))
    print("\n=========================== VERDICT ===========================\n")
    if (len(inp) == 0):
        print("Accepted")
        print("\n===============================================================")
        exit(0)

    # Parse
    CYKParser(inp, CNF, source)
    print("\n===============================================================")
