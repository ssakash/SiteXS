def scanfunction(content, tag):
    l1 = content.find(tag + '(')
    ln = content[l1:].find(')')
    if(l1 == -1):
        return 'not found xss vuln'
    return content[l1:ln+1]


def scanforxss(area):
    return scanfunction(area, 'getElementById')
