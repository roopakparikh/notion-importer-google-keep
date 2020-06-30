from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import os


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u"\n ".join(t.strip() for t in visible_texts)

def get_text(html_file):
    #html_file="/Users/rparikh/Downloads/Takeout/Keep/SuperValu.html"
    b = os.path.basename(html_file)
    n = b[:-5]+".txt"
    f = open(html_file)
    html= f.read()
    f.close()
    txt = text_from_html(html)
    nf = os.path.dirname(html_file)+"/"+n
    f = open(nf, "w")
    f.write(txt)
    f.close()
    return nf
