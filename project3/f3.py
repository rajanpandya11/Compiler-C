import sys
import Semantics
import lexical
import queue
import findcmnts
import parse


if __name__ == '__main__':
    lines = []
    newlines = []
    tokens = 0
    d = {}
    sym ={}
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
                q, e, sym, trud = lexical.lexical(line, q, d)
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
        # for line in newlines:
        #     print line
        if not q.isEmpty() and d:
            q.enqueue('$')
            d.update({'$': '$'})
            p = parse.Parsing(q,d)
            s = Semantics.semantics(q,d,sym,newlines)
            if p.start():
                if s.start():
                    print'ACCEPT'
                else:
                    print'REJECT'
            else:
                print 'REJECT'