import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

def main():
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)
    print(html.escape(s))
    print("Disable quotes escape")
    print(html.escape(s, quote=False))

    print("Displaying non-asc text as asc")
    s = 'Spicy Jalapeño'
    print(s.encode('ascii', errors='xmlcharrefreplace'))

    s = 'Spicy &quot;Jalape&#241;o&quot.'
    p = HTMLParser()
    print(p.unescape(s))

    t = 'The prompt is &gt;&gt;&gt;'
    print(unescape(t))

if __name__ == "__main__":
    main()