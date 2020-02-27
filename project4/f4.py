import sys
import lexical
import queue
import findcmnts
import parse
import codegen


if __name__ == '__main__':
    lines = []
    newlines = []
    tokens = 0
    d = {}

    sym ={}
    trud = {}
    q = queue.Queue()
    try:
        with open(sys.argv[1], 'r') as file:
            pass
            for e in file:
                lines.append(e.rstrip('\n'))
            file.close()
    except:
        print 'This program needs a file argument.'
    if lines:
        for line in lines:
            if len(line) > 0:
                line = findcmnts.findcmnts(line)
                q, e, sym, trud = lexical.lexical(line, q, d, trud)
                d.update(e)
                n = q.size() - tokens
                if e:
                    nq = []
                    while n >=1:
                        nq.append(q.indexed(n))
                        n-=1
                    if nq:
                        newlines.append(' '.join(nq))
                    tokens += len(nq)
        for line in newlines:
            print line
        if not q.isEmpty() and d:
            q.enqueue('$')
            d.update({'$': '$'})
            c = codegen.CodeGen(q,d,sym,trud)
            p = parse.Parsing(q,d,sym,c)
            if p.start():
                print'ACCEPT'
                c.printMatrix()
            else:
                print'REJECT'