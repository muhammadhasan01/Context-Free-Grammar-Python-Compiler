from converter import CFGfromFile, CFGtoCNF, printD
from cykparser import CYKParser
import re

key = ["if", "elif", "else", "for", "in", "while", "continue", "pass", "break", "class", "def", "return", "as", "import", "from", "raise", "and", "or", "not", "is", "True", "False", "None"]

def preprocessInput(inp):
    global key

    match = []
    newInp = ""
    while inp:
        x = re.search("[A-Za-z_][A-Za-z0-9_]*", inp)
        if x != None:
            newInp += inp[:x.span()[0]]
            if x.group() not in key:
                newInp += "var"
            else:
                newInp += x.group()
            inp = inp[x.span()[1]:]
        else:
            newInp += inp
            inp = ""

    newInp = re.sub("[0-9]+[A-Za-z_]+", "err", newInp)

    return (newInp.replace(" ", ""))

if __name__ == "__main__":
    # Get CNF
    CFG = CFGfromFile("grammar.txt")
    # print('CFG: '); printD(CFG); print()
    CNF = CFGtoCNF(CFG)
    # print('CNF: '); printD(CNF); print()

    # Input
    inp = "for i in x:continue"
    # inp = "if 123==((ifaif)): while ifwhile:"
    # inp = "if 123==((ifaif)):1a=2"
    print(inp)
    inp = preprocessInput(inp)
    print(inp)

    # Check
    if(len(inp) >= 1000):
        print("Bacot")
        exit(0)
    elif(len(inp) == 0):
        print("Accepted")
        exit(0)

    # Parse
    CYKParser(inp, CNF)
