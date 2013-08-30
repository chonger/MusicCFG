from collections import defaultdict
import random

class Grammar:

    def __init__(self,fname):

        self.rules = defaultdict(list)
        self.startSymbol = "S"
        
        for x in open(fname):
            xx = x.strip().split()
            prob = float(xx[0])
            ruleStr = " ".join(xx[1:]).strip()
            syms = ruleStr[1:-1].split()
            lhs = syms[0]
            rhs = syms[1:]
            rhs.reverse()
            self.rules[lhs].append((rhs,prob))


    def generate(self):

        proc = ["S"]
        out = []

        while len(proc) > 0:
            sym = proc.pop()
            choices = self.rules.get(sym)
            if choices:
                r = random.random()
                accum = 0.0
                for rhs,prob in choices:
                    accum += prob
                    if accum >= r:
                        proc.extend(rhs)
                        break
            else:
                out.append(sym)

        return " ".join(out)
