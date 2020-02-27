import re
import sys


counter = 0
keywords = ['else', 'if', 'while', 'return', 'int', 'float', 'void']


def findcmnts(lline):
    global counter
    counter2 = counter
    pat3 = re.compile('(?:([\/][\*])|([\*][\/])|([\/][\/]))')
    mlcs = []
    slc = []
    mlce = []
    indxs = []
    bl = False
    it = re.finditer(pat3, lline)
    change = False
    for match in it:
        if match.group():
            indxs.append(match.start())
            if match.group() == '/*':
                mlcs.append(match.group())
                mlce.append('')
                slc.append('')
                counter += 1
            elif match.group() == '*/':
                mlcs.append('')
                mlce.append(match.group())
                slc.append('')
                if counter > 0:
                    counter -= 1
                    change = True
            else:
                mlcs.append('')
                mlce.append('')
                slc.append(match.group())
            bl = True
    nwline = ''
    once = True
    if not bl:
        if counter > 0:
            return ''
        return lline
    elif len(indxs) == 1 and mlce[0] and counter == 0 and not change:
        return lline
    else:
        i = 0
        for index in indxs:
            if mlcs[i] or slc[i]:
                if once:
                    nwline += lline[:index]
                    once = False
                if mlcs:
                    counter2 += 1
            elif mlce[i]:
                if counter2 == 0:
                    if i + 1 == len(indxs):
                        nwline += lline[index:]
                    else:
                        nwline += lline[index:indxs[i + 1]]
                if counter2 > 0:
                    counter2 -= 1
                    if counter2 == 0:
                        if i + 1 == len(indxs):
                            nwline += lline[index + 2:]
                        else:
                            nwline += lline[index + 2:indxs[i + 1]]
            i += 1
    return nwline


def lexical(lline):
    lline = findcmnts(lline)
    if len(lline) > 0:
        desc = ['error:', 'num:', 'float:', 'error:', 'op:', '', '', 'op:', 'id:']
        i = 0
        pat2 = re.compile('''(?:((?<=[A-Za-z])[^A-Za-z\!\<\>\[\]\{\}\(\)\=\+\-\,\*\/\s][^\s]*)| # 1
                             ((?<=\s)[\d]+)| # 2
                             ([\d]+[\.][\d]+)| # 3
                             ((?<=\d)[^0-9\s\;\,\)\(\]\[\{\}\*\+\-\/][^\;\,\)\(\]\[\{\}]+)| #4
                             ([\+\-\*\/\=\!][\=])| # 5
                             ([\,\;])| # 6
                             ([\[\]\{\}\(\)])| # 7
                             ([\=\+\-\*\/])| # 8
                             ([A-Za-z]+))''', re.X)  # 9
        it = re.findall(pat2, lline)
        for match in it:
            n = 0
            for i in match:
                if i:
                    if n == 8:
                        findkeys(i)
                    else:
                        print desc[n], i
                    break
                n += 1
    else:
        print ''


def findkeys(inp):
    global keywords
    if inp in keywords:
        print 'keyword:', inp
    else:
        print 'id:', inp


if __name__ == '__main__':
    lines = []
    try:
        with open(sys.argv[1], 'r') as file:
            pass
            for e in file:
                lines.append(e.rstrip('\n'))
            file.close()
        for line in lines:
            if len(line) > 1:
                print 'Input: ', line
                lexical(line)
                print "\n"
    except:
        print 'This program needs a file argument.'