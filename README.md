# Terms_Extractor
A term extraction tool

# How to use
### Install virtualenv within your default python interpretor
`pip install virtualenv`

### Create a virtual environnement and install requirements
```
virtualenv environnement_name
source environnement_name/bin/activate
pip install requirements.txt
```
### How to use the tool
You need to call `rule-based-extractor.py` or `supervised-model-extractor.py` with the python interpretor. The argument should be a text file. After the execution of the command, an html file will be created in the same directory named : `render.html`. You will just have to display using your prefered browser.
```
python3 rule-based-extractor.py path_to_text
python3 supervised-model-extractor.py path_to_text
```

You can test on one of the NLP articles we converted to text files, to evaluate our tool:
```
python3 supervised-model-extractor.py test2/N18-2008.txt
```


