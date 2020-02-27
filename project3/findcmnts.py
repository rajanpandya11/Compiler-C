import re

counter = 0


def findcmnts(lline):
    """
    It finds and removes different types of comments from the given string.
    :param lline: It is a given string.
    :return: It returns the string after striping off comments.
    """
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