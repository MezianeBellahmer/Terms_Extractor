import spacy
from spacy import displacy
import sys

import os

file = open(sys.argv[1], 'r')
text = file.read()
file.close()

prdnlp = spacy.load("neural network annotator") #
doc = prdnlp(text)

html = displacy.render(doc, style="ent")
Html_file = open("render.html", "w")
Html_file.write(html)
Html_file.close()
