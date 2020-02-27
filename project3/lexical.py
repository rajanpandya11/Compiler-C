import re

keywords = ['else', 'if', 'while', 'return', 'int', 'float', 'void']
sym = {}
truedesc = ['error:',
            'float:', 'float:',
            'num:', 'num:',
            'float:', 'float:',
            'num:', 'num:',
            'error', 'error:', 'op:', 'op:', 'error', '', 'op:', '']

def lexical(lline, q, d):
    """It separates and prints a string into ids, keywords, numbers, and many different tokens.
    Args:
        lline: It is a input string.
        q: It is an object of class Queue
    Returns:
        Nothing
    """
    trud = {}
    if len(lline) > 0:
        desc = ['error',
                'num', 'num',
                'num', 'num',
                'num', 'num',
                'num', 'num',
                'error', 'error', 'op', 'op', 'error', '', 'op', '']
        i = 0
        pat2 = re.compile('''(?:((?<=[A-DF-Za-df-z])[^A-Za-z\!\<\>\[\]\{\}\(\)\=\+\-\,\;\*\/\s][^\s]*)| # 1
                             ((?<=[\s\+\-\*\/\=])[\d]+[\.][\d]+([Ee][\+\-\d][\d]*)?)| # 2 & 3
                             ((?<=[\s\+\-\*\/\=])[\d]+([Ee][\+\-\d][\d]*)?)| # 4 & 5
                             ([\d]+[\.][\d]+([Ee][\+\-\d][\d]*)?)| # 6 & 7
                             ([\d]+([Ee][\+\-\d][\d]*)?)| # 8 & 9
                             ((?<!\d)[\.]?[\d]*[Ee][+-]?[\d]+)| #10
                             ((?<=\d)[^0-9Ee\.\s\;\,\)\(\]\[\{\}\*\+\-\/][^\;\,\)\(\]\[\{\}]*)| #11
                             ([\<\>\+\-\*\/\=])| # 12
                             ([\<\>\+\-\*\/\=\!][\=])| #13
                             ([\!\.])| #14
                             ([\,\;])| # 15
                             ([\[\]\{\}\(\)])| # 16
                             ([A-Za-z]+))''', re.X)  # 17
        it = re.findall(pat2, lline)
        for match in it:
            n = 0
            for i in match:
                if i:
                    if n == 16:
                        e = findkeys(i, q, d)
                        d.update(e)
                    else:
                        if 0 < n < 9:
                            q.enqueue(i)
                            d.update({i: desc[n]})
                            trud.update({i:truedesc[n]})
                        elif n == 12:
                            q.enqueue(i[0])
                            q.enqueue(i[1])
                            d.update({i[0]: i[0]})
                            trud.update({i[0]: i[0]})
                            d.update({i[1]: i[1]})
                            trud.update({i[1]: i[1]})
                        else:
                            q.enqueue(i)
                            d.update({i: i})
                            trud.update({i: i})
                    break
                n += 1
    else:
        print ''
    return q, d, sym, truedesc


def findkeys(inp, q, d):
    """Determines and prints whether the given word is a keyword or an id.
    Args:
        inp: It takes a string as an argument.
        q: It is an object of class Queue
        d: It is a dictionary
    Returns:
        Nothing
    """
    global keywords, sym
    if inp in keywords:
        q.enqueue(inp)
        d.update({inp: inp})
    else:
        type = q.indexed(1)
        q.enqueue(inp)
        d.update({inp: "id"})
        if inp not in sym.keys():
            sym.update({inp:type})
    return d