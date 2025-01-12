import spacy
text = "Joe walks 2m north and the 3m east. What is the total distance?"
nlp = spacy.blank("en")
unit_list = ["m", "km", "cm", "mm", "ft", "yd", "mi", "in", "nmi", "N"]
direction_list = ["north", "east", "south", "west"]
ruler = nlp.add_pipe("entity_ruler")
patterns = [
    {"label": "MAGNITUDE", "pattern": [{"IS_DIGIT": True}, {"TEXT": {"IN": unit_list}}]},
    {"label": "DIRECTION", "pattern": [{"TEXT": {"IN": direction_list}}]}
]
ruler.add_patterns(patterns)
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)