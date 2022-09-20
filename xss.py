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
    domtags = ['getElementById','document.write','PostMessage','eval','location','document.cookie',
    'document.referrer','window.name', 'window.locaiton','document.URL','Database', 'JSON.parse']
    line = 0
    xssfile = open("debug/xssvuln.txt", "w")

    for tags in domtags:
        tag = -1
        while(tag != None):
            if(tag != -1):
                print(tag)
                xssfile.write(tag + '\n')
            area = area[line:]
            tag, line = scanfunction(area, tags)
            #print("line after call is:",line)
