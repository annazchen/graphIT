import spacy
text = "Joe walks 2m north. He walks 3m east. What is the total distance?"
nlp = spacy.load("en_core_web_sm")

unit_list = ["m", "km", "cm", "mm", "ft", "yd", "mi", "in", "nmi", "N"]
direction_list = ["north", "east", "south", "west"]
EIND_list = ["observer", "Observer", "observers", "Observers"]

vMag = []
vDir = []
vTyp = []



ruler = nlp.add_pipe("entity_ruler", before="ner")
patterns = [
    {"label": "MAGNITUDE", "pattern": [{"IS_DIGIT": True}, {"TEXT": {"IN": unit_list}}]},
    {"label": "DIRECTION", "pattern": [{"TEXT": {"IN": direction_list}}]},
    {"label": "EIND", "pattern": [{"TEXT": {"IN": EIND_list}}]}
]
ruler.add_patterns(patterns)
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)

# assume all qualities of a vector are given in a sentence 
# identify sentences with direction
for sent in doc.sents:
    if any(ent.label_ == "MAGNITUDE" for ent in sent.ents):
        #it is currently assumed to be a scalar
        #assuming 1 vector per sentence
        if any(ent.label_ == "DIRECTION" for ent in sent.ents):
            #it is now assumed to be a vector
            vMag.append([ent.text for ent in sent.ents if ent.label_ == "MAGNITUDE"])
            vDir.append([ent.text for ent in sent.ents if ent.label_ == "DIRECTION"])
            if any(ent.label_ == "EIND" for ent in sent.ents):
                vTyp.append("EIND")
            else:
                vTyp.append("PART")

print(vMag)
print(vDir)
print(vTyp)
