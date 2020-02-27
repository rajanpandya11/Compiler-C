#!/bin/bash python
import sys
import lexical
import findcmnts
import queue
import parse

if __name__ == '__main__':
    lines = []
    d = {}
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
                print line
                line = findcmnts.findcmnts(line)
                q, e = lexical.lexical(line, q, d)
                d.update(e)
                # if not q.isEmpty():
                #     q.printq()
                # if d:
                #     print d
        if not q.isEmpty() and d:
            q.enqueue('$')
            d.update({'$': '$'})
            p = parse.Parsing(q, d)
            if p.start():
                print'ACCEPT'
            else:
                print 'REJECT'
