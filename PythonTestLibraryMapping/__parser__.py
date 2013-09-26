#


from xml.sax import ContentHandler, make_parser
class MonHandler(ContentHandler):
  "Document Handler personnel"
  def __init__(self):
    "initialisation"
    pass
  def startDocument(self):
    "fonction appelee lorsque le parser rencontre le premierelement"
    pass
  def startElement(self, name, attrs):
    "fonction appelee lorsque le parser rencontre une balise ouvrante"
    pass
  def endElement(self, name):
    "fonction appelee lorsque le parser rencontre une balise fermante"
    pass
    
  def characters(self, chrs, offset, length):
    "fonction appelee lorsque le parser rencontre des donnees dans un element"
    pass
  def endDocument(self):
    "fonction appelee lorsque le parser rencontre le dernier element"
    pass

doc = MonHandler()
saxparser = make_parser()
saxparser.setContentHandler(doc)

def load(filename):
  datasource = open(filename,"r")
  saxparser.parse(datasource)
 
def dump(root,filename):
  pass


import unittest

class TestParser(unittest.TestCase):
  def testLoading(self):
    load("data/test.xmi")

if __name__ == '__main__':
    unittest.main()