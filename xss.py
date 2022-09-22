import backend
scancount = 0

def vuln_print(data):
    global scancount
    scancount += 1
    print(f'Vulnerability #{scancount}: \n')
    print(data)
    backend.end_vuln()

def scanfunction(content, tag):

    l1 = content.find(tag + '(')
    ln = content[l1:].find(')')
    last = l1+ln+1

    if(l1 == -1):
        return None, None
    return content[l1:last], last

def scantag(content, tag):

    soup = backend.BeautifulSoup( backend.io.StringIO(content), 'html.parser')
    tags = soup.findAll('script')

    for i in tags:
        vuln_print(i)

def scanattribute(content, tag):

#TODO
# maybe they can do without semicolon? think about it
    l1 = content.find(tag)
    leq = content[l1:].find('=')
    lend = content[l1+leq:].find(';')
    last = l1+ leq+ lend + 1

    if(l1 == -1):
        return None, None

    return content[l1:last], last



def scanforxss(area):
    src_area = area
    domsinks = ['getElementById','document.write','PostMessage','eval','location','document.cookie',
    'document.referrer','Database', 'JSON.parse','onevent']

    domtags = ['script']

    domattributes = ['innerHTML','outerHTML','window.location','window.name','document.URL']

    xssfile = open("debug/xssvuln.txt", "w")
    for sinks in domsinks:
        tag = -1
        line = 0
        area = src_area

        while(tag != None):
            if(tag != -1):
                vuln_print(tag)
                xssfile.write(tag + '\n')
            area = area[line:]
            tag, line = scanfunction(area, sinks)

    for tags in domtags:
            area = src_area
            scantag(area, tags)   

    for attributes in domattributes:
        tag = -1
        line = 0
        area = src_area

        while(tag != None):
            if(tag != -1):
                vuln_print(tag)
                xssfile.write(tag + '\n')
            area = area[line:]
            tag, line = scanattribute(area, attributes)                    

