import spacy
from spacy.tokens import Doc
from dateutil import parser
from public.helpers import word_to_number


class InputProcessing:
    def __init__(self, nlp):
        self.nlp = nlp
        self.nlp2 = spacy.load("en_core_web_sm")

    def __call__(self, doc):
        input_text = doc.text
        doc2 = self.nlp2(input_text)

        for ent in doc.ents:
            doc._.intents.append(ent.label_)
            if ent.label_ == "ASSET_NAME":
                doc._.asset_name = ent.text.capitalize()

        for ent in doc2.ents:
            if ent.label_ == "DATE":
                doc._.trade_date = parser.parse(ent.text).strftime("%Y-%m-%d")
            elif ent.label_ == "MONEY":
                doc._.trade_entry = float(ent.text)
            elif ent.label_ == "CARDINAL":
                doc._.trade_size = int(ent.text)

        for token in doc2:
            if token.like_email:
                doc._.user_email = token.text
            elif token.ent_type_ == "ORDINAL":
                doc._.journal_number = word_to_number(token.text)
            elif "short" in str(token).lower():
                doc._.trade_type = "Short"
            elif "long" in str(token).lower():
                doc._.trade_type = "Long"

        return doc


# Register the custom attribute
Doc.set_extension("intents", default=[], force=True)
Doc.set_extension("user_email", default=None, force=True)
Doc.set_extension("journal_number", default=None, force=True)
Doc.set_extension("asset_name", default=None, force=True)
Doc.set_extension("trade_date", default="", force=True)
Doc.set_extension("trade_entry", default=0, force=True)
Doc.set_extension("trade_size", default=0, force=True)
Doc.set_extension("trade_type", default="", force=True)


# Register the custom component factory globally
@spacy.registry.misc("input_processing")
def create_input_processing(nlp, name):
    return InputProcessing(nlp)
