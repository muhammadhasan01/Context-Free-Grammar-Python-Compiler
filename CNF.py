from copy import deepcopy
import string

class CNF:
    """Class untuk merepresentasikan CNF"""

    def __init__(self):
        self.CNF_RULE = {}

    def __repr__(self):
        return f"test"

    def CFGfromFile(self, grammarPath):
        CFG_RULE = {}
        with open(grammarPath, 'r') as f:
            lines = [line.split('->')
                        for line in f.read().split('\n')
                        if len(line.split('->')) == 2]
            for line in lines:
                variable = line[0].replace(" ", "")
                rawProductions = [rawProduction.split() for rawProduction in line[1].split('|')]
                production = []
                for rawProduction in rawProductions:
                    production.append([ " " if item == "__space__" else
                                        "|" if item == "__or_sym__" else
                                        item for item in rawProduction])
                CFG_RULE.update({variable: production})
        return CFG_RULE

    def isVariable(self, item):
        if len(item) == 1:
            return False
        for char in item:
            if char not in (string.ascii_uppercase + '_' + string.digits):
                return False
        return True

    def removeUnitProduction(self, CFG):
        for variable in CFG:
            productions = CFG[variable]
            repeat = True
            while repeat:
                repeat = False
                for production in productions:
                    if len(production) == 1 and self.isVariable(production[0]):
                        productions.remove(production)
                        newProduction = deepcopy([production for production in CFG[production[0]]
                                            if production not in productions])
                        productions.extend(newProduction)
                        repeat = True
                        break
        return CFG

    def updateToCNF(self, CFG):
        newRule = {}
        for variable in CFG:
            terminals = []
            productions = CFG[variable]
            # Search terminals
            processProduction = [production for production in productions if len(production) > 1]
            for production in processProduction:
                for item in production:
                    if not(self.isVariable(item)) and item not in terminals:
                        terminals.append(item)
            # Create new rule and update production
            for i, terminal in enumerate(terminals):
                newRule.update({f"{variable}_TERM_{i + 1}": [[terminal]]})
                for idx, j in enumerate(productions):
                    if len(j) > 1:
                        for k in range(len(j)):
                            productions[idx][k] = productions[idx][k].replace(terminal, f"{variable}_TERM_{i + 1}")
            # Update productions so match A -> BC or A -> terminal
            for i in range(len(productions)):
                idx = 1
                while len(productions[i]) > 2:
                    newRule.update({f"{variable}_EXT_{idx}": [[productions[i][0], productions[i][1]]]})
                    productions[i] = productions[i][1:]
                    productions[i][0] = f"{variable}_EXT_{idx}"
                    idx += 1
        CFG.update(newRule)
        return CFG

    def CFGtoCNF(self, CFG):
        CFG = self.removeUnitProduction(CFG)
        CNF = self.updateToCNF(CFG)
        return CNF

def printD(dict):
    for var in dict:
        print(var,"-> ",end="")
        for i in range(len(dict[var])):
            if i == len(dict[var]) - 1:
                print(dict[var][i])
            else:
                print(dict[var][i],"| ",end="")

if __name__ == '__main__':
    CNF = CNF()
    CFG = CNF.CFGfromFile("grammar.txt")
    print('CFG: ')
    printD(CFG)
    print()
    CNF = CNF.CFGtoCNF(CFG)
    print('CNF: ')
    printD(CNF)
    print()
