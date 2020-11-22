import pandas as pd
import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English
from spacy import displacy
import sys

file = open(sys.argv[1], 'r')
text = file.read()
file.close()

data = pd.read_csv("terms_cleaned.csv", sep=",")[['pattern', 'pilot']]
data = data.drop_duplicates()

patterns = []
for index, row in data.iterrows():
    patterns.append(
        {"label" : "NLP term", "pattern" : row["pilot"]}
    )
nlp = English()
ruler = EntityRuler(nlp)
ruler.add_patterns(patterns)
nlp.add_pipe(ruler)

doc = nlp(text)
html = displacy.render(doc, style="ent")
Html_file = open("render.html", "w")
Html_file.write(html)
Html_file.close()
