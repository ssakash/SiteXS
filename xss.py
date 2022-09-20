import backend

scancount = 0

def scanfunction(content, tag):

    l1 = content.find(tag + '(')
    ln = content[l1:].find(')')
    last = l1+ln+1

    #print(f'start index:{l1}, end index:{last}')
    if(l1 == -1):
        return None, None
    return content[l1:l1+ln+1], last


def scanforxss(area):
    domtag1 = 'getElementById'
    line = 0
    tag = ''
    xssfile = open("debug/xssvuln.txt", "w")

    while(tag != None):
        print(tag)
        xssfile.write(tag + '\n')
        area = area[line:]
        tag, line = scanfunction(area, domtag1)
        #print("line after call is:",line)
