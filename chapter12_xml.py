from xml.etree.ElementTree import (Element, SubElement, tostring, fromstring)

def analyze_xml(root, tabs=''):
    print(tabs+root.tag, root.attrib, root.text, root.tail, sep='|')
    for child in root:
        analyze_xml(child, tabs+'\t')

if __name__=="__main__":
    # parsing and searching XML
    
    with open('chapter12_xml2.xml') as file:
        root = fromstring(file.read())

    # with recursion
    analyze_xml(root)

    # returns object
    print("search for child tag:", root.find('body').tag)
    print("search for children of body:", [c.tag for c in root.find('body').getchildren()])
    print("search for children recursively:", root.find('.//em').tag)

    # returns text
    print('build path:', root.findtext('./body/article/em'))

    # root.findtext(path) = root.find(path).text
    
    ''' INITIAL (parsing and searching XML) EXAMPLE
    print("ROOT NODE")
    print("\ttag:", root.tag)
    print("\tnumber of children:", len(root))
    print("\tchildren:", [c.tag for c in root.getchildren()])

    head = root[0]   
    print("HEAD NODE")
    print("\tfirst child:", head[0].tag)
    print("\tsecond child:", head[1].tag)
    print("\tlink attributes:", head[1].attrib)

    article = root[1][1]   
    print("ARTICLE NODE")
    print("\ttag:", article.tag)
    print("\ttext:", article.text)
    print("\tfirst child:", article[0].tag, article[0].text)
    print("\t\tem's tail:", article[0].tail)
    print("\tsecond child:", article[1].tag, article[1].text)
    print("\tstrong's tail:", article[1].tail)
    
    
    with open('chapter12_xml.xml') as file:
        root = fromstring(file.read())

    # with recursion
    analyze_xml(root)
    '''
    
    # constructing XML
    root = Element("html")
    head = Element("head")
    root.append(head)

    title = SubElement(head, "title")
    title.text = "my page"
    link = SubElement(head, "link")
    link.attrib['rel'] = "stylesheet"
    link.attrib['href'] = "styles.css"

    body = Element("body")
    body.text = "This is my website."
    root.append(body)

    print(tostring(root)) # tostring returns byte type
