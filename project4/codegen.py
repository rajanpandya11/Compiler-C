class CodeGen(object):
    def __init__(self, q, d, sym, trud):
        self.matrix = []
        self.i = 0
        self.d = d
        self.sym = sym
        self.trud = trud
        self.t = 0
        self.q = q

    def add(self, a, b, s=''):
        line = []
        t=a
        while t>=b:
            line.append(self.q.indexed(t))
            t-=1
        if len(s)>0:
            self.matrix.append([str(self.i), 'end ',' ',' ', s])
            self.i += 1
            return ''
        else:
            if line[0] in ['int', 'float', 'void']:
                if '(' in line and ')' in line:
                    c = line.count(',')
                    #if c == 0:
                    #    c =-1
                    #self.matrix.append(['func', c+1, '\t\t', line[1]])
                    #self.i+=1
                    if line.index('(') + 1 == line.index(')') or line[1] == 'main':
                        self.matrix.append([str(self.i), 'func', line[1], self.sym[line[1]], '0'])
                        self.i+=1
                    else:
                        if c == 0:
                            self.matrix.append([str(self.i), 'func', line[1], self.sym[line[1]], '1'])
                            self.i += 1
                            self.matrix.append([str(self.i), 'param', '4', self.sym[line[line.index(')')-1]], line[line.index(')')-1]])
                            self.i += 1
                        elif c > 0:
                            temp = line.index(',')
                            self.matrix.append([str(self.i), 'func', str(c+1), ' ', line[1]])
                            self.i += 1
                            self.matrix.append([str(self.i), 'param', '4', self.sym[line[temp-1]], line[temp-1]])
                            self.i += 1
                            while c > 0:
                                nl = line[temp + 1:]
                                c1 = nl.count(',')
                                if c1 != 0:
                                    temp = nl.index(',')
                                else:
                                    temp = nl.index(')')
                                self.matrix.append([str(self.i), 'param', '4', self.sym[nl[temp-1]], nl[temp-1]])
                                self.i+=1
                                c -= 1
                    return line[1]
                else:
                    self.matrix.append([str(self.i), 'alloc', '4', self.sym[line[1]], line[1]])
                    self.i += 1
            elif line[0] == 'while':
                change = True
                BP = self.i
                line = self.arithmatics(line)
                while change:
                    if '<' in line:
                        c = line.index('<')
                        self.matrix.append([str(self.i), 'comp', line[c-1], line[c+1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 1] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRGTE', ' ', ' ', 'BP'])
                        self.i += 1
                    elif '>' in line:
                        c = line.index('>')
                        self.matrix.append([str(self.i), 'comp', line[c-1], line[c+1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 2] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRLTE', ' ', ' ', 'BP'])
                        self.i += 1
                    elif '<=' in line:
                        c = line.index('<=')
                        self.matrix.append([str(self.i), 'comp', line[c-1], line[c+1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 2] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRGT', ' ', ' ', 'BP\t'])
                        self.i += 1
                    elif '>=' in line:
                        c = line.index('>=')
                        self.matrix.append([str(self.i), 'comp', line[c-1], line[c+1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 2] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRLT', ' ', ' ', 'BP'])
                        self.i += 1
                    elif '==' in line:
                        c = line.index('==')
                        self.matrix.append([str(self.i), 'comp', line[c - 1], line[c + 1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 2] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRNE', ' ', ' ', 'BP'])
                        self.i += 1
                    else:
                        change = False
                return self.i - 1, BP
            elif line[0] == 'if':
                change = True
                line = self.arithmatics(line)
                while change:
                    if '<' in line:
                        c = line.index('<')
                        self.matrix.append([str(self.i), 'comp', line[c - 1], line[c + 1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 1] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRGTE', ' ', ' ', 'outofif'])
                        self.i += 1
                    elif '>' in line:
                        c = line.index('>')
                        self.matrix.append([str(self.i), 'comp', line[c - 1], line[c + 1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 2] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRLTE', ' ', ' ', 'outofif'])
                        self.i += 1
                    elif '<=' in line:
                        c = line.index('<=')
                        self.matrix.append([str(self.i), 'comp', line[c - 1], line[c + 1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 2] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRGT', ' ', ' ', 'outofif'])
                        self.i += 1
                    elif '>=' in line:
                        c = line.index('>=')
                        self.matrix.append([str(self.i), 'comp', line[c - 1], line[c + 1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 2] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRLT', ' ', ' ', 'outofif'])
                        self.i += 1
                    elif '==' in line:
                        c = line.index('==')
                        self.matrix.append([str(self.i), 'comp', line[c - 1], line[c + 1], self.makeaname()])
                        self.i += 1
                        line[c - 1:c + 2] = ''
                        line.insert(c - 1, self.getsamename())
                        self.matrix.append([str(self.i), 'BRNE', ' ', ' ', 'outofif'])
                        self.i += 1
                    else:
                        change = False
                return self.i - 1
            elif '(' in line and ')' in line and '=' in line:
                c = line.count(',')
                if line.index('(') + 1 == line.index(')'):
                    self.matrix.append([str(self.i), 'call', line[2], '0 ', self.makeaname()])
                    self.i+=1
                else:
                    if c == 0:
                        line = self.arithmatics(line)
                        self.matrix.append([str(self.i), 'args ', ' ', ' ', line[4]])
                        self.i += 1
                        self.matrix.append([str(self.i), 'call ', line[2], '1 ', line[0]])
                        self.i += 1
                    elif c > 0:
                        c1=c
                        temp = 4
                        line = self.arithmatics(line)
                        self.matrix.append([str(self.i), 'args ', '   ', '   ', line[temp]])
                        self.i += 1
                        while c > 0:
                            nl = line[temp + 1:]
                            temp += 2
                            self.matrix.append([str(self.i), 'args ', '   ', '   ', line[temp]])
                            self.i+=1
                            c -= 1
                        self.matrix.append([str(self.i), 'call ', line[2], str(c1+1), line[0]])
                        self.i += 1
                return line[2]
            elif '(' in line and ')' in line:
                c = line.count(',')
                if line.index('(') + 1 == line.index(')'):
                    self.matrix.append([str(self.i), 'call ', line[2], '0  ', '  '])
                    self.i+=1
                else:
                    if c == 0:
                        line = self.arithmatics(line)
                        self.matrix.append([str(self.i), 'args ', ' ', ' ', line[4]])
                        self.i += 1
                        self.matrix.append([str(self.i), 'call ', line[2], '1  ', '  '])
                        self.i += 1
                    elif c > 0:
                        temp = 4
                        line = self.arithmatics(line)
                        self.matrix.append([str(self.i), 'args ', '  ', '  ', line[temp-1]])
                        self.i += 1
                        while c > 0:
                            nl = line[temp + 1:]
                            temp += 2
                            self.matrix.append([str(self.i), 'args ', '  ', '  ', line[temp-1]])
                            self.i+=1
                            c -= 1
                        self.matrix.append([str(self.i), 'call ', line[2], str(c+1), '  '])
                        self.i += 1
                return line[2]
            elif 'return' in line:
                if line.index('return') + 1 == line.index(';'):
                    self.matrix.append([str(self.i), 'return ', '  ', '  ', ' '])
                    self.i += 1
                elif line.index('return') + 2 == line.index(';'):
                    self.matrix.append([str(self.i), 'return ', line[1], self.sym[line[1]], '  '])
                    self.i += 1
            elif '=' in line:
                line = self.arithmatics(line)
                self.matrix.append([str(self.i), 'assign ', line[2], ' ', line[0]])
                self.i += 1

    def arithmatics(self, line):
        change = True
        while change:
            if '/' in line:
                c = line.index('/')
                self.matrix.append([str(self.i), 'div ', line[c - 1], line[c + 1], self.makeaname()])
                self.i += 1
                line[c - 1:c + 2] = ''
                line.insert(c - 1, self.getsamename())
            elif '*' in line:
                c = line.index('*')
                self.matrix.append([str(self.i), 'mul ', line[c - 1], line[c + 1], self.makeaname()])
                self.i += 1
                line[c - 1:c + 2] = ''
                line.insert(c - 1, self.getsamename())
            elif '+' in line:
                c = line.index('+')
                self.matrix.append([str(self.i), 'add ', line[c - 1], line[c + 1], self.makeaname()])
                self.i += 1
                line[c - 1:c + 2] = ''
                line.insert(c - 1, self.getsamename())
            elif '-' in line:
                c = line.index('-')
                self.matrix.append([str(self.i), 'sub ', line[c - 1], line[c + 1], self.makeaname()])
                self.i += 1
                line[c - 1:c + 2] = ''
                line.insert(c - 1, self.getsamename())
            else:
                change = False
        return line

    def makeaname(self):
        temp = 't' + ' ' + str(self.t)
        r = '_'.join(temp.split())
        self.t+=1
        return r

    def getsamename(self):
        temp = 't' + ' ' + str(self.t-1)
        r = '_'.join(temp.split())
        return r

    def backpatch(self, a):
        self.matrix[a][4] = str(self.i)


    def printMatrix(self):
        from tabulate import tabulate
        print tabulate(self.matrix, headers=['#','opertn','opernd','opernd','result'])
