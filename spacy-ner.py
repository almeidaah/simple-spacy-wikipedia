# Import spacy
import spacy
from spacy import displacy

# Import pretrained models
import en_core_web_sm

import requests
from bs4 import BeautifulSoup

# Load model
nlp = spacy.load('en_core_web_sm')

# send a request to the website
page = requests.get("https://en.wikipedia.org/wiki/Natural_Language_Toolkit")

# Use BeautifulSoup to parse HTML using html5 protocol. It is slower
# but more efficient
page_content = BeautifulSoup(page.text, "html5lib")

# Now we look for the paragraphs
textContent = []
for i in range(0, 3):
    paragraphs = page_content.find_all("p")[i].text
    textContent.append(paragraphs)

# Join the paragraphs together and replace the `\n` for empty strings
wiki_nltk = " ".join(textContent).replace("\n", "")

def get_entities(text):
    """
    This function takes a text. Uses the Spacy model.
    The model will tokenize, POS-tag and recognize the entities named in the text.
    Then, the entities are retrieved and saved in a list.
    It outputs a list with the named entities. It also outputs the result of applying
    the model to the text.
    """
    # Apply the model
    tags = nlp(text)
    # Append all entities recognized
    entities = [X.text for X in tags.ents]
    # Return the list of entities and the result of the model.
    return entities, tags

# Apply method
spacy_tags, sentences = get_entities(wiki_nltk)

# print
print(spacy_tags)

sentences_full = [x for x in sentences.sents]
sentences_full = "".join(map(str, sentences_full))

displacy.render(nlp(str(sentences_full)), jupyter=True, style='ent')