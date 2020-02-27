import findcmnts
import lexical
import queue


class semantics(object):
    def __init__(self, q, d, sym, lines):
        self.q = q
        self.d = d
        self.sym = sym
        self.lines = lines

    def accept(self, s, a):
        if self.nt(a) in s:
            print'accepted:', self.nt(a)
            return a - 1

    def start(self):
        chk = []
        chk.append(self.mainchk())
        # chk.append(self.returnchk())
        chk.append(self.chkreturn())
        # it will call all the semantic check methods
        # it will store all return values in a list
        # at the end it will check it False is in the list
        # if yes, return False, else return True
        if False in chk:
            return False
        else:
            return True

    def nt(self):
        return self.q.currenttoken()

    def mainchk(self):
        n = 0
        for line in self.lines:
            if 'void main ( void )' in line:
                break
            n += 1
            if n == len(self.lines):
                return False
        for line in self.lines[n:]:
            if '{' in line:
                break
            n += 1
        for line in self.lines[n:]:
            if '}' in line:
                break
            n += 1
        if n + 1 == len(self.lines):
            return False
        return True

    def returnchk(self):
        n = 0
        for line in self.lines:
            line = findcmnts.findcmnts(line)
            nl = line.split()
            if nl:
                if 'void' not in nl and 'int' not in nl and 'float' not in nl and '{' not in nl:
                    break
            n += 1
        nq = queue.Queue()
        nd = {}
        for line in self.lines[n:]:
            if line:
                nq, nd, sym2, trud = lexical.lexical(line, nq, nd)
        n = self.q.size()
        tk = self.nt()
        while tk != 'return' and tk != '}':
            n -= 1
            tk = self.q.indexed(n)
        if tk == '}':
            return True
        elif tk == 'return':
            n -= 1
            if self.q.indexed(n) == ';':
                n -= 1
                while self.q.indexed(n) != '}':
                    n -= 1
                return self.q.indexed(n) == '}'
            else:
                return False
        else:
            return False

    def isfun(self, s):
        if s in self.sym.keys():
            if self.sym[s] == 'void':
                return True
            n = self.q.size()
            while n > 1:
                if self.q.indexed(n) == s and self.q.indexed(n - 1) == '(':
                    return True
                n -= 1
        return False

    def chkreturn(self):
        n = self.q.size()
        while n > 1:
            if self.q.indexed(n) in self.sym.keys():
                if self.isfun(self.q.indexed(n)):
                    fun = self.q.indexed(n)
                    while self.q.indexed(n) != 'return' and self.q.indexed(n) != '}':
                        n -= 1
                    if self.sym[fun] == 'void' and self.q.indexed(n) == '}':
                        if n == 1:
                            return True
                        else:
                            n-=1
                            continue
                    elif self.sym[fun] == 'void' and self.q.indexed(n) == 'return':
                        n -= 1
                        if self.q.indexed(n) == ';':
                            while self.q.indexed(n) != '}':
                                n-=1
                            if n == 1:
                                return True
                            else:
                                n-=1
                                continue
                    elif self.q.indexed(n) == 'return':
                        n-=1
                        temp=[]
                        while self.q.indexed(n) != ';':
                            temp.append(self.q.indexed(n))
                            n-=1
                        from f3 import trud
                        if len(temp) ==1:
                            if trud[self.q.indexed(n - 1)] == self.sym[fun]:
                                while self.q.indexed(n) != '}' and n>1:
                                    n -= 1
                                if n == 1:
                                    return True
                                else:
                                    n -= 1
                                    continue
                            else:
                                return False
                        else:
                            for i in temp:
                                if i in self.sym.keys() + ['[', ']', '(', ')', '%', '+', '-', '*', '/']:
                                    if i in self.sym.keys():
                                        if trud[i] == self.sym[fun]:
                                            if i!=temp[len(temp)-1]:
                                                continue
                                            while self.q.indexed(n) != '}' and n > 1:
                                                n -= 1
                                            if n == 1:
                                                return True
                                            else:
                                                n -= 1
                                                continue
                                    else:
                                        return False
                                else:
                                    return False
            n -= 1
