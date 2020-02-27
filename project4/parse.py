def exitpgm():
    print 'REJECT'
    exit()


class Parsing(object):
    def __init__(self, q, d, sym, c):
        self.q = q
        self.d = d
        self.sym = sym
        self.follows = {'pgm': ['$'],
                        'd-list': ['$'],
                        'A': ['$'],
                        'dclartn': ['int', 'void', 'float', '$'],
                        'B': ['int', 'void', 'float', '$'],
                        'var-dclartn': [';', '[', 'int', 'void', 'float', '$', 'id', '(', 'num', 'while', '{', 'if',
                                        'return'],
                        'fun-dclartn': ['int', 'void', 'float', '$'],
                        'type-specfr': ['id'],
                        'params': [')'],
                        'param-list': [')'],
                        'D': [')'],
                        'param': [',', ')'],
                        'E': [',', ')'],
                        'compnd-stmt': ['else', ';', 'id', '(', 'num', 'while', '{', 'if', 'return', 'int', 'void',
                                        'float', '$', '}'],
                        'local-dclartn': [';', 'id', '(', 'num', 'while', '{', 'if', 'return', '}'],
                        'F': [';', 'id', '(', 'num', 'while', '{', 'if', 'return', '}'],
                        'statmnt-list': ['}'],
                        'G': ['}'],
                        'statmnt': ['else', ';', 'id', '(', 'num', 'while', '{', 'if', 'return', '}'],
                        'exprsn-stmt': ['else', ';', 'id', '(', 'num', 'while', '{', 'if', 'return', '}'],
                        'selctn-stmt': ['else', ';', 'id', '(', 'num', 'while', '{', 'if', 'return', '}'],
                        'H': ['else', ';', 'id', '(', 'num', 'while', '{', 'if', 'return', '}'],
                        'itertn-stmt': ['else', ';', 'id', '(', 'num', 'while', '{', 'if', 'return', '}'],
                        'retrn-stmt': ['else', ';', 'id', '(', 'num', 'while', '{', 'if', 'return', '}'],
                        'exprsn': [',', ';', ']', ')'],
                        'two': [',', ';', ']', ')'],
                        'two2': [';', ']', ')'],
                        'three': [',', ';', ']', ')'],
                        'temp3': [',', '+', '-', '<', '>', '=', '!', ';', ']', ')', '('],
                        'temp2': [',', '<', '>', '=', '!', ';', ']', ')', '('],
                        'temp': [',', ';', ']', ')', '('],
                        'relop': ['(', 'num', 'id', ',', ';', ']', ')', '*', '/', '+', '-', '<', '>', '=', '!'],
                        'L': ['(', 'num', 'id'],
                        'add-exprsn': ['<', '>', '=', '!', ';', ']', ')'],
                        'addop': ['(', 'id', 'num'],
                        'term': ['+', '-', '<', '>', '=', '!', ';', ']', ')'],
                        'mulop': ['(', 'id', 'num'],
                        'factor': ['*', '/', '+', '-', '<', '>', '=', '!', ';', ']', ')', '('],
                        'one': ['*', '/', '+', '-', '<', '>', '=', '!', ';', ']', ')', '('],
                        'args': [')'],
                        'arg-list': [')'],
                        'O': [')']}
        self.firsts = {'pgm': ['int', 'void', 'float'],
                       'd-list': ['int', 'void', 'float'],
                       'A': ['', 'int', 'void', 'float'],
                       'dclartn': ['int', 'void', 'float'],
                       'B': [';', '[', '('],
                       'var-dclartn': [';', '['],
                       'fun-dclartn': ['('],
                       'type-specfr': ['int', 'void', 'float'],
                       'params': ['void', 'int', 'float'],
                       'param-list': ['int', 'void', 'float'],
                       'D': [',', ''],
                       'param': ['int', 'void', 'float'],
                       'E': ['[', ''],
                       'compnd-stmt': ['{'],
                       'local-dclartn': ['', ';', '['],
                       'F': ['int', 'float'],
                       'statmnt-list': ['', ';', 'id', '(', 'num', 'while', '{', 'if', 'return'],
                       'G': ['', ';', 'id', '(', 'num', 'while', '{', 'if', 'return'],
                       'statmnt': [';', 'id', '(', 'num', 'while', '{', 'if', 'return'],
                       'exprsn-stmt': [';', 'id', '(', 'num'],
                       'selctn-stmt': ['if'],
                       'H': ['else', ''],
                       'itertn-stmt': ['while'],
                       'retrn-stmt': ['return'],
                       'exprsn': ['id', '(', 'num'],
                       'two': ['', '=', '[', '('],
                       'two2': ['', '*', '/', '+', '-', '<', '>', '=', '!'],
                       'three': ['', '*', '/', '+', '-', '<', '>', '=', '!'],
                       'temp3': ['', '*', '/'],
                       'temp2': ['', '+', '-'],
                       'temp': ['', '<', '>', '=', '!'],
                       'relop': ['<', '>', '=', '!'],
                       'L': ['=', ''],
                       'add-exprsn': ['(', 'id', 'num'],
                       'addop': ['+', '-'],
                       'term': ['(', 'id', 'num'],
                       'mulop': ['*', '/'],
                       'factor': ['(', 'id', 'num'],
                       'one': ['[', ''],
                       'args': ['', '(', 'num', 'id'],
                       'arg-list': ['(', 'num', 'id'],
                       'O': [',', '']}
        self.i = self.q.size()
        self.terms = ['id', ';', '[', 'num', ']', '(', ')', 'int', 'void', 'float', ',', '{', '}', 'if', 'else',
                      'while', 'return', '=', '<', '>', '!', '+', '-', '*', '/']
        self.codegen = c
        self.func = ''

    def start(self):
        return self.pgm(self.q.size())

    def getfirst(self, nonterm):
        return self.firsts[nonterm]

    def getfollow(self, nonterm):
        return self.follows[nonterm]

    def nt(self, n):
        getid = self.q.indexed(n)
        return self.d[getid]

    def accept(self, s, a):
        if self.nt(a) in s:
            #if self.nt(a) == ';':
            #    pass
            if self.nt(a) in ['id', 'num']:
                if self.nt(a+1) == '[' and self.nt(a-1) in [']', '(']:
                    if self.q.indexed(a) in self.sym.keys() and self.sym[self.q.indexed(a)] == 'int':
                        return a-1
                    elif self.q.indexed(a).isdigit():
                        return a-1
                    else:
                        exitpgm()
            if self.nt(a) == 'id':
                if self.q.indexed(a) in self.sym.keys() and self.sym[self.q.indexed(a)] in ['void', 'int', 'float']:
                    return a-1
                else:
                    exitpgm()
            else:
                return a - 1
        else:
            exitpgm()

    def pgm(self, a):
        if self.nt(a) == '$':
            return True
        else:
            b = self.d_list(a)
            if b == 1:
                return True
            else:
                exitpgm()

    def d_list(self, a):
        if self.nt(a) in self.getfirst('dclartn'):
            b = self.dclartn(a)
            return self.A(b)
        else:
            exitpgm()

    def A(self, a):
        if self.nt(a) in self.getfollow('A'):
            return a
        elif self.nt(a) in self.getfirst('dclartn'):
            b = self.dclartn(a)
            return self.A(b)
        else:
            exitpgm()

    def dclartn(self, a):
        if self.nt(a) == 'void':
            b = self.accept('void', a)
            c = self.accept('id', b)
            return self.fun_dclartn(c)
        elif self.nt(a) in self.getfirst('type-specfr'):
            b = self.type_specfr(a)
            c = self.accept('id', b)
            return self.B(c)
        else:
            exitpgm()

    def B(self, a):
        if self.nt(a) in self.getfirst('var-dclartn'):
            return self.var_dclartn(a)
        elif self.nt(a) in self.getfirst('fun-dclartn'):
            return self.fun_dclartn(a)
        else:
            exitpgm()

    def type_specfr(self, a):
        if self.nt(a) == 'int':
            return self.accept('int', a)
        elif self.nt(a) == 'float':
            return self.accept('float', a)
        elif self.nt(a) == 'void':
            return self.accept('void', a)
        else:
            exitpgm()

    def var_dclartn(self, a):
        if self.nt(a) == ';':
            f = self.accept(';', a)
            # call code to generate code
            self.codegen.add(a+2,a)
            return f
        elif self.nt(a) == '[':
            b = self.accept('[', a)
            c = self.accept('num', b)
            d = self.accept(']', c)
            e = self.accept(';', d)
            # call code to generate code
            self.codegen.add(a + 2, d)
            return e
        else:
            exitpgm()

    def fun_dclartn(self, a):
        if self.nt(a) in ['(']:
            b = self.accept('(', a)
            c = self.params(b)
            d = self.accept(')', c)     # here a function is declared, so can do coding
            # call code to generate code maybe like code(a+2,c)
            self.func = self.codegen.add(a+2,c)
            e = self.compnd_stmt(d)
            self.func = self.codegen.add(a, b, self.func)
            return e
        else:
            exitpgm()

    def params(self, a):
        if self.nt(a) == 'void':
            return self.accept('void', a)
        elif self.nt(a) in self.getfirst('param-list'):
            return self.param_list(a)
        else:
            exitpgm()

    def param_list(self, a):
        if self.nt(a) in self.getfirst('param'):
            b = self.param(a)
            return self.D(b)
        else:
            exitpgm()

    def D(self, a):
        if self.nt(a) in [',']:
            b = self.accept(',', a)
            c = self.param(b)
            d = self.D(c)
            return d
        elif self.nt(a) in self.getfollow('D'):
            return a
        else:
            exitpgm()

    def param(self, a):
        if self.nt(a) in self.getfirst('type-specfr'):
            b = self.type_specfr(a)
            c = self.accept('id', b)
            return self.E(c)
        else:
            exitpgm()

    def E(self, a):
        if self.nt(a) in ['[']:
            b = self.accept('[', a)
            return self.accept(']', b)
        elif self.nt(a) in self.getfollow('E'):
            return a
        else:
            exitpgm()

    def compnd_stmt(self, a):
        if self.nt(a) in self.getfirst('compnd-stmt'):
            b = self.accept('{', a)
            c = self.local_dclartn(b)
            d = self.statmnt_list(c)
            return self.accept('}', d)
        else:
            exitpgm()

    def local_dclartn(self, a):
        if self.nt(a) in self.getfirst('F'):
            return self.F(a)
        elif self.nt(a) in self.getfollow('local-dclartn'):
            return a
        else:
            exitpgm()

    def F(self, a):
        if self.nt(a) in ['int', 'float']:
            b = self.type_specfr(a)
            c = self.accept('id', b)
            d = self.var_dclartn(c)
            return self.F(d)
        elif self.nt(a) in self.getfollow('F'):
            return a
        else:
            exitpgm()

    def statmnt_list(self, a):
        return self.G(a)

    def G(self, a):
        if self.nt(a) in self.getfirst('statmnt'):
            b = self.statmnt(a)
            return self.G(b)
        elif self.nt(a) in self.getfollow('G'):
            return a
        else:
            exitpgm()

    def statmnt(self, a):
        if self.nt(a) in self.getfirst('exprsn-stmt'):
            return self.exprsn_stmt(a)
        elif self.nt(a) in self.getfirst('selctn-stmt'):
            return self.selctn_stmt(a)
        elif self.nt(a) in self.getfirst('itertn-stmt'):
            return self.itertn_stmt(a)
        elif self.nt(a) in self.getfirst('retrn-stmt'):
            return self.retrn_stmt(a)
        elif self.nt(a) in self.getfirst('compnd-stmt'):
            return self.compnd_stmt(a)
        else:
            exitpgm()

    def exprsn_stmt(self, a):
        if self.nt(a) == ';':
            return self.accept(';', a)
        elif self.nt(a) in self.getfirst('exprsn'):
            b = self.exprsn(a)
            self.codegen.add(a,b)
            return self.accept(';', b)
        else:
            exitpgm()

    def selctn_stmt(self, a):
        if self.nt(a) == 'if':
            b = self.accept('if', a)
            c = self.accept('(', b)
            d = self.exprsn(c)
            e = self.accept(')', d)
            special = self.codegen.add(a, d)
            f = self.statmnt(e)
            self.codegen.backpatch(special)
            g = self.H(f)
            return g
        else:
            exitpgm()

    def H(self, a):
        if self.nt(a) == 'else':
            b = self.accept('else', a)
            return self.statmnt(b)
        elif self.nt(a) in self.getfollow('H'):
            return a
        else:
            exitpgm()

    def itertn_stmt(self, a):
        if self.nt(a) == 'while':
            b = self.accept('while', a)
            c = self.accept('(', b)
            d = self.exprsn(c)
            e = self.accept(')', d)
            special, br = self.codegen.add(a,d)
            f = self.statmnt(e)
            self.codegen.matrix.append([str(self.codegen.i), 'BR ', ' ', ' ', str(br)])
            self.codegen.i += 1
            self.codegen.backpatch(special)
            return f
        else:
            exitpgm()

    def retrn_stmt(self, a):
        if self.nt(a) == 'return':
            b = self.accept('return', a)
            c = self.exprsn_stmt(b)
            self.codegen.add(a,c+1)
            self.func = self.codegen.add(a, b, self.func)
            return c
        else:
            exitpgm()

    # CHANGES STARTS HERE

    def exprsn(self, a):
        if self.nt(a) == '(':
            b = self.accept('(', a)
            c = self.exprsn(b)
            self.codegen.add(b,c+1)
            d = self.accept(')', c)
            return self.three(d)
        elif self.nt(a) == 'num':
            b = self.accept('num', a)
            return self.three(b)
        elif self.nt(a) == 'id':
            b = self.accept('id', a)
            return self.two(b)
        else:
            exitpgm()

    def two(self, a):
        if self.nt(a) in self.getfirst('one') + ['=']:
            b = self.one(a)
            c = self.relop(b)
            return self.two2(c)
        elif self.nt(a) == '(':
            b = self.accept('(', a)
            c = self.args(b)
            d = self.accept(')', c)
            return self.three(d)
        elif self.nt(a) in self.getfirst('three')+self.getfollow('two'):
            return self.three(a)
        else:
            exitpgm()

    def three(self, a):
        b = self.temp3(a)
        c = self.temp2(b)
        return self.temp(c)

    def temp3(self, a):
        if self.nt(a) in self.getfirst('mulop'):
            b = self.mulop(a)
            c = self.factor(b)
            return self.temp3(c)
        elif self.nt(a) in self.getfollow('temp3'):
            return a
        else:
            exitpgm()

    def temp2(self, a):
        if self.nt(a) in self.getfirst('addop'):
            b = self.addop(a)
            c = self.term(b)
            # self.codegen.add(a+1,b)
            return self.temp2(c)
        elif self.nt(a) in self.getfollow('temp2'):
            return a
        else:
            exitpgm()

    def temp(self, a):
        if self.nt(a) in self.getfirst('relop'):
            b = self.relop(a)
            c = self.add_exprsn(b)
            return self.temp(c)
        elif self.nt(a) in self.getfollow('temp'):
            return a
        else:
            exitpgm()

    def two2(self, a):
        if self.nt(a) in self.getfirst('three'):
            return self.three(a)
        elif self.nt(a) in self.getfirst('exprsn'):
            return self.exprsn(a)
        elif self.nt(a) in self.getfollow('two2'):
            return a
        else:
            exitpgm()

    def relop(self, a):
        if self.nt(a) == '<':
            b = self.accept('<', a)
            return self.L(b)
        elif self.nt(a) == '>':
            c = self.accept('>', a)
            return self.L(c)
        elif self.nt(a) == '=':
            d = self.accept('=', a)
            return self.L(d)
        elif self.nt(a) == '!':
            e = self.accept('!', a)
            return self.accept('=', e)
        elif self.nt(a) in self.getfollow('relop'):
            return a
        else:
            exitpgm()

    # kept same
    def L(self, a):
        if self.nt(a) == '=':
            return self.accept('=', a)
        elif self.nt(a) in self.getfollow('L'):
            return a
        else:
            exitpgm()

    # changed
    def add_exprsn(self, a):
        if self.nt(a) in self.getfirst('term'):
            b = self.term(a)
            return self.temp2(b)
        else:
            exitpgm()

    # same
    def addop(self, a):
        if self.nt(a) == '+':
            return self.accept('+', a)
        elif self.nt(a) == '-':
            return self.accept('-', a)
        else:
            exitpgm()

    # changed
    def term(self, a):
        if self.nt(a) in self.getfirst('factor'):
            b = self.factor(a)
            return self.temp3(b)
        else:
            exitpgm()

    # same
    def mulop(self, a):
        if self.nt(a) in ['*']:
            return self.accept('*', a)
        if self.nt(a) in ['/']:
            return self.accept('/', a)
        else:
            exitpgm()

    # changed
    def factor(self, a):
        if self.nt(a) in ['(']:
            b = self.accept('(', a)
            c = self.exprsn(b)
            self.codegen.add(b,c+1)
            d = c
            if self.nt(c) == ',':
                d = self.O(c)
            return self.accept(')', d)
        elif self.nt(a) in ['id']:
            d = self.accept('id', a)
            if self.nt(d) in self.getfirst('factor'):
                return self.factor(d)
            else:
                return self.one(d)
        elif self.nt(a) in ['num']:
            return self.accept('num', a)
        else:
            exitpgm()

    def one(self, a):
        if self.nt(a) == '[':
            b = self.accept('[', a)
            c = self.exprsn(b)
            self.codegen.add(b, c + 1)
            return self.accept(']', c)
        elif self.nt(a) in self.getfollow('one'):
            return a
        else:
            exitpgm()

    # same
    def args(self, a):
        if self.nt(a) in self.getfirst('arg-list'):
            return self.arg_list(a)
        elif self.nt(a) in self.getfollow('arg-list'):
            return a
        else:
            exitpgm()

    def arg_list(self, a):
        if self.nt(a) in self.getfirst('arg-list'):
            b = self.exprsn(a)
            self.codegen.add(a, b + 1)
            return self.O(b)
        else:
            exitpgm()

    def O(self, a):
        if self.nt(a) in [',']:
            b = self.accept(',', a)
            c = self.exprsn(b)
            self.codegen.add(b, c + 1)
            d = self.O(c)
            return d
        elif self.nt(a) in self.getfollow('O'):
            return a
        else:
            exitpgm()

