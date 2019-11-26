from converter import CFGfromFile, CFGtoCNF, printD
from cykparser import CYKParser
import re

mkey = {"if" : "a", "elif" : "b", "else" : "c", "for" : "d", "in" : "e", "while" : "f", "continue" : "g", "pass" : "h", "break" : "i", "class" : "j", "def" : "k", "return" : "l", "as" : "m", "import" : "n", "from" : "o", "raise" : "p", "and" : "q", "or" : "r", "not" : "s", "is" : "t", "True" : "u", "False" : "v", "None" : "w"}

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

    newInp = re.sub("\"\"\"[\s\S]*\"\"\"|\'\'\'[\s\S]*\'\'\'", "z", newInp)
    newInp = re.sub("\"[\s\S]*\"|\'[\s\S]*\'", "z", newInp)
    return (newInp.replace(" ", ""))

def fileReader(path):
    with open(path, "r") as f:
        content = f.read()
    return content

if __name__ == "__main__":
    # Get CNF
    CFG = CFGfromFile("grammar.txt")
    # print('CFG: '); printD(CFG); print()
    CNF = CFGtoCNF(CFG)
    print('CNF: '); printD(CNF); print()

    # Input
    inp = fileReader("test.py")

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
